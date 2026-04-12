import wx
from Components import Button, Container, Input, CustomButton
from Style import StyleSheet

class LoginPanel(wx.Panel) :
    def __init__(self, parent):
        super().__init__(parent)

        #estilos
        styles = StyleSheet.StyleSheet({
            'btn1' : {
                'border' : 0,
                'bg_color': 'red'
            },
            'btn2' : {
                'radius' : 0
            }
        })

        #contenedor principal
        self.cont = wx.BoxSizer(wx.HORIZONTAL)
        self.was_pressed = 0

        #definiendo contenedor
        self.main_sizer = Container.Container(self, 'V')
        self.second = Container.Container(self, 'V')

        #definiendo componentes

        self.login_btn = Button.Button(self.main_sizer,'Boton de prueba', {'bg_color':'red', 'size': (100,40)})
        self.login_btn.Bind(wx.EVT_BUTTON, self.change_color)
        self.test_btn = CustomButton.CustomButton(self.main_sizer, size=(200,40),label="Hola")
        self.ipt = Input.Input(self.main_sizer, placeholder="AAAAAAAA")
        self.register_two = Button.Button(self.second,'Boton de prueba', {'bg_color':'blue', 'size': (200,40)})

        #añadiendo widgets
        self.main_sizer.add_widget(self.login_btn)
        self.main_sizer.add_widget(self.ipt, {'proportion': 0, 'flags': wx.ALL | wx.CENTRE, 'border': 5})
        self.main_sizer.add_widget(self.test_btn)
        self.second.add_widget(self.register_two)

        #definiendo los contenedores
        self.cont.Add(self.main_sizer, 1, wx.CENTRE)
        self.cont.Add(self.second, 3, wx.CENTRE)
        self.SetSizer(self.cont)

    def change_color(self, event) :
        if self.was_pressed == 1 :
            self.login_btn.set_styles({'bg_color' : 'blue'})
            self.was_pressed = 0
            return
        self.login_btn.set_styles({'bg_color' : 'red'})
        self.was_pressed = 1


