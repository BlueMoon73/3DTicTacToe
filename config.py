from ursina import Vec3, color
from ursina.shaders import *

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
gameFinished = False

# assets & properties

# gameboard models
gameboardModel = "assets/background/TicTacToeBase.obj"
gameboardColor = "#061052"
gameboardTexture = "vignette"
gameboardShader = colored_lights_shader
gameboardScale = .4

# slots properties
slotsModel = "sphere"
slotsCollider = "sphere"
slotsTexture = "horizontal_gradient"
slotsShader = transition_shader
slotsScale = 2.6


# player one symbol models
playerOneSymbolModel = "assets/player symbols/diamond.obj"
playerOneSymbolTexture= 'assets/player symbols/texture6.png'
playerOneSymbolShader = colored_lights_shader
playerOneSymbolScale = 20


# player two symbol models
playerTwoSymbolModel = 'assets/player symbols/pyramid.obj'
playerTwoSymbolTexture= 'vertical_gradient'
playerTwoSymbolShader = colored_lights_shader
playerTwoSymbolColor = color.hex("#b593a4")
playerTwoSymbolScale = .27

# player three symbol models
playerThreeSymbolModel = 'assets/player symbols/cube.obj'
playerThreeSymbolTexture= 'assets/player symbols/cubeTexture2.png'
playerThreeSymbolShader = colored_lights_shader
playerThreeSymbolColor = color.hex("#74bd73")
playerThreeSymbolScale = 1.2

# message properties
messageWordwrap = 15
messageColorRed = color.hex("#8c261b")
messageColorGreen = color.hex("#26694e")
messageColorPurple = color.hex("#0b135c")


#toggle button properties
toggleButtonDefaultColor = color.olive
toggleButtonClickedColor = color.blue
toggleButtonHighlightScale = 1.3
toggleButtonPressedScale = 1.3
toggleButtonHighlightTint = 0.2
toggleButtonPressedTint = 0.3


ssaoNumSamples = 16
ssaoAmt = .01
ssaoStrength = 0.5
ssaoFalloff = 0.00000000002



cameraShader = fxaa_shader

windowExitButtonVisibility = False
windowTitle = "3D Tic Tac Toe"
windowBorderless = False

mouseVisible = False
vysncEnabled = True

