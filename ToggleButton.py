from ursina import Button

import config


# Button class for all buttons that are toggle something on or off

class ToggleButton(Button):
    def __init__(self, **kwargs):
        super().__init__()
        self.position = kwargs.pop("pos")
        self.scale = kwargs.pop("scale")
        self.startValue = kwargs.pop("startVal")

        self.defaultColor = config.toggleButtonDefaultColor
        self.clickedColor = config.toggleButtonClickedColor
        self.color = self.defaultColor

        self.defaultText = kwargs.pop("defaultText")
        self.clickText = kwargs.pop("clickText")
        self.text = self.defaultText
        self.highlight_color = self.color.tint(config.toggleButtonHighlightTint)
        self.highlight_scale = config.toggleButtonHighlightScale
        self.pressed_color = self.color.tint(config.toggleButtonPressedTint)
        self.pressed_scale = config.toggleButtonPressedScale

        self.on_click = self.onClick
        self.value = self.startValue

    def onClick(self):
        if not self.startValue:
            if not self.value:
                self.value = not self.startValue
                self.text = self.clickText
                self.color = self.clickedColor
            else:
                self.value = self.startValue
                self.text = self.defaultText
                self.color = self.defaultColor
        else:
            if self.value:
                self.value = not self.startValue
                self.text = self.clickText
                self.color = self.clickedColor
            else:
                self.value = self.startValue
                self.text = self.defaultText
                self.color = self.defaultColor

