from ursina import Entity, color
from ursina.shaders import colored_lights_shader


# each symbol/gamepiece on the board

class PlayerSymbol(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.playerNum = kwargs.pop("player")
        if self.playerNum == 1:
            self.model = 'assets/player symbols/diamond2.obj'
            self.texture = 'assets/player symbols/diamondTexture3.png'
            self.shader = colored_lights_shader

            self.scale = 20

        elif self.playerNum == 2:
            self.model = 'assets/player symbols/pyramid9.obj'

            self.color = color.hsv(330, .19, .71)
            self.shader = colored_lights_shader

            self.scale = .25
        elif self.playerNum == 3:
            # self.model = 'assets/player symbols/cube4.glb'
            self.shader = colored_lights_shader
            self.model = "cube"
            self.color = color.hsv(119, .39, .92)

            self.scale = 2.5

        # self.rotation_x = -180
        self.position = kwargs.pop("position")
        self.parent = kwargs.pop("parent")
        self.multiplier = 2
