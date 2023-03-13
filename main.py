from ursina import Button, Entity, Vec3, color, mouse, destroy, Cursor, camera, window, Ursina, EditorCamera, \
    Text, Color
# from ursina.shaders import colored_lights_shader, basic_lighting_shader, transition_shader, unlit_shader,
# normals_shader,
from ursina.shaders import *

from GameBoard import GameBoard

# Global Variables to be used
initPos = Vec3(0, 0, 0)
slots = []
slotPos = []
slotsOccupied = []
currentSymbols = []
turn = 0
takeovers = [2, 3, 3]
horizontalCombos = []
multilayerCombos = []
cornerCombos = []


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


# class for the player, not a physical entity
# just to manage all players at once
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.turnNum = 1
        self.playerOneTakeovers = Text(text="Player 1 Takeovers: " + str(takeovers[0]), wordwrap=30, x=0.5, y=.3)
        self.playerTwoTakeovers = Text(text="Player 2 Takeovers: " + str(takeovers[1]), wordwrap=30, x=0.5, y=.2)
        self.playerThreeTakeovers = Text(text="Player 3 Takeovers: " + str(takeovers[2]), wordwrap=30, x=0.5, y=0.1)
        self.playerTurn = Text(text="Player # " + str(self.turnNum), wordwrap=30, x=0.5, y=0)
        self.msg = Text(text=" ", wordwrap=6, x=0.5, y=-0.1, scale=1.4, color=color.green)

    def input(self, keys):
        if keys == 'left mouse down':
            if gameBoard.hoverBoxIndex < 27:
                hoverIndex = gameBoard.hoverBoxIndex
                # print(takeOverButton.value)
                if not slotsOccupied[hoverIndex] and not takeOverButton.value:
                    self.placePlayerSymbol(hoverIndex)
                    self.msg.color = color.hsv(234, .88, .36)  # sets color to a light purple ish
                    self.msg.text = "Placed symbol sucessfully!"
                    # slots[hoverIndex].disable()

                elif slotsOccupied[hoverIndex] and takeOverButton.value and takeovers[self.turnNum - 1] > 0:

                    takeovers[self.turnNum - 1] -= 1
                    self.msg.color = color.hsv(156, .64, .41)
                    self.msg.text = "Took over player " + str(self.turnNum) + "'s spot sucessfully!"

                    self.replacePlayerSymbol(hoverIndex)
                elif not slotsOccupied[hoverIndex] and takeOverButton.value:
                    self.msg.color = color.hsv(6, .81, .55)
                    self.msg.text = "There is nothing in the spot to takeover! Please disable takeovers to place your symbol"
                elif slotsOccupied[hoverIndex] and not takeOverButton.value:
                    self.msg.color = color.hsv(6, .81, .55)
                    self.msg.text = "That spot is already taken! Please press the takeover button to use a " \
                                    "takeover!"

            else:
                pass

    # placing the player symbol, given a location (index)
    def placePlayerSymbol(self, index):
        p = PlayerSymbol(player=self.turnNum, position=slots[index].position)
        slotsOccupied[index] = True
        currentSymbols[index] = p
        self.turnNum += 1
        if self.turnNum > 3:
            self.turnNum = self.turnNum % 3

    # replacing a prexisiting symbol, if a takeover is used, given an index
    def replacePlayerSymbol(self, index):
        p = PlayerSymbol(player=self.turnNum, position=slots[index].position)
        slotsOccupied[index] = True
        destroy(currentSymbols[index])
        currentSymbols[index] = p
        self.turnNum += 1
        if self.turnNum > 3:
            self.turnNum = self.turnNum % 3

    def checkForHorizontalWin(self):
        # print(horizontalCombos)
        for row in range(len(horizontalCombos)):
            # if currentSymbols[self.findSymbolIndexWithPos(horizontalCombos[row][0])].playerNum and currentSymbols[self.findSymbolIndexWithPos(horizontalCombos[row][1])].playerNum and currentSymbols[self.findSymbolIndexWithPos(horizontalCombos[row][2])].playerNum:
            # if currentSymbols[self.findSymbolIndexWithPos(horizontalCombos[row][0])].playerNum:
            # print(currentSymbols[self.findSymbolIndexWithPos(horizontalCombos[row][0])].playerNum)
            # print("wtf")
            # print(horizontalCombos[row][0])
            # pos = horizontalCombos[row][0]
            #
            # print(self.findSymbolIndexWithPos(horizontalCombos[row][0]))
                print("someone has won")

                # i = self.findSymbolIndexWithPos()

        # pass

    def checkForMultilayerWin(self):
        pass

    def checkForCornerToCornerWin(self):
        pass

    def findSymbolIndexWithPos(self, pos):
        for i in range(len(slotPos)):
            if slotPos[i] == pos:
                return i
    def update(self):
        self.playerOneTakeovers.text = "Player 1 Takeovers: " + str(takeovers[0])
        self.playerTwoTakeovers.text = "Player 2 Takeovers: " + str(takeovers[1])
        self.playerThreeTakeovers.text = "Player 3 Takeovers: " + str(takeovers[2])
        self.playerTurn.text = "Player # " + str(self.turnNum)
        self.checkForHorizontalWin()


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
        self.parent = gameBoard
        self.multiplier = 2


def allPossibleHorziontalCombos():
    # HORIZONTAL COMBOS
    for x in range(3):
        for y in range(3):
            slot1 = [x, y, 0]
            slot2 = [x, y, 1]
            slot3 = [x, y, 2]

            row = [slot1, slot2, slot3]

            horizontalCombos.append(row)
def allPossibleDiagnolMultilayered():
    for x in range(3):
        slot1 = (x, 0, 0)
        slot2 = (x, 1, 1)
        slot3 = (x, 2, 2)
        row = (slot1, slot2, slot3)
        multilayerCombos.append(row)
    for y in range(3):
        slot1 = (0, y, 0)
        slot2 = (1, y, 1)
        slot3 = (2, y, 2)
        row = (slot1, slot2, slot3)
        multilayerCombos.append(row)
    for z in range(3):
        slot1 = (0, 0, z)
        slot2 = (2, 1, z)
        slot3 = (2, 2, z)
        row = (slot1, slot2, slot3)
        multilayerCombos.append(row)


def allPossibleCornerCombos():
    slot1 = (0, 0, 0)
    slot2 = (1, 1, 1)
    slot3 = (2, 2, 2)
    row = (slot1, slot2, slot3)
    cornerCombos.append(row)

    slot4 = (2, 0, 0)
    slot5 = (1, 1, 1)
    slot6 = (0, 2, 2)
    row = (slot4, slot5, slot6)
    cornerCombos.append(row)

    slot7 = (0, 2, 0)
    slot8 = (1, 1, 1)
    slot9 = (0, 0, 0)
    row = (slot7, slot8, slot9)
    cornerCombos.append(row)

    slot10 = (2, 2, 0)
    slot11 = (1, 1, 1)
    slot12 = (0, 0, 2)
    row = (slot10, slot12, slot12)
    cornerCombos.append(row)


def makeWinningCombos():
    allPossibleHorziontalCombos()
    allPossibleDiagnolMultilayered()
    allPossibleCornerCombos()


# create all the possible slots
def makeSlots():
    for x in range(3):
        for y in range(3):
            for z in range(3):
                xPos = (x - 1) / .25
                yPos = (y - 1) / .25
                zPos = (z - 1) / .25
                coords = (xPos, yPos, zPos)
                e = Slots(xpos=xPos, ypos=yPos, zpos=zPos, gameObj=gameBoard.model)

                pos = [x, y, z]
                slotPos.append(pos)
                slotsOccupied.append(False)
                currentSymbols.append(None)
                slots.append(e)


# initial settings to be declared
def settingsInit(**kwargs):
    eCam = EditorCamera()
    # gameboard = gameBoard
    Cursor(texture='cursor', scale=.1)
    makeWinningCombos()

    eCam.rotateMouse = kwargs.pop("mouseButton")

    camera.shader = unlit_shader

    camera.clip_plane_near = 1
    window.color = color.hsv(32, .9, .97)  # hsv color

    mouse.visible = False
    window.exit_button.visible = False
    window.fps_counter.enabled = False
    window.title = "3D Tic Tac Toe"
    window.borderless = False


# Code to run on initialization of app
if __name__ == '__main__':
    app = Ursina()
    highlightButton = ToggleButton(startVal=True, pos=(-0.8, -.4), scale=(0.3, 0.1), defaultText="Stop highlighting!",
                                   clickText="Start Highlighting!")
    takeOverButton = ToggleButton(startVal=False, pos=(-0.3, -.4), scale=(0.4, 0.1),
                                  defaultText="Click to  enable takeover mode!",
                                  clickText="Click to  disable takeover mode!")

    gameBoard = GameBoard(allSlots=slots, allSlotsPos=slotPos, highlightButton=highlightButton)

    settingsInit(
        gameboard=gameBoard,
        mouseButton="left mouse"
    )
    e = Entity(model='sphere', color=color.clear, parent=gameBoard, collider='sphere')
    Player(player=turn)
    print(turn)

    makeSlots()
    app.run()
