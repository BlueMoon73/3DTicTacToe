from ursina import Ursina
from GameBoard import GameBoard
from ToggleButton import ToggleButton
from Player import Player
import config
import GameInit

# Code to run on initialization of app
if __name__ == '__main__':
    #create the app
    app = Ursina()
    # create the takeover button
    takeOverButton = ToggleButton(startVal=False, pos=(0.8, -.4), scale=(0.4, 0.1),
                                  defaultText="Click to  enable takeover mode!",
                                  clickText="Click to  disable takeover mode!")

    # create the highlight button
    highlightButton = ToggleButton(startVal=True, pos=(-0.8, -.4), scale=(0.3, 0.1), defaultText="Stop highlighting!",
                                   clickText="Start Highlighting!")

    # create the gameboard
    gameBoard = GameBoard(allSlots=config.slots, allSlotsPos=config.slotPos, highlightButton=highlightButton)

    # create the player object
    Player(player=config.turn, gameboard=gameBoard, takeoverButton=takeOverButton)

    # make the potential slots
    GameInit.makeSlots(gameBoard)

    # initialize settings
    GameInit.settingsInit(gameboard=gameBoard,mouseButton="left mouse button")


    app.run()
