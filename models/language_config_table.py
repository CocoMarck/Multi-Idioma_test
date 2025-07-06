from .standard_table import StandardTable
from .language_database import LanguageDatabase
from .database_names import LANGUAGE_CONFIG_TABLE_NAMES, LANGUAGES, DEFAULT_LANGUAGE, NAME_SYSTEM_LANGUAGE

from core.system_util import get_system




import locale
import pycountry
def system_language():
    '''
    Obtener el lenguaje default del os. O el lenguaje establecido por el usuario.
    '''
    # Obtener lista de languaje default del OS y establecer el lang
    language = locale.getlocale()
    language = str(language[0])

    # Separar el el texto por _ y establecer el texto de la izq
    language = language.split('_')
    language = language[0]
    
    # Para windows
    if get_system() == 'win':
        object_country = pycountry.languages.get(name=language)
        language = object_country.alpha_2
    
    return language




class LanguageConfigTable( StandardTable ):
    def __init__(self):
        super().__init__( database=LanguageDatabase(), table=LANGUAGE_CONFIG_TABLE_NAMES['table'] )
        
        self.default_language = DEFAULT_LANGUAGE
    
    
    def get_system_language(self) -> str:
        return system_language()
    
    
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
    
    
    def language_filter( self, language:str=None ) -> str:
        '''
        Si no existe el lenguaje se pone el default, se establece el lenguaje default.
        '''
        # Obtener lenguaje de sistema o no
        if language == NAME_SYSTEM_LANGUAGE:
            language = self.get_system_language()
        else:
            # Obtener lenguaje puesto en tabla
            if language == None:
                language, sql_statement, commit, warning = self.get_language()
        # Si no existe el lenguaje como columna en la tabla `language`
        if self.language_exists( language ) == False:
            language = self.default_language
        
        # Devolver si o si un string
        return language
    
    
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
    
    
    def get_language( self ) -> (str, str, bool, bool):
        '''
        Devolver lenguaje. Si o si un str.
        '''
        # Determinar valor
        value, sql_statement, commit = self.select_language()
        if isinstance(value, tuple):
            language = value[0]
        else:
            language = self.default_language
            
        # Filtrar lenguaje
        if language == NAME_SYSTEM_LANGUAGE:
            language = self.get_system_language()
        
        # Determinar que exista
        if self.language_exists( language ):
            warning = False
        else:
            warning = True
            language = self.default_language

        # Devolver
        return language, sql_statement, commit, warning