from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QTableWidget, QTableWidgetItem, QSizePolicy
)
from PyQt6.QtCore import QRect

from utils import ResourceLoader
from utils.wrappers.language_wrapper import get_text
from .language_form import LanguageForm 
from .language_config_form import LanguageConfigForm

from views.interface.interface_number_language import *
from views.interface.css_util import text_widget_style, get_list_text_widget


import sys, os



# Directorio
resource_loader = ResourceLoader()
file_ui = resource_loader.ui_dir.joinpath( 'main_language_window.ui' )




# Estilo
font = "Liberation Mono"
qss_style = ''
for widget in get_list_text_widget( 'Qt' ):
    qss_style += text_widget_style(
        widget=widget, font=font, font_size=num_font, 
        margin_based_font=False, padding=num_space_padding, idented=4,
        margin_xy=num_margin_xy
    )
# Agregar limite de ancho de combobox.
qss_style += (
    "\nQComboBox{\n"
    f"    min-width: {num_combobox_width}px;\n"
    f"    max-width: {num_combobox_width}px;\n"
    "}"
)




class LanguageApp( QtWidgets.QMainWindow ):
    def __init__(self):
        super().__init__()
        
        self.resize( nums_win_main[0], nums_win_main[1] )
        self.setWindowTitle( get_text('language') )
        uic.loadUi(file_ui, self)
        
        self.menubar.setGeometry( QRect( 0, 0, 960, 24) )
        
        self.menu_setting.setTitle( get_text("setting") )
        
        # Boton
        self.action_update_database.triggered.connect( self.refresh_all )
        
        # Index 0, 1
        self.language_form = LanguageForm()
        self.tab_widget.addTab( self.language_form, get_text("language-form") )
        
        self.language_config_form = LanguageConfigForm()
        self.tab_widget.addTab( self.language_config_form, get_text("language-config-form") )
        
        # Cambio de tab
        self.tab_widget.currentChanged.connect( self.on_tab_changed )
        
        # Texto
        self.refresh_text()
    

    def refresh_text(self):
        self.setWindowTitle( get_text('language') )

        self.menu_setting.setTitle( get_text("setting") )
        self.action_update_database.setText( get_text("update-database") )

        self.tab_widget.setTabText( 0, get_text("language-form") )
        self.tab_widget.setTabText( 1, get_text("language-config-form") )
    
    
    def on_tab_changed(self, index):
        '''
        Referscar tab
        '''
        self.refresh_text()

        if index == 0:
            self.language_form.refresh_all()
        elif index == 1:
            self.language_config_form.refresh_all()
    

    def refresh_all(self):
        self.refresh_text()
        self.language_form.refresh_all()
        self.language_config_form.refresh_all()