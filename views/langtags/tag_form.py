# Formulario
from .base_form import BaseForm

# Controller
from controllers.langtags.tag_controller import TagController

# Formulario
class TagForm( BaseForm ):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, title='Tag Form', **kwargs)
