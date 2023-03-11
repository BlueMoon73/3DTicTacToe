# from ursina import *
#
# app = Ursina()
#
#
# def start():
#     player = Entity(model = "cube", color=color.blue, scale_y=2)
#     return player
# def updateFunc(item):
#     item.x += held_keys["d"] * 0.1
#
# player = start()
# def update():
#     updateFunc(player)
import PIL
from ursina import *

def addPlayerSymbol():
    b = Button(position=(-0.5,-.4), scale=(.2, .1), text='zzz')
    b.on_mouse_enter = Func(setattr, b, 'text', 'Hovering')
    b.on_mouse_exit = Func(setattr, b, 'text', 'Not Hovering')

initPos = Vec3(0,0,0)

app = Ursina()
Cursor(texture='cursor', scale=.1)
mouse.visible = False
window.exit_button.visible = False
window.fps_counter.enabled = False

player = Entity(parent=camera.ui,  model = "TicTacToeBase.obj", color=color.light_gray, scale=.04, position=initPos)
# bg = Entity(parent=camera.ui, model='quad', texture=, scale_x=camera.aspect_ratio, z=1)

addPlayerSymbol()
def update():
    # print(mouse.velocity)
    player.rotation_x += mouse.delta[1]
    player.rotation_y -= mouse.delta[0]
    player.rotation_z += mouse.delta[2]




app.run()