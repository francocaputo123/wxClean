import wx
from Ui.Components import Container, StyledButton

class Register(wx.Panel) :
    def __init__(self, parent, router, **args) :
        super().__init__(parent)

        self.nombre = args.get('nombre')
        self.router = router
        self.m_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_container = Container.Container(self, 'V')

        self.txt = wx.TextCtrl(self.main_container, value='Hola')
        self.test_btn = StyledButton.StyledButton(self.main_container, label="Presioname")
        self.second_btn = StyledButton.StyledButton(self.main_container, label="Ver nombre")

        self.main_container.add_widget(self.txt)
        self.main_container.add_widget(self.test_btn)
        self.main_container.add_widget(self.second_btn)

        self.Bind(wx.EVT_BUTTON, self.back, self.test_btn)
        self.Bind(wx.EVT_BUTTON, self.show_name, self.second_btn)

        self.m_sizer.Add(self.main_container)

        self.SetSizer(self.m_sizer)

    def back(self, event) :
        self.router.pop()

    def show_name(self, event) :
        print(self.nombre)



