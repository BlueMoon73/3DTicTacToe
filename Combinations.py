import config


def allPossibleHorziontalCombos():
    # HORIZONTAL COMBOS
    for x in range(3):
        for y in range(3):
            slot1 = [x, y, 0]
            slot2 = [x, y, 1]
            slot3 = [x, y, 2]

            row = [slot1, slot2, slot3]

            config.horizontalCombos.append(row)
    for x in range(3):
        for y in range(3):
            slot1 = [x, 0, y]
            slot2 = [x, 1, y]
            slot3 = [x, 2, y]

            row = [slot1, slot2, slot3]

            config.horizontalCombos.append(row)
    for x in range(3):
        for y in range(3):
            slot1 = [0, x, y]
            slot2 = [1, x, y]
            slot3 = [2, x, y]

            row = [slot1, slot2, slot3]

            config.horizontalCombos.append(row)
    print(config.horizontalCombos)


def allPossibleDiagonalMultilayeredCombos():
    for x in range(3):
        slot1 = [x, 0, 0]
        slot2 = [x, 1, 1]
        slot3 = [x, 2, 2]
        row = [slot1, slot2, slot3]
        config.multilayerCombos.append(row)
    for y in range(3):
        slot1 = [0, y, 0]
        slot2 = [1, y, 1]
        slot3 = [2, y, 2]
        row = [slot1, slot2, slot3]
        config.multilayerCombos.append(row)
    for z in range(3):
        slot1 = [0, 0, z]
        slot2 = [1, 1, z]
        slot3 = [2, 2, z]
        row = [slot1, slot2, slot3]
        config.multilayerCombos.append(row)


# diagonal

def allPossibleCornerCombos():
    slot1 = [0, 0, 0]
    slot2 = [1, 1, 1]
    slot3 = [2, 2, 2]
    row = [slot1, slot2, slot3]
    config.cornerCombos.append(row)

    slot4 = [2, 0, 0]
    slot5 = [1, 1, 1]
    slot6 = [0, 2, 2]
    row = (slot4, slot5, slot6)
    config.cornerCombos.append(row)

    slot7 = [0, 2, 0]
    slot8 = [1, 1, 1]
    slot9 = [2, 0, 2]
    row = [slot7, slot8, slot9]
    config.cornerCombos.append(row)

    slot10 = [2, 2, 0]
    slot11 = [1, 1, 1]
    slot12 = [0, 0, 2]
    row = (slot10, slot11, slot12)
    config.cornerCombos.append(row)


def makeWinningCombos():
    allPossibleHorziontalCombos()
    allPossibleDiagonalMultilayeredCombos()
    allPossibleCornerCombos()
