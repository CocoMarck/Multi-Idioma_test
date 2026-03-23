from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem

# Text util
from core.text_util import PREFIX_NUMBER, ignore_text_filter

# Rutas
from config.paths import TRANSLATION_FORM_UI

# Controller
from controllers.langtags.translation_controller import TranslationController

# Text
from utils.translation_util import get_text

# Formulario
class TranslationForm( QtWidgets.QWidget ):
    def __init__(self, controller: TranslationController, title='translation-form' ):
        super().__init__()

        self._TITLE = title

        self.resize( 16*64, 9*64 )
        uic.loadUi( TRANSLATION_FORM_UI, self )

        self.controller = controller
        self.model = self.controller.model

        self.refresh_table()
        self.refresh_text()

        self._PARAMETERS = [
            self.label_translation_id_text, self.entry_tag, self.entry_language, self.entry_value, self.label_created_at, self.label_updated_at, self.label_deleted_at
        ]

        self.button_save.clicked.connect( self.on_save )
        self.entry_tag.textChanged.connect( self.get_translation_row )
        self.entry_language.textChanged.connect( self.get_translation_row )
        self.button_refresh.clicked.connect( self.refresh_table )

    def refresh_text(self):
        self.setWindowTitle( get_text(self._TITLE) )

        self.label_tag.setText( get_text('tag') )
        self.label_language.setText( get_text('language') )
        self.label_value.setText( get_text('value') )

        self.checkbox_is_deleted.setText( get_text('is-deleted') )
        self.button_save.setText( get_text('save') )
        self.button_refresh.setText( get_text('refresh') )

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

    def refresh_parameters(self):
        self.label_translation_id_text.setText(
            str(self.model.translation_id) if self.model.translation_id else ""
        )
        self.entry_tag.setText(
            str(self.controller.get_tag_name( self.model.tag_id ))
        )
        self.entry_language.setText(
            str(self.controller.get_language_code( self.model.language_id ))
        )
        self.entry_value.setText(
            str(self.model.value) if self.model.value else ""
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

    def refresh_all(self):
        self.refresh_table()
        self.refresh_text()

    def clear_parameters(self, ignore_parameters=[]):
        for p in self._PARAMETERS:
            if p in ignore_parameters:
                continue
            p.clear()
        self.checkbox_is_deleted.setChecked( False )

    def get_translation_row( self):
        tag = self.entry_tag.text()
        language = self.entry_language.text()

        getting_row = False
        if tag and language:
            getting_row = self.controller.get_translation_row( tag, language )

        if getting_row:
            self.refresh_parameters()
        else:
            self.clear_parameters( [self.entry_tag, self.entry_language] )

        return getting_row

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
                self.refresh_parameters()
                self.refresh_table()
