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
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QMessageBox,

    QSpacerItem,
    QSizePolicy
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
        self.button_rm_tag.clicked.connect( self.remove_tag )
        hbox.addWidget( self.button_rm_tag )
        
        hbox.addStretch()
        
        self.combobox_tag = QComboBox( )
        hbox.addWidget( self.combobox_tag )
        
        
        # Sección vertical boton obtener tag.
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        self.button_get_text = QPushButton()
        self.button_get_text.clicked.connect( self.get_text )
        hbox.addWidget(self.button_get_text)
        
        hbox.addStretch()
        
        self.label_get_text_tag = QLabel( )
        self.entry_get_text_tag = QLineEdit( )
        hbox.addWidget( self.label_get_text_tag )
        hbox.addWidget(self.entry_get_text_tag)
        

        # VBox, separacion
        #vbox_main.addStretch()
        

        # Tabla
        hbox = QHBoxLayout()
        vbox_main.addLayout( hbox )

        hbox.addStretch()
        self.label_table = QLabel()
        hbox.addWidget( self.label_table )
        hbox.addStretch()

        self.table = QTableWidget(self)
        self.table.setEditTriggers( QAbstractItemView.EditTrigger.NoEditTriggers )
        #self.table.setMinimumSize(636, 300) # Ajusta el tamaño según lo necesites
        #self.table.setSizePolicy( QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding )
        vbox_main.addWidget(self.table)
        
        
        # VBox, separacion
        #vbox_main.addStretch()


        # Seccion vertical | Ver texto
        self.button_see_text = QPushButton( )
        self.button_see_text.clicked.connect(self.see_text)
        vbox_main.addWidget(self.button_see_text)
        
        # Actualizar texto de widgets contenidos en la ventana main
        self.update()
        
        # Fin, Mostrar todo
        self.show()
        
    def init_text(self):
        '''
        Establecer el texto de todos los widgets que necesitan texto.
        '''
        self.button_see_text.setText( get_text('see-text') )
        self.button_rm_tag.setText( get_text('rm-tag') )
        self.button_add_tag.setText( get_text('add-tag') )
        self.button_get_text.setText( get_text('get-text') )
        
        self.label_set_lang.setText( get_text('set-lang') )
        self.label_tag.setText( get_text('tag') )
        self.label_tag_value.setText( get_text('value') )
        self.label_table.setText( get_text('db') )
        self.label_get_text_tag.setText( get_text('tag') )
        
        self.setWindowTitle( get_text('app') )
    
    def init_combobox(self):
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
    
    def init_table(self):
        self.table.clear()
        column_name = get_column_name()
        column_value_list = get_all_column_value()
        self.table.setColumnCount( len(column_name) )
        self.table.setHorizontalHeaderLabels( column_name )
        self.table.setRowCount( len(column_value_list) )
        row_number = 0
        for column_value in column_value_list:
            for index in range(0, len(column_value) ):
                self.table.setItem(
                    row_number, index, QTableWidgetItem( str(column_value[index]) )
                )
            row_number += 1

        
    def update(self):
        '''
        Actualizar todos los datos posibles.
        '''
        self.init_text()
        self.init_combobox()
        self.init_table()

    
    def set_lang(self):
        # Actualizar texto de widgets contenidos en la ventana main
        print( self.combobox_lang.currentText() )
        print( update_lang( self.combobox_lang.currentText() ) )
        self.init_text()
        self.init_combobox()
    
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
    
    def remove_tag(self):
        # Tag a eliminar
        tag = self.combobox_tag.currentText()
        message = (
            f'{get_text("quest-you-sure")}\n'
            f'{get_text("it-be-rm")}: {tag}'
        )
        
        # Preguntar si estas seguro
        input_quest = QMessageBox.question(
            self,
            get_text('rm-tag'),
            message,
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if input_quest == QMessageBox.StandardButton.Yes:
            # Eliminar tag
            delete_tag( tag )
            
            # Restablecer contador en la tabla.
            reindex_table_language()
            
            self.update()
        
        
    def get_text(self):
        # Obtener texto
        text = get_text( self.entry_get_text_tag.text(), self.combobox_lang.currentText() )

        if text != '':
            # Mostrar mensaje
            print(text)
            
            QMessageBox.information(
                self,
                get_text('text'), # titulo
                text # Texto de contenido
            )
        '''
        else:
            # Error, datos malos
            QMessageBox.critical(
                self,
                get_text('error'),
                get_text('bad-params')
            )
        '''
        

    
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