from logic.Modulo_System import CleanScreen
from interface.Modulo_ShowPrint import (
    Title,
    Separator,
    Continue
)
from data.Modulo_Language import (
    get_text as Lang,
    Language,
    get_lang,
    List_Lang,
    set_lang,
    YesNo
)
from data.Modulo_Language_GT import Translate
import sys


class Main:
    def __init__(self):
        Translate(language_output='pt')
        self.loop = True
        while self.loop == True:
            # Parte visual - Opciones
            CleanScreen()
            Title( Lang('app') )
            
            self.dict_options = {
                '1': 'lang',
                '2': 'text',
                '0': 'exit'
            }
            
            for key in self.dict_options.keys():
                print(f'{key}. {  Lang( self.dict_options[key] )  }')
            
            option = input(f'{Lang("option")}: ')
            
            # Continuar o no
            go = Continue( f"¿{Lang('continue')}?" )
            if go == YesNo('no'):
                option = None

            # Opción elegida
            if option in self.dict_options.keys():
                self.select_option(option=option)
            elif option == None:
                pass
        
    def select_option(self, option):
        CleanScreen()
        if self.dict_options[option] == 'lang':
            self.select_language()
        
        elif self.dict_options[option] == 'text':
            self.show_text()
    
        elif self.dict_options[option] == 'exit':
            self.loop = False
    
    def select_language(self):
        # Visual - Menu de opciones
        Title( Lang('lang') )
        print(
            f'{Lang("lang")}: {get_lang()}'
        )
        
        # Mostrar opciones de lenguajes
        option_nmb = 0
        option_dict = {}
        for language in List_Lang():
            option_nmb += 1
            option_dict.update( { f"{option_nmb}" : language } )
            print( f'{option_nmb}. {language}' )
        
        option_dict.update( {'0' : 'default'} )
        print( f'0. {option_dict["0"]}' )
        
        # Input de opciones
        option = input( f'{Lang("option")}: ' )
        
        # Opción elegida
        if option in option_dict.keys():
            # Mostrar opción
            # Establecer, lang en el archivo Langauges.dat
            lang = option_dict[option]
            set_lang(set_lang=lang)
            input(f'{lang}...')

        else:
            input(Lang('error_parameter') + '...')
    
    def show_text(self):
        number = 0
        for key in Language().keys():
            number += 1
            print(
                f'key - {key}\n'
                f'{number}. {Lang(key)}\n'
            )
        
        input(
            '\n' +
            Lang('continue_enter') + '...'
        )



if __name__ == '__main__':
    Main()