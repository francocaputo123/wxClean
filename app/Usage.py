import wx
from Core import App
from Views import LoginPanel, Register

#Para usar app y el enrutador, se debe declarar un diccionario que contenga todas las rutas o paneles que queramos añadir.

routes = {
    'login' : LoginPanel.LoginPanel,
    'register' : Register.Register
}

#iniciamos app con las rutas, el panel raiz o incial, el nombre del frame y el tamaño que tendrá
app = App.App(
        routes,
        'login',
        "Primer app",
        size=(1000,800)
)

#se corre la app.
app.run()