import wx

class Input(wx.TextCtrl) :
    def __init__(self, parent, value="", placeholder="", conf=None) :

        self.settings = {
            'size': (150, -1),
            'bg_color': 'white',
            'fore_color': 'black',
            'font_size': 10,
            'password': False
        }

        if conf :
            self.settings.update(conf)

        style = wx.BORDER_SIMPLE
        if self.settings['password'] :
            style = wx.TE_PASSWORD

        super().__init__(parent, value=value, size=self.settings['size'] ,style=style)

        self.placeholder = placeholder

        if self.placeholder :
            self.SetValue(self.placeholder)