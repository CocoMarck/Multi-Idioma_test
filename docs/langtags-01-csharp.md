# LangTags
Base de datos, con información para obtener texto traducido. Funcionando con sqlite3.

La traducción se basa en `get_text(tag: str)` que retorna si o si texto, y si existe tag, que es el parametro de aca, en la db, pos devuevle value, que seria la traducción, eso y que get text es permisivo con formateo, lo normaliza a lower `kebab-case`. Asi que yo puedo poner `Set folder profile`, y normaliza a `set-folder-profile`.

--- 

## Tablas

- `languages`: Tabla con todos los lenguajes disponibles. Lengajes deben estar escritos estándar: `ISO 639-1`. Que en resumidas cuentas es esto: `es, en, pt, ru`.

- `tags`: Todas las etiquetas necesarias para obtener traduccion.

- `translations`: Traducciones, enlazadas a languages y tags

- `settings`: Configuración de lenguaje actual establecido. Inidica cual es el lengaje default. Y el actual lenguaje, puede ser default, el del system, o cualquiera que esta en languages. Tabla enlazada a languages, y contiene la opcion adicional de `system`, que simplemente es el lenguaje del sistema.


#### Naming en base da datos
Sera todo en `snake_case`. Incluso el achivo de base de datos. Se vale usar palabras en plural.
Ejemplos:
- Nombres de archivo de db: `langtags.sqlite`
- Nombres que se usaran en tablas: `languages, tags, translations, settings`
- Nombres de parametros: `tag_id, translation_id, parameter_name`


#### Campos de control
Todas las tablas tendran estos campos de control:
- `created_at`: Fecha de creación.
- `updated_at`: Fecha de modificación.
- `deleted_at`: Fecha de baja lógica.
- `is_active`: Bool si esta activo o no.

Bueno todas, menos la tabla `settings`. Esta tiedra filas estaticas, solo dos.

#### Query de tablas
```
CREATE TABLE languages (
    language_id   INTEGER PRIMARY KEY,
    code          TEXT NOT NULL UNIQUE,
    created_at    TEXT,
    updated_at    TEXT,
    deleted_at    TEXT.
    is_active     INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE tags (
    tag_id        INTEGER PRIMARY KEY,
    name          TEXT NOT NULL UNIQUE,
    created_at    TEXT,
    updated_at    TEXT,
    deleted_at    TEXT
    is_active     INTEGER NOT NULL DEFAULT 1
);

PRAGMA foreign_keys = ON;

CREATE TABLE translations (
    translation_id INTEGER PRIMARY KEY,
    tag_id         INTEGER NOT NULL,
    language_id    INTEGER NOT NULL,
    value          TEXT NOT NULL,
    created_at     TEXT,
    updated_at     TEXT,
    deleted_at     TEXT,
    is_active      INTEGER NOT NULL DEFAULT 1
    FOREIGN KEY(tag_id) REFERENCES tags(tag_id),
    FOREIGN KEY(language_id) REFERENCES languages(language_id)
);

CREATE TABLE settings (
    setting_id     INTEGER PRIMARY KEY,
    parameter_name TEXT NOT NULL UNIQUE,
    language_id    INTEGER NOT NULL DEFAULT 1
    FOREIGN KEY(language_id) REFERENCES languages(language_id)
);
```

Estos querys deberan ser `schemas`, es decir puro texto `tabla.sqlite`, en la carpeta `schemas` del proyecto. Para facil modificación. Ejemplo: `languages.sql  settings.sql  tags.sql  translations.sql`

---

## Función principal `get_text( tag, language )`

Se espera de parametros tanto `tag`, como `language`. La Busqueda sera por texto de tag y language. Por defecto language, sera el de la tabla `settings`. `get_text` sera a prueba de crash, si no existe tag o language, o en nada, devolver texto siempre, devolver parametro.

Ejemplos:
```python
get_text('exit', 'es') = 'Salir'
get_text('exit', 'en') = 'Exit'
get_text('Este texto no existe', 'este idioma no existe') = 'Este texto no existe'
```

Eso si, get text debera crear log de tag o y language, no encontrados.


---

## Modulos
El naming aca debe ser el que el lenguaje de programacion tenga como estandar.

- Controllers:
    - `language_controller`
    - `setting_controller`
    - `tag_controller`
    - `translation_controller`: Aca vive `get_text`.
    
    Y que usen logger los controller.
- Core:
    Modulo para obtener lenguaje del sistema en formato `ISO 639-1`.
    
    Modulo de formateo de texto para normalizar texto a `kebab-case`
    
    Modulo `datetime` a string, y de string a `datetime` object. SQLite si entiende string formateados tipo datetime, pero no tiene para valores tipo `datetime`.
    
    Clase `StandardDatabase`: Simple, solo normalizar trabajo. 
        De parametros dir, y nombre.
        - get path: solo para unir dir con name.
        - exists: solo para determinar si existe o no.
        - _connect: metodo privado para retornar objecto connect.
        - execute, para ejecutar statement. Debe permitir roll back (pero no es obligatorio), hace commit, y retorna el objeto cursor.
        - init schema: Simplemente lee un texto query de sqlite3. Y usa el connect, para `executescript`, y hacerle el `commit`.
        - create_file: crea la base de datos, simplemente si no existe, usa invoca a connect, cierra el connect, y retorna true, de lo contrario retorna false, porque ya existe file y no creara la base de datos.
        - delete, borra la base de datos.
        - get tables, obtiene todas las tablas de la base de datos.
        - get table names. Nombres.
        - drop table, elimina una tabla.

Entidades:
    - `control_fields`
    - `language`
    - `setting`
    - `tag`
    - `translation`
    Todas las tablas son hijas de control fields entity, pero pos es opcional, es solo para normalizar sus atributos.

Repositorios
    - `base_repository`
    - `language_repository`
    - `setting_repository`
    - `tag_repository`
    - `translation_repository`
    
    Usan standard database para hacer todos los query work. Ademas usan lo necesario del core, para poder filtrar texto, normalizar texto, etc.

Views:
    - Ventanas modulares, el main window, casi casi nomas puros tabs es. 
    
    - Los tabs son las ventanas para cada una de las base de datos. 
    
    - Y un tab para `get_text`. Donde se testeara el uso de la funcion principal. Todos los forms usaran get text para mostrar su texto, por lo que tiene que estar todo hecho ya.


La funcion principal, pos es un wrapper que usara translation controller, para `get text`. Esta estara en `core`. Y se podria llamar `LangTagsGetText` o algo asi.


## Notas para `C#`
Usar naming `C#` Style claro, pero mantener nombres dichos en `sqlite` work. En realidad esto es solo para mantener compatibilidad con mis antiguos db de traducciones.

1. Uso de Caché Obligatorio en C#: SQLite es rápido, pero hacer una consulta SQL mediante Interfaz de Usuario por cada etiqueta de texto (botones, títulos, tablas) va a degradar el rendimiento. La memoria RAM es perfecta para este diccionario.

2. Normalización Temprana: Cualquier string que entre a get_text pasa por limpieza regex antes de tocar repositorios o cachés.

3. Manejo de Errores Silencioso pero Rastreable: La aplicación nunca debe lanzar una excepción no controlada (Crash) si un tag falta o la base de datos se corrompe momentáneamente; simplemente pinta el string crudo en pantalla y genera una línea en el archivo .log.

4. IMPOTANTE: `dotnet CLI` puro, no `Visual Studio`. Y para las ventanas: [Avalonia UI](https://avaloniaui.net/). 

[Tutorial como usar dotnet](./dotnet-tutorial-instalacion.md)

Posiblemente una estructura asi:
```
 LangTags/
 --- Data/langtags.sqlite
│
├──  Core/
│   ├── StringExtensions.cs       # Normalizador lower kebab-case
│   ├── SystemLanguage.cs         # Obtiene el ISO 639-1 del sistema operativo
│   ├── DateTimeHelper.cs         # Conversiones de strings de SQLite a DateTime
│   └── StandardDatabase.cs       # Clase base para el manejo del archivo sqlite3
│
├──  Schemas/                   # Archivos SQL planos (Puro texto)
│   ├── languages.sql
│   ├── settings.sql
│   ├── tags.sql
│   └── translations.sql
│
├──  Entities/                  # Clases espejo de la base de datos
│   ├── ControlFields.cs
│   ├── LanguageEntity.cs
│   ├── SettingEntity.cs
│   ├── TagEntity.cs
│   └── TranslationEntity.cs
│
└──  Repositories/              # Queries SQL directos (sin ORM)
    ├── BaseRepository.cs
    ├── LanguageRepository.cs
    ├── SettingRepository.cs
    ├── TagRepository.cs
    └── TranslationRepository.cs  # Aquí se consume el Query para GetText
```
