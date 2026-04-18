import wx
from Core.Router import Router

class App(wx.App) :
    '''
    Pasamos las rutas: {}, la ruta inicial : '' el título : '', el tamaño del frame principal : () y la orientación del main_frame = wx.HORIZONTAL | wx.VERTICAL
    '''
    def __init__(self, routes, initial, title="", size=None, display=None) :

        self.routes = routes
        self.initial = initial
        self.title = title
        self.size = (800,600)
        if size :
            self.size = size
        self.display = wx.VERTICAL
        if display :
            self.display = display
        super().__init__()

    def OnInit(self) :
        self.router = Router(self.routes, self.initial, self.title, self.size, self.display)
        #self.touter.push(self.initial)
        return True

    def run(self) :
        self.MainLoop()