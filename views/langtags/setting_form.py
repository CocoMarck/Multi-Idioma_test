from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem

# Text util
from core.text_util import PREFIX_NUMBER, ignore_text_filter

# Rutas
from config.paths import SETTING_FORM_UI

# Controller
from controllers.langtags.translation_controller import TranslationController

# Text
from utils.translation_util import get_text

# Formulario
class SettingForm( QtWidgets.QWidget ):
    def __init__(self, controller: TranslationController, title='setting-form' ):
        super().__init__()

        self._TITLE = title

        self.resize( 16*64, 9*64 )
        uic.loadUi( SETTING_FORM_UI, self )

        self.controller = controller
        self.model = self.controller.model

        self.refresh_table()
        self.refresh_parameters()
        self.refresh_text()

        self.combobox_languages.currentIndexChanged.connect( self.on_languages )

    def refresh_text(self):
        self.setWindowTitle( get_text(self._TITLE) )

        self.label_current_language.setText( get_text('current-language') )

    def refresh_table(self):
        columns = self.controller.get_columns()

        self.table.clear()
        self.table.setColumnCount( len(columns) )
        self.table.setHorizontalHeaderLabels( columns )
        self.table.resizeColumnsToContents()

        values = self.controller.get_rows()
        self.table.setRowCount( len(values) )
        for index in range(0, len(columns)):
            for row in range(0, len(values) ):
                value = values[row][index]
                text = str( value )
                self.table.setItem( row, index, QTableWidgetItem(text) )
                if isinstance(value, str):
                    self.table.setColumnWidth(index, 140)

    def refresh_languages(self):
        dictionary = self.controller.get_language_dict()
        self.combobox_languages.clear()
        for code in dictionary:
            self.combobox_languages.insertItem(dictionary[code], code)

        return dictionary


    def refresh_parameters(self):
        dictionary = self.refresh_languages()
        self.controller.get_current_language_model()
        self.combobox_languages.setCurrentIndex( self.model.language_id )

    def refresh_all(self):
        self.refresh_table()
        self.refresh_text()

    def on_languages(self, index):
        self.controller.update_current_language_id( index )
        self.refresh_table()
