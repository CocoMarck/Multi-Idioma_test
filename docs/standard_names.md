# Nombres de variables, funciones, y clases. De todo.

### Las reglas gramaticales
Si se escribe en ingles algo, seguir reglas gramaticales del ingles. Eso aplica tambien si lo escribes en otro idioma.

La ventaja de escribir todo en ingles, es que el código sera legible para mas personas. Esto es casi necesario si haces proyectos `open source` y quieres que te coleboren.

No porque los que programan son nomas de habla inglesa, sino porque el ingles es muy hablado por todos los paises. Ademas incluso sin saber ingles, mucha gente programa en ingles.

---



# Nombres para base de datos
Usar estándar (`PEP8`, estilo `Python/PascalCase` para clases).

Para snake_case: `database`
Para PascalCase: `Database`
para camelCase: `database`

### Para las clases siempre se usa `PascalCase`
Para un model database. `StandardDatabase`, para su controller `StandardDatabaseController`

---




# Usar snake case casi todo
Para las var y funcs, solo usar snake_case:
```
var = bool

def good_state():
    ....
```

---




# Mayusculas + snake case para constantes
Para las constantes, no importa su tipo de valor, sus nombres son en mayusculas y `snake_case`:
```
CONSTANTE = str

CONSTANTE_DE_ALTO_RENDIMIENTO = str
```