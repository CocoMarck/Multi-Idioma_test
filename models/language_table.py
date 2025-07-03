from .standard_table import StandardTable
from .language_database import LanguageDatabase

from .database_names import TABLE_LANGUAGE_NAMES




class LanguageTable( StandardTable ):
    def __init__(self):
        super().__init__( database=LanguageDatabase(), table=TABLE_LANGUAGE_NAMES['table'] )
    

    def select_tag(self, tag: str, language: str) -> (tuple, str):
        '''
        Instrucción obtener texto de etiqueta
        '''
        sql_statement = (
            f"SELECT {TABLE_LANGUAGE_NAMES[language]} FROM {self.table} "
            f"WHERE {TABLE_LANGUAGE_NAMES['tag']}='{tag}';"
        )

        return self.execute_and_return_values(
            sql_statement=sql_statement, commit=False, return_type="fetchone"
        )
    
    
    def insert_tag(self, tag: str, language:str, text: str) -> (bool, str, bool):
        '''
        Instrucción insertar etiqueta
        '''
        sql_statement = (
            f"INSERT OR IGNORE INTO {self.table} "
            f"({TABLE_LANGUAGE_NAMES['tag']}, {TABLE_LANGUAGE_NAMES[language]}) "
            f"VALUES('{tag}', '{text}');"
        )
        
        return self.execute_and_return_values(
            sql_statement=sql_statement, commit=True, return_type="bool"
        )
    
    
    def update_tag(self, tag: str, language:str, text: str) -> (bool, str, bool):
        '''
        Instrucción actualizar etiqueta
        '''
        sql_statement = (
            f"UPDATE {self.table} SET {language}='{text}' WHERE {TABLE_LANGUAGE_NAMES['tag']}='{tag}';"
        )
        
        return self.execute_and_return_values(
            sql_statement=sql_statement, commit=True, return_type="bool"
        )
    
    
    def remove_tag(self, languageId: int) -> str | None:
        '''
        Intrucción eliminar etiqueta
        '''
        return self.delete_row_by_column_value( column=TABLE_LANGUAGE_NAMES['id'], value=languageId )