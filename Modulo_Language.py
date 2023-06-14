import locale
import Modulo_Util as Util


def Default_Language():
    # Obtener lista de languaje default del OS y establecer el lang
    lang_default = locale.getdefaultlocale()
    lang_default = lang_default[0]

    # Separar el el texto por _ y establecer el texto de la izq
    lang_default = lang_default.split('_')
    lang_default = lang_default[0]
    
    return lang_default


def Language( lang=Default_Language() ):
    # Leer Archivo languages
    file_text = Util.Ignore_Comment(
        Util.Text_Read(
            file_and_path='./Languages.dat',
            opc='ModeRead'
        )
    )
    # Obtener str de languages
    file_dict = Util.Text_Separe(
        text=file_text,
        text_separe='='
    )
    
    # Verificar un language establecido por el usuario
    if file_dict['set_lang'] == '':
        # Si no hay str, entonces se coloca el default
        pass

    elif (
        file_dict['set_lang'] == 'es' or
        file_dict['set_lang'] == 'en'
    ):
        # Si el str es correcto, establece en la app
        lang = file_dict['set_lang']

    else:
        # Si es incorrecto, entonces se coloca el default
        pass

    # Verificar que el lang sea español o english
    if (
        lang == 'es' or
        lang == 'en'
    ):
        pass
    else:
        # Si no es español o english, entonces.
        print(lang)
        lang = 'en'
    
    # Agregar str de languages a un dicionario
    if (
        lang == 'es' or
        lang == 'en'
    ):
        # Formato, es_opcion - en_opcion
        lang=f'{lang}_'
        
        # Declarar variables, tipo lista, si es necesario
        list_YesNo = []
        for option in (file_dict[f'{lang}YesNo']).split(','):
            list_YesNo.append(option)

        # Agregar al diccionario
        lang_dict = {
            'title': file_dict[f'{lang}title'],
            'option': file_dict[f'{lang}option'],
            'lang': file_dict[f'{lang}lang'],
            'exit': file_dict[f'{lang}exit'],
            'bye': file_dict[f'{lang}bye'],
            'continue': file_dict[f'{lang}continue'],
            'continue_enter': file_dict[f'{lang}continue_enter'],
            'YesNo': list_YesNo,
            'app': file_dict[f'{lang}app']
        }
    else:
        pass
    
    return lang_dict