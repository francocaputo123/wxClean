import wx

class Button(wx.Button) :
    def __init__(self, parent, label, conf=None):

        '''
        Por defecto, el boton va a tener estilos predefinidos en un dict.
        Este dict se puede cambiar pasando como parametro "conf", lo que sobreescribe los
        estilos que se le indiquen.
        '''
        default_styles = {
            'size' : (100,300),
            'bg_color' : None,
            'fore_color' : 'white'
        }

        self.settings = default_styles.copy()

        if conf :
            self.settings.update(conf)

        super().__init__(parent, label=label, size=self.settings['size'])

        #establecer estilos
        self.set_styles()

    #private
    def set_styles(self, configuration=None) :
        styles = {
            'bg_color': 'SetBackgroundColour',
            'fore_color': 'SetForegroundColour',
        }
        '''
        Define todos los estilos del color usando settings una vez inicializado
        '''

        conf = self.settings.copy()

        '''
        Copiamos la configuración por default que viene del constructor.
        Esto nos permite definir estilos personalizables a cada widget agregado.
        '''

        if configuration :
            conf.update(configuration)

        '''
        Para no definir cada propiedad por separada, definimos un diccionarioq que contiene los métodos
        del boton. Se mapea con .items() y obtenemos su key y el valor.
        Almacenamos el valor de la configuración del boton y lo metemos dentro de una nueva variable con
        getattr --> method = getattr(self, method_name) = self.SetBackgroundColour().
        Después al método le pasamos el valor obtenido.
        '''
        for key, method_name in styles.items() :
            value = conf.get(key)
            if value is not None and value != 'size':
                method = getattr(self, method_name)
                method(value)

        self.Layout()

