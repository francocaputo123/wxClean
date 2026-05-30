import wx
from Ui.Components import Button, Container, StyledButton, Input
from Ui.Style import StyleSheet

class LoginPanel(wx.Panel) :
    def __init__(self, parent, router):
        super().__init__(parent)

        #estilos
        styles = StyleSheet.StyleSheet({
            'btn1' : {
                'radius' : 15,
                'font_color' : 'black',
                'font_size' : 15,
                'bg_color' : 'red',
                'size' : (200,50),
                'hover_color' : 'blue',
                'btn_border' : ['blue', 1]
            },
            'btn2' : {
                'radius' : 0
            }
        })
        #contenedor principal
        self.router = router
        self.cont = wx.BoxSizer(wx.HORIZONTAL)
        self.was_pressed = 0

        #definiendo contenedor
        self.main_sizer = Container.Container(self, 'V')
        self.second = Container.Container(self, 'V')

        #definiendo componentes

        self.test_btn = StyledButton.StyledButton(self.main_sizer,label="Presioname", stylesheet=styles.btn1)

        #añadiendo widgets
        self.main_sizer.add_widget(self.test_btn, {'proportion': 0, 'flags': wx.ALL | wx.CENTRE, 'border': 5})
        self.Bind(wx.EVT_BUTTON, self.close, self.test_btn)

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

    def close(self, event) :
        self.router.push('register', nombre="Pedro")

