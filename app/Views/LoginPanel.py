import wx 
from Components import Button

class LoginPanel(wx.Panel) :
    def __init__(self, parent):
        super().__init__(parent)


        #setting components
        self.login_btn = Button.Button(self,'Boton de prueba', {'bg_color':'red'})

        #setting sizers
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.main_sizer.Add(self.login_btn, 0, wx.EXPAND | wx.CENTRE | wx.ALL, 5)
        
        self.SetSizer(self.main_sizer)
        self.SetSize(300,1)


