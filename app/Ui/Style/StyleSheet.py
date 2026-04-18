from Ui.Style import styles as allowed_styles

class StyleSheet :
    def __init__(self, styles_conf : dict) :
        self.styles_conf = styles_conf

        self.check_properties(self.styles_conf)

        for key, value in self.styles_conf.items() :
            setattr(self, key, styles_conf[key])

    def check_properties(self, styles) :
        for key, value in styles.items() :
            for key, value in value.items() :
                if key not in allowed_styles.styles :
                    raise AttributeError(f"The property {key} does not exist for class StyleSheet.")

