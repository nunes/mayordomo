#!/usr/bin/env python
import time
import wx

try: import win32gui
except ImportError:
    pass


class TaskBarFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, style=wx.FRAME_NO_TASKBAR | wx.NO_FULL_REPAINT_ON_RESIZE)

        self.tbicon = wx.TaskBarIcon()
        icon = wx.Icon('../images/administrator.ico', wx.BITMAP_TYPE_ICO)
        self.tbicon.SetIcon(icon, '')
        wx.EVT_TASKBAR_LEFT_DCLICK(self.tbicon, self.OnTaskBarLeftDClick)
        self.Show(True)

    def OnTaskBarLeftDClick(self, evt):
        time.sleep(1)
        print self.GetWindowName()

    def GetWindowName(self):
        return win32gui.GetWindowText (win32gui.GetForegroundWindow())

app = wx.App(False)
TaskBarFrame(None).Show(False)
app.MainLoop()
