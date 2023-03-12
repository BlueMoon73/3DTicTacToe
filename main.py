from ursina import *

# Global Variables to be used
initPos = Vec3(0,0,0)
slots = []
slotPos = []
shouldHighlight = True
turn = 1


class HighlightButton(Button):
    def __init__(self, **kwargs):
        super().__init__()
        self.position = kwargs.pop("pos")
        self.scale = kwargs.pop("scale")
        self.color = color.olive
        self.on_click = self.onClick
        self.text = "Stop highlighting"
        self.highlight_color = self.color.tint(.2)
        self.highlight_scale = 1.3
        self.pressed_color = self.color.tint(.3)
        self.pressed_scale = 1.3
    def onClick(self):
        global shouldHighlight
        if shouldHighlight:
            shouldHighlight = False
            self.text = "Start highlighting"
        else:
            shouldHighlight = True
            self.text = "Stop Highlighting"

# All potential slots for players to set their corresponding symbols
class Slots(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'sphere'
        self.scale = 2
        self.collider = 'sphere'

        self.x = kwargs.pop('xpos')
        self.y =  kwargs.pop('ypos')
        self.z =  kwargs.pop('zpos')
        self.always_on_top = False

        self.multiplier = 2
        self.parent = kwargs.pop("gameObj")
        self.shader = transition_shader
        self.texture = 'horizontal_gradient'
        self.getPos()

    def input(self, keys):
        if keys == "r":
            self.world_rotation_x = 0
            self.world_rotation_y = 0
            self.world_rotation_z = 0
        elif keys == "p":
            self.world_rotation_x = 90
            self.world_rotation_y = 90
            self.world_rotation_z = 90
        if keys == "q":
            self.world_rotation_x = 0
            self.world_rotation_y = 0
            self.world_rotation_z = 90
        elif keys == "t":
            self.world_rotation_x = 90
            self.world_rotation_y = 0
            self.world_rotation_z = 0



class GameBoard(Entity):
    def __init__(self, **kwargs):
        self.hoverBoxPos = None
        self.allSlots = kwargs.pop("allSlots")
        self.allSlotsPos = kwargs.pop("allSlotsPos")
        self.hoverBoxIndex = None

        super().__init__()
        self.model="assets/background/TicTacToeBase.obj"
        self.color = color.azure
        self.scale = .4
        self.shader = basic_lighting_shader
        self.position = initPos
        self.multiplier = 2
        self.texture = 'vignette'
    def update(self):
        self.hoverBoxPos = self.findHoverBox(self.allSlots, self.allSlotsPos)
        self.highlightBox(self.allSlots, self.allSlotsPos)
    def input(self, keys):
        if keys == "r":
            self.world_rotation_x = 0
            self.world_rotation_y = 0
            self.world_rotation_z = 0
        elif keys == "p":
            self.world_rotation_x = 90
            self.world_rotation_y = 90
            self.world_rotation_z = 90
        if keys == "q":
            self.world_rotation_x = 0
            self.world_rotation_y = 0
            self.world_rotation_z = 90
        elif keys == "t":
            self.world_rotation_x = 90
            self.world_rotation_y = 0
            self.world_rotation_z = 0
    def findHoverBox(self, slots, slotPos):
        for i in range(len(slots)):
            if slots[i].hovered:
                self.hoverBoxIndex = i
                return slotPos[i]
    def highlightBox(self, slots, slotPos):
        if self.hoverBoxPos and shouldHighlight:
            for i in range(len(slotPos)):

                if slotPos[i] == self.hoverBoxPos:
                    # slots[i].color = color.hsv(198,.66, .95)
                    # slots[i].color = color.rgb(82/255, 194/255, 242/255, .7)
                    # slots[i].color = color.rgb(204/255, 71/255, 155/255, .7)
                    slots[i].color = color.white33


                    slots[i].always_on_top = True
                else:
                    # slots[i].color = color.rgb(0,1,0, 1)
                    slots[i].color = color.clear
                    slots[i].always_on_top = False
        else:
            for i in range(len(slotPos)):
                    # slots[i].color = color.rgb(0,1,0, 1)
                    slots[i].color = color.clear
                    slots[i].always_on_top = False


class player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.turnNum = 1

        # self.texture = 'vignette'
    def input(self, keys):

        if keys == 'left mouse down':
            playerSymbol(player=self.turnNum, position=slots[gameBoard.hoverBoxIndex].position)
            self.turnNum += 1
            if self.turnNum > 3:
                self.turnNum = self.turnNum % 3




class playerSymbol(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.playerNum = kwargs.pop("player")
        if self.playerNum == 1:
            self.model = 'assets/player symbols/diamond.obj'
            self.color = color.rgb(0.31, .76, 0.96, 1)
            self.scale = .2
        elif self.playerNum == 2:
            self.model = 'assets/player symbols/pyramid9.obj'
            self.rotation_z = 180
            self.color = color.hsv(309, .76, 1)
            self.scale = .25
        elif self.playerNum == 3:
            self.model = "cube"
            self.color = color.hsv(138, .74, .84)
            self.scale = 2.5
        self.rotation_x = -180
        self.shader = colored_lights_shader
        self.position = kwargs.pop("position")
        self.parent = gameBoard
        self.multiplier = 2
        # self.texture = 'vignette'
def makeSlots():
    for x in range(3):
        for y in range(3):
            for z in range(3):
                xPos = (x-1) / .25
                yPos = (y-1) / .25
                zPos = (z-1) / .25
                e = Slots(xpos = xPos , ypos = yPos, zpos = zPos, gameObj=gameBoard.model )

                pos = [x, y, z]
                slotPos.append(pos)
                slots.append(e)
def settingsInit(**kwargs):
    eCam = EditorCamera()
    gameboard = kwargs.pop("gameboard")
    Cursor(texture='cursor', scale=.1)

    eCam.rotateMouse = kwargs.pop("mouseButton")

    camera.shader = basic_lighting_shader
    window.color = color.hsv(32, .68, .97)  # hsv color

    mouse.visible = False
    window.exit_button.visible = False
    window.fps_counter.enabled = False

# Code to run on initialization of app
if __name__ == '__main__':
    app = Ursina()
    from ursina.shaders import *
    gameBoard = GameBoard(allSlots=slots, allSlotsPos=slotPos)
    HighlightButton = HighlightButton(pos=(-0.8, -.4), scale=(0.3, 0.1))

    settingsInit(
        gameboard=gameBoard,
        mouseButton="left mouse"
    )

    player(player=turn)
    print(turn)

    makeSlots()
    app.run()