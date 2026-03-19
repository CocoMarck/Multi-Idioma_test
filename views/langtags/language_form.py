# Formulario base
from .base_form import BaseForm

# Controlador
from controllers.langtags.language_controller import LanguageController

# Formulario
class LanguageForm( BaseForm ):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, title='Langauge Form', **kwargs)
