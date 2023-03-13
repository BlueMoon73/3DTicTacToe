from ursina import Ursina
from GameBoard import GameBoard
from ToggleButton import ToggleButton
from Player import Player
import config
import GameInit

# Code to run on initialization of app
if __name__ == '__main__':
    app = Ursina()

    takeOverButton = ToggleButton(startVal=False, pos=(-0.3, -.4), scale=(0.4, 0.1),
                                  defaultText="Click to  enable takeover mode!",
                                  clickText="Click to  disable takeover mode!")

    highlightButton = ToggleButton(startVal=True, pos=(-0.8, -.4), scale=(0.3, 0.1), defaultText="Stop highlighting!",
                                   clickText="Start Highlighting!")

    gameBoard = GameBoard(allSlots=config.slots, allSlotsPos=config.slotPos, highlightButton=highlightButton)
    GameInit.settingsInit(gameboard=gameBoard,mouseButton="left mouse button")
    Player(player=config.turn, gameboard=gameBoard, takeoverButton=takeOverButton)


    GameInit.makeSlots(gameBoard)
    app.run()
