import Modulo_Util as Util
import Modulo_ShowPrint as Show
import Modulo_Lenguage as Leng


def Main():
    loop = True
    leng = Leng.Lenguage()
    while loop == True:
        # Menu - Visal - Ayuda
        Util.CleanScreen()
        Show.Title( leng['app'] )
        print(
            f'1. {leng["leng"]}\n'
            f'0. {leng["exit"]}'
        )
        option = input(f'{leng["option"]}: ')
        
        # Continuar o no con la opcion eligida
        option_continue = Show.Continue()
        if option_continue == (leng['YesNo'])[0]:
            pass
        elif option_continue == (leng['YesNo'])[1]:
            option = None
        else:
            Show.Continue(message_error=True)
        
        # Evento de Opciones
        Util.CleanScreen()
        if option == '1':
            leng = Select_Lenguage(leng=leng)
        
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
        print( f"{leng['bye']}..." )
        exit()


def Select_Lenguage( leng=Leng.Lenguage() ):
    # Menu de opciones - Visual
    Util.Title( leng['leng'] )
    option = input(
        '1. Español\n'
        '2. English\n'
        f'{leng["option"]}: '
    )
    
    # Archivo de Texto Lenguages.dat
    # Leer y verificar set_leng
    text_leng = Util.Text_Read(
        file_and_path='./Lenguages.dat',
        opc='ModeText'
    )
    change_leng = False
    for line in text_leng.split('\n'):
        if line.startswith('set_leng='):
            # Si la linea set_leng existe
            change_leng = True
        else:
            # Si la linea set_leng no existe
            pass
    
    # Opcion elegida
    if option == '1':
        #leng = Leng.Lenguage('es') Funciona, pero mal
        set_leng = 'es'

    elif option == '2':
        #leng = Leng.Lenguage('en') Funciona, pero mal
        set_leng = 'en'
        
    else:
        set_leng = ''
        
    # Establecer o no, leng en el archivo Lenguages.dat
    if change_leng == True:
        leng_ready = ''
        for line in text_leng.split('\n'):
            if line.startswith('set_leng='):
                leng_ready += f'set_leng={set_leng}\n'
            else:
                leng_ready += line + '\n'
        # Eliminar ultimo salto de linea
        leng_ready = leng_ready[:-1]
        with open('./Lenguages.dat', 'w') as text_leng:
            text_leng.write(leng_ready)
    else:
        pass
        
    return leng


if __name__ == '__main__':
    Main()