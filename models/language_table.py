from .standard_table import StandardTable
from .language_database import LanguageDatabase

from .database_names import LANGUAGE_TABLE_NAMES




class LanguageTable( StandardTable ):
    def __init__(self):
        super().__init__( database=LanguageDatabase(), table=LANGUAGE_TABLE_NAMES['table'] )
    

    def select_tag(self, tag: str, language: str) -> (tuple, str):
        '''
        Instrucción obtener texto de etiqueta
        '''
        sql_statement = (
            f"SELECT {language} FROM {self.table} "
            f"WHERE {LANGUAGE_TABLE_NAMES['tag']}='{tag}';"
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
            f"({LANGUAGE_TABLE_NAMES['tag']}, {language}) "
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
            f"UPDATE {self.table} SET {language}='{text}' WHERE {LANGUAGE_TABLE_NAMES['tag']}='{tag}';"
        )
        
        return self.execute_and_return_values(
            sql_statement=sql_statement, commit=True, return_type="bool"
        )
    
    
    def update_row(self, languageId: int, tag:str, language:str, text:str) -> (bool,str,bool):
        '''
        Actualizar fila completa. Util si un tag puesto no tienen sentido.
        '''
        sql_statement = (
            f"UPDATE {self.table} SET {LANGUAGE_TABLE_NAMES['tag']}='{tag}', {language}='{text}' "
            f"WHERE {LANGUAGE_TABLE_NAMES['id']}={languageId};"
        )
        return self.execute_and_return_values(
            sql_statement=sql_statement, commit=True, return_type="bool"
        )
    
    
    def remove_tag(self, languageId: int) -> str | None:
        '''
        Intrucción eliminar etiqueta
        '''
        return self.delete_row_by_column_value( column=LANGUAGE_TABLE_NAMES['id'], value=languageId )