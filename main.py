# python libs
from PyQt6.QtWidgets import QApplication
import pathlib
import sys

# DB
from core.sqlite.standard_database import StandardDatabase
from core.sqlite.standard_table import StandardTable

# Models
from models.langtags.language import Language
from models.langtags.tag import Tag

# Repostories
from repositories.langtags.language_repository import LanguageRepository
from repositories.langtags.tag_repository import TagRepository
from repositories.langtags.translation_repository import TranslationRepository

# Controllers
from controllers.langtags.language_controller import LanguageController
from controllers.langtags.tag_controller import TagController

# Window
from views.langtags.main_window import MainWindow

# Paths
from config.paths import SCHEMAS_LANGTAGS_FILES

# Creación de db si no exite.
db = StandardDatabase( directory=pathlib.Path('data'), name='langtags.sqlite' )
if not db.exists():
    print('Creando base de datos y aplicando schemas...')
    db.execute( 'PRAGMA foreign_keys = ON;', commit=True )
    for f in SCHEMAS_LANGTAGS_FILES:
        db.init_schema( f )

# Establecer controladores
table_language = StandardTable( database=db, name="languages" )
language_repository = LanguageRepository( table=table_language )
language_model = Language()
language_controller = LanguageController(language_repository, language_model)

tag_table = StandardTable( database=db, name="tags" )
tag_repository = TagRepository( table=tag_table )
tag_model = Tag()
tag_controller = TagController(tag_repository, tag_model)

translation_table = StandardTable( database=db, name="translations" )
translation_repository = TranslationRepository(
    table=translation_table, language_repository=language_repository, tag_repository=tag_repository
)

# Generación de DB
if __name__ == '__main__':
    app = QApplication( sys.argv )
    #app.setStyleSheet( STYLE_QSS )
    window = MainWindow( language_controller, tag_controller )
    window.show()
    sys.exit( app.exec() )
