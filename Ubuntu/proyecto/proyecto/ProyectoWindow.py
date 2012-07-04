# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('proyecto')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('proyecto')

from proyecto_lib import Window
from proyecto.AboutProyectoDialog import AboutProyectoDialog
from proyecto.PreferencesProyectoDialog import PreferencesProyectoDialog

# See proyecto_lib.Window.py for more details about how this class works
class ProyectoWindow(Window):
    __gtype_name__ = "ProyectoWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(ProyectoWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutProyectoDialog
        self.PreferencesDialog = PreferencesProyectoDialog

        # Code for other initialization actions should be added here.

    def urlentry_activate_cb(self, widget):
        print widget.get_text()

    def addbutton_clicked_cb(self, widget):
        print "add"

    def refreshbutton_clicked_cb(self, widget):
        print "refresh"
