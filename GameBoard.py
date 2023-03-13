from ursina import Entity, color, mouse
from ursina.shaders import basic_lighting_shader


# class for the main gameboard
class GameBoard(Entity):
    def __init__(self, **kwargs):
        self.hoverBoxPos = None
        self.allSlots = kwargs.pop("allSlots")
        self.allSlotsPos = kwargs.pop("allSlotsPos")
        self.hoverBoxIndex = None

        super().__init__()
        self.model = "assets/background/TicTacToeBase.obj"
        self.color = color.azure
        self.scale = .4
        self.shader = basic_lighting_shader
        self.position = (0, 0, 0)
        self.multiplier = 2
        self.texture = 'vignette'
        self.eternal = True

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
            return 27
            # else:

    # "highlight" the box that is being hovered over to indicate it is being hovered over
    def highlightBox(self, slots, slotPos):
        if self.hoverBoxPos and highlightButton.value:
            for i in range(len(slotPos)):

                if slotPos[i] == self.hoverBoxPos:
                    # slots[i].color = color.hsv(198,.66, .95)
                    # slots[i].color = color.rgb(82/255, 194/255, 242/255, .7)
                    # slots[i].color = color.rgb(204/255, 71/255, 155/255, .7)
                    slots[i].color = color.white33

                    slots[i].always_on_top = True
                else:
                    # slots[i].color = color.rgb(0,1,0, 1)
                    # slots[i].color = color.white10
                    slots[i].color = color.clear
                    slots[i].always_on_top = False
        else:
            for i in range(len(slotPos)):
                # slots[i].color = color.rgb(0,1,0, 1)
                slots[i].color = color.clear
                # slots[i].color = color.rgb(.1,.1,.1,.01)
                slots[i].always_on_top = False
