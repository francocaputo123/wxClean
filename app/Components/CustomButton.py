import wx

class CustomButton(wx.Control) :
    def __init__(self, parent, size=None,label="",stylesheet=None) :
        super().__init__(parent, style=wx.NO_BORDER)

        self.label = label
        self.style = stylesheet
        self.state = 'normal' #hover, pressed
        self.size = self.SetInitialSize((120, 40))
        if size :
            self.size = self.SetInitialSize((size))
        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self, event) :
        # 1. Usamos PaintDC para el buffer
        dc = wx.AutoBufferedPaintDC(self)

        dc.SetBackground(wx.Brush(self.GetParent().GetBackgroundColour()))
        dc.Clear()

        gc = wx.GraphicsContext.Create(dc)
        if not gc:
            return

        # 2. Definir colores (harcodeados por el momento)
        bg_color = wx.Colour('red')
        text_color = wx.Colour('white')

        # 3. Dibujar el cuerpo del botón
        gc.SetBrush(wx.Brush(bg_color))
        gc.SetPen(wx.Pen(text_color,1))

        w, h = self.GetSize()

        gc.DrawRoundedRectangle(0, 0, w, h, 15)

        font = self.GetFont()

        gc.SetFont(font, text_color)
        tw, th = gc.GetTextExtent(self.label)
        gc.DrawText(self.label, (w - tw) / 2, (h - th) / 2)