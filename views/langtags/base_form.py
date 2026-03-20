from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem

# Text util
from core.text_util import PREFIX_NUMBER, ignore_text_filter

# Rutas
from config.paths import BASE_FORM_UI

# Controller
from controllers.langtags.base_controller import BaseController

# Formulario
class BaseForm( QtWidgets.QWidget ):
    def __init__(self, controller: BaseController, title='base-form' ):
        super().__init__()

        self.resize( 16*64, 9*64 )
        self.setWindowTitle( title )
        uic.loadUi( BASE_FORM_UI, self )

        self.controller = controller
        self.model = self.controller.model

        # Tables
        self.refresh_table()
        self.refresh_parameters()

        # Connects
        self.entry_id.textChanged.connect( self.on_id )
        self.entry_value.textChanged.connect( self.on_value )
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

    def refresh_parameters(self):
        self.entry_id.setText(
            str(self.controller.get_model_attribute('id')) if self.controller.get_model_attribute('id') else ""
        )
        self.entry_value.setText(
            str(self.controller.get_model_attribute('value')) if self.controller.get_model_attribute('value') else ""
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

    def clear_parameters(self, ignore_parameters=[]):
        parameters = [
            self.entry_id, self.entry_value, self.label_created_at, self.label_updated_at,
            self.label_deleted_at
        ]
        for p in parameters:
            if p in ignore_parameters:
                continue
            p.clear()
        self.checkbox_is_deleted.setChecked( False )

    def on_id(self, text):
        text = ignore_text_filter( text, PREFIX_NUMBER )
        self.entry_id.setText( text )
        if text:
            try:
                self.controller.get_row( int(text) )
            finally:
                self.refresh_parameters()
        else:
            self.clear_parameters( [self.entry_id] )

    def on_value(self, text):
        if not (self.entry_id.text()):
            if self.controller.get_value_row( text ):
                self.refresh_parameters()
            else:
                self.clear_parameters( [self.entry_value] )
        else:
            if not text:
                self.clear_parameters( [self.entry_value] )

    def on_save(self):
        row_id = None
        value = None
        is_deleted = self.checkbox_is_deleted.isChecked()
        if self.entry_id.text():
            row_id = int( self.entry_id.text() )
            value = self.entry_value.text()
        elif self.entry_value.text():
            value = self.entry_value.text()
        if value:
            save = self.controller.save( row_id, value, is_deleted )
            if save:
                self.refresh_parameters()
                self.refresh_table()

    def on_refresh(self):
        self.refresh_parameters()
        self.refresh_table()
