from PyQt6 import QtWidgets, uic

# Rutas
from config.paths import MAIN_WINDOW_UI

# Controladores
from controllers.langtags.language_controller import LanguageController
from controllers.langtags.tag_controller import TagController
from controllers.langtags.translation_controller import TranslationController
from controllers.langtags.setting_controller import SettingController

# Formularios
from .language_form import LanguageForm
from .tag_form import TagForm
from .translation_form import TranslationForm
from .get_text_form import GetTextForm
from .setting_form import SettingForm

# Ventana
class MainWindow( QtWidgets.QMainWindow ):
    def __init__(self, tag_controller: TagController, language_controller: LanguageController, translation_controller: TranslationController, setting_controller: SettingController ):
        super().__init__()

        self.resize( 16*64, 9*64 )
        self.setWindowTitle( 'LangTags' )
        uic.loadUi( MAIN_WINDOW_UI, self )

        # Formularios
        self.tag_form = TagForm( tag_controller )
        self.tab_widget.addTab( self.tag_form, 'tag-form' )

        self.language_form = LanguageForm( language_controller )
        self.tab_widget.addTab( self.language_form, 'language-form' )

        self.translation_form = TranslationForm( translation_controller )
        self.tab_widget.addTab( self.translation_form, 'translation-form' )

        self.get_text_form = GetTextForm( translation_controller )
        self.tab_widget.addTab( self.get_text_form, 'get-text-form' )

        self.setting_form = SettingForm( setting_controller )
        self.tab_widget.addTab( self.setting_form, 'setting-form' )

        #self.tab_widget.currentChanged.connect(self.on_tab_changed)
