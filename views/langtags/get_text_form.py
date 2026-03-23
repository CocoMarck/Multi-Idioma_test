from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem

# Text util
from core.text_util import PREFIX_NUMBER, ignore_text_filter

# Rutas
from config.paths import GET_TEXT_FORM_UI

# Controller
from controllers.langtags.translation_controller import TranslationController

# Text
from utils.translation_util import get_text

# Formulario
class GetTextForm( QtWidgets.QWidget ):
    def __init__(self, controller: TranslationController, title='get-text-form' ):
        super().__init__()

        self._TITLE = title

        self.resize( 16*64, 9*64 )
        uic.loadUi( GET_TEXT_FORM_UI, self )

        self.controller = controller
        self.model = self.controller.model

        self.refresh_table()
        self.refresh_text()

        self.button_get_text.clicked.connect( self.on_get_text )

    def refresh_text(self):
        self.setWindowTitle( get_text(self._TITLE) )

        self.label_tag_name.setText( get_text('tag') )
        self.label_language_code.setText( get_text('language') )

        self.button_get_text.setText( get_text('get-text') )

    def refresh_table(self):
        columns = self.controller.get_view_columns()
        self.table.clear()
        self.table.setColumnCount( len(columns) )
        self.table.setHorizontalHeaderLabels( columns )
        self.table.resizeColumnsToContents()

        values = self.controller.get_view_rows()
        self.table.setRowCount( len(values) )
        for index in range(0, len(columns)):
            for row in range(0, len(values) ):
                value = values[row][index]
                text = str( value )
                self.table.setItem( row, index, QTableWidgetItem(text) )
                if isinstance(value, str):
                    self.table.setColumnWidth(index, 140)

    def refresh_all(self):
        self.refresh_table()
        self.refresh_text()

    def on_get_text(self):
        text = self.controller.get_text(
            tag_name=self.entry_tag_name.text(), language_code=self.entry_language_code.text()
        )
        self.label_get_text.setText( text )
