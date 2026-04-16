import wx
from Style import ButtonStyleMap as BtnStyle

class CustomButton(wx.Control) :
    def __init__(self, parent, label="",stylesheet=None, pos=None) :
        super().__init__(parent, style=wx.NO_BORDER)

        '''
        Definiendo estilos. Si recibe por parámetros stylesheet,
        verificamos que exista dentro de la lista de para buttons
        '''
        self.style = None
        if stylesheet :
            self.style = BtnStyle.ButtonStyleMap(stylesheet)

        #inicialización variables
        self.label = label
        self.state = 'normal' #hover, pressed
        self.hover = True
        if hasattr(self.style, 'hover') :
            self.hover = getattr(self.style, 'hover')
        self.bg_color = '#808080'
        self.radius = 0
        self.size = self.SetInitialSize((120, 40))
        if hasattr(self.style, 'size') :
            self.size = self.SetInitialSize((getattr(self.style, 'size')))
        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.SetCursor(wx.Cursor(wx.CURSOR_HAND))

        '''
        Dibujo y hover
        '''
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_ENTER_WINDOW, self.on_arrive)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave)

    def on_arrive(self, event) :
        self.state = 'hover'
        self.Refresh()

    def on_leave(self, event) :
        self.state = 'normal'
        self.Refresh()

    def hover_state(self, state : bool) :
        self.hover = state

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
        self.radius = getattr(self.style, 'radius', 0)
        offset = 2
        self.bg_color = wx.Colour(getattr(self.style, 'bg_color', '#808080'))
        border_attr = getattr(self.style, 'btn_border', None)

        '''
        btn_border recibe 2 posiciones en un array: el color y el ancho de la linea
        En caso se que exista, verificamos que sea una lista si o si, caso contrario
        definimos valores por defecto.
        border_attr[0] --> self.style.btn_border[0] (posición del color)
        border_attr[1] --> self.style.btn_border[1] (posición del border)
        Quien me mando a hacer esto...
        '''
        if isinstance(border_attr, list) and len(border_attr) > 0 :
            border_color = wx.Colour(border_attr[0])
            border_size = border_attr[1]
        else :
            border_color = self.bg_color
            border_size = 1


        # 3. Dibujar el cuerpo del botón
        gc.SetBrush(wx.Brush(self.bg_color))
        gc.SetPen(wx.Pen(border_color,border_size))

        w, h = self.GetSize()
        #margen para que se dibuje mejor
        draw_w = w - (offset * 2)
        draw_h = h - (offset * 2)


        gc.DrawRoundedRectangle(offset, offset, draw_w, draw_h, self.radius)

        if self.state == 'hover' and self.hover:
            '''
            Creamos otro rect dentro del actual para crear un efecto de hover.
            '''
            hover_layer = wx.Colour(getattr(self.style, 'hover_color', (255, 255, 255, 100)))
            gc.SetBrush(wx.Brush(hover_layer))
            gc.SetPen(wx.Pen(border_color, border_size))

            gc.DrawRoundedRectangle(offset, offset, draw_w, draw_h, self.radius)
        else :
            self.bg_color = wx.Colour(getattr(self.style, 'bg_color', '#808080'))

    def button_text(self, gc) :
        #estilos
        font = self.get_fonts()
        font_color = getattr(self.style, 'font_color', 'white')

        gc.SetFont(font, font_color)

        pos_x, pos_y = self.text_position(gc)
        gc.DrawText(self.label, pos_x, pos_y)

    def get_fonts(self) :
        #todos los estilos de font disponibles
        '''
        Importante revisar todos porque wx.Font recibe si o si 4 parámetros minimo.
        '''
        font_size = getattr(self.style, 'font_size', 10)
        font_color = getattr(self.style, 'font_color', '#fff')
        font_family = getattr(self.style, 'font_family', wx.DEFAULT)
        font_style = getattr(self.style, 'font_style', wx.NORMAL)
        font_weight = getattr(self.style, 'font_weight', wx.NORMAL)
        underline = getattr(self.style, 'underline', False)
        face_name = getattr(self.style, 'face_name', '')
        return wx.Font(font_size, font_family, font_style, font_weight, underline, face_name)

    def text_position(self, gc) :
        '''
        Posicionamiento del texto dentro del botón.
        Definimos estilos de antemano, además es poosible cambiar el relleno interno con padding
        '''
        w, h = self.GetSize()
        text_w, text_h = gc.GetTextExtent(self.label)
        padding = 5
        '''
        Verificamos que exista padding. Tanto padding como aligments devuelven tuplas de posiciones.
        '''
        if hasattr(self.style, 'padding') :
            x,y = getattr(self.style, 'padding')
            aligment = (3 + x, 3 + y)
            return aligment
        else :
            alignments = {
                'default' : (5, 5),
                'center' : ((w - text_w) / 2, (h - text_h) / 2),
                'start' : (padding, (h - text_h) / 2),
                'end' : ((w - text_w - padding), (h - text_h) / 2),
                'top' : ((w - text_w) / 2, padding),
                'bottom' : ((w - text_w) / 2, (h - text_h - padding))
            }
            align_type = getattr(self.style, 'text_align', 'default')
            return alignments.get(align_type, alignments['center'])

