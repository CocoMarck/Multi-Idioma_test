import Modulo_Util as Util
import Modulo_Language as Lang


sys = Util.System()
lang = Lang.Language()


def Title(
    text=lang['title'],
    smb='#',
    space=4,
    print_mode=True,
):
    '''
    Mostrar un Titulo
    
    Parametros:
    text=str
    # Texto titular
    
    smb=str
    # Caracter, con la funcion de simbolo
    
    space=int
    # Numero de espacios, es decir:
    #   4 = '    '
    
    print_mode=bool
    # False, Modo imprimir titulo sin devolver texto.
    # True, Devolver texto.
    '''
    
    
    # Establecer variables
    space = ' '*space
    text = f'{smb}{space}{text}{space}{smb}'
    
    # Print o String mode
    if print_mode == True:
        # Imprimir texto
        print(text)

    elif print_mode == False:
        # Devolver texto
        return text

    else:
        pass


def Continue(
    text=f'¿{lang["continue"]}?',
    yn=lang['YesNo'],
    message_error=False
):
    '''
    Mostrar un masaje para continuar o no.
    
    Parametros:
    text = str
    # Es el mensaje ¿Continuar?

    yn = list
    # Una lista así ['y', 'n']

    message_error = bool
    # Muestra un input de error, que se quita precionando enter.
    '''
    
    
    # Declarar variable, option
    option = None
    
    # Mostrar o no mensaje de error
    if message_error == True:
        # Se cancelara el continue loop
        loop = False

        # Se mostrara un input, que se quitara, precionando enter.
        #Util.CleanScreen()
        if text == '':
            input(lang['continue_enter'] + '...')
        else:
            input(
                f'ERROR - {text}\n' +
                lang['continue_enter'] + '...'
            )

    else:
        # Se activa el loop e continue
        loop = True

    # Continue - Loop
    while loop == True:
        # Visual input, si o no
        option = input(
            f'{text} {yn[0]}/{yn[1]}: '
        )
        
        # Eleccion de opcion
        Util.CleanScreen()
        if (
            option == yn[0] or
            option == yn[1]
        ):
            # Si la opcion es si o no, el loop para
            loop = False
        
        else:
            # Si la opcion es erronea, el loop sigue
            Continue(text=option, message_error=True)
            
    
    return option