from ursina import Entity, color, mouse
import config


# class for the main gameboard
class GameBoard(Entity):
    def __init__(self, **kwargs):
        self.hoverBoxPos = None
        self.allSlots = kwargs.pop("allSlots")
        self.allSlotsPos = kwargs.pop("allSlotsPos")
        self.hoverBoxIndex = None

        super().__init__()
        self.model = config.gameboardModel
        self.color = color.hex(config.gameboardColor)
        self.scale = config.gameboardScale
        self.shader = config.gameboardShader
        self.position = config.initPos
        self.texture = config.gameboardTexture
        self.eternal = True
        self.highlightButton = kwargs.pop("highlightButton")

    def update(self):
        self.hoverBoxPos = self.findHoverBox(self.allSlots, self.allSlotsPos)
        self.highlightBox(self.allSlots, self.allSlotsPos)

    # finding the box that is being hovered over, if any
    def findHoverBox(self, slots, slotPos):
        if mouse.hovered_entity:
            for i in range(len(slots)):
                if slots[i].hovered:
                    self.hoverBoxIndex = i
                    return slotPos[i]
        else:
            self.hoverBoxIndex = 30
            return 30

    # "highlight" the box that is being hovered over to indicate it is being hovered over
    def highlightBox(self, slots, slotPos):
        if self.hoverBoxPos and self.highlightButton.value:
            for i in range(len(slotPos)):

                if slotPos[i] == self.hoverBoxPos:

                    slots[i].color = color.white33

                    slots[i].always_on_top = True
                else:

                    slots[i].color = color.clear
                    slots[i].always_on_top = False
        else:
            for i in range(len(slotPos)):
                slots[i].color = color.clear

                slots[i].always_on_top = False
