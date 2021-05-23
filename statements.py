#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xbmc

"""
funtions

xbmc.executebuiltin(function)
xbmc.executeJSONRPC(jsonrpccommand)
xbmc.executescript(script)
xbmc.getCondVisibility(condition)
xbmc.getInfoLabel('infolabel')

"""

Myindex =      [
				{'title':'DailyMotion','function':'xbmc.executebuiltin','runcmd':'RunAddon(plugin.video.dailymotion_com,mode=sortVideos1&url=owner:Tv-Soap)'}
				]

Exampleindex = [
				{
				'title':'Run Youtube pluging',
				'function':'xbmc.executebuiltin',
				'runcmd':'RunAddon(plugin.video.youtube)'},

				{
				'title':'Run DailyMotion pluging',
				'function':'xbmc.executebuiltin',
				'runcmd':'RunAddon(plugin.video.dailymotion_com)'},

				{
				'title': 'JSONRPC cmd Get Favourites',
				'function':'xbmc.executeJSONRPC',
				'runcmd':'{"jsonrpc": "2.0", "method": "Favourites.GetFavourites", "params": {"properties": ["window", "path", "thumbnail", "windowparameter"]}, "id": 1}'},

				{
				'title':'JSONRPC cmd Get All Addons',
				'function':'xbmc.executeJSONRPC',
				'runcmd':'{"jsonrpc":"2.0","method":"Addons.GetAddons","params":{"properties":["path","enabled","dependencies"]},"id":1}'},
				{'title':'JSONRPC cmd Run DailyMotion plugin,with path','function':'xbmc.executeJSONRPC','runcmd':'{"jsonrpc": "2.0", "method": "Addons.ExecuteAddon", "params": {"addonid": "plugin.video.dailymotion_com", "params":["mode=sortVideos1","url=owner:Tv-Soap"]}, "id": 1}'},

				{
				'title':'Run Script via executescript func',
				'function':'xbmc.executescript',
				'runcmd':'special://home/addons/plugin.program.executable.methods/resources/lib/scripts/stop_note_start.py'},

				{
				'title':'System has Addon via getCondVisibility',
				'function':'xbmc.getCondVisibility',
				'runcmd':'System.HasAddon(plugin.video.youtube)'},

				{
				'title':'System IP address via getInfoLabel',
				'function':'xbmc.getInfoLabel',
				'runcmd':'Network.IPAddress'}
				]

