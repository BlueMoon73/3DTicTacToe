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


#
class Slots(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model=copy(combine_parent.model)
        # print(color)
        # self.scale = random.uniform(0.2, 0.7)
        self.scale = 0.5
        self.always_on_top = True
        # self.position =Vec3(500,0,0)
        # self.origin = (initPos)
        self.x = kwargs.pop('xpos')
        self.y =  kwargs.pop('ypos')
        self.z =  kwargs.pop('zpos')

        self.color = color.random_color()

        # self.parent=camera.ui
        self.getPos()

    def update(self):
        self.world_rotation_x += mouse.delta[1]
        self.world_rotation_y -= mouse.delta[0]
        self.world_rotation_z += mouse.delta[2]
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




class Player(Entity):
    def __init__(self, **kwargs):
        self.hoverBoxPos = None
        self.allSlots = kwargs.pop("allSlots")
        self.allSlotsPos = kwargs.pop("allSlotsPos")
        super().__init__()
        self.model="TicTacToeBase2.obj"
        self.color = color.light_gray
        self.scale = .4
        self.position = initPos

        # self.parent=camera.ui
        print(self.parent)
    def update(self):
        self.rotation_x += mouse.delta[1]
        self.rotation_y -= mouse.delta[0]
        self.rotation_z += mouse.delta[2]
        self.hoverBoxPos = self.findHoverBox()
        self.highlightBox(self.allSlots, self.allSlotsPos)
    def input(self, keys):
        if keys == "r":
            self.rotation_x = 0
            self.rotation_y = 0
            self.rotation_z = 0
        if keys == "p":
            self.rotation_x = 90
            self.rotation_y = 90
            self.rotation_z = 90

    def findHoverBox(self):
        if mouse.position:
            pos = mouse.position
            xVal = [abs(-.149254 - pos[0]), abs(-pos[0]), abs(.149254 - pos[0])]
            yVal = [abs(-.149254 - pos[1]), abs(-pos[1]), abs(.149254 - pos[1])]
            zVal = [abs(-.149254 - pos[2]), abs(-pos[2]), abs(.149254 - pos[2])]
            # print("xVal" + str(xVal))
            # print("yVal" + str(yVal))
            # print("zVal" + str(zVal))
            indexes = [xVal.index(min(xVal)), yVal.index(min(yVal)), zVal.index(min(zVal))]
            # print(indexes)
            return indexes
        else: return 0
    def highlightBox(self, slots, slotPos):
        if self.hoverBoxPos:
            for i in range(len(slotPos)):

                if slotPos[i] == self.hoverBoxPos:
                    slots[i].color = color.black
                    slots[i].scale = 0.6
                else:
                    slots[i].color = color.blue
                    # print(i)
                    # b = Slots(xpos=self.hoverBoxPos[0], ypos=self.hoverBoxPos[1], zpos=self.hoverBoxPos[2])
                    # b.scale= 0.6
                    # b.color = color.black
                    # for x in range(len(slots)):
                    #     slot

                    # print(slots[i].color)


        # if mouse.hovered_entity:
        #     print(mouse.hovered_entity)
        # print(mouse.position)
        # print(slots)
    # def update(self):
        # print(mouse.velocity)




slots = []
slotPos = []
if __name__ == '__main__':
    app = Ursina()

    combine_parent = Entity(enabled=False)
    for i in range(3):
        dir = Vec3(0, 0, 0)
        dir[i] = 1

        e = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube')
        e.look_at(dir, 'up')

        e_flipped = Entity(parent=combine_parent, model='plane', origin_y=-.5, texture='white_cube',)
        e_flipped.look_at(-dir, 'up')

    combine_parent.combine()
    for x in range(3):
        print(x)
        print("==========")
        for y in range(3):
            for z in range(3):
                e = Slots(xpos = (x-1) / .67, ypos = (y-1) / .67, zpos = (z-1) / .67  )
                if z == 2:
                    e.color = color.red

                print("x y and z: " + str(x) + ", " + str(y)  + ", " + str(z))
                print("screen pos" + str(e.screen_position))
                pos = [x, y, z]
                print("get pos" + str(e.getPos()))
                slotPos.append(pos)
                slots.append(e)

    print("===================================================================")

    player = Player(allSlots=slots, allSlotsPos=slotPos)
    # time.sleep(5)

    # print(player.hoverBoxPos)



    print(slots)
    Cursor(texture='cursor', scale=.1)
    mouse.visible = False
    window.exit_button.visible = False
    window.fps_counter.enabled = False

    # player = Entity(parent=camera.ui,  model = "TicTacToeBase.obj", color=color.light_gray, scale=.04, position=initPos)
    # bg = Entity(parent=camera.ui, model='quad', texture=, scale_x=camera.aspect_ratio, z=1)

    addPlayerSymbol()


    app.run()