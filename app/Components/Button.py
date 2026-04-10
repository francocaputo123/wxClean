import wx

class Button(wx.Button) :
    def __init__(self, parent, label, conf=None):

        '''
        Por defecto, el boton va a tener estilos predefinidos en un dict.
        Este dict se puede cambiar pasando como parametro "conf", lo que sobreescribe los
        estilos que se le indiquen.
        '''
        default_styles = {
            'size' : (100,30),
            'bg_color' : None,
            'fore_color' : 'white',
        }

        self.settings = default_styles.copy()

        if conf :
            self.settings.update(conf)

        super().__init__(parent, label=label)

        #establecer estilos
        self.setStyles()

    def setStyles(self) :
        '''
        Define todos los estilos del color usando settings una vez inicializado
        '''
        self.SetBackgroundColour(self.settings['bg_color'])
        self.SetForegroundColour(self.settings['fore_color'])
        self.SetSize(self.settings['size'])

    

    