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

from data.language import *
from interface.interface_number import *
from interface import Modulo_Util_Qt as Util_Qt


class Window_Main(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle( get_text('app') )
        self.resize( nums_win_main[0], nums_win_main[1] )
        
        # Contenedor Principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Secciones Verticales, botones de opcion
        self.button_lang = QPushButton( get_text('lang') )
        #self.button_lang.clicked.connect(self.set_lang)
        vbox_main.addWidget(self.button_lang)
        
        self.button_see_text = QPushButton( get_text('see-text') )
        self.button_see_text.clicked.connect(self.see_text)
        vbox_main.addWidget(self.button_see_text)
        
        # VBox, separacion de botones de opcion
        vbox_main.addStretch()
        
        # Seccion vertical final, Boton agregar y remover
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        self.label = QLabel( get_text('add-or-remove-tag') )
        hbox.addWidget( self.label )
        
        hbox.addStretch()
        
        self.button_add = QPushButton( get_text('add') )
        self.button_add.clicked.connect( self.add_or_remove_tag )
        hbox.addWidget( self.button_add )
        
        self.button_remove = QPushButton( get_text('remove') )
        hbox.addWidget( self.button_remove )
        
        # Actualizar texto de widgets contenidos en la ventana main
        self.update()
        
        # Fin, Mostrar todo
        self.show()
        
    def update(self):
        self.button_lang.setText( get_text('lang') )
        self.button_see_text.setText( get_text('see-text') )
        self.label.setText( get_text('add-or-remove-tag') )
        self.button_add.setText( get_text('add') )
        self.button_remove.setText( get_text('rm') )
    
    def set_lang():
        # Actualizar texto de widgets contenidos en la ventana main
        self.update()
        
        
    def add_or_remove_tag(self):
        print()
        self.update()

    
    def see_text(self):
        list_column = get_column_name()
        list_value = get_all_column_value()
        text = ''
        
        for x in list_value:
            for y in range( 0, len(x) ):
                text += f'{list_column[y]}: {x[y]}\n'
            text += '\n'

        Util_Qt.Dialog_TextEdit(
            parent=self,
            text=text,
            edit=False,
            size=nums_win_textedit,
        ).exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_Main()
    sys.exit(app.exec())