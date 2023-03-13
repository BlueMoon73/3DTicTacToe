from main import takeovers



class Player(Entity):

    def __init__(self, **kwargs):
        super().__init__()
        self.gameboard = kwargs.pop("gameboard")
        self.slotsOccupied = kwargs.pop("slotsOccupied")
        self.takeOverButton = kwargs.pop("takeOverButton")
        self.turnNum = 1
        self.playerOneTakeovers = Text(text="Player 1 Takeovers: " + str(takeovers[0]), wordwrap=30, x=0.5, y=.3)
        self.playerTwoTakeovers = Text(text="Player 2 Takeovers: " + str(takeovers[1]), wordwrap=30, x=0.5, y=.2)
        self.playerThreeTakeovers = Text(text="Player 3 Takeovers: " + str(takeovers[2]), wordwrap=30, x=0.5, y=0.1)
        self.playerTurn = Text(text="Player # " + str(self.turnNum), wordwrap=30, x=0.5, y=0)
        self.msg = Text(text=" ", wordwrap=6, x=0.5, y=-0.1, scale=1.4, color=color.green)

    def input(self, keys):
        if keys == 'left mouse down':
            gameBoard = self.gameboard
            slotsOccupied = self.slotsOccupied
            if gameBoard.hoverBoxIndex < 27:
                hoverIndex = gameBoard.hoverBoxIndex
                # print(takeOverButton.value)
                if not slotsOccupied[hoverIndex] and not takeOverButton.value:
                    self.placePlayerSymbol(hoverIndex)
                    self.msg.color = color.hsv(234, .88, .36)  # sets color to a light purple ish
                    self.msg.text = "Placed symbol sucessfully!"
                    # slots[hoverIndex].disable()

                elif slotsOccupied[hoverIndex] and takeOverButton.value and takeovers[self.turnNum - 1] > 0:

                    takeovers[self.turnNum - 1] -= 1
                    self.msg.color = color.hsv(156, .64, .41)
                    self.msg.text = "Took over player " + str(self.turnNum) + "'s spot sucessfully!"

                    self.replacePlayerSymbol(hoverIndex)
                elif not slotsOccupied[hoverIndex] and takeOverButton.value:
                    self.msg.color = color.hsv(6, .81, .55)
                    self.msg.text = "There is nothing in the spot to takeover! Please disable takeovers to place your symbol"
                elif slotsOccupied[hoverIndex] and not takeOverButton.value:
                    self.msg.color = color.hsv(6, .81, .55)
                    self.msg.text = "That spot is already taken! Please press the takeover button to use a " \
                                    "takeover!"

            else:
                pass

    # placing the player symbol, given a location (index)
    def placePlayerSymbol(self, index):
        p = PlayerSymbol(player=self.turnNum, position=slots[index].position)
        slotsOccupied[index] = True
        currentSymbols[index] = p
        self.turnNum += 1
        if self.turnNum > 3:
            self.turnNum = self.turnNum % 3

    # replacing a prexisiting symbol, if a takeover is used, given an index
    def replacePlayerSymbol(self, index):
        p = PlayerSymbol(player=self.turnNum, position=slots[index].position)
        slotsOccupied[index] = True
        destroy(currentSymbols[index])
        currentSymbols[index] = p
        self.turnNum += 1
        if self.turnNum > 3:
            self.turnNum = self.turnNum % 3

    def checkForHorizontalWin(self):
        # print(horizontalCombos)
        for row in range(len(horizontalCombos)):
            # if currentSymbols[self.findSymbolIndexWithPos(horizontalCombos[row][0])].playerNum and currentSymbols[self.findSymbolIndexWithPos(horizontalCombos[row][1])].playerNum and currentSymbols[self.findSymbolIndexWithPos(horizontalCombos[row][2])].playerNum:
            # if currentSymbols[self.findSymbolIndexWithPos(horizontalCombos[row][0])].playerNum:
            # print(currentSymbols[self.findSymbolIndexWithPos(horizontalCombos[row][0])].playerNum)
            # print("wtf")
            # print(horizontalCombos[row][0])
            # pos = horizontalCombos[row][0]
            #
            # print(self.findSymbolIndexWithPos(horizontalCombos[row][0]))
                print("someone has won")

                # i = self.findSymbolIndexWithPos()

        # pass

    def checkForMultilayerWin(self):
        pass

    def checkForCornerToCornerWin(self):
        pass

    def findSymbolIndexWithPos(self, pos):
        for i in range(len(slotPos)):
            if slotPos[i] == pos:
                return i
    def update(self):
        self.playerOneTakeovers.text = "Player 1 Takeovers: " + str(takeovers[0])
        self.playerTwoTakeovers.text = "Player 2 Takeovers: " + str(takeovers[1])
        self.playerThreeTakeovers.text = "Player 3 Takeovers: " + str(takeovers[2])
        self.playerTurn.text = "Player # " + str(self.turnNum)
        self.checkForHorizontalWin()
