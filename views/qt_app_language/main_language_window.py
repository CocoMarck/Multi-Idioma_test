from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import QRect

from utils import ResourceLoader
from utils.wrappers.language_wrapper import get_text
from .language_form import LanguageForm

import sys, os



# Directorio
resource_loader = ResourceLoader()
dir_views = resource_loader.get_base_path( 'views' )
dir_ui = dir_views.joinpath( 'ui' )
file_ui = dir_ui.joinpath( 'main_language_window.ui' )




class LanguageApp( QtWidgets.QMainWindow ):
    def __init__(self):
        super().__init__()
        
        self.resize( 960, 540 )
        self.setWindowTitle( get_text('language') )
        uic.loadUi(file_ui, self)
        
        self.menubar.setGeometry( QRect( 0, 0, 960, 24) )
        
        self.menu_setting.setTitle( get_text("setting") )
        
        self.language_form = LanguageForm()
        self.tab_widget.addTab( self.language_form, get_text("table") )