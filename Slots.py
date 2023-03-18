from ursina import Entity
import config


# All potential slots for players to set their corresponding symbols
class Slots(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = config.slotsModel
        self.scale = config.slotsScale
        self.collider = config.slotsCollider

        self.x = kwargs.pop('xpos')
        self.y = kwargs.pop('ypos')
        self.z = kwargs.pop('zpos')

        self.parent = kwargs.pop("gameObj")
        self.shader = config.slotsShader
        self.texture = config.slotsTexture
