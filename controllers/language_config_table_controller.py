from models import LanguageConfigTable
from .table_controller import TableController
from models.database_names import DEFAULT_LANGUAGE, LANGUAGES




class LanguageConfigTableController( TableController ):
    def __init__(self, log_level="warning" ):
        super().__init__( table=LanguageConfigTable(), log_level=log_level )
    
    
    def language_exists(self, language:str) -> bool:
        '''
        Determinar que exita el lenguaje
        '''
        exists = False
        for key in LANGUAGES.keys():
            if language == LANGUAGES[key]:
                exists = True
                break

        return exists
        
    
    def get_language(self):
        # Obtener valor, y si no hay, ponerle uno default
        value, sql_statement, commit = self.table.select_language()
        if isinstance(value, tuple):
            language = value[0]
            log_type = "info"
            message = f"Language: {language}"
        else:
            language = DEFAULT_LANGUAGE
            log_type = "warning"
            message = f"El lenguaje no existe, devolviendo: {language}"
        message += f": {sql_statement}: commit={commit}"
        
        # Determinar que exista
        if self.language_exists( language=language ) == False:
            language = DEFAULT_LANGUAGE

        # Devolver
        return self.return_value( value=language, message=message, log_type=log_type)
    
    
    def update_language(self, language=str):
        if isinstance(language, str):        
            value, sql_statement, commit = self.table.update_language( language=language )
            if value:
                log_type = "info"
                message = f"Now, de language is: {language}"
            else:
                log_type = "error"
                message = f"Very strange case, update cannot be performed"
            message += f": {sql_statement}: commit={commit}"
        else:
            log_type = "error"
            message = "The language parameteris are not a string"
            value = False
        
        return self.return_value( value=value, message=message, log_type=log_type )