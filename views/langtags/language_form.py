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
        self.table  = self.controller.table

        # Texto
        self.entry_language_id.setText( str(self.table.language_id) )
        self.entry_code.setText( str(self.table.code) )
        self.label_created_at.setText( str(self.table.created_at) )
        self.label_updated_at.setText( str(self.table.updated_at) )
        self.label_deleted_at.setText( str(self.table.deleted_at) )
