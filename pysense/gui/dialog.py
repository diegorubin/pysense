import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Dialog(Gtk.Dialog):

    def __init__(self, question):
        Gtk.Dialog.__init__(self, "Pysense", None, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(150, 100)

        label = Gtk.Label(question)

        self.entry = Gtk.Entry()
        self.entry.set_visibility(False)
        self.entry.set_invisible_char("*")
        self.entry.set_activates_default(True)

        ok_button = self.get_widget_for_response(response_id=Gtk.ResponseType.OK)
        ok_button.set_can_default(True)
        ok_button.grab_default()
        ok_button.connect("clicked", self.on_button_clicked)

        cancel_button = self.get_widget_for_response(response_id=Gtk.ResponseType.CANCEL)
        cancel_button.connect("clicked", self.on_button_clicked)

        box = self.get_content_area()
        box.add(label)
        box.add(self.entry)
        self.show_all()
        Gtk.main()

    def on_button_clicked(self, widget):
        self.hide()
        Gtk.main_quit()

    def value(self):
        return self.entry.get_text()

def ask(question):
    dialog = Dialog(question)
    return dialog.value()

