#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from urllib.parse import parse_qs,quote_plus
import json
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

import statements




__addon__ = xbmcaddon.Addon('plugin.program.executable.methods')


def MainMenu():
	AddDir('Examples','int_menu_Exampleindex','',isFolder=True)
	AddDir('My Test Menu','int_menu_Myindex','',isFolder=True)

def ExampleMenu():
	for i in statements.Exampleindex:
		AddDir(i.get('title'),i.get('function'),i.get('runcmd'))

def MyMenu():
	for i in statements.Myindex:
		AddDir(i.get('title'),i.get('function'),i.get('runcmd'))

def AddDir(title,runFunc,runCMD,isFolder=False):
	if runFunc == 'xbmc.executebuiltin':
		runCMD = quote_plus(runCMD)
	u = f'{sys.argv[0]}?title={quote_plus(title)}&runFunc={runFunc}&runCMD={runCMD}'
	liz=xbmcgui.ListItem(title)
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)


def Log(msg):
	from inspect import getframeinfo, stack
	fileinfo = getframeinfo(stack()[1][0])
	xbmc.log('*__{}__{}*{} Python file name = {} Line Number = {}'.format(__addon__.getAddonInfo('name'),__addon__.getAddonInfo('version'),msg,fileinfo.filename,fileinfo.lineno), level=xbmc.LOGINFO)

Log(sys.argv[2][1:])
args    = parse_qs(sys.argv[2][1:])
runFunc = args.get('runFunc', None)
runCMD  = args.get('runCMD',None)
if runFunc:
	runFunc = (runFunc[0])
if runCMD:
	runCMD = (runCMD[0])

try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_DATE)
except:
    pass

Log(f'runFunc={runFunc} runcmd={runCMD}')
if runFunc==None:
	MainMenu()
elif runFunc=='int_menu_Exampleindex':
	ExampleMenu()
elif runFunc=='int_menu_Myindex':
	MyMenu()
elif runFunc=='xbmc.executebuiltin':
	xbmc.executebuiltin(runCMD)
elif runFunc=='xbmc.executeJSONRPC':
	Log(xbmc.executeJSONRPC(runCMD))
	xbmcgui.Dialog().textviewer('xbmc.executeJSONRPC',f'[I][COLOR blue]Method[/COLOR][/I]\n{json.dumps(json.loads(runCMD),indent=2)}\n[I][COLOR blue]Output[/COLOR][/I]\n {json.dumps(json.loads(xbmc.executeJSONRPC(runCMD)),indent=2)}')
elif runFunc=='xbmc.executescript':
	xbmc.executescript(runCMD)
elif runFunc=='xbmc.getCondVisibility':
	xbmcgui.Dialog().ok('xbmc.getCondVisibility',f'{runCMD} is {xbmc.getCondVisibility(runCMD)}')
elif runFunc=='xbmc.getInfoLabel':
	xbmcgui.Dialog().ok('xbmc.getInfoLabel',f'Return for [COLOR blue]{runCMD}[/COLOR] is [COLOR green]{xbmc.getInfoLabel(runCMD)}[/COLOR]')
xbmcplugin.endOfDirectory(int(sys.argv[1]))	
	
