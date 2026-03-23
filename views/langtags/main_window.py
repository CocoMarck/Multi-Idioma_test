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

# Text
from utils.translation_util import get_text

# Ventana
class MainWindow( QtWidgets.QMainWindow ):
    def __init__(self, tag_controller: TagController, language_controller: LanguageController, translation_controller: TranslationController, setting_controller: SettingController ):
        super().__init__()

        self.resize( 16*64, 9*64 )
        self.setWindowTitle( 'LangTags' )
        uic.loadUi( MAIN_WINDOW_UI, self )

        # Formularios
        self.form_dict = {}
        self.tab_texts = []

        self.tag_form = TagForm( tag_controller )
        self.tab_texts.append('tag-form')
        self.tab_widget.addTab( self.tag_form, get_text(self.tab_texts[0]) )
        self.form_dict[0] = self.tag_form

        self.language_form = LanguageForm( language_controller )
        self.tab_texts.append('language-form')
        self.tab_widget.addTab( self.language_form, get_text(self.tab_texts[1]) )
        self.form_dict[1] = self.language_form

        self.translation_form = TranslationForm( translation_controller )
        self.tab_texts.append('translation-form')
        self.tab_widget.addTab( self.translation_form, get_text(self.tab_texts[2]) )
        self.form_dict[2] = self.translation_form

        self.get_text_form = GetTextForm( translation_controller )
        self.tab_texts.append('get-text-form')
        self.tab_widget.addTab( self.get_text_form, get_text(self.tab_texts[3]) )
        self.form_dict[3] = self.get_text_form

        self.setting_form = SettingForm( setting_controller )
        self.tab_texts.append('setting-form')
        self.tab_widget.addTab( self.setting_form, get_text(self.tab_texts[4]) )
        self.form_dict[4] = self.setting_form

        self.tab_widget.currentChanged.connect(self.on_tab_changed)

    def on_tab_changed(self, index):
        self.form_dict[index].refresh_all()
        self.tab_widget.setTabText( index, get_text(self.tab_texts[index]) )
