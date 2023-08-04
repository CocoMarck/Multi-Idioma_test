from Modulos.Modulo_System import CleanScreen
from Modulos import Modulo_ShowPrint as Show
from Modulos import Modulo_Language as Lang
from Modulos.Modulo_Language_GT import Translate as GoogleTranslate
import sys


def Main():
    loop = True
    #lang = GoogleTranslate(language_output='pt')
    GoogleTranslate(language_output='pt')
    #lang = Lang.Language()
    while loop == True:
        # Menu - Visal - Ayuda
        CleanScreen()
        Show.Title( Lang.get_text('app') )
        print(
            f'1. {Lang.get_text("lang")}\n'
            f'2. {Lang.get_text("text")}\n'
            f'0. {Lang.get_text("exit")}'
        )
        option = input(f'{Lang.get_text("option")}: ')
        
        # Continuar o no con la opcion eligida
        option_continue = Show.Continue()
        if option_continue == Lang.YesNo('yes'):
            pass
        elif option_continue == Lang.YesNo('no'):
            option = None
        else:
            Show.Continue(message_error=True)
        
        # Evento de Opciones
        CleanScreen()
        if option == '1':
            Select_Language()
            
        elif option == '2':
            Show_Text()
        
        elif option == '0':
            loop=False
            
        elif option == None:
            pass

        else:
            Show.Continue(
                text=option,
                message_error=True
            )
    
    else:
        print( f"{Lang.get_text('bye')}..." )
        exit()


def Select_Language( ):
    # Menu de opciones - Visual
    Show.Title( Lang.get_text('lang') )
    print(
        f'{Lang.get_text("lang")}: {Lang.get_lang()}'
    )
    
    # Mostrar opciones de lenguajes
    option_nmb = 0
    option_dict = {}
    for text in Lang.List_Lang():
        option_nmb += 1
        option_dict.update({ option_nmb : text })
    
    for key in option_dict.keys():
        print(f'{key}. {option_dict[key]}')
    
    print('0. default')
    
    # Input de opciones
    option = input(
        f'{Lang.get_text("option")}: '
    )
    
    # Opcion elegida
    try:
        if int(option) in option_dict.keys():
            set_lang = option_dict[int(option)]
    
        else:
            set_lang = ''
    except:
        set_lang = ''
    
    # Mostrar opcion
    input(f'{set_lang}...')
        
    # Establecer, lang en el archivo Languages.dat
    Lang.set_lang(set_lang=set_lang)
    sys.exit()


def Show_Text():
    number = 0
    for key in (Lang.Language()).keys():
        number += 1
        print(
            f'key - {key}\n'
            f'{number}. {Lang.get_text(key)}'
            '\n'
        )
        
    input( 
        '\n' +
        Lang.get_text('continue_enter') + '...' 
    )


if __name__ == '__main__':
    Main()