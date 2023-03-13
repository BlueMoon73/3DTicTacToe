import config
from ursina import Entity, Text, color, destroy

from PlayerSymbol import PlayerSymbol


# class for the player, not a physical entity
# just to manage all players at once
class Player(Entity):

    def __init__(self, **kwargs):
        super().__init__()
        self.gameboard = kwargs.pop("gameboard")
        self.turnNum = 1
        self.playerOneTakeovers = Text(text="Player 1 Takeovers: " + str(config.takeovers[0]), wordwrap=30, x=0.5, y=.3)
        self.playerTwoTakeovers = Text(text="Player 2 Takeovers: " + str(config.takeovers[1]), wordwrap=30, x=0.5, y=.2)
        self.playerThreeTakeovers = Text(text="Player 3 Takeovers: " + str(config.takeovers[2]), wordwrap=30, x=0.5,
                                         y=0.1)
        self.playerTurn = Text(text="Player # " + str(self.turnNum), wordwrap=30, x=0.5, y=0)
        self.msg = Text(text=" ", wordwrap=6, x=0.5, y=-0.1, scale=1.4, color=color.green)
        self.takeOverButton = kwargs.pop("takeoverButton")

    def input(self, keys):
        if keys == 'left mouse down':
            if not config.gameFinished:
                if self.gameboard.hoverBoxIndex < 27:
                    hoverIndex = self.gameboard.hoverBoxIndex
                    if not config.slotsOccupied[hoverIndex] and not self.takeOverButton.value:
                        self.placePlayerSymbol(hoverIndex)
                        self.msg.color = color.hsv(234, .88, .36)  # sets color to a light purple ish
                        self.msg.text = "Placed symbol successfully!"

                    elif config.slotsOccupied[hoverIndex] and self.takeOverButton.value and config.takeovers[
                        self.turnNum - 1] > 0:
                        config.takeovers[self.turnNum - 1] -= 1
                        self.msg.color = color.hsv(156, .64, .41)
                        self.msg.text = "Took over player " + str(self.turnNum) + "'s spot successfully!"

                        self.replacePlayerSymbol(hoverIndex)
                    elif not config.slotsOccupied[hoverIndex] and self.takeOverButton.value:
                        self.msg.color = color.hsv(6, .81, .55)
                        self.msg.text = "There is nothing in the spot to takeover! Please disable takeovers to place your " \
                                        "symbol"
                    elif config.slotsOccupied[hoverIndex] and not self.takeOverButton.value:
                        self.msg.color = color.hsv(6, .81, .55)
                        self.msg.text = "That spot is already taken! Please press the takeover button to use a " \
                                        "takeover!"
            else:
                self.msg.text = "The game has finished! Please reset the game to play again!"

    # placing the player symbol, given a location (index)
    def placePlayerSymbol(self, index):
        p = PlayerSymbol(player=self.turnNum, position=config.slots[index].position, parent=self.gameboard)
        config.slotsOccupied[index] = True
        config.currentSymbols[index] = p
        self.turnNum += 1
        if self.turnNum > 3:
            self.turnNum = self.turnNum % 3

    # replacing a preexisting symbol, if a takeover is used, given an index
    def replacePlayerSymbol(self, index):
        p = PlayerSymbol(player=self.turnNum, position=config.slots[index].position, parent=self.gameboard)
        config.slotsOccupied[index] = True
        destroy(config.currentSymbols[index])
        config.currentSymbols[index] = p
        self.turnNum += 1
        if self.turnNum > 3:
            self.turnNum = self.turnNum % 3

    def checkForHorizontalWin(self):
        # print(horizontalCombos)
        for row in range(len(config.horizontalCombos)):
            slotOneSymbol = config.currentSymbols[self.findSymbolIndexWithPos(config.horizontalCombos[row][0])]
            slotTwoSymbol = config.currentSymbols[self.findSymbolIndexWithPos(config.horizontalCombos[row][1])]
            slotThreeSymbol = config.currentSymbols[self.findSymbolIndexWithPos(config.horizontalCombos[row][2])]

            if not (slotOneSymbol is None) and not (slotTwoSymbol is None) and not (slotThreeSymbol is None):
                if slotOneSymbol.playerNum == slotTwoSymbol.playerNum == slotThreeSymbol.playerNum:
                    self.gameWin(slotOneSymbol.playerNum, [slotOneSymbol, slotTwoSymbol, slotThreeSymbol])

        # pass

    def checkForMultilayerWin(self):
        for row in range(len(config.multilayerCombos)):
            slotOneSymbol = config.currentSymbols[self.findSymbolIndexWithPos(config.multilayerCombos[row][0])]
            slotTwoSymbol = config.currentSymbols[self.findSymbolIndexWithPos(config.multilayerCombos[row][1])]
            slotThreeSymbol = config.currentSymbols[self.findSymbolIndexWithPos(config.multilayerCombos[row][2])]

            if not (slotOneSymbol is None) and not (slotTwoSymbol is None) and not (slotThreeSymbol is None):
                print(slotOneSymbol.playerNum, slotTwoSymbol.playerNum, slotThreeSymbol.playerNum)
                if slotOneSymbol.playerNum == slotTwoSymbol.playerNum == slotThreeSymbol.playerNum:
                    self.gameWin(slotOneSymbol.playerNum, [slotOneSymbol, slotTwoSymbol, slotThreeSymbol])

    def checkForCornerToCornerWin(self):
        for row in range(len(config.cornerCombos)):
            slotOneSymbol = config.currentSymbols[self.findSymbolIndexWithPos(config.cornerCombos[row][0])]
            slotTwoSymbol = config.currentSymbols[self.findSymbolIndexWithPos(config.cornerCombos[row][1])]
            slotThreeSymbol = config.currentSymbols[self.findSymbolIndexWithPos(config.cornerCombos[row][2])]
            if not (slotOneSymbol is None) and not (slotTwoSymbol is None) and not (slotThreeSymbol is None):
                if slotOneSymbol.playerNum == slotTwoSymbol.playerNum == slotThreeSymbol.playerNum:
                    self.gameWin(slotOneSymbol.playerNum, [slotOneSymbol, slotTwoSymbol, slotThreeSymbol])

    def checkForAnyWin(self):
        self.checkForHorizontalWin()
        self.checkForMultilayerWin()
        self.checkForCornerToCornerWin()

    def findSymbolIndexWithPos(self, pos):
        for i in range(len(config.slotPos)):
            if config.slotPos[i] == pos:
                return i

    def gameWin(self, winningPlayer, winningSlots):
        self.msg.text = "GAME OVER! Player " + str(winningPlayer) + " HAS WON!"
        self.msg.scale = 1.5
        config.gameFinished = True
        for slot in winningSlots:
            slot.rotation_y += 5

    def update(self):
        self.playerOneTakeovers.text = "Player 1 Takeovers: " + str(config.takeovers[0])
        self.playerTwoTakeovers.text = "Player 2 Takeovers: " + str(config.takeovers[1])
        self.playerThreeTakeovers.text = "Player 3 Takeovers: " + str(config.takeovers[2])
        self.playerTurn.text = "Player # " + str(self.turnNum)
        self.checkForAnyWin()
