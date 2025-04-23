import sqlite3
import os

db_format = 'db'
def create_database():
    db_name='language'
    db_full_path=os.path.join( '', f'{db_name}.{db_format}' )
    languages = [
        'en',
        'es',
        'pt',
        'ru'
    ]
    sql_statement = (
        f'CREATE TABLE IF NOT EXISTS "{db_name}" (\n'
        '    "languageId" INTEGER NOT NULL,\n'
        '    "text"  TEXT UNIQUE,\n'
    )

    for text in languages:
        sql_statement += f'    "{text}"    TEXT,\n'
    sql_statement += (
        '    PRIMARY KEY("languageId" AUTOINCREMENT)\n'
        ');'
    )
    print(sql_statement)




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

create_database()