# AGENTS.md

## Principio rector
- El código que el dev ya escribió tiene la última palabra. Si una convención de
  aquí contradice lo que el dev codificó, se respeta el código del dev y el cambio
  se recomienda solo como sugerencia futura.
- Este archivo es para RECORDAR y RECOMENDAR convenciones, no para imponer
  refactors grandes sin confirmar antes con el dev.

## Proyecto
- App de escritorio Avalonia 12 + .NET 10 (`net10.0`), SQLite
  (`Microsoft.Data.Sqlite`), logging por consola (`Microsoft.Extensions.Logging`).
- Capas: `Views` → `Controllers` → `Repositories` → `Core` / `Services` /
  `Entities` / `Utils` / `Config`.

## Estilo C# (moderno .NET)
- Namespaces en bloque estilo proyecto: `namespace Views.Forms {` (NO
  file-scoped). El namespace sigue la carpeta (`Views.Forms`,
  `Controllers.LangTags`, `Repositories.LangTags`, `Core.LangTags`,
  `Core.Sqlite`, `Core.Common`, `Entities.LangTags`, `Services.LangTags`,
  `Utils.Text`, `Config`, `Views`).
- Llaves: abrir `{` en la misma línea en namespaces y clases; mantener el estilo
  que el dev ya usa en los métodos (misma línea o siguiente).
- Naming:
  - PascalCase: clases, métodos, propiedades, `x:Name` del XAML.
  - `_camelCase`: campos privados.
  - `camelCase`: variables locales y parámetros.
- Moderno .NET: `var` cuando el tipo es obvio, `out var`, interpolación `$""`,
  `new()` target-typed, `using var` para `IDisposable`, nullables (`string?`,
  `object? sender`), argumentos con nombre en llamadas largas
  (`Execute(sql: ..., commit: true, ...)`).
- Comentarios: cortos, en español, marcando secciones (`// Constructor`,
  `// Methods`, `// EventHandlers`).

## Arquitectura
- Views (`.axaml` / `.axaml.cs`): solo UI + handlers; llaman al controller. Las
  vistas con tabla heredan de `Views.Forms.TableUserControl`.
- Controllers: reciben repository + entity + `ILogger`; envuelven en try/catch y
  loguean (`LogInformation` / `LogError`); implementan `ITableController` cuando
  manejan una tabla.
- Repositories: sin try/catch (crash intencional); normalizan inputs antes del
  SQL; usan `StandardDatabase` / `StandardTable`.
- La UI nunca brinca el Controller para tocar la base de datos.

## Normalizaciones del dominio
- Language codes: ISO 639-1 (2 letras minúsculas) vía `LanguageCodeNormalizer`.
- Tag names: kebab-case vía `TagNameNormalizer`.
- Fechas de control (`created_at` / `updated_at` / `deleted_at`): `TextualDateTime`.

## Verificación
- Compilar: `dotnet build`. Warnings conocidos que no bloquean: NU1903
  (SQLitePCLRaw), CS8625 (literales null).
