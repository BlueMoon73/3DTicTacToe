import config
from ursina import Entity, Text, color, destroy

from PlayerSymbol import PlayerSymbol


# class for the player, not a physical entity
# just to manage all players at once
class Player(Entity):

    def __init__(self, **kwargs):
        super().__init__()
        self.rowNum = None
        self.winningPattern = None
        self.winType = None
        self.gameboard = kwargs.pop("gameboard")
        self.turnNum = 1
        self.playerOneTakeovers = Text(text="Player 1 Takeovers: " + str(config.takeovers[0]), wordwrap=30, x=0.5, y=.3)
        self.playerTwoTakeovers = Text(text="Player 2 Takeovers: " + str(config.takeovers[1]), wordwrap=30, x=0.5, y=.2)
        self.playerThreeTakeovers = Text(text="Player 3 Takeovers: " + str(config.takeovers[2]), wordwrap=30, x=0.5,
                                         y=0.1)
        self.playerTurn = Text(text="Player # " + str(self.turnNum), wordwrap=30, x=0.5, y=0)
        self.msg = Text(text=" ", wordwrap=config.messageWordwrap, x=0.5, y=-0.1, scale=1.4, color=color.green)
        self.takeOverButton = kwargs.pop("takeoverButton")
        self.currentTurnLoc = None

    def input(self, keys):
        if keys == 'left mouse down':
            if not config.gameFinished:
                if self.gameboard.hoverBoxIndex < 27:
                    hoverIndex = self.gameboard.hoverBoxIndex
                    if not config.slotsOccupied[hoverIndex] and not self.takeOverButton.value:
                        self.placePlayerSymbol(hoverIndex)
                        self.msg.color = config.messageColorPurple  # sets color to a light purple ish
                        self.msg.text = "Placed symbol successfully!"
                        self.msg.wordwrap = config.messageWordwrap
                        print(config.slotPos[hoverIndex])
                    elif config.slotsOccupied[hoverIndex] and self.takeOverButton.value and config.takeovers[
                        self.turnNum - 1] > 0:
                        if self.calculateIfNextMoveWin(hoverIndex) is None:
                            if not config.currentSymbols[hoverIndex].playerNum == self.turnNum:
                                config.takeovers[self.turnNum - 1] -= 1
                                self.msg.color = config.messageColorGreen
                                self.msg.text = "Took over player " + str(self.turnNum) + "'s spot successfully!"
                                self.msg.wordwrap = config.messageWordwrap
                                print(config.slotPos[hoverIndex])
                                self.replacePlayerSymbol(hoverIndex)
                            else:
                                self.msg.color = config.messageColorRed
                                self.msg.text = "Cannot take over your own slot!"
                                self.msg.wordwrap = config.messageWordwrap
                                print(config.slotPos[hoverIndex])
                        elif not self.calculateIfNextMoveWin(hoverIndex) is None:
                            self.msg.text = "That move, is a TTW (takeover to win)! Please move elsewhere"
                            self.msg.wordwrap = config.messageWordwrap
                            self.msg.color = config.messageColorRed
                    elif not config.slotsOccupied[hoverIndex] and self.takeOverButton.value:
                        self.msg.color = config.messageColorRed
                        self.msg.text = "There is nothing in the spot to takeover! Please disable takeovers to place your " \
                                        "symbol"
                        self.msg.wordwrap = config.messageWordwrap
                    elif config.slotsOccupied[hoverIndex] and not self.takeOverButton.value:
                        self.msg.color = config.messageColorRed
                        self.msg.text = "That spot is already taken! Please press the takeover button to use a " \
                                        "takeover!"
                        self.msg.wordwrap = 10
            else:
                self.msg.text = "The game has finished! Please reset the game to play again!"
                self.msg.wordwrap = 10

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
        config.slotsOccupied[index] = False
        destroy(config.currentSymbols[index])

        config.slotsOccupied[index] = True
        config.currentSymbols[index] = p
        self.turnNum += 1
        if self.turnNum > 3:
            self.turnNum = self.turnNum % 3

    def findWinningSlotIndex(self, winningSlots, currentSlots ):
        indexOfWinningSlots = []
        matchingSlotIndexes = []
        matchingWinIndex = []

        for winSlot in winningSlots:
            indexOfWinningSlots.append(self.findSymbolIndexWithWorldPos(winSlot.position))
        for index in indexOfWinningSlots:
            for winSlotIndex in range(len(winningSlots)):
                if currentSlots[index] == winningSlots[winSlotIndex]:
                    matchingSlotIndexes.append(index)
                    matchingWinIndex.append(winSlotIndex)
                else:
                    return index, winSlotIndex # maube this needs ot be changed to matchingWinIndex

    def calculateIfNextMoveWin(self, index):
        p = PlayerSymbol(player=self.turnNum, position=config.slots[index].position, parent=self.gameboard)
        p.disable()
        potentialSlotsOccupied = config.slotsOccupied.copy()
        potentialCurrentSymbols = config.currentSymbols.copy()
        potentialSlotsOccupied[index] = True
        potentialCurrentSymbols[index] = p

        winningSlots = self.checkForAnyWin(potentialCurrentSymbols)
        if not winningSlots is None:
            winningIndex, winSlotIndex = self.findWinningSlotIndex(winningSlots, list(potentialCurrentSymbols))
            print(winningIndex)
            print(winningIndex)
            print(winningIndex)
            return winningIndex
        else:
            return None

    def checkForHorizontalWin(self, positions):
        for row in range(len(config.horizontalCombos)):
            slotOneSymbol = positions[self.findSymbolIndexWithPos(config.horizontalCombos[row][0])]
            slotTwoSymbol = positions[self.findSymbolIndexWithPos(config.horizontalCombos[row][1])]
            slotThreeSymbol = positions[self.findSymbolIndexWithPos(config.horizontalCombos[row][2])]

            if not (slotOneSymbol is None) and not (slotTwoSymbol is None) and not (slotThreeSymbol is None):
                if slotOneSymbol.playerNum == slotTwoSymbol.playerNum == slotThreeSymbol.playerNum:
                    self.winningPattern = ([[slotOneSymbol, slotTwoSymbol, slotThreeSymbol]])
                    self.rowNum = row
                    return [slotOneSymbol, slotTwoSymbol, slotThreeSymbol]

    def checkForMultilayerWin(self, positions):
        for row in range(len(config.multilayerCombos)):
            slotOneSymbol = positions[self.findSymbolIndexWithPos(config.multilayerCombos[row][0])]
            slotTwoSymbol = positions[self.findSymbolIndexWithPos(config.multilayerCombos[row][1])]
            slotThreeSymbol = positions[self.findSymbolIndexWithPos(config.multilayerCombos[row][2])]

            if not (slotOneSymbol is None) and not (slotTwoSymbol is None) and not (slotThreeSymbol is None):
                if slotOneSymbol.playerNum == slotTwoSymbol.playerNum == slotThreeSymbol.playerNum:
                    self.winningPattern = ([[slotOneSymbol, slotTwoSymbol, slotThreeSymbol]])
                    self.rowNum = row
                    return [slotOneSymbol, slotTwoSymbol, slotThreeSymbol]

    def checkForCornerToCornerWin(self, positions):
        for row in range(len(config.cornerCombos)):
            slotOneSymbol = positions[self.findSymbolIndexWithPos(config.cornerCombos[row][0])]
            slotTwoSymbol = positions[self.findSymbolIndexWithPos(config.cornerCombos[row][1])]
            slotThreeSymbol = positions[self.findSymbolIndexWithPos(config.cornerCombos[row][2])]
            if not (slotOneSymbol is None) and not (slotTwoSymbol is None) and not (slotThreeSymbol is None):
                if slotOneSymbol.playerNum == slotTwoSymbol.playerNum == slotThreeSymbol.playerNum:
                    self.winningPattern = ([[slotOneSymbol, slotTwoSymbol, slotThreeSymbol]])
                    self.rowNum = row
                    return [slotOneSymbol, slotTwoSymbol, slotThreeSymbol]

    def checkForAnyWin(self, positions):
        horizontalSlots = self.checkForHorizontalWin(positions)
        multilayerSlots = self.checkForMultilayerWin(positions)
        cornerSlots = self.checkForCornerToCornerWin(positions)
        if not horizontalSlots is None:
            self.winType = "horizontalSlots"
            return horizontalSlots
        if not multilayerSlots is None:
            self.winType = "multilayerSlots"
            return multilayerSlots
        if not cornerSlots is None:
            self.winType = "cornerSlots"
            return cornerSlots

    def findSymbolIndexWithPos(self, pos):
        for i in range(len(config.slotPos)):
            if config.slotPos[i] == pos:
                return i

    def findSymbolIndexWithWorldPos(self, pos):
        for i in range(len(config.slots)):
            if config.slots[i].position == pos:
                return i

    def gameWin(self, winningPlayer, winningSlots):
        self.msg.text = "Player " + str(winningPlayer) + " HAS WON! with a " + str(self.winType) + str(self.rowNum)
        self.msg.scale = 1.0
        config.gameFinished = True
        for slot in winningSlots:
            slot.rotation_y += 5

    def update(self):
        self.playerOneTakeovers.text = "Player 1 Takeovers: " + str(config.takeovers[0])
        self.playerTwoTakeovers.text = "Player 2 Takeovers: " + str(config.takeovers[1])
        self.playerThreeTakeovers.text = "Player 3 Takeovers: " + str(config.takeovers[2])
        self.playerTurn.text = "Player # " + str(self.turnNum)
        winningSlots = self.checkForAnyWin(config.currentSymbols)
        if not winningSlots is None:
            self.gameWin(winningSlots[0].playerNum, winningSlots)
