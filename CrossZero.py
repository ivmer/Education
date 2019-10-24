import random
from tkinter import *

lstMainTable = []
lstDefeats = []
lstWins = []
lstRandomRate = []
bt1 = None
bt2 = None
bt3 = None
bt4 = None
bt5 = None
bt6 = None
bt7 = None
bt8 = None
bt9 = None
firstStep = 0

def ChangeLabelButton(row, col):
    global bt1, bt2, bt3, bt4, bt5, bt6,  bt7, bt8, bt9
    if row == 0 and col == 0:
        bt1['text'] = 'O'
    if row == 0 and col == 1:
        bt2['text'] = 'O'
    if row == 0 and col == 2:
        bt3['text'] = 'O'
    if row == 1 and col == 0:
        bt4['text'] = 'O'
    if row == 1 and col == 1:
        bt5['text'] = 'O'
    if row == 1 and col == 2:
        bt6['text'] = 'O'
    if row == 2 and col == 0:
        bt7['text'] = 'O'
    if row == 2 and col == 1:
        bt8['text'] = 'O'
    if row == 2 and col == 2:
        bt9['text'] = 'O'

def checkRow(character, mainIt, lst):
    global lstMainTable
    countHitsRow = countHitsCol = 0
    lastHitRow = lastHitCol = -1
    for it in range(3):
        if lstMainTable[mainIt][it] == character:
            countHitsRow += 1
        if lstMainTable[mainIt][it] == None:
            lastHitRow = it
        if lstMainTable[it][mainIt] == character:
            countHitsCol += 1
        if lstMainTable[it][mainIt] == None:
            lastHitCol = it
    if (lastHitRow != -1) and (countHitsRow == 2):
        lst += [[mainIt, lastHitRow]]
    if (lastHitCol != -1) and (countHitsCol == 2):
        lst += [[lastHitCol, mainIt]]

def checkCrossLines(character, lst):
    global lstMainTable
    countHitsMainCross = countHitsSlaveCross = 0
    lastHitMainCross = lastHitSlaveCross = -1
    for it in range(3):
        if lstMainTable[it][it] == character:
            countHitsMainCross += 1
        if lstMainTable[it][it] == None:
            lastHitMainCross = it
        if lstMainTable[it][2 - it] == character:
            countHitsSlaveCross += 1
        if lstMainTable[it][2 - it] == None:
            lastHitSlaveCross = it
    if (countHitsMainCross == 2) and (lastHitMainCross != -1):
        lst += [[lastHitMainCross, lastHitMainCross]]
    if (countHitsSlaveCross == 2) and (lastHitSlaveCross != -1):
        lst += [[lastHitSlaveCross, lastHitSlaveCross]]

def CollectAllSituations():
    global lstDefeats, lstWins, lstMainTable
    lstDefeats = []
    lstWins = []
    for it in range(3):
        checkRow('O', it, lstWins)
        checkRow('X', it, lstDefeats)
    checkCrossLines('O', lstWins)
    checkCrossLines('X', lstDefeats)

def CheckChanceDefeat():
    global lstDefeats, lstRandomRate, lstMainTable
    if len(lstDefeats):
        Position = lstDefeats[0]
        lstMainTable[Position[0]][Position[1]] = 'O'
        ChangeLabelButton(Position[0], Position[1])
        lstRandomRate.remove(Position)
        return False
    return True

def CheckChanceWin():
    global lstWins, lstRandomRate, lstMainTable
    if len(lstWins):
        Position = lstWins[0]
        lstMainTable[Position[0]][Position[1]] = 'O'
        ChangeLabelButton(Position[0], Position[1])
        lstRandomRate = []
        return False
    return True

def NextRate():
    global lstRandomRate, lstMainTable
    Max = len(lstRandomRate) - 1
    if Max > 0:
        NextStep = random.randint(0, Max)
        Position = lstRandomRate[NextStep]
        lstMainTable[Position[0]][Position[1]] = 'O'
        ChangeLabelButton(Position[0], Position[1])
        lstRandomRate.remove(Position)

def initilization():
    global lstRandomRate, lstMainTable
    for row in range(3):
        lstRowNextRate = []
        lstRowMaintable = []
        for col in range(3):
            lstRowNextRate += [[row, col]]
            lstRowMaintable += [None]
        lstRandomRate += lstRowNextRate
        lstMainTable += [lstRowMaintable]

def checkFreePlace(lstSep):
    global lstRandomRate, lstMainTable
    for posFree in lstRandomRate:
        if posFree == lstSep:
            lstMainTable[posFree[0]][posFree[1]] = 'X'
            lstRandomRate.remove(posFree)
            return True
    return False

def nextstepMan(lstSep):
    lstSepInt = [int(lstSep[0]), int(lstSep[1])]
    checkFreePlace(lstSepInt)

def checkWinLosing(character, message = "The man won!"):
    global lstMainTable, lstRandomRate
    for it in range(3):
        if (lstMainTable[it][0] == character and lstMainTable[it][1] == character and lstMainTable[it][2] == character) or (lstMainTable[0][it] == character and lstMainTable[1][it] == character and lstMainTable[2][it] == character):
            print(message)
            lstRandomRate = []
            return True
    if lstMainTable[0][0] == character and lstMainTable[1][1] == character and lstMainTable[2][2] == character:
        print(message)
        lstRandomRate = []
        return True
    if lstMainTable[0][2] == character and lstMainTable[1][1] == character and lstMainTable[2][0] == character:
        print(message)
        lstRandomRate = []
        return True
    return False


def onClickButton1():
    changeStatusButton(bt1, 0, 0)
    mainGame()

def onClickButton2():
    changeStatusButton(bt2, 0, 1)
    mainGame()

def onClickButton3():
    changeStatusButton(bt3, 0, 2)
    mainGame()

def onClickButton4():
    changeStatusButton(bt4, 1, 0)
    mainGame()

def onClickButton5():
    changeStatusButton(bt5, 1, 1)
    mainGame()

def onClickButton6():
    changeStatusButton(bt6, 1, 2)
    mainGame()

def onClickButton7():
    changeStatusButton(bt7, 2, 0)
    mainGame()

def onClickButton8():
    changeStatusButton(bt8, 2, 1)
    mainGame()

def onClickButton9():
    changeStatusButton(bt9, 2, 2)
    mainGame()

def changeStatusButton(bt, row, col):
    global lstRandomRate
    if [row, col] in lstRandomRate:
        bt['text'] = 'X'
        nextstepMan([row, col])
        checkWinLosing("X")
    else:
        print("This button is busy yet!!!")

def mainGame():
    global firstStep, lstRandomRate
    CollectAllSituations()
    if CheckChanceDefeat():
        if CheckChanceWin():
            NextRate()
    checkWinLosing('O', "The computer won!")

#if __name__ == "__main__":
initilization()
firstStep = random.random()
if firstStep >= 0.5:
   print("First step is Man")
else:
    print("First step is Computer")
    mainGame()

root = Tk()
bt1 = Button(text=' ', height=1, width=1, command=onClickButton1)
bt2 = Button(text=' ', height=1, width=1, command=onClickButton2)
bt3 = Button(text=' ', height=1, width=1, command=onClickButton3)
bt4 = Button(text=' ', height=1, width=1, command=onClickButton4)
bt5 = Button(text=' ', height=1, width=1, command=onClickButton5)
bt6 = Button(text=' ', height=1, width=1, command=onClickButton6)
bt7 = Button(text=' ', height=1, width=1, command=onClickButton7)
bt8 = Button(text=' ', height=1, width=1, command=onClickButton8)
bt9 = Button(text=' ', height=1, width=1, command=onClickButton9)
bt1.grid(row=0, column=0)
bt2.grid(row=0, column=1)
bt3.grid(row=0, column=2)
bt4.grid(row=1, column=0)
bt5.grid(row=1, column=1)
bt6.grid(row=1, column=2)
bt7.grid(row=2, column=0)
bt8.grid(row=2, column=1)
bt9.grid(row=2, column=2)
root.mainloop()


