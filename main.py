from controllers import LanguageDatabaseController, LanguageTableController, LanguageConfigTableController

from PyQt6.QtWidgets import QApplication
from views.qt_app_language.main_language_window import LanguageApp, qss_style
import sys


language_database = LanguageDatabaseController( )
language_database.start_database()

language_config_table = LanguageConfigTableController( )

# Abrir ventana
def main():
    app = QApplication( sys.argv )
    app.setStyleSheet( qss_style )
    window = LanguageApp()
    window.show()
    sys.exit( app.exec() )

if __name__ == '__main__':
    main()