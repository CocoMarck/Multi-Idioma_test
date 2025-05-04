import locale
from logic.Modulo_Text import *
from logic.Modulo_System import get_system
import sqlite3
import os, sys


# Ruta
current_dir = os.path.dirname( os.path.abspath(sys.argv[0]) )
dir_data = os.path.join( current_dir, 'data' )

# Archivo de data base.
db_format = 'db'
name_table_config = 'config'
db_name='language'
db_full_path=os.path.join( dir_data, f'{db_name}.{db_format}' )
default_language = 'en'
languages = [
    'en',
    'es',
    'pt',
    'ru'
]
columns = [
    'languageId',
    'tag'
]
columns_config = [
    'configId',
    'lang'
]
default_config = 'default'
for i in languages:
    columns.append(i)
    

# Filtros
filter_abc = 'abcdefghijklmnñopqrstuvwxyz'
filter_numbers = '1234567890'
filter_for_tag = filter_abc + filter_numbers + '-_'
filter_for_lang = filter_abc
    



def system_language():
    '''
    Obtener el lenguaje default del os. O el lenguaje establecido por el usuario.
    '''
    # Obtener lista de languaje default del OS y establecer el lang
    lang_default = locale.getlocale()
    lang_default = str(lang_default[0])

    # Separar el el texto por _ y establecer el texto de la izq
    lang_default = lang_default.split('_')
    lang_default = lang_default[0]
    
    # Para windows
    #if get_system() == 'win':
    #    import pycountry
    #    object_country = pycountry.languages.get(name=lang_default)
    #    lang_default = object_country.alpha_2
    
    return lang_default


    
    
def create_table_language():
    '''
    Generar base de datos y crear tablas language y config
    
    Respocto a la tabla language:
    Debe de tener las siguientes columnas
    id = entero que no puede ser nulo.
    text = string unico, no se puede repetir
    lang(en,es,pt. etc...) = string

    El id se incrementa solito. Como debe ser.
    '''
    # Instruccion para crear tabla language.db
    sql_statement_language = (
        f'CREATE TABLE IF NOT EXISTS "{db_name}" (\n'
        f'    "{columns[0]}" INTEGER NOT NULL,\n'
        #f'    "{columns[0]}"  INTEGER PRIMARY KEY,\n'
        f'    "{columns[1]}"   TEXT UNIQUE,\n'
    )

    for i in languages:
        sql_statement_language += f'    "{i}"    TEXT,\n'
    sql_statement_language += (
        f'    PRIMARY KEY("{columns[0]}" AUTOINCREMENT)\n'
        ');'
    )
    
    
    # Instruccion para crear tabla text.db
    sql_statement_config = (
        f'CREATE TABLE IF NOT EXISTS "{name_table_config}" (\n'
        f'    {columns_config[0]} INTEGER PRIMARY KEY CHECK ({columns_config[0]}=1),\n'
        f'    {columns_config[1]} TEXT\n'
        f');'
    )
    
    # Texto a devolver
    text_return = f'{sql_statement_language}\n{sql_statement_config}'



    # Instrucción de crear tabla.
    #if not os.path.isfile(db_full_path):
    try:
        with sqlite3.connect(db_full_path) as conn:
            # Crear un cursor
            cursor = conn.cursor()
            
            # Ejecturar declaracion
            cursor.execute(sql_statement_language)
            cursor.execute(sql_statement_config)
            
            # Establecer cambios
            conn.commit()

            print( f'Data base {db_full_path} is ready' )
    except sqlite3.OperationalError as e:
        print( f'ERROR {db_full_path} {e}' )
    #else:
    #    print( f'The data base {db_full_path} exists' )
    
    # Texto a devolver
    return text_return




def update_lang( lang ):
    '''
    Actualizar lenguage.
    
    Filtros del texto:
    - El texto sere en minusculas
    - Si Tendra letras del abecedario
    - Si Signo del menos y guion bajo
    '''
    # Texto de lenguaje
    lang = ignore_text_filter( lang.lower(), filter_for_lang )
    
    # Determinar si el texto esta bueno o no.
    if lang == None or lang == '':
        good_lang = False
    else:
        good_lang = True
    
    
    # Instrucción
    sql_statement = (
        f'UPDATE {name_table_config} SET {columns_config[1]}="{lang}" WHERE {columns_config[0]}=1'
    )

    # Ejecutar instrucción | Establcer lenguaje
    if good_lang == True:
        print( f'The estructure of text "{lang}" is correct.' )
        try:
            with sqlite3.connect(db_full_path) as conn:
                cur = conn.cursor()
                cur.execute( sql_statement )
                conn.commit()
                print(f'The language "{lang}" updated successfully')
        except sqlite3.OperationalError as e:
            print(e)
    else:
        print( f'The estructure of text "{lang}" is incorrect.' )
    
    
    # Devolver instrucción
    return sql_statement
    

    

def set_lang( lang ):
    '''
    Establecer lenguage.
    
    Filtros del texto:
    - El texto sere en minusculas
    - SI Tendra letras del abecedario
    - SI Signo del menos y guion bajo
    '''
    # Texto de lenguaje
    lang = ignore_text_filter( lang.lower(), filter_for_lang )
    
    # Determinar si el texto esta bueno o no.
    if lang == None or lang == '':
        good_lang = False
    else:
        good_lang = True
    
    
    # Instrucción
    sql_statement = (
        f"INSERT OR IGNORE INTO {name_table_config} ({columns_config[0]}, {columns_config[1]})\n"
        f"VALUES(1, '{lang}')"
    )

    # Ejecutar instrucción | Establcer lenguaje
    if good_lang == True:
        print( f'The estructure of text "{lang}" is correct.' )
        try:
            with sqlite3.connect(db_full_path) as conn:
                cur = conn.cursor()
                cur.execute( sql_statement )
                conn.commit()
                print(f'The language "{lang}" inserted successfully')
        except sqlite3.OperationalError as e:
            print(e)
    else:
        print( f'The estructure of text "{lang}" is incorrect.' )
    
    
    # Devolver instrucción
    return sql_statement




def get_lang():
    '''
    Obtener el lenguaje almacenado en la tabla config.
    
    Situaciones a tener en cuenta
    1. Si no hay nadota "", None o no hay 1nada en la tabla. Devuelve el lenguaje default.
    2. Si esta el texto "default", devolver el langueje defualt.
    
    Si no pasa las dos situaciones anteriores, devolver lo indicado en la tabla config.
    
    return string
    '''
    sql_statement = f'SELECT {columns_config[1]} FROM {name_table_config}'
    #print(sql_statement)
    
    
    # Ejecutar instrucción
    text = None
    try:
        with sqlite3.connect(db_full_path) as conn:
            cur = conn.cursor()
            cur.execute( sql_statement )
            text = cur.fetchone()[0]
    except sqlite3.OperationalError as e:
        print(e)
    
    # Determinar que el texto esta bueno
    if not isinstance(text, str):
        text = default_config
    
    # Devolver
    return text





def get_column_name():
    '''
    Obtener todos los nombres de las columnas de la tabla language
    '''
    # Instrucción para seleccionar todos los nombres de las columnas. Tambien sirve para obtener los valores de las columnas.
    sql_statement = f'SELECT * FROM {db_name}'
    
    # Obtener nombres de las columnas.
    try:
        with sqlite3.connect(db_full_path) as conn:
            cur = conn.cursor()
            cur.execute( sql_statement )
            column_names = [description[0] for description in cur.description]
            return column_names
    except sqlite3.OperationalError as e:
        print(e)
        



def get_available_lang():
    '''
    Devolver todos los lenguajes disponibles, en la tabla language
    '''
    return_list = get_column_name()[2:] 
    # Ignorar los dos primeros indices. Serian languageId y tag

    return_list.append( default_config )
    # Agregar a la lista, la opcion default.

    return return_list




def get_all_column_value():
    '''
    Obtener todos los valores de las columnas.
    '''
    # Obtener nombres de todas las columnas
    columns = get_column_name()
    
    # Establecer comando para obtener todos los valores de las columnas
    sql_statement = 'SELECT'
    for text in columns:
        sql_statement += f' {text},'
    sql_statement = sql_statement[:-1]
    sql_statement += f' FROM {db_name}'
    print(sql_statement)
    
    # Ejecutar comando
    try:
        with sqlite3.connect( db_full_path ) as conn:
            cur = conn.cursor()
            cur.execute( sql_statement )
            list_text = cur.fetchall()
            return list_text
    except sqlite3.OperationalError as e:
        print(e)
        return None




def get_all_tag( ):
    sql_statement = f"SELECT {columns[1]} FROM {db_name}"
    
    # Ejecutar comando
    try:
        with sqlite3.connect( db_full_path ) as conn:
            cur = conn.cursor()
            cur.execute( sql_statement )

            list_text = []
            for tag in cur.fetchall():
                list_text.append(tag[0])
            return list_text
    except sqlite3.OperationalError as e:
        print(e)
        return None




def update_tag_text( tag, lang, text  ):
    # Establecer lang defualt
    if lang == default_config: lang = system_language()
    
    # Instrucción para actualizar datos
    sql_statement = (
        f"UPDATE {db_name} SET {lang}='{text}' WHERE {columns[1]}='{tag}';"
    )
    
    # Actualizar datos.
    try:
        with sqlite3.connect(db_full_path) as conn:
            cur = conn.cursor()
            cur.execute( sql_statement )
            print(f'Update of the "{tag}" tag is complete')
    except sqlite3.OperationalError as e:
        print(e)
    
    return sql_statement




def insert_tag( tag, lang, text ):
    '''
    Agregar texto a la base de datos.
    Si ya existe el tag, no agregar absolutamente nada.
    
    Parametros:
        tag = str, etiqueta
        lang = str, idioma donde se guardara el text
        text = str, valor de etiqueta
    
    Reglas para agregar tag:
    El tag no puede existir. El text, no puede ser el resultado de lang.
    El tag tiene que ser con puras letras minusculas.
    El tag tiene puede tener caracteres del abecedario (abc) y; "-" "_"
    '''
    # Establecer lang defualt
    if lang == default_config: lang = system_language()
    
    # Etiqueta
    # Determinar si el texto esta bueno o no.
    tag = ignore_text_filter( tag, filter_for_tag )
    
    if tag == None or tag == '':
        good_tag = False
    else:
        good_tag = True
    
    
    # Determinar si el tag no existe en la tabla languages.db
    tag_not_exists = True

    column_value = get_all_column_value()
    for list_value in column_value:
        if tag == list_value[1]:
            tag_not_exists = False
            break
    
    
    # Intentar actualizar tag
    if tag_not_exists == False and good_tag == True:
        print( f'The tag "{tag}" exists.' )
        print( f'Trying to upgrade the tag "{tag}"' )
        print( update_tag_text(tag, lang, text) )
    
    
    # Instrucción
    sql_statement = (
        f"INSERT INTO {db_name}({columns[1]}, {lang})\n"
        f"VALUES('{tag}', '{text}')\n"
        f"ON CONFLICT({columns[1]}) DO UPDATE SET {lang}='{text}';\n"
    )
    

    if tag_not_exists == True and good_tag == True:
        # Ejecutar instrucción
        try:
            with sqlite3.connect(db_full_path) as conn:
                cur = conn.cursor()
                cur.execute( sql_statement )
                print(f'The tag "{tag}" inserted successfully')
        except sqlite3.OperationalError as e:
            print(e)
    
    
    # Devolver instrucción
    return sql_statement




def delete_tag( tag ):
    '''
    Eliminación de tag.
    
    Un tag no se puede eliminar, se eliminara lo contenido en las columnas language.
    '''
    # Instrucción
    sql_statement = (
        f'DELETE FROM {db_name}\n'
        f'WHERE {columns[1]} = "{tag}"'
    )
    
    # Determinar que existe el tag
    list_value = get_all_column_value()
    exists_tag = False
    for column_value in list_value:
        if column_value[1] == tag:
            exists_tag = True
    
    # Ejecutar comando
    if exists_tag == True:
        try:
            # Ejetutar comando
            with sqlite3.connect(db_full_path) as conn:
                cur = conn.cursor()
                cur.execute( sql_statement )
                print(f'The tag "{tag}" deleting successfully.')
        except sqlite3.OperationalError as e:
            print(e)
    else:
        print( f'The tag "{tag}" not exists' )
    
    # Devolver texto del comando a ejecutar
    return sql_statement




def get_text( tag, lang=get_lang() ):
    # Recordatorio: Ponerle un WHERE, al sql_statement, para evitar hacer un bucle de busqueda.
    '''
    Siempre devuelve un string.
    
    Si el texto no existe en la columna lang, entonces lo busacara en el lang='en'. Y si no existe alli, devolvera la entrada "text", el parametro text.
    
    Parametros:
        tag = string, etiqueta a buscar en la base de datos.
        lang = string, idioma que contendra el valor de la etiqueta.
    
    return string
    '''
    # Establecer lang defualt
    if lang == default_config: lang = system_language()
    
    # Instrucción, seleccionar resultado de columnas "text" y "lang"
    # lang puede ser = en, es, pt. etc....
    sql_statement = f'SELECT {columns[1]}, {lang} FROM {db_name}'

    # Variables: String/Texto a retornar : Bool texto obtenido o no
    text_return = tag
    text_obtained = False

    # Obtener texto de la base de datos
    try:
        with sqlite3.connect(db_full_path) as conn:
            cur = conn.cursor()
            cur.execute( sql_statement )
            list_textlang = cur.fetchall()
            
            for item in list_textlang:
                if len(item) == 2:
                    if (tag == item[0]) and (item[1] != None):
                        text_return = item[1]
                        text_obtained = True

            
    except sqlite3.OperationalError as e:
        print(e)
    
    # Mensaje de que no se obtuvo ningun texto.
    if text_obtained == False:
        if lang != default_language:
            # Usar recursividad de funciones. Usando de nuevo get_text
            print( 
                f'The column "{lang}" not have "{tag}" tag. '
                f'Searching text in "{default_language}" column'
            )
            text_return = get_text( tag, default_language )
        else:
            print('No text was obtained. Non-existent tag.')
        
    
    
    # Retornar string
    return text_return




# Crear tabla
print( 'Creating data base' )
print( create_table_language() + '\n\n' )

# Obtener lenguajes disponibles
print( 'Available languages: ' )
print( f'{get_available_lang()}\n\n' )

# Inicializar configuración
print( 'Init config' )
#print( set_lang( 'default' ) + '\n\n' )

# Obtener el lenguaje actual
print( 'Getting current lang' )
print( get_lang() + '\n\n' )


# Filtros del los textos
print(
    'Filters for the texts\n'
    f'- For the tag: {filter_for_tag}\n'
    f'- For the language: {filter_for_lang}\n\n'
)


#print( get_column_name() )
#print( get_all_column_value() )

#print( insert_tag( 'pc','es', 'Computadora personal' ) )
#print( insert_tag( 'hello-w', 'en', 'Hello World' ) )
#print( insert_tag( 'text', 'es', 'Texto' ) )
#print( insert_tag( 'see-text', 'en', 'See text' ) )

#print( update_tag_text('pc', 'en', 'Personal Computer') )
#print( update_tag_text('pc', 'es', 'Computadora Personal') )
#print( update_tag_text('hello-w', 'es', 'Hola Mundo') )
#print( update_tag_text('text', 'en', 'Text') )
#print( update_tag_text( 'see-text', 'es', 'Ver texto' ) )

#print( delete_tag('cocos') )
#print( delete_tag('text') )

#print( get_text('hello-w') )

#print( get_text('text', 'es') )
#print( get_text('text', 'pt') )

#print( get_text('pc') )

#print( get_text('pc', 'pt') )
#print( get_text('pc', 'en') )

#print( get_text('hello-w', 'chinote') )
print( get_text('tagote', 'chinote') )