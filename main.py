from controllers import LanguageDatabaseController, LanguageTableController, LanguageConfigTableController

from PyQt6.QtWidgets import QApplication
from views.qt_app_language.main_language_window import LanguageApp
import sys


language_database = LanguageDatabaseController( log_level="warning" )
language_database.start_database()

language_config_table = LanguageConfigTableController( log_level="warning" )
language_config_table.update_language( "system" )
print( language_config_table.get_language() )

# Abrir ventana
def main():
    app = QApplication( sys.argv )
    #app.setStyleSheet( )
    window = LanguageApp()
    window.show()
    sys.exit( app.exec() )

if __name__ == '__main__':
    main()