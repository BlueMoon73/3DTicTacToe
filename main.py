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


from ursina import *

def addPlayerSymbol():
    b = Button(position=(-0.5,-.4), scale=(.2, .1), text='zzz')
    b.on_mouse_enter = Func(setattr, b, 'text', 'Hovering')
    b.on_mouse_exit = Func(setattr, b, 'text', 'Not Hovering')

app = Ursina()
initPos = Vec3(1,1,1)
player = Entity(model = "TicTacToeBase.obj", color=color.white, scale=.3, position=initPos)
addPlayerSymbol()
def update():
    player.x += held_keys['d']*0.1
    player.x -= held_keys['a']*0.1
    player.y += held_keys['w'] * 0.1
    player.y -= held_keys['s'] * 0.1
    player.rotation_x += held_keys["r"] * 5
    player.rotation_y +=  held_keys["r"] * 5




app.run()