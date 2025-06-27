from logic.Modulo_GT import Translate as GoogleTranslator
from data.Modulo_Language import (
    Default_Language,
    Language,
    set_lang,
    lang_dir
)
from pathlib import Path as pathlib
import os, sys

lang_dir = lang_dir


def Translate(
    language_input='es',
    language_output='pt'
):
    # Si el language input es Enlgish (el default)
    if language_input == 'en':
        # El lenguaje sera español
        language_input = 'es'
    else:
        pass
        
    # Si el output es en o es.
    if (
        language_output == 'en' or
        language_output == 'es'
    ):
        language_output = 'pt'
    else:
        pass
    
    # Verificar si existe o no el language
    if pathlib(
        os.path.join( lang_dir, f'Language_{language_output}.dat' )
    ).exists():
        # El language es igual al output
        dict_lang = Language(language_output)
    else:
        set_lang(language_input)
        # Establecer dict-lang por medio del parametro
        lang = Language(language_input)
        #input(lang)
        
        # Declarar list_text, que obtendra el texto traducido.
        # Obtener el texto, del dicionario lang
        list_text = []
        for text in lang.keys():
            # Verificar que sea un str o una lista.
            if type(lang[text]) is list:
                # Si es una lista, concatenar lista a un str
                # Para que lo puede traducir el GoogleTraductor
                lang_ready = ''
                for text in lang[text]:
                    lang_ready += f'{text} . '
                    #input(lang_ready)

                # Eliminar ultima estos caracteres: ' . '
                # Modo lista activado
                lang_ready = lang_ready[:-3]
                #input(lang_ready)
                is_list = True

            else:
                # Si es un str, entonces ya esta listo lo demas
                is_list = False
                lang_ready = lang[text]
        
            # Traducir texto obtenido del dict-lang
            try:
                text = GoogleTranslator(
                    text_only=lang_ready,
                    language_input=language_input,
                    language_output=language_output,
                    print_mode=True
                )

                # Verificar que el caracter esta listo para ser una lista
                if is_list == True:
                    # Sera una lista
                    lst = []
                    for txt in text.split(' . '):
                        lst.append(txt)
                    text = lst

                else:
                    # De lo contrario, no se hace nada.
                    pass
                
                # Alistar texto
                list_text.append(text)
            except:
                # No hay interet, asi que, se colocara la traduccion local.
                list_text = list( lang.values() )
        
        # Declarar dict que tendra el texto.
        dict_lang = {}
        
        # Contar la cantidad de str que hay en list_text
        total_number = 0
        for text in list_text:
            # Sumar texto
            total_number += 1

        #input(list_text)
        # Añadir key y texto al dict_lang
        # Es -1 porque se enpieza por el cero, y en el for le sumo uno
        number_ready = -1
        for key in lang.keys():
            # Verificar que el number_ready sea igual al numero_total
            # Se le resta al total_number uno porque se cuenta el cero.
            if number_ready == total_number-1:
                pass
            else:
                number_ready += 1

            # Añadir key y texto
            dict_lang.update(
                { key : list_text[number_ready] } 
            )
            
            # Escribir datos traducidos
            with open(
                os.path.join( lang_dir, f'Language_{language_output}.dat' ),
                'a'
            ) as file_text:
                if type(list_text[number_ready]) is list:
                    # Si es una lista
                    lst_ready = ''
                    for lst in list_text[number_ready]:
                        lst_ready += f'{lst},'
                    # Eliminar ultimo caracter (coma)
                    lst_ready = lst_ready[:-1]
                    
                    file_text.write(
                        f'{key}={lst_ready}\n'
                    )
                else:
                    # De lo contraro, se escribe de forma normal
                    file_text.write(
                        f'{key}={list_text[number_ready]}\n'
                    )

        # Etablecer lenguaje default del sistema
        set_lang('')
    
    # Devolver el diccionario listo.
    return dict_lang