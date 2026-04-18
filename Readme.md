# Título

Proyecto creado en base a la librería wxPython con el fin de facilitar la creación de interfaces gráficas con mayor personalización de componentes, enrutamiento y mayor control de estados entre interfaces. Aún está en desarrollo por lo que puede contener errores o falta de contenido.

## Pre-requisitos

El único requisito previo que se necesesita es tener instalada la librería wxPython. Para mas información, puedes visitar: [wxPython](https://wxpython.org/pages/downloads/index.html).

## Comenzando

## Enturamiento

## Componentes

"" provee componentes personalizados capaces de soportar el uso de estilos y permitir la creación de vistas más modernas.

- ### Button

Es una mejora del botón nativo que soporta estados visuales y bordes personalizables. Se declara como el botón de wxPython:

```
self.my_btn = Button(self, label="Mi botón")
```

**Parámetros disponibles**

* label: String | Texto interno del botón
* stylesheet: None, StryleSheet | Hoja de estilos aplicable al botón

**Estilos soportados**

Button acepta todos los estilos globales además de sus estilos propios.

Solo para Button: *btn_border*


## Estilado

Una de las partes más importantes de "" es la personalización propia de los componentes, para ello, entra la clase StyleSheet. Esta clase permite crear una hoja de estilos para personalizar a medida como quieres que se vea un componente. Su creación es sencilla:

```
from Ui.Style import StyleSheet

stylesheet = StyleSheet({
    'btn' : {
        'color' : '#fff'
    },
    'container' : {
        'bg_color': '#ff0'
    }
})
```

Se define dentro de la clase un objeto el cual cada posición es un nombre de estilo, para consultar si un estilo tiene algún estilo único, puedes ir a [Componentes](#componentes).
Después, se llama el estilo que queramos pasando por parámetro stylesheet a cualquier componente:

```
self.my_btn = Button(self, label="Mi botón",stylesheet=stylesheet.btn)
```

### Estilos disponibles

A contunación, se detallarán todos los estilos que StyleSheet puede soportar:

| Categoría    | Propiedad    | Uso     |
|--------------|--------------|---------|
| Color        | bg_color     | Define el color de fondo del componente|
| Borde        | radius       | Define la curvatura de las esquinas (int)|
|              | btn_border   | Solo disponible para botón: Define tanto el color como el grosor del borde (array['red', 1])|
| Texto        | font_size    | Define el tamaño del texto (acepta números enteros)|
|              | font_color   | Define el color del texto (hex/string)|
|              | font_family  | Define la fuente del texto: (acepta los tipos nativos [wxPython](https://docs.wxpython.org/wx.FontFamily.enumeration.html))|
|              | font_style   | Define la inclinación de la letra (acepta los tipos nativos [wxPython](https://docs.wxpython.org/wx.FontStyle.enumeration.html))|
|              | font_weight  | Define el grosor de la letra (acepta los tipos nativos [wxPython](https://docs.wxpython.org/wx.FontWeight.enumeration.html))|
|              | underline    | Define el subrayado (boolean)|
|              | face_name    | Define la el nombre del texto (string)|
|              | text_align   | Define la alineación con respecto al contenedor (center, start, end, top, bottom)|
| Dimensiones  | size         | Define el tamaño del componente (tuple(w,h))|
|              | padding      | Define el margen interno del componente (tuple(x,y))|
| Interacción  | hover        | Define si admite hover (boolean)|
|              | hover_color  | Define el color del hover (hex/string)|
