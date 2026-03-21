from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem

# Text util
from core.text_util import PREFIX_NUMBER, ignore_text_filter

# Rutas
from config.paths import GET_TEXT_FORM_UI

# Controller
from controllers.langtags.translation_controller import TranslationController

# Formulario
class GetTextForm( QtWidgets.QWidget ):
    def __init__(self, controller: TranslationController, title='get-text-form' ):
        super().__init__()

        self.resize( 16*64, 9*64 )
        self.setWindowTitle( title )
        uic.loadUi( GET_TEXT_FORM_UI, self )

        self.controller = controller
        self.model = self.controller.model

        self.refresh_table()

        self.button_get_text.clicked.connect( self.on_get_text )

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

    def on_get_text(self):
        text = self.controller.get_text(
            tag_name=self.entry_tag_name.text(), language_code=self.entry_language_code.text()
        )
        self.label_get_text.setText( text )
