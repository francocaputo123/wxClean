from Ui.Style import styles as allowed_styles

class StyleSheet :
    def __init__(self, styles_conf : dict) :
        self.styles_conf = styles_conf

        self.check_properties(self.styles_conf)

        for key, value in self.styles_conf.items() :
            setattr(self, key, styles_conf[key])

    def check_properties(self, styles) :
        properties = {prop for props in styles.values() for prop in props}

        invalid = properties - set(allowed_styles.styles)

        if invalid :
            raise AttributeError(f"The property or properties {invalid} does not exist for class StyleSheet.")




