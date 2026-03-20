from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem

# Text util
from core.text_util import PREFIX_NUMBER, ignore_text_filter

# Rutas
from config.paths import TRANSLATION_FORM_UI

# Controller
from controllers.langtags.translation_controller import TranslationController

# Formulario
class TranslationForm( QtWidgets.QWidget ):
    def __init__(self, controller: TranslationController, title='translation-form' ):
        super().__init__()

        self.resize( 16*64, 9*64 )
        self.setWindowTitle( title )
        uic.loadUi( TRANSLATION_FORM_UI, self )

        self.controller = controller
        self.model = self.controller.model

        self.refresh_table()

        self.button_save.clicked.connect( self.on_save )

    def refresh_table(self):
        columns = self.controller.get_columns()
        self.table.clear()
        self.table.setColumnCount( len(columns) )
        self.table.setHorizontalHeaderLabels( columns )
        self.table.resizeColumnsToContents()

        values = self.controller.get_column_values()
        self.table.setRowCount( len(values) )
        for index in range(0, len(columns)):
            for row in range(0, len(values) ):
                value = values[row][index]
                text = str( value )
                self.table.setItem( row, index, QTableWidgetItem(text) )
                if isinstance(value, str):
                    self.table.setColumnWidth(index, 140)

    def on_save(self):
        row_id = None
        tag_name = self.entry_tag.text()
        language_code = self.entry_language.text()
        value = None
        is_deleted = self.checkbox_is_deleted.isChecked()
        if self.entry_value.text():
            value = self.entry_value.text()
        if value:
            save = self.controller.save_value( tag_name, language_code, value, is_deleted )
            if save:
                #self.refresh_parameters()
                self.refresh_table()
