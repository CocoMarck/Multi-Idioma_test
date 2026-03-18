from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem

# Text util
from core.text_util import PREFIX_NUMBER, ignore_text_filter

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
        self.refresh_parameters()
        self.refresh_table()

        # Connects
        self.entry_language_id.textChanged.connect( self.on_language_id )
        self.entry_code.textChanged.connect( self.on_code )
        self.button_refresh.clicked.connect( self.on_refresh )
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

    def clear_parameters(self, ignore_parameters=[]):
        parameters = [
            self.entry_language_id, self.entry_code, self.label_created_at, self.label_updated_at,
            self.label_deleted_at
        ]
        for p in parameters:
            if p in ignore_parameters:
                continue
            p.clear()
        self.checkbox_is_deleted.setChecked( False )

    def refresh_parameters(self):
        self.entry_language_id.setText(
            str(self.model.language_id) if self.model.language_id else ""
        )
        self.entry_code.setText(
            str(self.model.code) if self.model.code else ""
        )
        self.label_created_at.setText(
            str(self.model.created_at) if self.model.created_at else ""
        )
        self.label_updated_at.setText(
            str(self.model.updated_at) if self.model.updated_at else ""
        )
        self.label_deleted_at.setText(
            str(self.model.deleted_at) if self.model.deleted_at else ""
        )
        self.checkbox_is_deleted.setChecked( self.controller.is_model_deleted() )

    def on_language_id(self, text):
        text = ignore_text_filter( text, PREFIX_NUMBER )
        self.entry_language_id.setText( text )
        if text:
            try:
                self.controller.get_row( int(text) )
            finally:
                self.refresh_parameters()
        else:
            self.clear_parameters( [self.entry_language_id] )

    def on_code(self, text):
        if not (self.entry_language_id.text()):
            if self.controller.get_code_row( text ):
                self.refresh_parameters()
            else:
                self.clear_parameters( [self.entry_code] )

    def on_save(self):
        row_id = None
        code = None
        is_deleted = self.checkbox_is_deleted.isChecked()
        if self.entry_language_id.text():
            row_id = int( self.entry_language_id.text() )
            code = self.entry_code.text()
        elif self.entry_code.text():
            code = self.entry_code.text()
        if code:
            save = self.controller.save( row_id, code, is_deleted )
            if save:
                self.refresh_parameters()
                self.refresh_table()

    def on_refresh(self):
        self.refresh_parameters()
        self.refresh_table()
