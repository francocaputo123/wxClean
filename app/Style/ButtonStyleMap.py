'''
Esta clase es un puente de validación de estilos que llegan de StyleSheet desde el botón.
Principalmente se encarga de validar la existencia de estilos para el botón y devolverlos.
'''

class ButtonStyleMap :
    def __init__(self, btn_styles : dict) :
        self.styles_conf = btn_styles

        '''
        Serie de atributos permitidos
        '''
        self.allowed_styles = {
            'border',
            'radius',
            'btn_border',
            'bg_color',
            'txt_color'
        }

        self.check_properties(self.styles_conf)

        for key, value in self.styles_conf.items() :
            setattr(self, key, self.styles_conf[key])

    def check_properties(self, styles) :
        '''
        De alguna manera va a funcionar :D
        Los convertimos a sets para mejor rendimineto y nos fijamos si invalid tiene algo.
        '''
        keys = set(styles.keys())
        allowed_styles = set(self.allowed_styles)

        invalid = keys - allowed_styles

        if invalid :
            raise AttributeError(f"Invalid. The properties {invalid} are not avalible for ButtonSyles.")
