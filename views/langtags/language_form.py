from PyQt6 import QtWidgets, uic

# Rutas
from config.paths import LANGUAGE_FORM_UI

# Controlador
from controllers.langtags.language_controller import LanguageController

# Formulario
class LanguageForm( QtWidgets.QWidget ):
    def __init__(self, controller: LanguageController):
        super().__init__()

        self.resize( 16*64, 9*64 )
        self.setWindowTitle( 'language-form' )
        uic.loadUi( LANGUAGE_FORM_UI, self )

        self.controller = controller
        self.model  = self.controller.model

        # Texto
        self.entry_language_id.setText( str(self.model.language_id) )
        self.entry_code.setText( str(self.model.code) )
        self.label_created_at.setText( str(self.model.created_at) )
        self.label_updated_at.setText( str(self.model.updated_at) )
        self.label_deleted_at.setText( str(self.model.deleted_at) )
