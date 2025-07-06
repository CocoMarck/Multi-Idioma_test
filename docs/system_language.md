# Obtener el lenguaje del sistema
La función `system_language` devuelve el lenguaje del sistema, con esta estructura:
`es, en, pt, ru`. Dos letrillas, o tres.

Podria ir en `core.system_util`, pero al ser algo tan especifico mejor seria algo como: `core.language_util`. Aunque para que no esta tan solito el modulo `language_util`, pos ponerle mas funciones utiles en el futuro.


```python
from core.system_util import get_system
import locale
import pycountry
def system_language():
    '''
    Obtener el lenguaje default del os. O el lenguaje establecido por el usuario.
    '''
    # Obtener lista de languaje default del OS y establecer el lang
    language = locale.getlocale()
    language = str(language[0])

    # Separar el el texto por _ y establecer el texto de la izq
    language = language.split('_')
    language = language[0]
    
    # Para windows
    if get_system() == 'win':
        object_country = pycountry.languages.get(name=language)
        language = object_country.alpha_2
    
    return language
```