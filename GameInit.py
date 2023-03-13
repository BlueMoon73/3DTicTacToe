import config
import Combinations
from ursina import window, Cursor, EditorCamera, camera, mouse, color
from ursina.shaders import unlit_shader
from Slots import Slots


def makeSlots(gameBoard):
    for x in range(3):
        for y in range(3):
            for z in range(3):
                xPos = (x - 1) / .25
                yPos = (y - 1) / .25
                zPos = (z - 1) / .25
                coords = (xPos, yPos, zPos)
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

    camera.shader = unlit_shader

    camera.clip_plane_near = 1
    window.color = color.hsv(32, .9, .97)  # hsv color

    mouse.visible = False
    window.exit_button.visible = False
    window.fps_counter.enabled = False
    window.title = "3D Tic Tac Toe"
    window.borderless = False
