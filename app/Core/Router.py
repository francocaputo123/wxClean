import wx

'''
Router trabaja con las rutas pasadas por app y el usuario y las almacena en un stack.
Router constantemente sabe que rutas existen en la App.
'''

class Router :
    def __init__(self, routes ,initial ,title, size=None, display=None) :
        self.routes = routes
        self.stack = [] #será la pila necesaria para saber en que panel se encuentra
        self.main_frame = wx.Frame(None, title=title, size=size)
        self.main_sizer = wx.BoxSizer(display)
        self.main_frame.SetSizer(self.main_sizer)
        self.main_frame.Show()

    #añade la vista nueva al stack. Se tiene la posibilidad de usar replace, que destruye la ruta actual.
    #Como parámetro adicional, podemos pasar datos para despues usar en las demás vistas
    def push(self, route_name, replace=None, **args) :
        if self.stack :
            self.stack[-1].Hide()

        if self.stack and replace :
            self.stack[-1].Destroy()

        new_view = self._create_view(route_name, **args)
        self.stack.append(new_view)
        self._refresh_view()


    #Nos permite volver a la anterior vista.
    def pop(self) :
        if len(self.stack) > 1 :
            current_view = self.stack.pop()
            current_view.Destroy()

            self.stack[-1].Show()
            self._refresh_view()
        else :
            raise Exception("There is no more routes in the stack.")
        pass
    '''
    Eventos privados.
    '''
    def _create_view(self, route_name, **args) :
        view = self.routes[route_name]
        return view(self.main_frame, router=self, **args)


    #refresca la vista una vez usado alguno de los métodos para destruir o agregar otra vista.
    def _refresh_view(self) :
        if self.stack :
            self.main_sizer.Clear()
            self.main_sizer.Add(self.stack[-1], 1, wx.EXPAND)
            self.main_frame.Layout()
            self.main_frame.Show()
