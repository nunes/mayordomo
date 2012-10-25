#!/usr/bin/env python

#import win32gui
#import time
#import wx
#
#w=win32gui
#time.sleep(1)
#
#print w.GetWindowText (w.GetForegroundWindow())
#
#app = wx.App(False)
#frame = wx.Frame(None, wx.ID_ANY, "Hello World")
#frame.Show(True)
#app.MainLoop()


import wx
import win32gui
import time

ID_ICON_TIMER = wx.NewId()

class TaskBarFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, style=wx.FRAME_NO_TASKBAR | wx.NO_FULL_REPAINT_ON_RESIZE)

        self.tbicon = wx.TaskBarIcon()
        icon = wx.Icon('administrator.ico', wx.BITMAP_TYPE_ICO)
        self.tbicon.SetIcon(icon, '')
        wx.EVT_TASKBAR_LEFT_DCLICK(self.tbicon, self.OnTaskBarLeftDClick)
        self.Show(True)

    def OnTaskBarLeftDClick(self, evt):
        w=win32gui
        time.sleep(1)
        print w.GetWindowText (w.GetForegroundWindow())
        
app = wx.App(False)
TaskBarFrame(None).Show(False)
app.MainLoop()
