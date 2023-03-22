import config
import Combinations
from ursina import window, Cursor, EditorCamera, camera, mouse, color, Entity, DirectionalLight
from ursina.shaders import ssao_shader
from Slots import Slots


# for making the possible slots to put the game pieces onto.
def makeSlots(gameBoard):
    for x in range(3):
        for y in range(3):
            for z in range(3):
                xPos = (x - 1) / .25
                yPos = (y - 1) / .25
                zPos = (z - 1) / .25
                e = Slots(xpos=xPos, ypos=yPos, zpos=zPos, gameObj=gameBoard)

                pos = [x, y, z]
                config.slotPos.append(pos)
                config.slotsOccupied.append(False)
                config.currentSymbols.append(None)
                config.slots.append(e)


# initial settings to be declared
def settingsInit(**kwargs):
    eCam = EditorCamera()
    Cursor(texture='cursor', scale=.1)
    Combinations.makeWinningCombos()

    eCam.rotateMouse = kwargs.pop("mouseButton")

    ssao_shader.default_input['numsamples'] = config.ssaoNumSamples
    ssao_shader.default_input['amount'] = config.ssaoAmt
    ssao_shader.default_input['strength'] = config.ssaoStrength
    ssao_shader.default_input['falloff'] = config.ssaoFalloff

    camera.shader = config.cameraShader

    window.color = color.hsv(217, .27, .94)  # hsv color

    pivot = Entity()
    DirectionalLight(parent=pivot, y=2, z=3, shadows=True)

    mouse.visible = config.mouseVisible
    window.exit_button.visible = config.windowExitButtonVisibility
    window.vsync = config.vysncEnabled

    window.fps_counter.enabled = False
    window.title = "3D Tic-TacToe"
    window.icon= "assets/Icon.ico"
    window.borderless = config.windowBorderless
