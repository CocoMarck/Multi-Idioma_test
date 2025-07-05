from .standard_table import StandardTable
from .language_database import LanguageDatabase
from .database_names import LANGUAGE_CONFIG_TABLE_NAMES



class LanguageConfigTable( StandardTable ):
    def __init__(self):
        super().__init__( database=LanguageDatabase(), table=LANGUAGE_CONFIG_TABLE_NAMES['table'] )
    
    
    def update_language( self, language: str ):
        '''
        Atualizar lenguaje
        '''
        sql_statement = (
            f"UPDATE {self.table} SET {LANGUAGE_CONFIG_TABLE_NAMES['language']}='{language}' "
            f"WHERE {LANGUAGE_CONFIG_TABLE_NAMES['id']}=1;"
        )
        return self.execute_and_return_values(
            sql_statement=sql_statement, commit=True, return_type="bool"
        )
    
    
    def select_language( self ):
        '''
        Obtener lenguaje establecido.
        '''
        sql_statement = (
            f"SELECT {LANGUAGE_CONFIG_TABLE_NAMES['language']} FROM {self.table} "
            f"WHERE {LANGUAGE_CONFIG_TABLE_NAMES['id']}=1;"
        )
        return self.execute_and_return_values(
            sql_statement=sql_statement, commit=False, return_type="fetchone"
        )