from ursina import *

# Global Variables to be used
initPos = Vec3(0,0,0)
slots = []
slotPos = []
slotsOccupied = []
currentSymbols = []
turn = 0


shouldTakeover = False
takeovers = [2, 3, 3]

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

# All potential slots for players to set their corresponding symbols
class Slots(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'sphere'
        self.scale = 2.6
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
        self.eternal = True
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
        if mouse.hovered_entity:
            for i in range(len(slots)):
                if slots[i].hovered:
                    self.hoverBoxIndex = i
                    return slotPos[i]
        else:
            self.hoverBoxIndex = 30
            return 27
            # else:
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
                    slots[i].color = color.clear
                    slots[i].always_on_top = False
        else:
            for i in range(len(slotPos)):
                    # slots[i].color = color.rgb(0,1,0, 1)
                    slots[i].color = color.clear
                    slots[i].always_on_top = False


class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.turnNum = 1
        self.playerOneTakeovers = Text(text="Player 1 Takeovers: " + str(takeovers[0]), wordwrap=30, x=0.5, y=.3)
        self.playerTwoTakeovers = Text(text="Player 2 Takeovers: " + str(takeovers[1]), wordwrap=30, x=0.5, y=.2)
        self.playerThreeTakeovers = Text(text="Player 3 Takeovers: " + str(takeovers[2]), wordwrap=30, x=0.5, y=0.1)
        self.playerTurn = Text(text="Player # " + str(self.turnNum), wordwrap=30, x=0.5, y=0)
        self.errorMsg = Text(text=" ", wordwrap=30, x=0.5, y=-0.1, scale=1.4, color=color.red)

        # self.texture = 'vignette'
    def input(self, keys):
        if keys == 'left mouse down':
            if gameBoard.hoverBoxIndex < 27:
                hoverIndex = gameBoard.hoverBoxIndex
                # print(takeOverButton.value)
                if not slotsOccupied[hoverIndex] and not takeOverButton.value:
                    self.placePlayerSymbol(hoverIndex)
                    print(hoverIndex)
                elif slotsOccupied[hoverIndex] and takeOverButton.value and takeovers[self.turnNum - 1] > 0:
                    takeovers[self.turnNum - 1] -= 1
                    self.replacePlayerSymbol(hoverIndex)
            else:
                self.errorMsg.text="Please select a valid place to move"

    def placePlayerSymbol(self, index):
        p = PlayerSymbol(player=self.turnNum, position=slots[index].position)
        slotsOccupied[index] = True
        currentSymbols[index] = p
        self.turnNum += 1
        if self.turnNum > 3:
            self.turnNum = self.turnNum % 3
    def replacePlayerSymbol(self, index):
        p = PlayerSymbol(player=self.turnNum, position=slots[index].position)
        slotsOccupied[index] = True
        print(currentSymbols[index].playerNum)
        destroy(currentSymbols[index])
        currentSymbols[index] = p
        print(currentSymbols[index].playerNum)

        print("removed")
        # currentSymbols[index] = p

        self.turnNum += 1
        if self.turnNum > 3:
            self.turnNum = self.turnNum % 3
    def update(self):
        self.playerOneTakeovers.text = "Player 1 Takeovers: " + str(takeovers[0])
        self.playerTwoTakeovers.text = "Player 2 Takeovers: " + str(takeovers[1])
        self.playerThreeTakeovers.text = "Player 3 Takeovers: " + str(takeovers[2])
        self.playerTurn.text = "Player # " + str(self.turnNum)




class PlayerSymbol(Entity):
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
                slotsOccupied.append(False)
                currentSymbols.append(None)
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
    highlightButton = ToggleButton(startVal=True, pos=(-0.8, -.4), scale=(0.3, 0.1), defaultText="Stop highlighting!", clickText="Start Highlighting!")
    takeOverButton = ToggleButton(startVal=False, pos=(-0.4, -.4), scale=(0.3, 0.1), defaultText="Click to  enable takeover mode!", clickText="Click to  disable takeover mode!")

    settingsInit(
        gameboard=gameBoard,
        mouseButton="left mouse"
    )



    Player(player=turn)
    print(turn)

    makeSlots()
    app.run()