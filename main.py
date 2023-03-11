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
slots = []

#
class Slots(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model="cube"
        # print(color)
        self.scale = .05
        # self.position =Vec3(500,0,0)
        self.x = kwargs.pop('ypos')
        self.y =  kwargs.pop('xpos')
        self.z =  kwargs.pop('zpos')

        if self.x > .1:
            self.color = color.red
        elif self.y > .1:
            self.color = color.blue
        elif self.y > .1:
            self.color = color.green
        elif -self.x> .1:
            self.color = color.azure
        elif -self.y > .1:
            self.color = color.olive
        elif -self.y > .1:
            self.color = color.orange

        self.parent=camera.ui
        self.getPos()

    def update(self):
        self.rotation_x += mouse.delta[1]
        self.rotation_y -= mouse.delta[0]
        self.rotation_z += mouse.delta[2]
    def input(self, keys):
        if keys == "r":
            self.rotation_x = 0
            self.rotation_y = 0
            self.rotation_z = 0
        if keys == "p":
            self.rotation_x = 90
            self.rotation_y = 90
            self.rotation_z = 90
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model="TicTacToeBase.obj"
        self.color = color.light_gray
        self.scale = .04
        self.position = initPos
        self.parent=camera.ui
    def update(self):
        self.rotation_x += mouse.delta[1]
        self.rotation_y -= mouse.delta[0]
        self.rotation_z += mouse.delta[2]
        self.highlight()
    def input(self, keys):
        if keys == "r":
            self.rotation_x = 0
            self.rotation_y = 0
            self.rotation_z = 0
        if keys == "p":
            self.rotation_x = 90
            self.rotation_y = 90
            self.rotation_z = 90
    def highlight(self):
        if mouse.hovered_entity:
            print(mouse.hovered_entity)
        # print(mouse.position)
        # print(slots)
    # def update(self):
        # print(mouse.velocity)

if __name__ == '__main__':
    app = Ursina()
    player = Player()

    for x in range(3):
        for y in range(3):
            for z in range(3):
                e = Slots(xpos = (x-1) / 6.7, ypos = (y-1) / 6.7, zpos = (z-1) / 6.7  )
                print(x/18.75, y/18.75, z/18.75)
                print(e.color)
                print(e.getPos())
                slots.append(e)

    print(len(slots))
    Cursor(texture='cursor', scale=.1)
    mouse.visible = False
    window.exit_button.visible = False
    window.fps_counter.enabled = False

    # player = Entity(parent=camera.ui,  model = "TicTacToeBase.obj", color=color.light_gray, scale=.04, position=initPos)
    # bg = Entity(parent=camera.ui, model='quad', texture=, scale_x=camera.aspect_ratio, z=1)

    addPlayerSymbol()





    app.run()