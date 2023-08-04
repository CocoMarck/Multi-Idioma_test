import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

from Modulos import Modulo_Language as Lang
from Interface import Modulo_Util_Qt as Util_Qt


class Window_Main(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle(Lang.get_text('app'))
        self.resize(256, 128)
        
        # Contenedor Principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Secciones Verticales, botones de opcion
        button_lang = QPushButton( Lang.get_text('lang') )
        button_lang.clicked.connect(self.evt_set_lang)
        vbox_main.addWidget(button_lang)
        
        button_see_text = QPushButton( Lang.get_text('text') )
        button_see_text.clicked.connect(self.evt_see_text)
        vbox_main.addWidget(button_see_text)
        
        # VBox, separacion de botones de opcion, y boton de salir
        vbox_main.addStretch()
        
        # Seccion vertical final, boton para salir
        button_exit = QPushButton( Lang.get_text('exit') )
        button_exit.clicked.connect(self.evt_exit)
        vbox_main.addWidget(button_exit)
        
        # Fin, Mostrar todo
        self.show()
        
    def evt_set_lang(self):
        self.hide()
        Dialog_Select_Language(self).exec()
        self.show()
    
    def evt_see_text(self):
        number = 0
        text = ''
        for key in (Lang.Language()).keys():
            text += (
                f'key - {key}\n'
                f'{number}. {Lang.get_text(key)}\n'
                '\n'
            )
        Util_Qt.Dialog_TextEdit(self, text).exec()
    
    def evt_exit(self):
        self.close()


class Dialog_Select_Language(QDialog):
    def __init__ (
        self, parent=None
    ):
        super().__init__(parent)
        self.setWindowTitle(
            f'{Lang.get_text("lang")}: {Lang.get_lang()}',
        )
        self.resize(256, -1)
        
        # Contenedor Principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Secciones Verticales, Botones de idiomas
        self.button = None
        for text in Lang.List_Lang():
            self.button = QPushButton(text)
            self.button.clicked.connect(self.evt_set_lang)
            vbox_main.addWidget(self.button)
            
        # VBox Separacion
        vbox_main.addStretch()
        
        # Seccion Vertical final, boton de lenguaje por defecto
        self.button = QPushButton( Lang.get_text('default') )
        self.button.clicked.connect(self.evt_set_lang)
        vbox_main.addWidget(self.button)
    
    def evt_set_lang(self):
        button = app.sender()
        if isinstance(button, QPushButton):
        # Si la señal del widget es un boton
            if button.text() == Lang.get_text('default'):
                Lang.set_lang('')
            else:
                Lang.set_lang( button.text() )
            self.close()
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_Main()
    sys.exit(app.exec())