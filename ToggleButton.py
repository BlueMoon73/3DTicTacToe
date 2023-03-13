from ursina import Button, color

# Button class for all buttons that are toggle something on or off

class ToggleButton(Button):
    def __init__(self, **kwargs):
        super().__init__()
        self.position = kwargs.pop("pos")
        self.scale = kwargs.pop("scale")
        self.startValue = kwargs.pop("startVal")

        self.color = color.olive

        self.defaultText = kwargs.pop("defaultText")
        self.clickText = kwargs.pop("clickText")
        self.text = self.defaultText
        self.highlight_color = self.color.tint(.2)
        self.highlight_scale = 1.3
        self.pressed_color = self.color.tint(0.3)
        self.pressed_scale = 1.3

        self.on_click = self.onClick
        self.value = self.startValue

    def onClick(self):
        if not self.startValue:
            if not self.value:
                self.value = not self.startValue
                self.text = self.clickText
                self.color = color.blue
            else:
                self.value = self.startValue
                self.text = self.defaultText
                self.color = color.olive
        else:
            if self.value:
                self.value = not self.startValue
                self.text = self.clickText
                self.color = color.blue
            else:
                self.value = self.startValue
                self.text = self.defaultText
                self.color = color.olive

