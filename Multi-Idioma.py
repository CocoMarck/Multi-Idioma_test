import Modulo_Util as Util
import Modulo_ShowPrint as Show
import Modulo_Language as Lang


def Main():
    loop = True
    #lang = Lang.Translate(language_output='fr')
    lang = Lang.Language()
    while loop == True:
        # Menu - Visal - Ayuda
        Util.CleanScreen()
        Show.Title( lang['app'] )
        print(
            f'1. {lang["lang"]}\n'
            f'0. {lang["exit"]}'
        )
        option = input(f'{lang["option"]}: ')
        
        # Continuar o no con la opcion eligida
        option_continue = Show.Continue()
        if option_continue == Lang.YesNo('yes'):
            pass
        elif option_continue == Lang.YesNo('no'):
            option = None
        else:
            Show.Continue(message_error=True)
        
        # Evento de Opciones
        Util.CleanScreen()
        if option == '1':
            lang = Select_Language(lang=lang)
        
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
        print( f"{lang['bye']}..." )
        exit()


def Select_Language( lang=Lang.Language() ):
    # Menu de opciones - Visual
    Show.Title( lang['lang'] )
    option = input(
        '1. Español\n'
        '2. English\n'
        f'{lang["option"]}: '
    )
    
    # Archivo de Texto Languages.dat
    # Leer y verificar set_lang
    text_lang = Util.Text_Read(
        file_and_path='./Languages.dat',
        opc='ModeText'
    )
    change_lang = False
    for line in text_lang.split('\n'):
        if line.startswith('set_lang='):
            # Si la linea set_lang existe
            change_lang = True
        else:
            # Si la linea set_lang no existe
            pass
    
    # Opcion elegida
    if option == '1':
        #lang = Lang.Language('es') Funciona, pero mal
        set_lang = 'es'

    elif option == '2':
        #lang = Lang.Language('en') Funciona, pero mal
        set_lang = 'en'
        
    else:
        set_lang = ''
        
    # Establecer o no, lang en el archivo Languages.dat
    if change_lang == True:
        Lang.set_lang(set_lang=set_lang)
    else:
        pass
        
    return lang


if __name__ == '__main__':
    Main()