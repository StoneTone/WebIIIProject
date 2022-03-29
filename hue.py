import wx
from phue import Bridge
import random as r
from time import sleep

"""Connecting to the bridge"""
bridge = Bridge("192.168.4.20")
bridge.connect()

"""
Getting the specific names for the lights without 
having to use the numbers
"""
lights = bridge.get_light_objects('name')

"""
for x in range(100):
    lights["Light Strip"].hue = r.randint(1,16000)
    lights["Outside Light"].hue = r.randint(1,16000)
    sleep(1)
"""
class Window(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Philips Hue")
        
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5,5))
        
        """On and Off buttons"""
        on_btn = wx.Button(panel, label = "On", pos = (5,55))
        off_btn = wx.Button(panel, label = "Off", pos = (5,80))

        
        self.Show()

        on_btn.Bind(wx.EVT_BUTTON, self.press_on)
        off_btn.Bind(wx.EVT_BUTTON, self.press_off)

    def press_on(self, event):
        lights["Light Strip"].on = True

    def press_off(self, event):
        lights["Light Strip"].on = False

if __name__ == '__main__':
    app = wx.App()
    frame = Window()
    app.MainLoop()
    
    


