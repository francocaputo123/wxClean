import wx
from Views import LoginPanel

class Main :
    def __init__(self):
        app = wx.App()

        frame = wx.Frame(None, title='Prueba', size=(1000,600))
        login_panel = LoginPanel.LoginPanel(frame)

        frame.Show()

        app.MainLoop()


app = Main()
