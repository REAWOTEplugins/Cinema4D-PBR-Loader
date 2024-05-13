# -*- coding: utf-8 -*-
# #### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import os.path
import sys
import socket

import c4d
from c4d import plugins, bitmaps, threading, gui, PLUGINFLAG_COMMAND_OPTION_DIALOG

import time
import json

ROOT_DIR = os.path.split(__file__)[0]

REAWOTE_PLUGIN_ID=1056421
REAWOTE_APP_PORT=46515

texturepath=""

class CommandThread(c4d.threading.C4DThread):
    def Main(self):
        global texturepath
        src = os.path.join(ROOT_DIR, "src")
        if src not in sys.path: 
            sys.path.append(src)
        import reawotematerialloader as ReawoteFileLoader

        #     time.sleep(30)
        c4d.StatusClear()

class TimerMessage(c4d.plugins.MessageData):

    def GetTimer(self):
        return 100

    def CoreMessage(self, id, bc):
        global texturepath
        if id == REAWOTE_PLUGIN_ID:
            print("YES")
            print("Path is: " + texturepath)
            import reawotematerialloader as ReawoteFileLoader
            loader=ReawoteFileLoader.ReawoteFileLoader()
            loader.materialFolder=texturepath
            loader.HandleLoadMaterial()
        return True
    
if __name__=='__main__':
    src = os.path.join(ROOT_DIR, "src")
    if src not in sys.path: 
        sys.path.append(src)
    import reawotematerialloader as ReawoteMaterialLoader

    icon = c4d.bitmaps.BaseBitmap()
    icon.InitWith(os.path.join(ROOT_DIR, "res", "images", "icon.png"))

    loader=ReawoteMaterialLoader.ReawoteMaterialLoader()
    loader.thread=CommandThread()
    
    c4d.plugins.RegisterMessagePlugin(id=1234567, str="", info=0, dat=TimerMessage())

    c4d.plugins.RegisterCommandPlugin(id=REAWOTE_PLUGIN_ID, 
        str="Reawote PBR Loader",
        help="HELP",
        dat=loader, 
        info=0, 
        icon=icon)
    
    loader.thread.Start()
