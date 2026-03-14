# Base de datos `langtags.sqlite`
Para traducir aplicaciones, con sqlite3.

### Campos de control
- `created_at`: Fecha de creación
- `updated_at`: Fecha de modificación
- `deleted_at`: Fecha de baja lógica

> Si `deleted_at` `IS NULL`: existe. Si no, esta de baja.

## Tablas
### `languages`
| `language_id` | `code` | *CAMPOS DE CONTROL...*
|---------------|--------|--|

### `tags`
| `tag_id` | `tag_key` | *CAMPOS DE CONTROL...*
|----------|-----------|--|

### `translations`
| `translation_id` | `tag_id` | `language_id` | `value` | *CAMPOS DE CONTROL...*
|------------------|---------------|--------------|--|--|

### `settings`
| `setting_id` | `parameter_name`   | `language_id` |
|-------------|---------------------|---------------|
| `1`         | `default_language`  | `1`           |
| `2`         | `selected_language` | `4`           |



---
# Función principal `get_text( tag, language )`

Se espera de parametros tanto `tag`, como `language`. La Busqueda sera por texto de tag o language. Por defecto language, sera el de la tabla `settings`. `get_text` sera a prueba de crash, si no existe tag o language, o en nada, devolver texto siempre, devolver tag.

Ejemplos:
```python
get_text('exit', 'es') = 'Salir'
get_text('exit', 'en') = 'Exit'
```