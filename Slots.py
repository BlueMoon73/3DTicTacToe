from ursina import Entity
from ursina.shaders import basic_lighting_shader

# All potential slots for players to set their corresponding symbols
class Slots(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'sphere'
        self.scale = 2.6
        self.collider = 'sphere'

        self.x = kwargs.pop('xpos')
        self.y = kwargs.pop('ypos')
        self.z = kwargs.pop('zpos')
        # self.always_on_top = False

        self.parent = kwargs.pop("gameObj")
        self.shader = basic_lighting_shader
        # self.texture = 'horizontal_gradient'

