import wx

class Router :
    def __init__(self, routes ,initial ,title, size=None, display=None) :
        self.routes = routes
        self.stack = [] #será la pila necesaria para saber en que panel se encuentra
        self.main_frame = wx.Frame(None, title=title, size=size)
        self.main_sizer = wx.BoxSizer(display)
        self.main_frame.SetSizer(self.main_sizer)
        self.main_frame.Show()

    def push(self) :
        pass