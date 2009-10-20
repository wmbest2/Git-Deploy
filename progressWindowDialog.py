import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import gobject

import os,sys

class ProgressWindowDialog:
    def _performOperation(self):
        self.prgOperationProgress.set_fraction(0.25)
        self.operation(self.param)
        self.prgOperationProgress.set_fraction(1)
        self.btnOkay.set_sensitive(True)

    def onBtnOkayClicked(self, widget, data = None):
        self.window.destroy()

    def deleteEvent(self, widget, event, data = None):
        self.window.destroy()

    def __init__(self, operation, param):
        # Pull widgets from Glade
        glade = gtk.glade.XML(os.path.abspath(sys.path[0]) + '/glade/mainWindow.glade')

        self.btnOkay = glade.get_widget('btnOkay')
        self.prgOperationProgress = glade.get_widget('prgOperationProgress')
        self.lblTitle = glade.get_widget('lblTitle')
        self.window = glade.get_widget('wndProgressDialog')

        # Disable the okay button
        self.btnOkay.set_sensitive(False)

        glade.signal_autoconnect(self)

        self.operation = operation
        self.param = param

        # Display the window
        self.window.show_all()
        self._performOperation()
