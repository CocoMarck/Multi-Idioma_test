from PyQt6 import QtWidgets, uic

# Rutas
from config.paths import MAIN_WINDOW_UI

# Controladores
from controllers.langtags.language_controller import LanguageController

# Formularios
from .language_form import LanguageForm

# Ventana
class MainWindow( QtWidgets.QMainWindow ):
    def __init__(self, language_controller: LanguageController):
        super().__init__()

        self.resize( 16*64, 9*64 )
        self.setWindowTitle( 'LangTags' )
        uic.loadUi( MAIN_WINDOW_UI, self )

        # Formularios
        self.language_form = LanguageForm( language_controller )
        self.tab_widget.addTab( self.language_form, 'language-form' )

        #self.tab_widget.currentChanged.connect(self.on_tab_changed)
