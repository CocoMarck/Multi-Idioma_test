from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import ( QTableWidget, QTableWidgetItem )

import sys, os

from utils import ResourceLoader
from utils.wrappers.language_wrapper import get_text

from controllers import LanguageTableController


# Recursos
resource_loader = ResourceLoader()
dir_views = resource_loader.get_base_path( 'views' )
dir_ui = dir_views.joinpath( 'ui' )
file_ui = dir_ui.joinpath( 'language_form.ui' )


language_table_controller = LanguageTableController()



# Ventana
class LanguageForm( QtWidgets.QWidget ):
    def __init__(self):
        super().__init__()
        
        self.resize( 960, 540 )
        self.setWindowTitle( get_text("language-form") )
        uic.loadUi( file_ui, self )
        
        self.table_controller = language_table_controller
        
        self.refresh_all()
    
    
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
        self.refresh_table()