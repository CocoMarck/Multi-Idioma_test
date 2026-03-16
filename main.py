from core.sqlite.standard_database import StandardDatabase
from core.sqlite.standard_table import StandardTable
from repositories.langtags.language_repository import LanguageRepository
from repositories.langtags.tag_repository import TagRepository
import pathlib

# Usando méotods de infrestructura.
db = StandardDatabase(
    directory=pathlib.Path('data'), name='langtags.sqlite'
)
table_language = StandardTable(
    database=db, name="languages"
)
language_repository = LanguageRepository( table=table_language )
#language_repository.save_code( 'es' )
#language_repository.save_code( 'en' )
#language_repository.toggle_code_state( 'en' )
#language_repository.save_code( 'ru' )
#language_repository.toggle_code_state( 'ru' )
#language_repository.get_code_state( 'ru' )
tag_table = StandardTable(
    database=db, name="tags"
)
tag_repository = TagRepository( table=tag_table )
#tag_repository.save_name( 'exit' )
#tag_repository.toggle_name_state( 'exit' )

print(
    db.get_table_names(),
    db.table_exists( 'languages' ),
    db.get_path(),
    table_language.get_columns(),
    table_language.get_column_values(),
    tag_table.get_columns(),
    tag_table.get_column_values()
)
