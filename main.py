# python libs
from PyQt6.QtWidgets import QApplication
import pathlib
import sys

# Window
from views.langtags.main_window import MainWindow

# Establecer controladores
from utils.translation_util import tag_controller, language_controller, translation_controller, setting_controller, get_text

# Generación de DB
if __name__ == '__main__':
    app = QApplication( sys.argv )
    #app.setStyleSheet( STYLE_QSS )
    window = MainWindow( tag_controller, language_controller, translation_controller, setting_controller )
    window.show()
    sys.exit( app.exec() )
