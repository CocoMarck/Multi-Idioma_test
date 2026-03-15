from core.sqlite.standard_database import StandardDatabase
from core.sqlite.standard_table import StandardTable
import pathlib

# Usando méotods de infrestructura.
db = StandardDatabase(
    directory=pathlib.Path('data'), name='langtags.sqlite'
)
table_language = StandardTable(
    database=db, name="languages"
)
print(
    db.get_table_names(),
    db.table_exists( 'languages' ),
    db.get_path(),
    table_language.get_columns(),
    table_language.get_column_values()
)
