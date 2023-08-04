from Modulos import Modulo_Language as Lang
from Interface import Modulo_Util_Gtk as Util_Gtk

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Window_Main(Gtk.Window):
    def __init__(self):
        super().__init__( title=Lang.get_text('app') )
        self.set_resizable(True)
        self.set_default_size(256, -1)
        
        # Contenedor Principal
        vbox_main = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=8
        )
        
        # Secciones Verticales, Botones
        button_lang = Gtk.Button( label=Lang.get_text('lang') )
        button_lang.connect('clicked', self.evt_set_lang)
        vbox_main.pack_start(button_lang, False, True, 0)
        
        button_see_text = Gtk.Button( label=Lang.get_text('text') )
        button_see_text.connect('clicked', self.evt_see_text)
        vbox_main.pack_start(button_see_text, False, True, 0)
        
        # Seccion vertical final, boton para salir
        button_exit = Gtk.Button( label=Lang.get_text('exit') )
        button_exit.connect('clicked', self.evt_exit)
        vbox_main.pack_end(button_exit, False, True, 16)
        
        # Agragar contenedor principal
        self.add(vbox_main)
    
    def evt_set_lang(self, widget):
        dialog = Dialog_Select_Language(self)
        self.hide()
        dialog.run()
        dialog.destroy()
        self.show_all()
    
    def evt_see_text(self, widget):
        number = 0
        text = ''
        for key in (Lang.Language()).keys():
            number += 1
            text += (
                f'key - {key}\n'
                f'{number}. {Lang.get_text(key)}\n'
                '\n'
            )
        Util_Gtk.Dialog_TextView(self, text)
    
    def evt_exit(self, widget):
        self.destroy()


class Dialog_Select_Language(Gtk.Dialog):
    def __init__(
        self, parent
    ):
        super().__init__(
            title=f'{Lang.get_text("lang")}: {Lang.get_lang()}',
            transient_for=parent, flags=0
        )
        self.set_default_size(308, -1)
        
        # Contenedor Principal
        vbox_main = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=8
        )
        vbox_main.set_property('expand', True)
        
        # Secciones verticales, botones de idiomas
        button = None
        for text in Lang.List_Lang():
            button = Gtk.Button(label=text)
            button.connect('clicked', self.evt_set_lang)
            vbox_main.pack_start(button, False, True, 0)
            
        # Seccion Vertical final, boton language por defecto
        button = Gtk.Button(label=Lang.get_text('default'))
        button.connect('clicked', self.evt_set_lang)
        vbox_main.pack_end(button, False, True, 16)
        
        # Fin, mostrar todo y el contenedor principal
        self.get_content_area().add(vbox_main)
        self.show_all()
    
    def evt_set_lang(self, button):
        if button.get_label() == Lang.get_text('default'):    
            Lang.set_lang( '' )
        else:
            Lang.set_lang( button.get_label() )
        self.destroy()
        win.destroy()


win = Window_Main()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()