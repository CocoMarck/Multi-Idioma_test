from . import Modulo_Util as Util
from . import Modulo_Language as Lang


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
    message_error=False
):
    '''
    Mostrar un masaje para continuar o no.
    
    Parametros:
    text = str
    # Es el mensaje ¿Continuar?

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
        # [:1] Es el primer caracter
        # lower() modo minusculas, upper() Modo Mayusculas
        option = input(
            f'{text} '
            f'{ Lang.YesNo("yes") }'
            '/'
            f'{ Lang.YesNo("no") }: '
        )
        
        # Eleccion de opcion
        # lower() modo minusculas, upper() Modo Mayusculas
        Util.CleanScreen()
        if (
            option == Lang.YesNo('yes') or
            option == Lang.YesNo('no')
        ):
            # Si la opcion es si o no, el loop para
            loop = False
        
        else:
            # Si la opcion es erronea, el loop sigue
            Continue(text=option, message_error=True)
            
    
    return option


def Separator(
    smb = '#',
    smb_number = 128,
    print_mode = True,
):
    '''
    Separador
    Muestra una serie de un solo caracter, tiene la funcion de separar textos.
    Te devuele un str.


    Parametros:
    smb = str
    # Un simbolo/caracter, que se repetira por smb_number
    
    smb_number = int
    # Catidad de simbolos/caracteres.
    
    print_mode = bool
    # Mostrar con print o no.
    '''
    separator = f'\n\n{smb*smb_number}\n\n'
    if print_mode == True:
        print(separator)
    else:
        return separator