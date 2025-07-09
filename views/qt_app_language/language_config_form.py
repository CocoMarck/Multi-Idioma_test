from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import ( QTableWidget, QTableWidgetItem )


import os, sys

from utils import ResourceLoader
from utils.wrappers.language_wrapper import get_text
from core.text_util import ignore_text_filter, PREFIX_NUMBER

from controllers import LanguageConfigTableController


# Recursos
resource_loader = ResourceLoader()
file_ui = resource_loader.ui_dir.joinpath( 'language_config_form.ui' )


class LanguageConfigForm( QtWidgets.QWidget ):
    def __init__(self):
        super().__init__()
        
        self.resize( 960, 540 )
        self.setWindowTitle( get_text("language-config-form") )
        uic.loadUi( file_ui, self )
        
        self.table_controller = LanguageConfigTableController()
        
        self.refresh_all()
    
    
    def refresh_text(self):
        self.language_label.setText( get_text("language") )
        self.current_language_label.setText( self.table_controller.get_language() )
        self.select_language_label.setText( get_text("select-language") )
    
    
    def refresh_combobox(self):
        self.language_combobox.clear()
        for language in self.table_controller.get_list_of_languages():
            self.language_combobox.addItem( language )
        

    def refresh_table(self):
        all_columns = self.table_controller.get_all_columns()
        self.table.clear()
        self.table.setColumnCount( len(all_columns) )
        self.table.setHorizontalHeaderLabels( all_columns )
        self.table.resizeColumnsToContents()
        
        all_values = self.table_controller.get_all_values()
        self.table.setRowCount( len(all_values) )
        number = 0
        for column in all_columns:
            for row in range(0, len(all_values)):
                final_text = str( all_values[row][number] )
                self.table.setItem( row, number, QTableWidgetItem( final_text ) )
            number += 1
        
        
    def refresh_all(self):
        self.refresh_text()
        self.refresh_table()
        self.refresh_combobox()