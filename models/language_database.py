from .standard_database import StandardDatabase
from .database_names import TABLE_LANGUAGE_NAMES, TABLE_CONFIG_NAMES

class LanguageDatabase( StandardDatabase ):
    def __init__(self):
        super().__init__( name_database="language", name_dir_data="data"  )
        

        self.dictionary_of_tables = {
            TABLE_LANGUAGE_NAMES['table'] : [
                [ TABLE_LANGUAGE_NAMES['id'], 'integer', 'primary key autoincrement' ],
                [ TABLE_LANGUAGE_NAMES['tag'], 'text', 'unique' ],
                [ TABLE_LANGUAGE_NAMES['en'], 'text' ],
                [ TABLE_LANGUAGE_NAMES['es'], 'text' ],
                [ TABLE_LANGUAGE_NAMES['pt'], 'text' ],
                [ TABLE_LANGUAGE_NAMES['ru'], 'text' ]
            ],

            TABLE_CONFIG_NAMES['table']: [
                [ TABLE_CONFIG_NAMES['id'], 'integer', 'primary key autoincrement' ],
                [ TABLE_CONFIG_NAMES['lang'], 'text' ]
            ]
        }