from ursina import Entity

import config


# each symbol/gamepiece on the board

class PlayerSymbol(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.playerNum = kwargs.pop("player")
        if self.playerNum == 1:

            self.model = config.playerOneSymbolModel
            self.texture = config.playerOneSymbolTexture
            self.shader = config.playerOneSymbolShader
            self.scale = config.playerOneSymbolScale

        elif self.playerNum == 2:
            self.model = config.playerTwoSymbolModel
            self.texture = config.playerTwoSymbolTexture
            self.shader = config.playerTwoSymbolShader
            self.scale = config.playerTwoSymbolScale
            self.color = config.playerTwoSymbolColor

        elif self.playerNum == 3:
            self.shader = config.playerThreeSymbolShader
            self.model = config.playerThreeSymbolModel
            # self.texture = config.playerThreeSymbolTexture
            self.color = config.playerThreeSymbolColor
            self.scale = config.playerThreeSymbolScale

        self.position = kwargs.pop("position")
        self.parent = kwargs.pop("parent")
