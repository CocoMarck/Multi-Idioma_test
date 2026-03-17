from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem

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
        self.button_refresh.clicked.connect( self.refresh_parameters )

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

    def refresh_parameters(self):
        self.entry_language_id.setText( str(self.model.language_id) )
        self.entry_code.setText( str(self.model.code) )
        self.label_created_at.setText( str(self.model.created_at) )
        self.label_updated_at.setText( str(self.model.updated_at) )
        self.label_deleted_at.setText( str(self.model.deleted_at) )

    def on_language_id(self, text):
        if text:
            try:
                self.controller.get_row( int(text) )
            finally:
                self.refresh_parameters()
        else:
            self.clear_parameters( [self.entry_language_id] )


    def on_code(self, text):
        if self.controller.get_code_row( text ):
            self.refresh_parameters()
        else:
            self.clear_parameters( [self.entry_code] )
