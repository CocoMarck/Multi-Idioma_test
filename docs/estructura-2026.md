# `language_store.sqlite`
Base de datos reutilizable para manejar idiomas, tags y traducciones en múltiples apps.

---

# Modelos de Tablas

## Campos de control
- `is_active`: Baja lógica
- `created_at`: Fecha de creación
- `updated_at`: Fecha de modificación
- `deleted_at`: Fecha de baja lógica

---

## `LanguageTable`

Idiomas disponibles en el sistema.

**Campos clave**:

- `id`
- `code` -> "es", "en", "fr"
- `name` -> "Español", "English"
- Campos de control...

---

## `ConfigTable`
Idioma activo por app / entorno.
- `id`
- `key`
- `value`

### Columnas creadas por defecto
- `0 | "current_language_id" | Null`
- `1 | "default_language_id" | 0`
> `default_language_id`: Por decisión primeriza, `0 = "en"`.

Nombres de los `key` como `snake_case`. Teoricamente, solo se necesitaran las configs creadas por defecto.

## `TagTable`
Etiquetas de textos.
- `id`
- `tag`: ejemplos `"hello" "bye" "title" "very-good-things"`
- Campos de control...
`hello`

El tag debera ser un string formateado, estilo `kebab-case`. El tag debe ser unico. De preferencia los tags en un solo idioma.


## `TranslationTagTable`
- `id`
- `language_id`
- `tag_id`
- `text`: String
- `is_active`
- Campos de control...

El `text`, podra ser cualquier string loco, `utf-8`.

- No mas de una columna, que contenga mismo `tag_id` y `language_id`.

---

# Flujo mental

```
Lenguaje de OS -> LanguageTable.code
    |
    V
ConfigTable -> language_id
    |
    V
TranslationTagTable -> TextTagTable.tag
    |
    V
TranslationTagTable.text
```

---

# `Models`
```
models/language_store/
    config_table.py
    language_table.py
    tag_table.py
    translation_tag_table.py
```


---

# Función principal
## `get_text( tag, language_code=None )`
- Si no se elige `language_code`, se establece el de `ConfigTable default_language_id`. 
- El parametro `tag`, da igual que string pongas puede ser `Hello   pipol`, se formateara como `hello-pipol`.
- Si no existe el `tag/text` para ese `language`, se usara el language `default`, si aun así no existe, se devolvera el `tag`.

Devolvera si o si un texto. Usara todo, o casi todo el `db`.