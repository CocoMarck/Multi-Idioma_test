import locale
import Modulo_Util as Util


def Default_Lenguage():
    # Obtener lista de lenguaje default del OS y establecer el leng
    leng_default = locale.getdefaultlocale()
    leng_default = leng_default[0]

    # Separar el el texto por _ y establecer el texto de la izq
    leng_default = leng_default.split('_')
    leng_default = leng_default[0]
    
    return leng_default


def Lenguage( leng=Default_Lenguage() ):
    # Leer Archivo lenguages
    file_text = Util.Ignore_Comment(
        Util.Text_Read(
            file_and_path='./Lenguages.dat',
            opc='ModeRead'
        )
    )
    # Obtener str de lenguages
    file_dict = Util.Text_Separe(
        text=file_text,
        text_separe='='
    )
    
    # Verificar un lenguage establecido por el usuario
    if file_dict['set_leng'] == '':
        # Si no hay str, entonces se coloca el default
        pass

    elif (
        file_dict['set_leng'] == 'es' or
        file_dict['set_leng'] == 'en'
    ):
        # Si el str es correcto, establece en la app
        leng = file_dict['set_leng']

    else:
        # Si es incorrecto, entonces se coloca el default
        pass

    # Verificar que el leng sea español o english
    if (
        leng == 'es' or
        leng == 'en'
    ):
        pass
    else:
        # Si no es español o english, entonces.
        print(leng)
        leng = 'en'
    
    # Agregar str de lenguages a un dicionario
    if (
        leng == 'es' or
        leng == 'en'
    ):
        # Formato, es_opcion - en_opcion
        leng=f'{leng}_'
        
        # Declarar variables, tipo lista, si es necesario
        list_YesNo = []
        for option in (file_dict[f'{leng}YesNo']).split(','):
            list_YesNo.append(option)

        # Agregar al diccionario
        leng_dict = {
            'title': file_dict[f'{leng}title'],
            'option': file_dict[f'{leng}option'],
            'leng': file_dict[f'{leng}leng'],
            'exit': file_dict[f'{leng}exit'],
            'bye': file_dict[f'{leng}bye'],
            'continue': file_dict[f'{leng}continue'],
            'continue_enter': file_dict[f'{leng}continue_enter'],
            'YesNo': list_YesNo,
            'app': file_dict[f'{leng}app']
        }
    else:
        pass
    
    return leng_dict