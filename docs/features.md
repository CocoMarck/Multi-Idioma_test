# Features

## Importante
Durante todo este proceso de crear mi DB para textos pa apps. Me di cuenta, que mi `StandarDatabase` ta bueno, pero el usar `repo x` y `repo y`, en `repo h`, lo puedo evitar un monton, nomas con querys. Y que añadir constantes de `name` de `tables` y `parameters`, ta hasta mejor evitarlo. La proxima vez, intentare solo usar `StandardDatabase` para crear mis repos de tablas, y usar a full los `querys`, para evitar depeder de repos en un repo. Es lo mas legible, y lo mejor para el coco del pc.

No estoy manejando un `text file`, toy manejando un `sql file`. Es completamente diferente.

---

## Modulos
- Crear para los filtros un modulo `repositories.lantags.text_filters`

---
## Tags
- `name` de tags tipo `kebab-case`, en minusculas, nada de `KebAb-caSE`.
- No permitir string de tag con numeros. Solo abecedario español.
- No permitir string de tag vacio `""`, no guarde eso, ta feo.

---
## Languages
- Formateo de lenguajes tipo `ISO 639-1`. `kebab-case`. Ejemplos: `es, en, pt, ru, zh`.
- Hacer que directamente solo elimine espacios, y que solo acepte abecedario en minusculas.

