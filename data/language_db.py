import sqlite3
import os




db_format = 'db'
db_name='language'
db_full_path=os.path.join( '', f'{db_name}.{db_format}' )
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
for i in languages:
    columns.append(i)
def create_database():
    '''
    Generar base de datos
    
    La base de datos de tener las siguientes columnas
    id = entero que no puede ser nulo.
    text = string unico, no se puede repetir
    lang(en,es,pt. etc...) = string

    El id se incrementa solito. Como debe ser.
    '''
    # Instruccion para crear tabla language.db
    sql_statement = (
        f'CREATE TABLE IF NOT EXISTS "{db_name}" (\n'
        f'    "{columns[0]}" INTEGER NOT NULL,\n'
        f'    "{columns[1]}"  TEXT UNIQUE,\n'
    )

    for i in languages:
        sql_statement += f'    "{i}"    TEXT,\n'
    sql_statement += (
        f'    PRIMARY KEY("{columns[0]}" AUTOINCREMENT)\n'
        ');'
    )



    # Instrucción de crear tabla.
    if not os.path.isfile(db_full_path):
        try:
            with sqlite3.connect(db_full_path) as conn:
                # Crear un cursor
                cursor = conn.cursor()
                
                # Ejecturar declaracion
                cursor.execute(sql_statement)
                
                # Establecer cambios
                conn.commit()

                print( f'Data base {db_full_path} is ready' )
        except sqlite3.OperationalError as e:
            print( f'ERROR {db_full_path} {e}' )
    else:
        print( f'The data base {db_full_path} exists' )
    
    return sql_statement

#print( create_database() )




def get_column_names():
    '''
    Obtener los nombres de las columnas
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

print( get_column_names() )




def get_all_values():
    '''
    Obtener todos los valores de las columnas.
    '''
    # Obtener nombres de todas las columnas
    columns = get_column_names()
    
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

print( get_all_values() )




def insert_tag( tag, lang, text ):
    '''
    Agregar texto a la base de datos.
    
    Parametros:
        tag = str, etiqueta
        lang = str, idioma donde se guardara el text
        text = str, valor de etiqueta
    '''
    sql_statement = (
        f'INSERT INTO {db_name}({columns[1]}, {lang})\n'
        f'VALUES("{tag}", "{text}")'
    )
    
    # Ejecutar instrucción
    try:
        with sqlite3.connect(db_full_path) as conn:
            cur = conn.cursor()
            cur.execute( sql_statement )
            print('tag added successfully')
    except sqlite3.OperationalError as e:
        print(e)
    
    return sql_statement

#print( insert_tag( 'pc','es', 'Computadora personal' ) )
#print( insert_tag( 'hello-w', 'en', 'Hello World' ) )
#print( insert_tag( 'text', 'es', 'Texto' ) )




def update_tag_text( tag, lang, text  ):
    # Instrucción para actualizar datos
    sql_statement = (
        f'UPDATE {db_name} SET {lang}="{text}" WHERE {columns[1]}="{tag}"'
    )
    
    # Actualizar datos.
    try:
        with sqlite3.connect(db_full_path) as conn:
            cur = conn.cursor()
            cur.execute( sql_statement )
            print("changes completed")
    except sqlite3.OperationalError as e:
        print(e)
    
    return sql_statement

#print( update_tag_text('pc', 'en', 'Personal Computer') )
#print( update_tag_text('pc', 'es', 'Computadora Personal') )
#print( update_tag_text('hello-w', 'es', 'Hola Mundo') )
#print( update_tag_text('text', 'en', 'Text') )




def current_language():
    return 'en'




def get_text( tag, lang=current_language()):
    '''
    Siempre devuelve un string.
    
    Si el texto no existe en la columna lang, entonces lo busacara en el lang='en'. Y si no existe alli, devolvera la entrada "text", el parametro text.
    
    Parametros:
        tag = string, etiqueta a buscar en la base de datos.
        lang = string, idioma que contendra el valor de la etiqueta.
    
    return string
    '''
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

print( get_text('hello-w') )

print( get_text('text', 'es') )
print( get_text('text', 'pt') )

print( get_text('pc') )

print( get_text('pc', 'pt') )
print( get_text('pc', 'en') )