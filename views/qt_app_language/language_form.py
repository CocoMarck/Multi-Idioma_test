from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import ( QTableWidget, QTableWidgetItem )

import sys, os

from utils import ResourceLoader
from utils.wrappers.language_wrapper import get_text
from core.text_util import ignore_text_filter, PREFIX_NUMBER

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
        self.id_entry.textChanged.connect( self.on_id_changed )
        self.save_button.clicked.connect( self.save_tag )

        self.combobox_tag.activated.connect( self.on_tag_changed )
        self.combobox_language.activated.connect( self.refresh_parameter )
        self.refresh_button.clicked.connect( self.refresh_all )
        
        self.current_id = None
        
        self.refresh_all()
    
    
    def clear_parameter(self):
        self.id_entry.clear()
        self.tag_entry.clear()
        self.text_entry.clear()
    
    
    def refresh_text(self):
        self.id_label.setText( get_text('id') )
        self.tag_label.setText( get_text('tag') )
        self.text_label.setText( get_text('text') )
        self.save_button.setText( get_text('save') )
        self.filter_button.setText( get_text('filter') )
        self.refresh_button.setText( get_text('refresh') )
    
    
    def refresh_combobox(self):
        self.combobox_tag.clear()
        self.combobox_language.clear()
        for row in self.table_controller.get_all_values():
            self.combobox_tag.addItem( row[1], userData=row[0] ) # tag, id
            
        language_number = 2
        for language in self.table_controller.get_all_columns()[language_number:]:
            self.combobox_language.addItem( language, userData=language_number )
            language_number += 1
            
            
    def refresh_parameter(self):
        if isinstance(self.current_id, int):
            for row in self.table_controller.get_all_values():
                if self.current_id == row[0]:
                    default_values = False
                    
                    # Establecer tag
                    self.tag_entry.setText( row[1] )
                    
                    # Establecer texto de tag
                    self.text_entry.setText( row[ self.combobox_language.currentData() ] )
                    
                    # Establecer tag del combobox, dependiendo del id
                    index_tag = self.combobox_tag.findData( self.current_id )
                    self.combobox_tag.setCurrentIndex( index_tag )
                    break
                else:
                    default_values = True
        else:
            default_values = True

        if default_values:
            self.clear_parameter()
    
    
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
        self.clear_parameter()
        self.refresh_text()
        self.refresh_combobox()
        self.refresh_parameter()
        self.refresh_table()
    
    
    def on_id_changed(self, text):
        '''
        Descartar cambio de ID, si no existe el id, y si no es un numero.
        '''
        self.id_entry.setText( ignore_text_filter(text, PREFIX_NUMBER ) )
        
        if self.id_entry.text() != "":
            self.current_id = int( self.id_entry.text() )
        else:
            self.current_id = None
        self.refresh_parameter()
    
    
    def on_tag_changed(self):
        self.current_id = self.combobox_tag.currentData()
        self.id_entry.setText( str(self.current_id) )
        self.refresh_parameter()
    
    
    def save_tag(self):
        save = self.table_controller.save_tag( 
            languageId=self.current_id, tag=self.tag_entry.text(), 
            text=self.text_entry.text(), language=self.combobox_language.currentText()
        )
        self.refresh_table()
        self.clear_parameter()
        self.refresh_parameter()
        self.refresh_combobox()
        self.refresh_text()