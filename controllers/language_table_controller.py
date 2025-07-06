from models import LanguageTable, LanguageConfigTable
from .table_controller import TableController
from models.database_names import DEFAULT_LANGUAGE

from core.text_util import ignore_text_filter




# Filtros
FILTER_ABC = 'abcdefghijklmnñopqrstuvwxyz'
FILTER_NUMBERS = '1234567890'
FILTER_FOR_TAG = FILTER_ABC + FILTER_NUMBERS + '-'




class LanguageTableController( TableController ):
    '''
    Controller para modelo LangaugeTable
    El tag siempre recibira un filtro.
    '''
    def __init__( self, log_level="warning" ):
        super().__init__( 
            table=LanguageTable(), verbose=True, log_level=log_level, save_log=True, only_the_value=True
        )
        self.language_config_table = LanguageConfigTable()
    
    
    # Filtros de texto
    def tag_filter( self, text:str ):
        return ignore_text_filter( text.lower(), FILTER_FOR_TAG )
    
    def language_filter( self, text:str=None ):
        '''
        Si no existe el lenguaje se pone el default, se establece el lenguaje default.
        '''
        return self.language_config_table.language_filter(language=text)
        
    
    # Funciones chidas
    def get_text(self, tag: str, language: str=None ) -> str:
        # tag
        filtered_tag = self.tag_filter( tag )
        filtered_language = self.language_filter(language)

        value, sql_statement, commit = self.table.select_tag( tag=filtered_tag, language=filtered_language )
        string_value = filtered_tag
        if isinstance(value, tuple):
            # Si no existe el tag en el lenguaje que no sea en
            if value[0] == None and language != self.language_config_table.default_language:
                log_type = "warning"
                message = f"The tag value no exists in `{filtered_language}`"
                value, sql_statement, commit = self.table.select_tag(
                    tag=tag, language=self.language_config_table.default_language
                )
            # Existe el tag
            else:
                log_type = "info"
                message = f"Nice, the tag `{filtered_tag}` exists"
            
            string_value = value[0]
        else:
            # Si no existe el tag, devolver el texto tag que no exite.
            log_type = "warning"
            message = f"The tag `{filtered_tag}` does not exist"
        message = self.structure_sql_message( message, sql_statement, commit )
        
        # Asegurarse que el valor final sea un string
        string_value = str(string_value) if string_value is not None else filtered_tag
        
        return self.return_value( value=string_value, message=message, log_type=log_type )
        
        
        
    def insert_tag(self, tag: str, language: str=None, text: str=str) -> bool:
        filtered_tag = self.tag_filter( tag )
        filtered_language = self.language_filter(language)
    
        value, sql_statement, commit = self.table.insert_tag( 
            tag=filtered_tag, language=filtered_language, text=text
        )
        if value:
            log_type = "info"
            message = "Good insert"
        else:
            log_type = "error"
            message = "Bad insert"
        message = self.structure_sql_message( message, sql_statement, commit )
        
        return self.return_value( value=value, message=message, log_type=log_type)
    
    
    def update_tag(self, tag:str, language: str="en", text: str="") -> bool:
        filtered_tag = self.tag_filter(tag)
        filtered_language = self.language_filter(language)
        
        value, sql_statement, commit = self.table.update_tag( 
            tag=filtered_tag, language=filtered_language, text=text
        )
        if value:
            log_type = "info"
            message = "Good update"
        else:
            log_type = "error"
            message = "Bad update"
        message = self.structure_sql_message( message, sql_statement, commit )
        
        return self.return_value( value=value, message=message, log_type=log_type )
    
    
    def update_row(self, languageId: int=1, tag:str="", language: str=None, text: str="") -> bool:
        language = self.language_filter(language)
        value, sql_statement, commit = self.table.update_row(
            languageId=languageId, tag=tag, language=language, text=text
        )
        if value:
            log_type = "info"
            message = "Good update"
        else:
            log_type = "error"
            message = "Bad update"
        message = self.structure_sql_message( message, sql_statement, commit )
        
        return self.return_value( value=value, message=message, log_type=log_type )
    
    
    def save_tag(self, tag:str, language: str=None, text: str="") -> bool:
        filtered_tag = self.tag_filter(tag)
        filtered_language = self.language_filter(language)
        
        # Determinar que exista el tag
        value, sql_statement, commit = self.table.select_tag(
            tag=filtered_tag, language=filtered_language
        )
        exists_text = ( isinstance(value, tuple) )
        
        # Devolver
        if exists_text:
            return self.update_tag( tag=tag, language=filtered_language, text=text )
        else:
            return self.insert_tag( tag=tag, language=filtered_language, text=text )