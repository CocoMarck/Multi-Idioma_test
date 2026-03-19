from PyQt6.QtWidgets import QApplication
from views.langtags.main_window import MainWindow
import sys

# DB
from core.sqlite.standard_database import StandardDatabase
from core.sqlite.standard_table import StandardTable

from repositories.langtags.language_repository import LanguageRepository
from repositories.langtags.tag_repository import TagRepository
from repositories.langtags.translation_repository import TranslationRepository

from models.langtags.language import Language
from models.langtags.tag import Tag
from controllers.langtags.language_controller import LanguageController
from controllers.langtags.tag_controller import TagController

import pathlib

# Usando méotods de infrestructura.
db = StandardDatabase( directory=pathlib.Path('data'), name='langtags.sqlite' )
table_language = StandardTable(
    database=db, name="languages"
)
language_repository = LanguageRepository( table=table_language )

tag_table = StandardTable( database=db, name="tags" )
tag_repository = TagRepository( table=tag_table )

translation_table = StandardTable( database=db, name="translations" )
translation_repository = TranslationRepository(
    table=translation_table, language_repository=language_repository, tag_repository=tag_repository
)

language_model = Language()
language_controller = LanguageController(language_repository, language_model)
tag_model = Tag()
tag_controller = TagController(tag_repository, tag_model)


if __name__ == '__main__':
    app = QApplication( sys.argv )
    #app.setStyleSheet( STYLE_QSS )
    window = MainWindow( language_controller, tag_controller )
    window.show()
    sys.exit( app.exec() )
