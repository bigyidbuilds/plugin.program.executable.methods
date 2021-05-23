#!/usr/bin/python3
# -*- coding: utf-8 -*-
from xbmc import executebuiltin,sleep
from xbmcgui import Dialog

executebuiltin("ActivateWindow(Home)")
sleep(500)
Dialog().notification('Example script','The addon will restart now')
sleep(500)
executebuiltin("RunAddon(plugin.program.executable.methods,runFunc=int_menu_Exampleindex)")
