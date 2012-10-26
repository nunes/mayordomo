#!/usr/bin/env python
import os
import pythoncom
import time
import wx

if os.name == 'posix':
    import pyxhook as hooklib
elif os.name == 'nt':
    import pyHook as hooklib
else:
    print "OS is not recognised as windows or linux."
    exit()

try:
    import win32gui
    useWin32gui = True
except ImportError:
    useWin32gui = False


ID_ICON_TIMER = wx.NewId()

class TaskBarFrame(wx.Frame):
    def __init__(self, parent, iconPath):
        wx.Frame.__init__(self, parent, style=wx.FRAME_NO_TASKBAR | wx.NO_FULL_REPAINT_ON_RESIZE)

        self.tbicon = wx.TaskBarIcon()
        icon = wx.Icon(iconPath, wx.BITMAP_TYPE_ICO)
        self.tbicon.SetIcon(icon, '')
        wx.EVT_TASKBAR_LEFT_UP(self.tbicon, self.OnTaskBarLeftUp)

        self.icontimer = wx.Timer(self, ID_ICON_TIMER)
        wx.EVT_TIMER(self, ID_ICON_TIMER, self.GetCurrentWindowName)
        self.icontimer.Start(100)

        self.Show(True)

    def OnTaskBarLeftUp(self, evt):
        print self.currentWindow


    def GetCurrentWindowName(self, evt):
        if useWin32gui:
            newName = win32gui.GetWindowText (win32gui.GetForegroundWindow())
            if newName:
                self.currentWindow = newName

def OnKeyboardEvent(event):
    print 'MessageName: ', event.MessageName, ', Key ', event.Key
    return True


def OnMouseEvent(event):
    # called when mouse events are received
    print 'MessageName:', event.MessageName, ', Position: ', event.Position
    return True


def startUp(iconPath='./images/administrator.ico'):
    hm = hooklib.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()

    hm.MouseMove = OnMouseEvent
    hm.HookMouse()

    app = wx.App(False)
    TaskBarFrame(None, iconPath).Show(False)
    app.MainLoop()


