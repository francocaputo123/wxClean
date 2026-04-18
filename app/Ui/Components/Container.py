import wx

class Container(wx.Panel) :
    def __init__(self, parent, orient, config=None) :
        super().__init__(parent)

        '''
        El constructor admite dos valores posibles: V y H para la orientación respectivamente.

        '''
        if not orient or orient not in ("V", "H"):
            raise Exception("Orient was not provided for constructor or is not an admitted value.")
        else :
            orient = wx.VERTICAL if orient == "V" else wx.HORIZONTAL

        self.defaultConfig = {
            'proportion' : 0,
            'flags' : wx.ALL,
            'border' : 0
        }

        '''
        Por defecto, el contenedor será de tipo BoxSizer, se define a sí mismo.
        '''
        self.internal_sizer = wx.BoxSizer(orient)
        self.SetSizer(self.internal_sizer)

    def add_widget(self, widget, configuration=None) :
        conf = self.defaultConfig.copy()

        '''
        Copiamos la configuración por default que viene del constructor.
        Esto nos permite definir estilos personalizables a cada widget agregado.
        '''

        if configuration :
            conf.update(configuration)

        self.internal_sizer.Add(widget,
        conf['proportion'],
        conf['flags'],
        conf['border']
        )
        self.Layout()