import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QPushButton,
    QLabel,
    QComboBox,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout
)

from data.language import *
from interface.interface_number import *
from interface import Modulo_Util_Qt as Util_Qt


class Window_Main(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize( nums_win_main[0], nums_win_main[1] )
        
        # Contenedor Principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Secciones Vertical, Seleccionar lenguaje
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        self.label_set_lang = QLabel()
        hbox.addWidget(self.label_set_lang)
        
        self.combobox_lang = QComboBox()
        self.combobox_lang.activated.connect(self.set_lang)
        hbox.addWidget(self.combobox_lang)




        # Seccion vertical, Boton agregar tag
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        self.button_add_tag = QPushButton( )
        self.button_add_tag.clicked.connect( self.add_tag )
        hbox.addWidget( self.button_add_tag )
        
        hbox.addStretch()
        
        self.label_tag = QLabel()
        hbox.addWidget( self.label_tag )

        self.entry_tag = QLineEdit()
        hbox.addWidget( self.entry_tag )
        
        self.label_tag_value = QLabel()
        hbox.addWidget( self.label_tag_value )

        self.entry_tag_value = QLineEdit()
        hbox.addWidget( self.entry_tag_value )
        



        # Sección vertical Boton remover
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        self.button_rm_tag = QPushButton( )
        hbox.addWidget( self.button_rm_tag )
        
        hbox.addStretch()
        
        self.combobox_tag = QComboBox( )
        hbox.addWidget( self.combobox_tag )
        



        # VBox, separacion
        vbox_main.addStretch()
        



        # Seccion vertical | Ver texto
        self.button_see_text = QPushButton( )
        self.button_see_text.clicked.connect(self.see_text)
        vbox_main.addWidget(self.button_see_text)
        
        # Actualizar texto de widgets contenidos en la ventana main
        self.start_combobox()
        self.update()
        
        # Fin, Mostrar todo
        self.show()
        
    def set_text(self):
        '''
        Establecer el texto de todos los widgets que necesitan texto.
        '''
        self.button_see_text.setText( get_text('see-text', get_lang()) )
        self.button_rm_tag.setText( get_text('rm-tag', get_lang()) )
        self.button_add_tag.setText( get_text('add-tag', get_lang()) )
        self.label_set_lang.setText( get_text('set-lang', get_lang()) )
        self.label_tag.setText( get_text('tag', get_lang()) )
        self.label_tag_value.setText( get_text('value', get_lang()) )
        self.setWindowTitle( get_text('app', get_lang()) )
    
    def start_combobox(self):
        '''
        Establecer opciones a los combobox.
        '''
        self.combobox_lang.clear()
        index = 0
        index_to_set = None
        for lang in get_available_lang():
            self.combobox_lang.addItem(lang)
            if lang == get_lang() and index_to_set == None:
                index_to_set = index
            index += 1
        if index_to_set != None:
            self.combobox_lang.setCurrentIndex(index_to_set)
            
        self.combobox_tag.clear()
        for tag in get_all_tag():
            print(tag)
            self.combobox_tag.addItem(tag)

        
    def update(self):
        '''
        Actualizar todos los datos posibles.
        '''
        self.set_text()
        self.start_combobox()

    
    def set_lang(self):
        # Actualizar texto de widgets contenidos en la ventana main
        print( self.combobox_lang.currentText() )
        print( update_lang( self.combobox_lang.currentText() ) )
        self.set_text()
        self.update()
    
    def add_tag(self):
        print( self.combobox_lang.currentText() )
        instruction = insert_tag( 
            self.entry_tag.text(), 
            self.combobox_lang.currentText(), 
            self.entry_tag_value.text() 
        )
        print(instruction)
        self.entry_tag.clear()
        self.entry_tag_value.clear()
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