import wx
from Style import ButtonStyleMap as BtnStyle

class CustomButton(wx.Control) :
    def __init__(self, parent, size=None,label="",stylesheet=None) :
        super().__init__(parent, style=wx.NO_BORDER)

        '''
        Definiendo estilos
        '''
        self.style = {}
        if stylesheet :
            self.style = BtnStyle.ButtonStyleMap(stylesheet)

        self.label = label
        self.state = 'normal' #hover, pressed
        self.size = self.SetInitialSize((120, 40))
        if size :
            self.size = self.SetInitialSize((size))

        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)

        '''
        Dibujo y hover automático
        '''
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_ENTER_WINDOW, self.on_arrive)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave)

    def on_arrive(self, event) :
        self.state = 'hover'
        print("hola")
        self.Refresh()

    def on_leave(self, event) :
        self.state = 'normal'
        print("adios")
        self.Refresh()

    def on_paint(self, event) :
        # 1. Usamos PaintDC para el buffer, sirve para que no parpadee al actualizar y reescribir lo que tiene os por defecto
        dc = wx.AutoBufferedPaintDC(self)

        dc.SetBackground(wx.Brush(self.GetParent().GetBackgroundColour()))
        dc.Clear()

        gc = wx.GraphicsContext.Create(dc)
        if not gc:
            return

        #cuerpo del botón
        self.button_body(gc)

        #texto del botón
        self.button_text(gc)


    def button_body(self,gc) :
        # 2. Definir colores si hubiese, caso contrario, usar valores por defecto.
        border_color = None
        border_size = None
        border = getattr(self.style, 'border', 0)
        bg_color = wx.Colour(getattr(self.style, 'bg_color', '#808080'))
        border_attr = getattr(self.style, 'btn_border', None)

        if isinstance(border_attr, list) and len(border_attr) > 0 :
            border_color = wx.Colour(border_attr[0])
            border_size = border_attr[1]
        else :
            border_color = bg_color
            border_size = 1


        # 3. Dibujar el cuerpo del botón
        gc.SetBrush(wx.Brush(bg_color))
        gc.SetPen(wx.Pen(border_color,border_size))

        w, h = self.GetSize()

        #margen para que se dibuje mejor
        margin = border_size

        gc.DrawRoundedRectangle(margin/2, margin/2, w - margin, h - margin, border)

    def button_text(self, gc) :
        w, h = self.GetSize()
        font = self.GetFont()

        gc.SetFont(font, 'black')
        tw, th = gc.GetTextExtent(self.label)
        gc.DrawText(self.label, (w - tw) / 2, (h - th) / 2)
