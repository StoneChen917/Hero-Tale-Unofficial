import pygame
import os
#from pydub import *
from decimal import *
from random import randint
import math
#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (51,204,51)
ORANGE = (255,153,0)
PURPLE = (102,0,51)
PINK = (255,0,255)
CYAN = (204,255,255)
DBLUE = (51,51,204)
DGREEN = (0,51,0)
LY = (255,255,204)
NICE = (204,204,255)
FORESTWHITE = (226, 228, 223)
#Create Level---------------------------------------------------------------------------------------------------------------------------------
#Loading Creation
def CreateLoad(loading_list):
    #Loading
    loading = LoadingClass()
    loading_list.add(loading)
#endfunction
#Pause Panel Creation
def CreatePanel(button_list, optionBlock_list, pauseButton_list, panelButton_list, levelOne_list, levelTwo_list, levelThree_list, nextLevelBlock_list, restartLevel_list, directionArrow_list, levelUp_list, upgradeButton_list, upgradeInstruction_list, upgradeTextButton_list, upgradeBox_list, okButton_list, quitLevel_list):
    upgradeButton = Button(15, 60, 60, 0, 1360, 820) #Upgrade
    button_list.add(upgradeButton)
    upgradeButton_list.add(upgradeButton)
    pauseButton = Button(8, 60, 60, 0, 1430, 820) #Pause
    pauseButton_list.add(pauseButton)
    button_list.add(pauseButton)
    levelOne_list.add(pauseButton)
    levelTwo_list.add(pauseButton)
    levelThree_list.add(pauseButton)
    quitButton = Button(11, 100, 40, 1, 700, 503)
    button_list.add(quitButton)
    panelButton_list.add(quitButton)
    restartButton2 = Button(13, 191, 40, 2, 654, 573)
    button_list.add(restartButton2)
    panelButton_list.add(restartButton2)
    optionBox = BlockClass(6, 800, 475, 350, 212) #Option box
    optionBlock_list.add(optionBox)
    nextLevelBlock_list.add(optionBox)
    restartLevel_list.add(optionBox)
    levelUp_list.add(optionBox)
    quitLevel_list.add(optionBox)
    upgradeTextButton = Button(16, 160, 40, 0, 670, 503) #Upgrade
    button_list.add(upgradeTextButton)
    levelUp_list.add(upgradeTextButton)
    upgradeTextButton_list.add(upgradeTextButton)
    upgradeInstruction = InstructionClass(14, 626, 90, 437, 359)
    levelUp_list.add(upgradeInstruction)
    quitInstruction = InstructionClass(10, 698, 77, 401, 362) #Instruction
    optionBlock_list.add(quitInstruction)
    savedInstruction = InstructionClass(11, 495, 60, 502, 379) #Instruction
    nextLevelBlock_list.add(savedInstruction)
    restartInstruction = InstructionClass(12, 585, 82, 457, 357) #Instruction
    restartLevel_list.add(restartInstruction)
    finishInstruction = InstructionClass(15, 0, 0, 378, 357) #Instruction
    quitLevel_list.add(finishInstruction)
    closeButton = Button(10, 60, 60, 0, 1068, 234) #Pause
    button_list.add(closeButton)
    panelButton_list.add(closeButton)
    levelUp_list.add(closeButton)
    nextButton = Button(12, 268, 40, 0, 616, 503)
    button_list.add(nextButton)
    nextLevelBlock_list.add(nextButton)
    quitButton3 = Button(11, 100, 40, 3, 700, 573)
    button_list.add(quitButton3)
    nextLevelBlock_list.add(quitButton3)
    quitButton2 = Button(11, 100, 40, 2, 700, 573)
    button_list.add(quitButton2)
    restartLevel_list.add(quitButton2)
    quitButton4 = Button(11, 100, 40, 4, 700, 533)
    button_list.add(quitButton4)
    quitLevel_list.add(quitButton4)
    restartButton = Button(13, 191, 40, 1, 654, 503)
    button_list.add(restartButton)
    restartLevel_list.add(restartButton)
    arrow = ItemClass(8, 0, 0, 1180, 400)
    directionArrow_list.add(arrow)
    optionBox2 = BlockClass(6, 800, 475, 350, 212) #Option box
    upgradeBox_list.add(optionBox2)
    levelUpInstruction = InstructionClass(13, 583, 77, 458, 362) #Instruction
    upgradeInstruction_list.add(levelUpInstruction)
    upgradeBox_list.add(levelUpInstruction)
    OkButton = Button(17, 54, 30, 0, 723, 503) #Upgrade
    upgradeBox_list.add(OkButton)
    okButton_list.add(OkButton)
#endfunction
#Characters Of Different Levels
def CreateCharacters0(oden_list, skull_list, skullAttack_list, character2_list, character3_list, mehira_list, talene2_list, yellowTriangle_list, player_list, leftPlayerAttack_list, rightPlayerAttack_list, tutorialEnemy_list, tutorial_list, levelOne_list, levelTwo_list, levelThree_list, leftEnemyAttack_list, rightEnemyAttack_list, character1_list, talene_list, taleneAttack_list):
    player = PlayerClass(50, 700, leftPlayerAttack_list, rightPlayerAttack_list)
    player_list.add(player)
    dummy = BanditClass(1, 295, 250, tutorial_list, leftEnemyAttack_list, rightEnemyAttack_list, 0)
    tutorialEnemy_list.add(dummy) #Specify Level
    character1_list.add(dummy)
    talene = RogueClass(-1000, 710, levelTwo_list, leftPlayerAttack_list, rightPlayerAttack_list, taleneAttack_list)
    talene_list.add(talene)
    character2_list.add(talene)
    talene2 = RogueClass(-500, 710, levelThree_list, leftPlayerAttack_list, rightPlayerAttack_list, taleneAttack_list)
    talene2_list.add(talene2)
    character3_list.add(talene2)
    mehira = ArunClass(-500, 700, levelThree_list, leftPlayerAttack_list, rightPlayerAttack_list)
    mehira_list.add(mehira)
    character3_list.add(mehira)
    oden = WarlockClass(-1000, 730, levelThree_list)
    oden_list.add(oden)
    character3_list.add(oden)
    yellowTriangle = ItemClass(11, 0, 0, -1000, 670)
    yellowTriangle_list.add(yellowTriangle)
    levelOne_list.add(yellowTriangle)
    levelTwo_list.add(yellowTriangle)
    levelThree_list.add(yellowTriangle)
    skull = ItemClass(12, 0, 0, -1000, 50)
    skull.SkullInitiation(skullAttack_list)
    levelThree_list.add(skull)
    skull_list.add(skull)
#endfunction
def CreateCharacters1(levelOne_list, enemy_list, warlock_list, wordBox_list, nextButton_list, rogue_list, leftEnemyAttack_list, rightEnemyAttack_list, rogueAttack_list, banditGroup1_list, banditGroup2_list, character1_list):
    warlock = WarlockClass(150,730,levelOne_list)
    warlock_list.add(warlock)
    character1_list.add(warlock)
    wordbox = BlockClass(5, 1065, 150, 217, 750)
    wordBox_list.add(wordbox)
    nextButton = Button(9, 60, 20, 0, 1195, 850)
    nextButton_list.add(nextButton)
    rogue = RogueClass(2260, 710, levelOne_list, leftEnemyAttack_list, rightEnemyAttack_list, rogueAttack_list)
    rogue_list.add(rogue)
    character1_list.add(rogue)
    for i in range(3):
        bandit = BanditClass(1, 2000+i*100, 700, levelOne_list, leftEnemyAttack_list, rightEnemyAttack_list, 3)
        banditGroup1_list.add(bandit) #Specify Level
        character1_list.add(bandit)
    #endfor
    bandit1 = BanditClass(1, 1670, 450, levelOne_list, leftEnemyAttack_list, rightEnemyAttack_list,4)
    bandit2 = BanditClass(1, 1780, 450, levelOne_list, leftEnemyAttack_list, rightEnemyAttack_list,4)
    bandit3 = BanditClass(1, 2670, 450, levelOne_list, leftEnemyAttack_list, rightEnemyAttack_list,4)
    bandit4 = BanditClass(1, 2780, 450, levelOne_list, leftEnemyAttack_list, rightEnemyAttack_list,4)
    bandit5 = BanditClass(1, 2170, 700, levelOne_list, leftEnemyAttack_list, rightEnemyAttack_list,4)
    bandit6 = BanditClass(1, 2280, 700, levelOne_list, leftEnemyAttack_list, rightEnemyAttack_list,4)
    banditGroup2_list.add(bandit1, bandit2, bandit3, bandit4, bandit5, bandit6)
    character1_list.add(bandit1, bandit2, bandit3, bandit4, bandit5, bandit6)
#endfunction
def CreateCharacters2(levelTwo_list, enemyAttack_list, leftEnemyAttack_list, rightEnemyAttack_list, banditGroup3_list, banditGroup4_list, mushroomGroup1_list, mushroomGroup2_list, mushroomGroup3_list, character2_list, arun_list, mushroomAttack_list, warlock2_list):
    arun = ArunClass(1400, 700, levelTwo_list, leftEnemyAttack_list, rightEnemyAttack_list)#Arun Boss
    arun_list.add(arun)
    for i in range(2):#Mushroom1
        mush1 = MushroomClass(randint(1,3), randint(200,1300), 720, levelTwo_list, mushroomAttack_list)
        mushroomGroup1_list.add(mush1)
        character2_list.add(mush1)
    #endfor
    bandit1 = BanditClass(0, 350, 450, levelTwo_list, leftEnemyAttack_list, rightEnemyAttack_list,5)#Bandit3
    bandit2 = BanditClass(0, 1100, 450, levelTwo_list, leftEnemyAttack_list, rightEnemyAttack_list,5)
    banditGroup3_list.add(bandit1, bandit2)
    for i in range(3):#Mushroom2
        mush2 = MushroomClass(randint(1,3), randint(1700,2800), 720, levelTwo_list, mushroomAttack_list)
        mushroomGroup2_list.add(mush2)
        character2_list.add(mush2)
    #endfor
    bandit3 = BanditClass(0, 1725, 450, levelTwo_list, leftEnemyAttack_list, rightEnemyAttack_list,6)#Bandit4
    bandit4 = BanditClass(0, 2725, 450, levelTwo_list, leftEnemyAttack_list, rightEnemyAttack_list,6)
    bandit5 = BanditClass(0, 2225, 280, levelTwo_list, leftEnemyAttack_list, rightEnemyAttack_list,6)
    banditGroup4_list.add(bandit3, bandit4, bandit5)
    for i in range(2):#Mushroom3
        mush3 = MushroomClass(randint(1,3), 2000, 720, levelTwo_list, mushroomAttack_list)
        mushroomGroup3_list.add(mush3)
        character2_list.add(mush3)
    #endfor
    warlock = WarlockClass(-500,730,levelTwo_list)#Warlock
    warlock2_list.add(warlock)
    character2_list.add(arun, bandit1, bandit2, bandit3, bandit4, bandit5, warlock)
#endfunction
def CreateCharacters3(levelThree_list, leftEnemyAttack_list, rightEnemyAttack_list, character3_list, skeleton1_list, abomination_list, abominationAttack_list, necromancer_list, warlock3_list):
    for i in range(2):
        skeleton1 = SkeletonClass(randint(200, 1000), 680, levelThree_list, leftEnemyAttack_list, rightEnemyAttack_list)
        skeleton1_list.add(skeleton1)
        character3_list.add(skeleton1)
    #endfor
    necromancer = NecromancerClass(1390, 700, levelThree_list, leftEnemyAttack_list, rightEnemyAttack_list)
    necromancer_list.add(necromancer)
    character3_list.add(necromancer)
    abomination = AbominationClass(-500, 565, levelThree_list, leftEnemyAttack_list, rightEnemyAttack_list)
    abomination_list.add(abomination)
    character3_list.add(abomination)
    warlock = WarlockClass(-500,730,levelThree_list)
    warlock3_list.add(warlock)
    character3_list.add(warlock)
#endfunction
#Currency Creation
def CreateMoney(tutorial_list, levelOne_list, levelTwo_list, levelThree_list, thousand_list, hundred_list, ten_list, one_list):
    coin = ItemClass(1, 50, 50, 15, 120)
    tutorial_list.add(coin)
    levelOne_list.add(coin)
    levelTwo_list.add(coin)
    levelThree_list.add(coin)
    #Thousand
    thousand = WordClass(0, 0, 24, 31, 85, 130)
    thousand_list.add(thousand)
    tutorial_list.add(thousand)
    levelOne_list.add(thousand)
    levelTwo_list.add(thousand)
    levelThree_list.add(thousand)
    #Hundred
    hundred = WordClass(0, 0, 24, 31, 115, 130)
    hundred_list.add(hundred)
    tutorial_list.add(hundred)
    levelOne_list.add(hundred)
    levelTwo_list.add(hundred)
    levelThree_list.add(hundred)
    #Ten
    ten = WordClass(0, 0, 24, 31, 145, 130)
    ten_list.add(ten)
    tutorial_list.add(ten)
    levelOne_list.add(ten)
    levelTwo_list.add(ten)
    levelThree_list.add(ten)
    #One
    one = WordClass(0, 0, 24, 31, 175, 130)
    one_list.add(one)
    tutorial_list.add(one)
    levelOne_list.add(one)
    levelTwo_list.add(one)
    levelThree_list.add(one)
#endfunction
#Menu Creation
def CreateMenu(menu_list, button_list):
    herotale = Title() #Creates title
    menu_list.add(herotale) #Make it visible
    #Start
    startButton = Button(1, 309, 93, 0, 595, 420)
    button_list.add(startButton)
    menu_list.add(startButton)
    settingsButton = Button(2, 615, 93, 0, 442, 560) #Settings
    button_list.add(settingsButton)
    menu_list.add(settingsButton)
    tutorialButton = Button(3, 639, 93, 0, 430, 700) #Tutorial
    button_list.add(tutorialButton)
    menu_list.add(tutorialButton)
#endfunction
#Setting Creation
def CreateSettings(setting_list, button_list, invincibleOn_list, invincibleOff_list, instantKillOn_list, instantKillOff_list, playerInvincible, instantKill):
    on = Button(18, 0, 0, 0, 844, 390) #On Button
    invincibleOn_list.add(on)
    off = Button(19, 0, 0, 0, 844, 390) #Off Button
    invincibleOff_list.add(off)
    on2 = Button(18, 0, 0, 1, 844, 470) #On Button
    instantKillOn_list.add(on2)
    off2 = Button(19, 0, 0, 1, 844, 470) #Off Button
    instantKillOff_list.add(off2)
    button_list.add(on, off, on2, off2)
    f = open("Game_Files/Setting.txt","r+") #Open Setting
    lines = f.readlines() #All data
    f.close() #Close
    #Determine which button to keep
    if lines[0].rstrip("\n") == "0":
        setting_list.add(off)
    else:
        setting_list.add(on)
        playerInvincible[0] = 1
    #endif
    if lines[1].rstrip("\n") == "0":
        setting_list.add(off2)
    else:
        setting_list.add(on2)
        instantKill[0] = 1
    #endif
    #More Buttons
    back = Button(5, 106, 31, 0, 50, 820) #Back Button
    credit = Button(20, 0, 0, 0, 1315, 820) #Back Button
    button_list.add(back, credit)
    #Text
    invin = InstructionClass(16, 0, 0, 537, 390) #Invincible instruction
    insta = InstructionClass(17, 0, 0, 537, 470) #Instant Kill instruction
    setting_list.add(insta, invin, back, credit)
#endfunction
def CreateCredits(credit_list, button_list):
    #Instructions
    pro = InstructionClass(18, 0, 0, 493, 290)
    des = InstructionClass(19, 0, 0, 551, 360)
    scr = InstructionClass(20, 0, 0, 493, 430)
    ani = InstructionClass(21, 0, 0, 551, 500)
    tes = InstructionClass(22, 0, 0, 578, 570)
    #Back
    back2 = Button(5, 106, 31 ,0, 50, 820) #Back Button
    button_list.add(back2)
    credit_list.add(pro, des, scr, ani, tes, back2)
#endfunction
#Reset some objects in file
def ResetFile(file_list, currentFileData_list):
    for item in currentFileData_list:
        currentFileData_list.remove(item)
        file_list.remove(item)
    #endfor
    #Open File 1
    f = open("Game_Files/File1.txt","r+") #Open file 1
    lines = f.readlines() #All data
    f.close() #Close
    WriteWords(0, lines[0], 293, 310, file_list, currentFileData_list) #Coin1 number
    WriteWords(0, lines[1], 293, 410, file_list, currentFileData_list) #Live1 number
    WriteWords(0, lines[3], 293, 510, file_list, currentFileData_list) #Shield1 number
    WriteWords(0, lines[2], 293, 610, file_list, currentFileData_list) #Level1 number
    WriteWords(0, lines[4], 293, 210, file_list, currentFileData_list) #Lvl1 number
    #Open File 2
    f = open("Game_Files/File2.txt","r+") #Open file 2
    lines = f.readlines() #All data
    f.close() #Close
    WriteWords(0, lines[0], 713, 310, file_list, currentFileData_list) #Coin2 number
    WriteWords(0, lines[1], 713, 410, file_list, currentFileData_list) #Live2 number
    WriteWords(0, lines[3], 713, 510, file_list, currentFileData_list) #Shield2 number
    WriteWords(0, lines[2], 713, 610, file_list, currentFileData_list) #Level2 number
    WriteWords(0, lines[4], 713, 210, file_list, currentFileData_list) #Lvl2 number
    #Open File 3
    f = open("Game_Files/File3.txt","r+") #Open file 3
    lines = f.readlines() #All data
    f.close() #Close
    WriteWords(0, lines[0], 1133, 310, file_list, currentFileData_list) #Coin3 number
    WriteWords(0, lines[1], 1133, 410, file_list, currentFileData_list) #Live3 number
    WriteWords(0, lines[3], 1133, 510, file_list, currentFileData_list) #Shield2 number
    WriteWords(0, lines[2], 1133, 610, file_list, currentFileData_list) #Level3 number
    WriteWords(0, lines[4], 1133, 210, file_list, currentFileData_list) #Lvl3 number
#endfunction
#Save Progress of the Game
def SaveProgress(currentFile, currency, live, gameLevel, shieldNum, playerLive, gameMode):
    if currentFile == 1:
        #Open File 1
        f = open("Game_Files/File1.txt","w+") #Open file 1
    elif currentFile == 2:
        #Open File 2
        f = open("Game_Files/File2.txt","w+") #Open file 2
    elif currentFile == 3:
        #Open File 3
        f = open("Game_Files/File3.txt","w+") #Open file 3
    #endif
    data = str(currency[0]) + str(currency[1]) + str(currency[2]) + str(currency[3]) + "\n" #Coins
    data += str(live[0]) + "\n" #Live
    data += str(gameLevel) + "\n" #Level
    data += str(shieldNum[0]) + "\n" #Shield
    data += str(playerLive[0]) + "\n" #Player Level
    data += str(gameMode[0])
    f.write(data)
    f.close()
#endfunction
#Reset Progress
def ResetProgress(num):
    f = open("Game_Files/File0.txt","r+") #Open file 0
    data = f.read()
    f.close()
    if num == 1:
        #Open File 1
        f = open("Game_Files/File1.txt","w+") #Open file 1
    elif num == 2:
        #Open File 2
        f = open("Game_Files/File2.txt","w+") #Open file 2
    elif num == 3:
        #Open File 3
        f = open("Game_Files/File3.txt","w+") #Open file 3
    #endif
    f.write(data)
    f.close()
#endfunction
#Save Files Creation
def CreateFile(file_list, button_list, item_list, crown_list, currentFileData_list):
    #File 1
    fileBox1 = BlockClass(2, 333, 639, 163, 130) #File box 1
    file_list.add(fileBox1)
    select1 = Button(4, 161, 31, 1, 249, 680) #Select Button 1
    button_list.add(select1)
    file_list.add(select1)
    lvl1 = ItemClass(6, 50, 50, 213, 200) #Level
    file_list.add(lvl1)
    coin1 = ItemClass(1, 50, 50, 213, 300) #Coin etc 1
    file_list.add(coin1)
    item_list.add(coin1)
    heart1 = ItemClass(2, 50, 50, 213, 400)
    file_list.add(heart1)
    shield1 = ItemClass(5, 50, 50, 213, 500)
    file_list.add(shield1)
    flag1 = ItemClass(3, 50, 50, 213, 600)
    file_list.add(flag1)
    #Open File 1
    f = open("Game_Files/File1.txt","r+") #Open file 1
    lines = f.readlines() #All data
    f.close() #Close
    WriteWords(0, lines[0], 293, 310, file_list, currentFileData_list) #Coin1 number
    WriteWords(0, lines[1], 293, 410, file_list, currentFileData_list) #Live1 number
    WriteWords(0, lines[3], 293, 510, file_list, currentFileData_list) #Shield1 number
    WriteWords(0, lines[2], 293, 610, file_list, currentFileData_list) #Level1 number
    WriteWords(0, lines[4], 293, 210, file_list, currentFileData_list) #Lvl1 number
    #File 2
    fileBox2 = BlockClass(2, 333, 639, 583, 130) #File box 2
    file_list.add(fileBox2)
    select2 = Button(4, 161, 31, 2, 669, 680) #Select Button 2
    button_list.add(select2)
    file_list.add(select2)
    lvl2 = ItemClass(6, 50, 50, 633, 200) #Level
    file_list.add(lvl2)
    coin2 = ItemClass(1, 50, 50, 633, 300) #Coin etc 2
    file_list.add(coin2)
    item_list.add(coin2)
    shield2 = ItemClass(5, 50, 50, 633, 500)
    file_list.add(shield2)
    heart2 = ItemClass(2, 50, 50, 633, 400)
    file_list.add(heart2)
    flag2 = ItemClass(3, 50, 50, 633, 600)
    file_list.add(flag2)
    #Open File 2
    f = open("Game_Files/File2.txt","r+") #Open file 2
    lines = f.readlines() #All data
    f.close() #Close
    WriteWords(0, lines[0], 713, 310, file_list, currentFileData_list) #Coin2 number
    WriteWords(0, lines[1], 713, 410, file_list, currentFileData_list) #Live2 number
    WriteWords(0, lines[3], 713, 510, file_list, currentFileData_list) #Shield2 number
    WriteWords(0, lines[2], 713, 610, file_list, currentFileData_list) #Level2 number
    WriteWords(0, lines[4], 713, 210, file_list, currentFileData_list) #Lvl2 number
    #File 3
    fileBox3 = BlockClass(2, 333, 639, 1003, 130) #File box 3
    file_list.add(fileBox3)
    select3 = Button(4, 161, 31 ,3, 1089, 680) #Select Button 3
    button_list.add(select3)
    file_list.add(select3)
    lvl3 = ItemClass(6, 50, 50, 1053, 200) #Level
    file_list.add(lvl3)
    coin3 = ItemClass(1, 50, 50, 1053, 300) #Coin etc 3
    file_list.add(coin3)
    item_list.add(coin3)
    shield3 = ItemClass(5, 50, 50, 1053, 500)
    file_list.add(shield3)
    heart3 = ItemClass(2, 50, 50, 1053, 400)
    file_list.add(heart3)
    flag3 = ItemClass(3, 50, 50, 1053, 600)
    file_list.add(flag3)
    #Open File 3
    f = open("Game_Files/File3.txt","r+") #Open file 3
    lines = f.readlines() #All data
    f.close() #Close
    WriteWords(0, lines[0], 1133, 310, file_list, currentFileData_list) #Coin3 number
    WriteWords(0, lines[1], 1133, 410, file_list, currentFileData_list) #Live3 number
    WriteWords(0, lines[3], 1133, 510, file_list, currentFileData_list) #Shield2 number
    WriteWords(0, lines[2], 1133, 610, file_list, currentFileData_list) #Level3 number
    WriteWords(0, lines[4], 1133, 210, file_list, currentFileData_list) #Lvl3 number
    #Back
    back = Button(5, 106, 31 ,0, 50, 820) #Back Button
    button_list.add(back)
    file_list.add(back)
    #Crown
    crown = BlockClass(3, 333, 140, 163, 7) #Crown
    file_list.add(crown)
    crown_list.add(crown)
    #Reset Buttons
    reset1 = Button(14, 92, 20, 1, 284, 778) #Reset Button 1
    button_list.add(reset1)
    file_list.add(reset1)
    reset2 = Button(14, 92, 20, 2, 704, 778) #Reset Button 2
    button_list.add(reset2)
    file_list.add(reset2)
    reset3 = Button(14, 92, 20, 3, 1124, 778) #Reset Button 3
    button_list.add(reset3)
    file_list.add(reset3)
    SetCrown(crown_list)
#endfunction
#LevelCreation(Tutorial)-----------------------------------------------------------------------------------
def CreateTutorialPlatform(tutorialBlock_list, tutorial_list, button_list):
    #Files
    f = open("Game_Files/Tutorial.txt","r+") #Open platforms file
    nodes = f.readlines() #All platforms
    nodesNum = len(nodes) #Number of platforms
    f.close() #Close
    #Nodes
    for i in range(nodesNum):
        line = nodes[i-2] #Skip the last line because it is empty
        #Type of Block
        typeOfBlock = int(line[0])
        #x position
        if line[1] == "0" and line[2] == "0": #If first two numbers are 0, than the number is the last two numbers (0030)
            xpos = int(str(line[3])+str(line[4]))
        elif line[1] == "0" and line[2] != "0": #If first number is 0, the number is the following three numbers (0300)
            xpos = int(str(line[2])+str(line[3])+str(line[4]))
        elif line[4] == str(0) and line[3] == str(0) and line[2] == str(0) and line[1] == str(0) : #If all numbers are 0, the number is (0)
            xpos = 0
        else: #If else, the number is just a four digit number (4300)
            xpos = int(str(line[1])+str(line[2])+str(line[3])+str(line[4]))
        #endif
        #y position
        if line[5] == str(0): #If first number is 0, the number is the last two numbers
            ypos = int(str(line[6])+str(line[7]))
        else:
            ypos = int(str(line[5])+str(line[6])+str(line[7]))
        #endif
        #width
        if line[8] == str(0): #If first number is 0, the number is the last two numbers
            width = int(str(line[9])+str(line[10]))
        else:
            width = int(str(line[8])+str(line[9])+str(line[10]))
        #endif
        #hieght
        if line[11] == str(0): #If first number is 0, the number is the last two numbers
            height = int(str(line[12])+str(line[13]))
        else:
            height = int(str(line[11])+str(line[12])+str(line[13]))
        #endif
        if line[0] == str(1): #If it is a normal block, create a normal platform
            block = BlockClass(typeOfBlock, width, height, xpos, ypos) #Creates a block with given width & height
            tutorialBlock_list.add(block) #Used for later collision
            tutorial_list.add(block) #Make it visible
        #endif
    #endfor
    ground = GroundClass() #Creates ground
    tutorial_list.add(ground) #Make it visible
    #Some blocks
    startBlock = BlockClass(0, 10, 800, -10, 0)
    tutorialBlock_list.add(block)
    #Instructions
    moveInstruction = InstructionClass(1, 334, 27, 88, 670)
    jumpInstruction = InstructionClass(2, 274, 25, 778, 670)
    attackInstruction = InstructionClass(3, 229, 20, 205, 182)
    rollInstruction = InstructionClass(4, 187, 20, 1126, 330)
    dJumpInstruction = InstructionClass(5, 369, 25, 728, 580)
    blockInstruction = InstructionClass(6, 327, 20, 157, 102)
    coinInstruction = InstructionClass(8, 487, 27, 15, 26)
    fakeInstruction = InstructionClass(9, 354, 20, 15, 72)
    tutorial_list.add(moveInstruction, jumpInstruction, attackInstruction, rollInstruction, dJumpInstruction, blockInstruction, coinInstruction, fakeInstruction)
    #Quit Button
    closeButton1 = Button(10, 60, 60, 0, 1430, 10) #Pause
    button_list.add(closeButton1)
    tutorial_list.add(closeButton1)
#endfunction
def CreateBackgrounds(levelOne_list, levelTwo_list, levelThree_list, background1_list, background2_list, background3_list, cloud_list, ground_list, allBackgrounds_list, background_list, whiteScreen_list):
    back1 = BackgroundClass(0, 2560, 800, 0, 0)
    back2 = BackgroundClass(1, 2560, 800, 0, 0)
    back3 = BackgroundClass(1, 2560, 800, 2560, 0)
    allBackgrounds_list.add(back1, back2)
    background_list.add(back1, back2, back3)
    background1_list.add(back1)
    background2_list.add(back1,back2)
    cloud_list.add(back3, back2)
    levelOne_list.add(back3, back2, back1)
    levelTwo_list.add(back2, back1)
    levelThree_list.add(back2, back1)
    ground = GroundClass() #Creates ground
    ground_list.add(ground)
    levelOne_list.add(ground) #Make it visible
    levelTwo_list.add(ground)
    levelThree_list.add(ground)
    screen1 = ItemClass(10, 0, 0, 0, 0)
    whiteScreen_list.add(screen1)
#endfunction
#LevelCreation(Level 1-3)
def CreateLevelPlatform(block1_list, levelOne_list, block2_list, levelTwo_list):
    #Files
    f = open("Game_Files/LevelPlatform.txt","r+") #Open platforms file
    nodes = f.readlines() #All platforms
    nodesNum = len(nodes) #Number of platforms
    f.close() #Close
    #Nodes
    for i in range(nodesNum):
        line = nodes[i] #Skip the last line because it is empty
        #Type of Block
        typeOfBlock = int(line[0])
        #x position
        if line[1] == "0" and line[2] == "0": #If first two numbers are 0, than the number is the last two numbers (0030)
            xpos = int(str(line[3])+str(line[4]))
        elif line[1] == "0" and line[2] != "0": #If first number is 0, the number is the following three numbers (0300)
            xpos = int(str(line[2])+str(line[3])+str(line[4]))
        elif line[4] == str(0) and line[3] == str(0) and line[2] == str(0) and line[1] == str(0) : #If all numbers are 0, the number is (0)
            xpos = 0
        else: #If else, the number is just a four digit number (4300)
            xpos = int(str(line[1])+str(line[2])+str(line[3])+str(line[4]))
        #endif
        #y position
        if line[5] == str(0): #If first number is 0, the number is the last two numbers
            ypos = int(str(line[6])+str(line[7]))
        else:
            ypos = int(str(line[5])+str(line[6])+str(line[7]))
        #endif
        #width
        if line[8] == str(0): #If first number is 0, the number is the last two numbers
            width = int(str(line[9])+str(line[10]))
        else:
            width = int(str(line[8])+str(line[9])+str(line[10]))
        #endif
        #hieght
        if line[11] == str(0): #If first number is 0, the number is the last two numbers
            height = int(str(line[12])+str(line[13]))
        else:
            height = int(str(line[11])+str(line[12])+str(line[13]))
        #endif
        if line[0] == str(1): #If it is a normal block, create a normal platform
            block = BlockClass(typeOfBlock, width, height, xpos, ypos) #Creates a block with given width & height
            if line[14] == "1":
                block1_list.add(block) #Used for later collision
                levelOne_list.add(block) #Make it visible
            elif line[14] == "2":
                block2_list.add(block) #Used for later collision
                levelTwo_list.add(block) #Make it visible
            #endif
        #endif
    #endfor
#endfunction
#Load Scripts into the game
def ReadScript(script1, script2, script3):
    f = open("Game_Files/Level1Script.txt","r+") #Open
    lines = f.readlines() #All lines
    num = len(lines) #Number of lines
    f.close() #Close
    for i in range(num):
        script1.append(lines[i])
    #endfor
    f = open("Game_Files/Level2Script.txt","r+") #Open
    lines = f.readlines() #All lines
    num = len(lines) #Number of lines
    f.close() #Close
    for i in range(num):
        script2.append(lines[i])
    #endfor
    f = open("Game_Files/Level3Script.txt","r+") #Open
    lines = f.readlines() #All lines
    num = len(lines) #Number of lines
    f.close() #Close
    for i in range(num):
        script3.append(lines[i])
    #endfor
#endfunction
#Menu Class ----------------------------------------------------------------------------------------
#Title
class Title(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([1250, 184])
        self.rect = self.image.get_rect() #Get the shape
        self.rect.x = 125 #Set pos
        self.rect.y = 100
        self.titleImage = [pygame.transform.scale(pygame.image.load('Game_Images/Text/GameTitle.png'), (1250, 184))]
        self.image = self.titleImage[0]
    #endmethod
#endclass
#ButtonClass
class Button(pygame.sprite.Sprite):
    def __init__(self, imageNumber, width, height, number, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect() #Get the shape
        self.imageNum = imageNumber
        self.num = number
        self.rect.x = x
        self.rect.y = y
        #Images
        self.play = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Play1.png'), (309, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Play2.png'), (309, 93))]
        self.set = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Settings1.png'), (615, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Settings2.png'), (615, 93))]
        self.tutorial = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Tutorial1.png'), (639, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Tutorial2.png'), (639, 93))]
        self.select = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Select1.png'), (161, 31)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Select2.png'), (161, 31))]
        self.back = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Back1.png'), (106, 31)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Back2.png'), (106, 31))]
        self.easy = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Easy1.png'), (411, 120)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Easy2.png'), (411, 120))]
        self.hard = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Hard1.png'), (441, 120)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Hard2.png'), (441, 120))]
        self.pause = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Pause1.png'), (60, 60)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Pause2.png'), (60, 60))]
        self.close = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Close1.png'), (60, 60)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Close2.png'), (60, 60))]
        self.next = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Next1.png'), (60, 20)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Next2.png'), (60, 20))]
        self.quit = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Quit1.png'), (width, height)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Quit2.png'), (width, height))]
        self.nextLevel = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/NextLevel1.png'), (width, height)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/NextLevel2.png'), (width, height))]
        self.restart = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Restart1.png'), (width, height)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Restart2.png'), (width, height))]
        self.reset = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Reset1.png'), (width, height)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Reset2.png'), (width, height))]
        self.upgrade = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Upgrade1.png'), (60, 60)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Upgrade2.png'), (60, 60))]
        self.upgradeText = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/UpgradeText1.png'), (160, 40)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/UpgradeText2.png'), (160, 40))]
        self.ok = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Ok1.png'), (54, 30)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Ok2.png'), (54, 30))]
        self.on = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/On1.png'), (74, 40)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/On2.png'), (74, 40))]
        self.off = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Off1.png'), (100, 40)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Off2.png'), (100, 40))]
        self.credits = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Credits1.png'), (135, 31)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Credits2.png'), (135, 31))]
        if self.imageNum == 1:
            self.image = self.play[0]
        elif self.imageNum == 2:
            self.image = self.set[0]
        elif self.imageNum == 3:
            self.image = self.tutorial[0]
        elif self.imageNum == 4:
            self.image = self.select[0]
        elif self.imageNum == 5:
            self.image = self.back[0]
        elif self.imageNum == 6:
            self.image = self.easy[0]
        elif self.imageNum == 7:
            self.image = self.hard[0]
        elif self.imageNum == 8:
            self.image = self.pause[0]
        elif self.imageNum == 9:
            self.image = self.next[0]
        elif self.imageNum == 10:
            self.image = self.close[0]
        elif self.imageNum == 11:
            self.image = self.quit[0]
        elif self.imageNum == 12:
            self.image = self.nextLevel[0]
        elif self.imageNum == 13:
            self.image = self.restart[0]
        elif self.imageNum == 14:
            self.image = self.reset[0]
        elif self.imageNum == 15:
            self.image = self.upgrade[0]
        elif self.imageNum == 16:
            self.image = self.upgradeText[0]
        elif self.imageNum == 17:
            self.image = self.ok[0]
        elif self.imageNum == 18:
            self.image = self.on[0]
        elif self.imageNum == 19:
            self.image = self.off[0]
        elif self.imageNum == 20:
            self.image = self.credits[0]
        #endif
    #endmethod
    def Change(self, pos, level):
        if level == 0 and pos[0] >= 595 and pos[1] >= 420 and pos[0] <= 904 and pos[1] <= 513 and self.imageNum == 1: #Menu
            self.image = self.play[1] #Hover on start button
        elif level == 0 and pos[0] >= 442 and pos[1] >= 560 and pos[0] <= 1057 and pos[1] <= 653 and self.imageNum == 2: #Settings
            self.image = self.set[1] #Hover on Settings
        elif level == 0 and pos[0] >= 430 and pos[1] >= 700 and pos[0] <= 1069 and pos[1] <= 793 and self.imageNum == 3: #Tutorial
            self.image = self.tutorial[1] #Hover on Tutorial
        elif level == 1 and pos[0] >= 544 and pos[1] >= 300 and pos[0] <= 955 and pos[1] <= 420 and self.imageNum == 6: #Easy
            self.image = self.easy[1] #Hover on Easy
        elif level == 1 and pos[0] >= 529 and pos[1] >= 300 and pos[0] <= 970 and pos[1] <= 420 and self.imageNum == 7: #Hard
            self.image = self.hard[1] #Hover on Hard
        elif level == 1 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851 and self.imageNum == 5: #Back Button on Settings
            self.image = self.back[1] #Hover on back
        elif level == 3 and pos[0] >= 249 and pos[1] >= 680 and pos[0] <= 410 and pos[1] <= 711 and self.imageNum == 4 and self.num == 1: #Save Files Select
            self.image = self.select[1] #Hover on select file 1
        elif level == 3 and pos[0] >= 669 and pos[1] >= 680 and pos[0] <= 830 and pos[1] <= 711 and self.imageNum == 4 and self.num == 2:
            self.image = self.select[1] #Hover on select file 2
        elif level == 3 and pos[0] >= 1089 and pos[1] >= 680 and pos[0] <= 1250 and pos[1] <= 711 and self.imageNum == 4 and self.num == 3:
            self.image = self.select[1] #Hover on select file 3
        elif level == 3 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851 and self.imageNum == 5:
            self.image = self.back[1] #Hover on back
        elif level == 2 and pos[0] >= 1430 and pos[1] >= 10 and pos[0] <= 1490 and pos[1] <= 70 and self.imageNum == 10:
            self.image = self.close[1] #Hover on pause
        elif level == 4 and pos[0] >= 1430 and pos[1] >= 820 and pos[0] <= 1490 and pos[1] <= 880 and self.imageNum == 8:
            self.image = self.pause[1] #Hover on close
        elif level == 4 and pos[0] >= 1195 and pos[1] >= 850 and pos[0] <= 1255 and pos[1] <= 870 and self.imageNum == 9:
            self.image = self.next[1]
        elif level == 4 and pos[0] >= 1068 and pos[1] >= 234 and pos[0] <= 1128 and pos[1] <= 294 and self.imageNum == 10:
            self.image = self.close[1]
        elif level == 4 and pos[0] >= 700 and pos[1] >= 503 and pos[0] <= 800 and pos[1] <= 543 and self.imageNum == 11 and self.num == 1:
            self.image = self.quit[1]
        elif level == 4 and pos[0] >= 616 and pos[1] >= 503 and pos[0] <= 884 and pos[1] <= 543 and self.imageNum == 12:
            self.image = self.nextLevel[1]
        elif level == 4 and pos[0] >= 700 and pos[1] >= 573 and pos[0] <= 800 and pos[1] <= 613 and self.imageNum == 11 and self.num == 3:
            self.image = self.quit[1]
        elif level == 4 and pos[0] >= 700 and pos[1] >= 573 and pos[0] <= 800 and pos[1] <= 613 and self.imageNum == 11 and self.num == 2:
            self.image = self.quit[1]
        elif level == 4 and pos[0] >= 654 and pos[1] >= 503 and pos[0] <= 845 and pos[1] <= 543 and self.imageNum == 13 and self.num == 1:
            self.image = self.restart[1]
        elif level == 4 and pos[0] >= 654 and pos[1] >= 573 and pos[0] <= 845 and pos[1] <= 613 and self.imageNum == 13 and self.num == 2:
            self.image = self.restart[1]
        elif level == 3 and pos[0] >= 284 and pos[1] >= 778 and pos[0] <= 376 and pos[1] <= 798 and self.imageNum == 14 and self.num == 1: #Save Files Reset
            self.image = self.reset[1] #Hover on reset file 1
        elif level == 3 and pos[0] >= 704 and pos[1] >= 778 and pos[0] <= 796 and pos[1] <= 798 and self.imageNum == 14 and self.num == 2:
            self.image = self.reset[1] #Hover on reset file 2
        elif level == 3 and pos[0] >= 1124 and pos[1] >= 778 and pos[0] <= 1216 and pos[1] <= 798 and self.imageNum == 14 and self.num == 3:
            self.image = self.reset[1] #Hover on reset file 3
        elif level == 4 and pos[0] >= 1360 and pos[1] >= 820 and pos[0] <= 1420 and pos[1] <= 880 and self.imageNum == 15:
            self.image = self.upgrade[1] #Hover on close
        elif level == 4 and pos[0] >= 670 and pos[1] >= 503 and pos[0] <= 830 and pos[1] <= 543 and self.imageNum == 16:
            self.image = self.upgradeText[1]
        elif level == 4 and pos[0] >= 723 and pos[1] >= 503 and pos[0] <= 777 and pos[1] <= 533 and self.imageNum == 17:
            self.image = self.ok[1]
        elif level == 4 and pos[0] >= 700 and pos[1] >= 533 and pos[0] <= 800 and pos[1] <= 573 and self.imageNum == 11 and self.num == 4:
            self.image = self.quit[1]
        elif level == 1 and pos[0] >= 844 and pos[1] >= 390 and pos[0] <= 918 and pos[1] <= 430 and self.imageNum == 18 and self.num == 0:
            self.image = self.on[1]
        elif level == 1 and pos[0] >= 844 and pos[1] >= 390 and pos[0] <= 944 and pos[1] <= 430 and self.imageNum == 19 and self.num == 0:
            self.image = self.off[1]
        elif level == 1 and pos[0] >= 844 and pos[1] >= 470 and pos[0] <= 918 and pos[1] <= 510 and self.imageNum == 18 and self.num == 1:
            self.image = self.on[1]
        elif level == 1 and pos[0] >= 844 and pos[1] >= 470 and pos[0] <= 944 and pos[1] <= 510 and self.imageNum == 19 and self.num == 1:
            self.image = self.off[1]
        elif level == 5 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851 and self.imageNum == 5:
            self.image = self.back[1] #Hover on back
        elif level == 1 and pos[0] >= 1315 and pos[1] >= 820 and pos[0] <= 1450 and pos[1] <= 851 and self.imageNum == 20:
            self.image = self.credits[1]
        else:
            if self.imageNum == 1:
                self.image = self.play[0]
            elif self.imageNum == 2:
                self.image = self.set[0]
            elif self.imageNum == 3:
                self.image = self.tutorial[0]
            elif self.imageNum == 4:
                self.image = self.select[0]
            elif self.imageNum == 5:
                self.image = self.back[0]
            elif self.imageNum == 6:
                self.image = self.easy[0]
            elif self.imageNum == 7:
                self.image = self.hard[0]
            elif self.imageNum == 8:
                self.image = self.pause[0]
            elif self.imageNum == 9:
                self.image = self.next[0]
            elif self.imageNum == 10:
                self.image = self.close[0]
            elif self.imageNum == 11:
                self.image = self.quit[0]
            elif self.imageNum == 12:
                self.image = self.nextLevel[0]
            elif self.imageNum == 13:
                self.image = self.restart[0]
            elif self.imageNum == 14:
                self.image = self.reset[0]
            elif self.imageNum == 15:
                self.image = self.upgrade[0]
            elif self.imageNum == 16:
                self.image = self.upgradeText[0]
            elif self.imageNum == 17:
                self.image = self.ok[0]
            elif self.imageNum == 18:
                self.image = self.on[0]
            elif self.imageNum == 19:
                self.image = self.off[0]
            elif self.imageNum == 20:
                self.image = self.credits[0]
            #endif
        #endif
    #endmethod
#endclass
#Save Files Class------------------------------------------------------------------------------------------------------------------
#ItemClassPos
class ItemClass(pygame.sprite.Sprite):
    def __init__(self, typeOfItem, width, height, x, y):
        super().__init__()
        width1 = width
        if typeOfItem == 4:
            width = 160
        #endif
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape
        self.rect.x = x #Set position
        self.rect.y = y
        self.item = typeOfItem
        #Attributes
        self.vertSpeed = 0
        self.horiSpeed = 0
        self.finalX = randint(-30,30)
        if self.finalX > 0:
            self.horiSpeed = 1
        elif self.finalX < 0:
            self.horiSpeed = -1
        #endif
        self.moveX = 0
        #Coin
        self.dropped = False
        self.getCoin = False
        self.coinAnimationEnd = False
        #self.coinSound = AudioSegment.from_wav('Game_Sounds/Object/coin.wav')
        #Counters
        self.coinCounter = 0
        #Javelin
        self.javelinCounter = 0
        #Timers
        self.startAnimation = 0
        self.endAnimation = 0
        self.startDisappear = 0
        self.endDisappear = 0
        self.coins = []
        for x in range(7):
            add_str = str(x+1)
            self.coins.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Coins/Coin" + add_str + ".png"), (width, height)))
        #endfor
        self.javelin = []
        for x in range(4):
            add_str = str(x)
            self.javelin.append(pygame.transform.scale(pygame.image.load("Game_Images/Arun/Javelin/Javelin_" + add_str + ".png"), (160, 40)))
        #endfor
        self.stars = []
        for x in range(4):
            add_str = str(x)
            self.stars.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Stars/Star" + add_str + ".png"), (150, 50)))
        #endfor
        self.hearts = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Hearts/Heart.png"), (50, 50))] #Hearts
        self.flags = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Flags/Flag.png"), (50, 50))] #Flags
        self.shields = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Shields/Shield1.png"), (50, 50)), pygame.transform.scale(pygame.image.load("Game_Images/Object/Shields/Shield2.png"), (50, 50))] #Shields
        self.levels = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Levels/LevelIcon.png"), (width, height))] #Level
        self.levelNumbers = [pygame.transform.scale(pygame.image.load("Game_Images/Text/Level0.png"), (14, 20)), pygame.transform.scale(pygame.image.load("Game_Images/Text/Level1.png"), (14, 20)), pygame.transform.scale(pygame.image.load("Game_Images/Text/Level2.png"), (14, 20)), pygame.transform.scale(pygame.image.load("Game_Images/Text/Level3.png"), (14, 20))]
        self.arrows = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Arrows/Arrow.png"), (140, 121))] #Arrow
        self.whiteScreen = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Screens/White.png"), (1500, 900))] #White Screen
        self.yellowTriangle = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Shapes/YellowTriangle.png"), (50, 30))] #Yellow Triangle
        self.skull = [pygame.transform.scale(pygame.image.load("Game_Images/Skull/Skull1.png"), (400, 400)), pygame.transform.scale(pygame.image.load("Game_Images/Skull/Skull2.png"), (400, 400))] #Skull
        if self.item == 1: #Set image
            self.image = self.coins[0]
        elif self.item == 2:
            self.image = self.hearts[0]
        elif self.item == 3:
            self.image = self.flags[0]
        elif self.item == 4:
            self.image = self.javelin[0]
            self.speed = width1
        elif self.item == 5:
            self.image = self.shields[0]
        elif self.item == 6:
            self.image = self.levels[0]
        elif self.item == 7:
            self.image = self.levelNumbers[0]
        elif self.item == 8:
            self.image = self.arrows[0]
            self.visible = True
            self.firstTime = True
        elif self.item == 9:
            self.image = self.stars[0]
        elif self.item == 10:
            self.image = self.whiteScreen[0]
        elif self.item == 11:
            self.image = self.yellowTriangle[0]
        elif self.item == 12:
            self.image = self.skull[0]
            self.scaley = self.rect.y*10
            self.scalex = self.rect.x*10
            self.up = True
        #endif
    #endmethod
    def SkullMove(self):
        if self.up:
            self.scaley -= 5
            self.rect.y = self.scaley/10
            if self.rect.y == 45:
                self.up = False
            #endif
        else:
            self.scaley += 5
            self.rect.y = self.scaley/10
            if self.rect.y == 55:
                self.up = True
            #endif
        #endif
    #endmethod
    def SkullInitiation(self, skullAttack_list):
        self.attack = AttackClass(400, 400, -1000, 0) #Attack
        skullAttack_list.add(self.attack)
    #endmethod
    def SkullResetY(self):
        self.scaley = 500
        self.rect.y = self.scaley/10
        self.scalex = 5500
        self.rect.x = self.scalex/10
    #endmethod
    def SkullReset(self):
        self.scaley = 500
        self.rect.y = self.scaley/10
        self.scalex = -10000
        self.rect.x = self.scalex/10
        self.attack.rect.x = -1000
    #endmethod
    def SkullUpdate(self, num):
        self.image = self.skull[num]
    #endmethod
    def SkullCrush(self):
        self.scalex += 660
        self.scaley += 515
        self.rect.x = self.scalex/10
        self.rect.y = self.scaley/10
        if self.rect.x % 1 == 0 and self.rect.y % 1 == 0:
            self.attack.rect.x = self.rect.x
            self.attack.rect.y = self.rect.y
        #endif
    #endmethod
    def ArrowUpdate(self, level_list):
        if self.firstTime:
            level_list.add(self)
            self.firstTime = False
        #endif
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Record current time
        if self.endAnimation - self.startAnimation >= 500:
            self.startAnimation = self.endAnimation
            if self.visible:
                self.visible = False
                level_list.remove(self)
            else:
                self.visible = True
                level_list.add(self)
            #endif
        #endif
    #endmethod
    def ArrowReset(self, level_list):
        self.firstTime = True
        self.visible = True
        level_list.remove(self)
        self.startAnimation = 0
        self.endAnimation = 0
    #endmethod
    def UpdateLevel(self, num):
        self.image = self.levelNumbers[num]
    #endmethod
    def StarUpdate(self, num):
        self.image = self.stars[num]
    #endmethod
    def ShieldUpdate(self, num):
        if num == 0:
            self.image = self.shields[1]
        else:
            self.image = self.shields[0]
        #endif
    #endmethod
    def JavelinUpdate(self, leftJavelin_list, rightJavelin_list, levelTwo_list):
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Record current time
        if self.endAnimation - self.startAnimation >= 60:
            self.endAnimation = 0
            self.startAnimation = 0
            if self.javelinCounter < 3:
                self.javelinCounter += 1
            else:
                self.javelinCounter = 0
            #endif
            if self.speed > 0:
                self.image = self.javelin[self.javelinCounter]
            else:
                self.image = pygame.transform.flip(self.javelin[self.javelinCounter],1,0)
            #endif
        #endif
        self.rect.x += self.speed
        if self.rect.x <= -160:
            leftJavelin_list.remove(self)
            levelTwo_list.remove(self)
        elif self.rect.x >= 1660:
            rightJavelin_list.remove(self)
            levelTwo_list.remove(self)
        #endif
    #endmethod
    def Change(self):
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        if self.endAnimation - self.startAnimation >= 120 and self.item == 1 and not self.getCoin:
            self.startAnimation = self.endAnimation #Reset timer
            self.image = self.coins[self.coinCounter]
            if self.coinCounter == 4:
                self.coinCounter = 0
            else:
                self.coinCounter += 1
            #endif
        elif self.endAnimation - self.startAnimation >= 150 and self.item == 1 and self.getCoin:
            self.startAnimation = self.endAnimation #Reset timer
            self.image = self.coins[self.coinCounter]
            if self.coinCounter == 6:
                self.coinCounter = 6
                if self.startDisappear == 0: #If start timer has not started yet
                    self.startDisappear = pygame.time.get_ticks() #Record current time
                #endif
                self.endDisappear = pygame.time.get_ticks()#Record current time
                if self.endDisappear - self.startDisappear >= 80:
                    self.endDisappear = 0
                    self.startDisappear = 0
                    self.coinAnimationEnd = True
                #endif
            elif self.coinCounter == 5:
                self.coinCounter += 1
            #endif
        #endif
    #endmethod
    def CoinDelete(self, sprite_list):
        sprite_list.remove(self)
    #endmethod
    def CoinSet(self, x, y):
        self.image = self.coins[0]
        self.rect.x = x
        self.rect.y = y
        self.dropped = False
        self.getCoin = False
        self.vertSpeed = 0
        self.horiSpeed = 0
        self.finalX = randint(-30,30)
        self.coinAnimationEnd = False
        if self.finalX > 0:
            self.horiSpeed = 1
        elif self.finalX < 0:
            self.horiSpeed = -1
        #endif
        self.coinCounter = 0
        self.moveX = 0
    #endmethod
    def CoinUpdate(self, player_list, block_list, level_list, coin_list, currency):
        if not self.dropped:
            self.dropped = True
            self.vertSpeed = randint(6,7)
        #endif
        if not self.getCoin:
            for player in player_list: #If player touch coin
                if self.rect.colliderect(player.rect):
                    self.getCoin = True
                    if self.coinCounter < 5:
                        self.coinCounter = 5
                    #endif
                #endif
            #endfor
            if abs(self.moveX) < abs(self.finalX) and self.horiSpeed != 0:
                self.rect.x += self.horiSpeed
                self.moveX += self.horiSpeed
            #endif
            for block in block_list:
                if self.rect.colliderect(block.rect):
                    if self.horiSpeed > 0:
                        self.rect.right = block.rect.left
                    elif self.horiSpeed < 0:
                        self.rect.left = block.rect.right
                    #endif
                    self.horiSpeed = 0
                #endif
            #endfor
            if self.vertSpeed == 0: #Keep testing if coin hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif
            if self.rect.y >= 780 and self.vertSpeed <= 0: #If sinks into the ground
                self.rect.y = 780 #Stands on the ground
                self.vertSpeed = 0
            elif self.rect.y <= 0 and self.vertSpeed > 0:
                self.rect.y = 0
                self.vertSpeed = 0
            #endif
            if self.rect.y - self.vertSpeed > 780:
                self.rect.y += (780-self.rect.y)
                self.vertSpeed = 0
            else:
                self.rect.y -= self.vertSpeed #coin move vertically
            #endif
            coinVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in coinVertBlock_list:
                if self.vertSpeed <= 0: #If coin is falling
                    self.rect.bottom = block.rect.top
                elif self.vertSpeed >= 0: #If coin is jumping
                    self.rect.top = block.rect.bottom
                #endif
                self.vertSpeed = 0 #Stop coin
            #endfor
        elif self.getCoin and self.coinAnimationEnd:
            if self.coinCounter == 6:
                self.coinAnimationEnd = False
                level_list.remove(self)
                coin_list.remove(self)
                currency[3] += 1
                if currency[3] == 10:
                    currency[2] += 1
                    currency[3] = 0
                #endif
                if currency[2] == 10:
                    currency[1] += 1
                    currency[2] = 0
                #endif
                if currency[1] == 10:
                    currency[0] += 1
                    currency[1] = 0
                #endif
                if currency[0] == 10:
                    currency[0] = 0
                    currency[1] = 0
                    currency[2] = 0
                    currency[3] = 0
                #endif
            #endif
        #endif
    #endmethod
#endclass
#Timer Class
class TimerClass():
    def __init__(self):
        #Timers
        self.start = 0
        self.end = 0
    #endmethod
    def Counter(self, loTime, timeUp):
        if self.start == 0:
            self.start = pygame.time.get_ticks() #Record current time
            timeUp[0] = 0
        #endif
        self.end = pygame.time.get_ticks() #Record current time
        if self.end - self.start >= loTime:
            timeUp[0] = 1
            self.start = 0
            self.end = 0
        #endif
    #endmethod
#endclass
#Word
class WordClass(pygame.sprite.Sprite):
    def __init__(self, typeOfWord, wordNum, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape
        self.rect.x = x #Set position
        self.rect.y = y
        self.wordType = typeOfWord
        self.num = wordNum
        #Counters
        #Timers
        self.startAnimation = 0
        self.endAnimation = 0
        self.numbers = [] #Numbers
        for x in range(10):
            add_str = str(x)
            self.numbers.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Numbers/" + add_str + ".png"), (width, height)))
        #endfor
        self.small = []
        for x in range(26):
            add_str = str(x+1)
            self.small.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Characters/Small" + add_str + ".png"), (width, height)))
        #endfor
        self.capital = []
        for x in range(26):
            add_str = str(x+1)
            self.capital.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Characters/Capital" + add_str + ".png"), (width, height)))
        #endfor
        self.exclamation = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Characters/Exclamation.png"), (width, height))]
        self.comma = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Characters/Comma.png"), (width, height))]
        self.question = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Characters/Question.png"), (width, height))]
        if self.wordType == 0:
            self.image = self.numbers[int(self.num)]
        elif self.wordType == 1:
            if self.num >= 97 and self.num <= 122:
                self.image = self.small[self.num-97]
            elif self.num >= 65 and self.num <= 90:
                self.image = self.capital[self.num-65]
            elif self.num == 44:
                self.image = self.comma[0]
            elif self.num == 33:
                self.image = self.exclamation[0]
            elif self.num == 63:
                self.image = self.question[0]
            #endif
        #endif
    #endmethod
    def Update(self, num):
        self.image = self.numbers[num]
    #endmethod
#endclass
#Write Words
def WriteWords(typeOfWord, line, x, y, level_list, currentLine_list):
    line = line.rstrip("\n") #Get rid of next line (\n)
    length = len(str(line))
    if typeOfWord == 1:
        x = 242
    for i in range(length): #Loop
        if typeOfWord == 0: #If type is number
            width = 24
            height = 31
            xIncrement = 29
            if line[i] != " ":
                word = WordClass(0, line[i], width, height, x, y) #Create word
            #endif
            x += xIncrement #Move Further
            level_list.add(word) #Add to list
            currentLine_list.add(word) #Add to current data
        elif typeOfWord == 1:
            officialY = y
            charNum = ord(line[i])
            xIncrement = 16
            if line[i] != " ":
                if charNum >= 97 and charNum <= 122:
                    width = 14
                    height = 20
                    xIncrement = 16
                    if charNum == 108:
                        width = 4
                        xIncrement = 6
                        height = 25
                        y = y- 5
                    elif charNum == 105:
                        width = 4
                        xIncrement = 6
                    elif charNum == 121 or charNum == 103 or charNum == 112 or charNum == 113:
                        height = 25
                    elif charNum == 100 or charNum == 104 or charNum == 107 or charNum == 98:
                        height = 25
                        y = y - 5
                    #endif
                elif charNum >= 65 and charNum <= 90:
                    width = 16
                    height = 23
                    xIncrement = 18
                    y = y - 3
                    if charNum == 73:
                        width = 8
                        xIncrement = 10
                    #endif
                elif charNum == 44:
                    width = 4
                    height = 8
                    xIncrement = 6
                    y = y + 12
                elif charNum == 33:
                    width = 4
                    height = 25
                    xIncrement = 6
                    y = y - 5
                elif charNum == 63:
                    width = 14
                    height = 25
                    xIncrement = 16
                    y = y - 5
                #endif
                word = WordClass(1, charNum, width, height, x, y) #Create word
                currentLine_list.add(word)
                y = officialY
                level_list.add(word)
            #endif
            x += xIncrement
        #endif
    #endfor
#endfunction
#Place the Crown at the best file
def SetCrown(crown_list):
    maxLevel = 0
    xPos = 0
    #Open File 1
    f = open("Game_Files/File1.txt","r+") #Open file 1
    lines = f.readlines() #All data
    f.close() #Close
    currentLevel = int(lines[2][0])
    if currentLevel > maxLevel:
        maxLevel = currentLevel
        xPos = 163
    #endif
    #Open File 2
    f = open("Game_Files/File2.txt","r+") #Open file 2
    lines = f.readlines() #All data
    f.close() #Close
    currentLevel = int(lines[2][0])
    if currentLevel > maxLevel:
        maxLevel = currentLevel
        xPos = 583
    #endif
    #Open File 3
    f = open("Game_Files/File3.txt","r+") #Open file 3
    lines = f.readlines() #All data
    f.close() #Close
    currentLevel = int(lines[2][0])
    if currentLevel > maxLevel:
        maxLevel = currentLevel
        xPos = 1003
    #endif
    for crown in crown_list:
        crown.rect.x = xPos
    #endfor
#endfunction
#Loading Class----------------------------------------------------------------------------------------------------------------
#Load Animation
class LoadingClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([149, 42])
        self.rect = self.image.get_rect() #Get the shape
        self.rect.x = 1270
        self.rect.y = 800
        self.loading = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading1.png'), (149, 42)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading2.png'), (157, 42)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading3.png'), (165, 42)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading4.png'), (173, 42))]
        self.image = self.loading[0]
    #endmethod
    def Animation(self, num):
        self.image = self.loading[num]
    #endmethod
#endclass
#Instruction Class----------------------------------------------------------------------------------
class InstructionClass(pygame.sprite.Sprite): #Instruction is a sprite, because I need to create multiple instructions
    #Instantiation
    def __init__(self, typeNum, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape
        #Assign Position
        self.rect.x = x
        self.rect.y = y
        #Images
        self.move = [pygame.transform.scale(pygame.image.load('Game_Images/Text/MoveInstruction.png'), (344, 27))]
        self.jump = [pygame.transform.scale(pygame.image.load('Game_Images/Text/JumpInstruction.png'), (274, 25))]
        self.dJump = [pygame.transform.scale(pygame.image.load('Game_Images/Text/DoubleJumpInstruction.png'), (369, 25))]
        self.attack = [pygame.transform.scale(pygame.image.load('Game_Images/Text/AttackInstruction.png'), (229, 20))]
        self.roll = [pygame.transform.scale(pygame.image.load('Game_Images/Text/RollInstruction.png'), (187, 20))]
        self.block = [pygame.transform.scale(pygame.image.load('Game_Images/Text/BlockInstruction.png'), (327, 20))]#254
        self.minus = [pygame.transform.scale(pygame.image.load('Game_Images/Text/-.png'), (18, 8))]
        self.coin = [pygame.transform.scale(pygame.image.load('Game_Images/Text/CoinsInstruction.png'), (487, 27))]
        self.fake = [pygame.transform.scale(pygame.image.load('Game_Images/Text/FakeCoinInstruction.png'), (327, 20))]
        self.quit = [pygame.transform.scale(pygame.image.load('Game_Images/Text/QuitInstruction.png'), (698, 77))]
        self.saved = [pygame.transform.scale(pygame.image.load('Game_Images/Text/SavedInstruction.png'), (495, 60))]
        self.restart = [pygame.transform.scale(pygame.image.load('Game_Images/Text/DiedInstruction.png'), (585, 82))]
        self.levelUp = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Level1Instruction.png'), (583, 77)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Level2Instruction.png'), (583, 77)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Level3Instruction.png'), (583, 77))]
        self.upgradeCost = [pygame.transform.scale(pygame.image.load('Game_Images/Text/CostInstruction.png'), (626, 90))]
        self.finish = [pygame.transform.scale(pygame.image.load('Game_Images/Text/FinishInstruction.png'), (743, 82))]
        self.invincible = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Invincible.png'), (287, 47))]
        self.instantKill = [pygame.transform.scale(pygame.image.load('Game_Images/Text/InstantKill.png'), (261, 40))]
        self.programmer = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Programmer.png'), (514, 54))]
        self.designer = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Designer.png'), (398, 54))]
        self.screenwriter = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Screenwriter.png'), (514, 40))]
        self.animator = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Animator.png'), (398, 40))]
        self.tester = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Tester.png'), (344, 40))]
        #Decide Which Instruction
        if typeNum == 1:
            self.image = self.move[0]
        elif typeNum == 2:
            self.image = self.jump[0]
        elif typeNum == 3:
            self.image = self.attack[0]
        elif typeNum == 4:
            self.image = self.roll[0]
        elif typeNum == 5:
            self.image = self.dJump[0]
        elif typeNum == 6:
            self.image = self.block[0]
        elif typeNum == 7:
            self.image = self.minus[0]
        elif typeNum == 8:
            self.image = self.coin[0]
        elif typeNum == 9:
            self.image = self.fake[0]
        elif typeNum == 10:
            self.image = self.quit[0]
        elif typeNum == 11:
            self.image = self.saved[0]
        elif typeNum == 12:
            self.image = self.restart[0]
        elif typeNum == 13:
            self.image = self.levelUp[0]
        elif typeNum == 14:
            self.image = self.upgradeCost[0]
        elif typeNum == 15:
            self.image = self.finish[0]
        elif typeNum == 16:
            self.image = self.invincible[0]
        elif typeNum == 17:
            self.image = self.instantKill[0]
        elif typeNum == 18:
            self.image = self.programmer[0]
        elif typeNum == 19:
            self.image = self.designer[0]
        elif typeNum == 20:
            self.image = self.screenwriter[0]
        elif typeNum == 21:
            self.image = self.animator[0]
        elif typeNum == 22:
            self.image = self.tester[0]
        #endif
    #endmethod
    def LevelUpdate(self, num):
        self.image = self.levelUp[num-1]
    #endmethod
#endclass
#Gameplay Class ------------------------------------------------------------------------------------
#Draw / Remove object on / from Canvas
def DrawOrRemove(num, listOne, listTwo):
    if num == 0:
        for stuff in listTwo:
            listOne.remove(stuff)
        #endfor
    elif num == 1:
        for stuff in listTwo:
            listOne.add(stuff)
        #endfor
    #endif
#endfunction
#Convert Image
def loadify(img):
    return pygame.image.load(img).convert_alpha()
#endfunction
#Block
class BlockClass(pygame.sprite.Sprite): #Block is a sprite, because I need to create multiple blocks
    def __init__(self, typeOfBlock, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape
        self.rect.x = x
        self.rect.y = y
        self.originalX = x
        #Images
        self.grassBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Background/GroundBlock.png'), (240, 40))]
        self.saveFileBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Text/SaveFileBox.png'), (333, 639))]
        self.crown = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Crown.png'), (333, 141))]
        self.chooseDifficulty = [pygame.transform.scale(pygame.image.load('Game_Images/Text/ChooseDifficulty.png'), (1220, 202))]
        self.wordBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Text/TextBox.png'), (1065, 150))]
        self.optionBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Text/OptionBox.png'), (800, 475))]
        if typeOfBlock == 1:
            self.image = self.grassBlock[0]
        elif typeOfBlock == 2:
            self.image = self.saveFileBlock[0]
        elif typeOfBlock == 3:
            self.image = self.crown[0]
        elif typeOfBlock == 4:
            self.image = self.chooseDifficulty[0]
        elif typeOfBlock == 5:
            self.image = self.wordBlock[0]
        elif typeOfBlock == 6:
            self.image = self.optionBlock[0]
        #endif
    #endmethod
    def Reset(self):
        self.rect.x = self.originalX
    #endmethod
#endclass
#Ground
class GroundClass(pygame.sprite.Sprite): #Block is a sprite, because I need to create multiple blocks
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([1500,100])
        self.rect = self.image.get_rect() #Get the shape
        self.rect.x = 0
        self.rect.y = 800
        self.originalX = 0
        self.ground = []
        for x in range(2):
            add_str = str(x+1)
            self.ground.append(pygame.transform.scale(loadify("Game_Images/Background/Ground" + add_str + ".png"), (3000, 100)))
        #endfor
        self.image = self.ground[0]
    #endmethod
    def Update(self, num):
        if num == 1:
            self.rect.x -= 10
        elif num == 0:
            self.rect.x = self.originalX
        #endif
    #endmethod
    def ChangeTheme(self, gameLevel):
        if gameLevel == 1:
            self.image = self.ground[0]
        elif gameLevel == 2:
            self.image = self.ground[0]
        elif gameLevel == 3:
            self.image = self.ground[1]
        #endif
    #endmethod
#endclass
#Background Class
class BackgroundClass(pygame.sprite.Sprite): #Class of the background
    def __init__(self, picNum, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.scalex = x*10 #Scaled up x and y position
        self.scaley = y*10
        self.rect.x = self.scalex//10
        self.rect.y = self.scaley//10
        self.originalX = x
        self.originalScaleX = x*10
        self.num = picNum
        #Images
        self.mountains = [] #Mountains
        for x in range(2):
            add_str = str(x+1)
            self.mountains.append(pygame.transform.scale(loadify("Game_Images/Background/Mountains/Mountain" + add_str + ".png"), (self.width, self.height)))
        #endfor
        self.forest = [] #Forest
        for x in range(2):
            add_str = str(x+1)
            self.forest.append(pygame.transform.scale(loadify("Game_Images/Background/Forest/Forest" + add_str + ".png"), (self.width, self.height)))
        #endfor
        self.castle = [] #Castle
        for x in range(2):
            add_str = str(x+1)
            self.castle.append(pygame.transform.scale(loadify("Game_Images/Background/Castle/Castle" + add_str + ".png"), (self.width, self.height)))
        #endfor
        self.image = self.mountains[self.num]
    #endmethod
    def ChangeTheme(self, gameLevel):
        if gameLevel == 1:
            self.image = self.mountains[self.num]
        elif gameLevel == 2:
            self.image = self.forest[self.num]
        elif gameLevel == 3:
            self.image = self.castle[self.num]
        #endif
    #endmethod
    def BackUpdate(self):
        if self.num == 0:
            self.scalex -= 16
        elif self.num == 1:
            self.scalex -= 10
        #endif
        self.rect.x = self.scalex//10
    #endmethod
    def CloudUpdate(self):
        self.scalex -= 5
        if self.scalex <= -25600:
            self.scalex = 25600
        #endif
        self.rect.x = self.scalex//10
    #endmethod
    def Reset(self):
        self.scalex = self.originalScaleX
        self.rect.x = self.scalex//10
    #endmethod
#endclass
#Attack Class
class AttackClass(pygame.sprite.Sprite): #Class of Attack
    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0
        self.speed2 = 0
    #endmethod
    def Speed(self,speed):
        self.speed = speed
    #endmethod
    def Direction(self):
        self.speed2 = self.speed
        print(self.speed, self.speed2)
        return self.speed2
    #endmethod
#endclass
#Health Class
class HealthClass(pygame.sprite.Sprite): #Class of Attack
    def __init__(self, healthType, num, width, height, xPos, yPos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos
        self.enemyHealth = [] #Health
        for x in range(6):
            add_str = str(x)
            self.enemyHealth.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Hearts/Health" + add_str + ".png"), (width, height)))
        #endfor
        if healthType == 1:
            self.image = self.enemyHealth[num]
        #endif
    #endmethod
    def Update(self,num):
        self.image = self.enemyHealth[num]
    #endmethod
#endclass
#Player Class
class PlayerClass(pygame.sprite.Sprite): #Class of the player
    def __init__(self, x, y, leftPlayerAttack_list, rightPlayerAttack_list):
        super().__init__()
        self.image = pygame.Surface([50, 100])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.playerAnimation = PlayerAnimation(self.rect.x, self.rect.y) #Animation
        self.playerAttackLeft = AttackClass(120, 130, -1000, 0) #Attack
        self.playerAttackRight = AttackClass(120, 130, -1000, 0) #Attack
        leftPlayerAttack_list.add(self.playerAttackLeft)
        rightPlayerAttack_list.add(self.playerAttackRight)
        self.playerHealth = HealthClass(1, 5, 250, 50, 15, 10) #Health
        self.playerHealth2 = HealthClass(1, 5, 250, 50, 65, 10) #Health
        self.playerShield1 = ItemClass(5, 50, 50, 15, 65)
        self.playerShield2 = ItemClass(5, 50, 50, 65, 65)
        self.playerShield3 = ItemClass(5, 50, 50, 115, 65)
        self.playerShield4 = ItemClass(5, 50, 50, 165, 65)
        self.playerShield5 = ItemClass(5, 50, 50, 215, 65)
        self.playerShield6 = ItemClass(5, 50, 50, 265, 65)
        self.playerShield7 = ItemClass(5, 50, 50, 315, 65)
        self.playerShield8 = ItemClass(5, 50, 50, 365, 65)
        self.playerLevel = ItemClass(6, 30, 30, self.rect.x, self.rect.y - 30)
        self.playerLevelNumber = ItemClass(7, 14, 20, self.rect.x + 36, self.rect.y - 25)
        self.playerStar = ItemClass(9, 150, 50, 15, 175)
        self.playerStar.StarUpdate(0)
        #Attributes
        self.hp = 5
        self.shield = 8
        self.hp2 = 0
        self.lvl = 0
        self.reduceHealth = False
        self.speedX = 10
        self.horiSpeed = 0
        self.lastHoriSpeed = 1
        self.doubleJump = False
        self.vertSpeed = -0.4
        self.jumped = False
        self.doubleJumped = False
        self.attacked = False
        self.spell = False
        self.attackStep = 1
        self.stopSelf = False
        self.resetAttack = False
        self.freeze = False
        self.freezeAnimation = False
        self.block = False
        self.blocked = False
        self.unblock = False
        self.roll = False
        self.hurt = False
        self.keepMoving = False
        self.death = False
        self.getAttack = False
        self.fired = False
        self.star = 0
        self.limitX = False
        self.leftSide = False
        self.invincible = False
        #Background
        self.backMove = 0
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startCombo = 0
        self.endCombo = 0
        self.startBlocked = 0
        self.endBlocked = 0
        self.startRoll = 0
        self.endRoll = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRest = 0
        self.endRest = 0
        self.startAddShield = 0
        self.endAddShield = 0
        self.startStar = 0
        self.endStar = 0
        self.startRecover=0
        self.endRecover=0
        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.jumpCounter = 0
        self.fallCounter = 0
        self.attackCounter1 = 0
        self.attackCounter2 = 0
        self.attackCounter3 = 0
        self.blockCounter = 0
        self.blockedCounter = 0
        self.rollCounter = 0
        self.deathCounter = 0
        self.hurtCounter = 0
        self.spellCounter = 0
    #endmethod
    def Turn(self, num):
        if num == 0:
            self.lastHoriSpeed = -1
        elif num == 1:
            self.lastHoriSpeed = 1
        #endif
    #endmethod
    def Invincible(self, num):
        if num == 0:
            self.invincible = False
        else:
            self.invincible = True
        #endif
    #endmethod
    def LimitMovement(self, num):
        if num == 1:
            if self.rect.x <= 650:
                self.leftSide = True
            else:
                self.leftSide = False
            #endif
            self.limitX = True
        else:
            self.limitX = False
        #endif
    #endmethod
    def TurnAround(self, posX):
        if posX >= 670:
            self.lastHoriSpeed = self.speedX
        elif posX < 670:
            self.lastHoriSpeed = -self.speedX
        #endif
    #endmethod
    def LevelSet(self, playerLevel):
        self.lvl = playerLevel[0]
        self.playerLevelNumber.UpdateLevel(self.lvl)
        if self.lvl == 1:
            if self.star == 0:
                self.star = 1
                self.playerStar.StarUpdate(self.star)
            #endif
        #endif
        if self.lvl < 2:
            self.speedX = 10
        elif self.lvl >= 2:
            self.speedX = 13
        #endif
    #endmethod
    def DrawOnCanvas(self, tutorial_list, levelOne_list, levelTwo_list, levelThree_list):
        tutorial_list.add(self.playerAnimation)
        levelOne_list.add(self.playerStar, self.playerHealth, self.playerAnimation, self.playerShield1, self.playerShield2, self.playerShield3, self.playerShield4, self.playerShield5, self.playerShield6, self.playerShield7, self.playerShield8, self.playerLevel, self.playerLevelNumber)
        levelTwo_list.add(self.playerStar, self.playerHealth, self.playerAnimation, self.playerShield1, self.playerShield2, self.playerShield3, self.playerShield4, self.playerShield5, self.playerShield6, self.playerShield7, self.playerShield8, self.playerLevel, self.playerLevelNumber)
        levelThree_list.add(self.playerStar, self.playerHealth, self.playerAnimation, self.playerShield1, self.playerShield2, self.playerShield3, self.playerShield4, self.playerShield5, self.playerShield6, self.playerShield7, self.playerShield8, self.playerLevel, self.playerLevelNumber)
    #endmethod
    def ResetLive(self, live, shieldNum, playerLevel):
        self.hp = live[0]
        self.playerHealth.Update(self.hp)
        self.lvl = playerLevel[0]
        self.playerLevelNumber.UpdateLevel(self.lvl)
        self.shield = shieldNum[0]
        self.playerShield8.ShieldUpdate(1)
        self.playerShield7.ShieldUpdate(1)
        self.playerShield6.ShieldUpdate(1)
        self.playerShield5.ShieldUpdate(1)
        self.playerShield4.ShieldUpdate(1)
        self.playerShield3.ShieldUpdate(1)
        self.playerShield2.ShieldUpdate(1)
        self.playerShield1.ShieldUpdate(1)
        if self.shield < 8:
            self.playerShield8.ShieldUpdate(0)
        #endif
        if self.shield < 7:
            self.playerShield7.ShieldUpdate(0)
        #endif
        if self.shield < 6:
            self.playerShield6.ShieldUpdate(0)
        #endif
        if self.shield < 5:
            self.playerShield5.ShieldUpdate(0)
        #endif
        if self.shield < 4:
            self.playerShield4.ShieldUpdate(0)
        #endif
        if self.shield < 3:
            self.playerShield3.ShieldUpdate(0)
        #endif
        if self.shield < 2:
            self.playerShield2.ShieldUpdate(0)
        #endif
        if self.shield < 1:
            self.playerShield1.ShieldUpdate(0)
        #endif
    #endmethod
    def ResetForTransition(self):
        self.horiSpeed = 0
        self.jumped = False
        self.attacked = False
        self.spell = False
        self.attackStep = 1
        self.stopSelf = False
        self.resetAttack = False
        self.block = False
        self.blocked = False
        self.unblock = False
        self.roll = False
        self.hurt = False
        self.keepMoving = False
        self.death = False
        self.jumpCounter = 0
        self.fallCounter = 0
        self.attackCounter1 = 0
        self.attackCounter2 = 0
        self.attackCounter3 = 0
        self.blockedCounter = 0
        self.rollCounter = 0
        self.deathCounter = 0
        self.hurtCounter = 0
        self.spellCounter = 0
        self.getAttack = False
        self.fired = False
        self.limitX = False
        self.leftSide = False
    #endmethod
    def Reset(self):
        if self.lvl >= 2:
            self.speedX = 13
        else:
            self.speedX = 10
        #endif
        self.lastHoriSpeed = 1
        self.horiSpeed = 0
        self.jumped = False
        self.attacked = False
        self.spell = False
        self.attackStep = 1
        self.stopSelf = False
        self.resetAttack = False
        self.freeze = False
        self.freezeAnimation = False
        self.block = False
        self.blocked = False
        self.unblock = False
        self.roll = False
        self.hurt = False
        self.keepMoving = False
        self.death = False
        self.jumpCounter = 0
        self.fallCounter = 0
        self.attackCounter1 = 0
        self.attackCounter2 = 0
        self.attackCounter3 = 0
        self.blockedCounter = 0
        self.rollCounter = 0
        self.deathCounter = 0
        self.hurtCounter = 0
        self.spellCounter = 0
        self.rect.x = 50
        self.rect.y = 700
        self.getAttack = False
        self.fired = False
        self.limitX = False
        self.leftSide = False
        self.startAddShield = 0
        self.endAddShield = 0
        self.startStar = 0
        self.endStar = 0
        self.startRecover=0
        self.endRecover=0
        if self.lvl >= 1:
            self.star = 3
            self.playerStar.StarUpdate(self.star)
        else:
            self.star = 0
            self.playerStar.StarUpdate(0)
        #endif
        self.playerAttackLeft.rect.x = -1000
        self.playerAttackRight.rect.x = -1000
        self.Animation()
    #endmethod
    def FreezeTrigger(self, num):
        if num == 1:
            self.ChangeSpeed(2)
            self.freeze = True
            self.keepMoving = False
        elif num != 1:
            self.freeze = False
        #endif
    #endmethod
    def Freeze(self, num):
        if num == 1:
            self.freezeAnimation = True
        else:
            self.freezeAnimation = False
        #endif
    #endmethod
    def Animation(self):
        if self.shield == 7:
            self.playerShield8.ShieldUpdate(0)
        elif self.shield == 6:
            self.playerShield7.ShieldUpdate(0)
        elif self.shield == 5:
            self.playerShield6.ShieldUpdate(0)
        elif self.shield == 4:
            self.playerShield5.ShieldUpdate(0)
        elif self.shield == 3:
            self.playerShield4.ShieldUpdate(0)
        elif self.shield == 2:
            self.playerShield3.ShieldUpdate(0)
        elif self.shield == 1:
            self.playerShield2.ShieldUpdate(0)
        elif self.shield == 0:
            self.playerShield1.ShieldUpdate(0)
        #endif
        self.playerLevel.rect.x = self.rect.x
        self.playerLevelNumber.rect.x = self.rect.x + 36
        self.playerLevel.rect.y = self.rect.y - 30
        self.playerLevelNumber.rect.y = self.rect.y - 25
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        self.playerAnimation.rect.y = self.rect.y - 38
        self.playerAnimation.rect.x = self.rect.x - 100
        if self.death == False and not self.freezeAnimation:
            if self.hurt == False and self.attacked == False and not self.spell and self.horiSpeed == 0 and self.jumped == False and self.block == False and self.blocked == False:
                if self.endAnimation - self.startAnimation >= 160: #If next image
                    self.startAnimation = self.endAnimation #If player is idle
                    self.playerAnimation.PlayerIdle(self.lastHoriSpeed, self.idleCounter)
                    if self.idleCounter != 7: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif
                #endif
            elif not self.hurt and self.attacked == False and self.horiSpeed != 0 and self.jumped == False and self.roll == False and not self.spell:
                if self.endAnimation - self.startAnimation >= 80:
                    self.startAnimation = self.endAnimation #If player running
                    self.playerAnimation.PlayerRun(self.lastHoriSpeed, self.runCounter)
                    if self.runCounter != 9: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif
                #endif
            elif self.jumped == True and self.vertSpeed >= 0 and not self.hurt and not self.spell:
                if self.endAnimation - self.startAnimation >= 200:
                    self.startAnimation = self.endAnimation #If player jumping
                    self.playerAnimation.PlayerJump(self.lastHoriSpeed, self.jumpCounter)
                    if self.jumpCounter != 2: #If reached the end
                        self.jumpCounter += 1
                    else:
                        self.jumpCounter = 2 #Stay at the last frame
                    #endif
                #endif
            elif self.jumped == True and self.vertSpeed < 0 and not self.hurt and not self.spell:
                if self.endAnimation - self.startAnimation >= 200:
                    self.startAnimation = self.endAnimation #If player falling
                    self.playerAnimation.PlayerFall(self.lastHoriSpeed, self.fallCounter)
                    if self.fallCounter != 3: #If reached the end
                        self.fallCounter += 1
                    else:
                        self.fallCounter = 3 #Stay at the last frame
                    #endif
                #endif
            elif self.attacked == True and self.attackStep == 1 and not self.hurt and not self.spell:
                if self.endAnimation - self.startAnimation >= 60:
                    self.startAnimation = self.endAnimation
                    self.playerAnimation.PlayerAttack1(self.lastHoriSpeed, self.attackCounter1)
                    if self.attackCounter1 != 5:
                        self.attackCounter1 += 1
                    else:
                        self.attackCounter1 = 5
                    #endif
                #endif
            elif self.attacked == True and self.attackStep == 2 and not self.hurt and not self.spell:
                if self.endAnimation - self.startAnimation >= 60:
                    self.startAnimation = self.endAnimation
                    self.playerAnimation.PlayerAttack2(self.lastHoriSpeed, self.attackCounter2)
                    if self.attackCounter2 != 5:
                        self.attackCounter2 += 1
                    else:
                        self.attackCounter2 = 5
                    #endif
                #endif
            elif self.attacked == True and self.attackStep == 3 and not self.hurt and not self.spell:
                if self.endAnimation - self.startAnimation >= 60:
                    self.startAnimation = self.endAnimation
                    self.playerAnimation.PlayerAttack3(self.lastHoriSpeed, self.attackCounter3)
                    if self.attackCounter3 != 7:
                        self.attackCounter3 += 1
                    else:
                        self.attackCounter3 = 7
                    #endif
                #endif
            elif self.block == True and self.blocked == False and self.hurt == False and not self.spell:
                if self.endAnimation - self.startAnimation >= 80:
                    self.startAnimation = self.endAnimation #If player blocking
                    self.playerAnimation.PlayerBlock(self.lastHoriSpeed, self.blockCounter)
                    if self.blockCounter != 7: #If reached the end
                        self.blockCounter += 1
                    else:
                        self.blockCounter = 0 #Start over
                    #endif
                #endif
            elif self.blocked and not self.hurt and not self.reduceHealth:
                if self.endAnimation - self.startAnimation >= 80:
                    self.startAnimation = self.endAnimation #If player blocking
                    self.playerAnimation.PlayerBlocked(self.lastHoriSpeed, self.blockedCounter)
                    if self.blockedCounter != 4: #If reached the end
                        self.blockedCounter += 1
                    else:
                        self.blockedCounter = 4 #Stops
                    #endif
                #endif
            elif self.roll == True:
                if self.endAnimation - self.startAnimation >= 60:
                    self.startAnimation = self.endAnimation #If player falling
                    self.playerAnimation.PlayerRoll(self.lastHoriSpeed, self.rollCounter)
                    if self.rollCounter != 8: #If reached the end
                        self.rollCounter += 1
                    else:
                        self.rollCounter = 8 #Stay at the last frame
                    #endif
                #endif
            elif self.hurt == True:
                if self.endAnimation - self.startAnimation >= 90:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.playerAnimation.PlayerHurt(self.lastHoriSpeed, self.hurtCounter)
                    if self.hurtCounter != 2: #If reached the end
                        self.hurtCounter += 1
                    else:
                        self.hurtCounter = 2 #Stay at the last frame
                    #endif
                #endif
            elif self.spell and not self.attacked and not self.hurt:
                if self.endAnimation - self.startAnimation >= 60:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.playerAnimation.PlayerSpell(self.lastHoriSpeed, self.spellCounter)
                    if self.spellCounter != 4: #If reached the end
                        self.spellCounter += 1
                    else:
                        self.spellCounter = 4 #Stay at the last frame
                    #endif
                #endif
            #endif
        elif self.death == True and not self.freezeAnimation:
            if self.endAnimation - self.startAnimation >= 75: #If next image
                self.startAnimation = self.endAnimation #If player is Dead
                self.playerAnimation.PlayerDeath(self.lastHoriSpeed, self.deathCounter)
                if self.deathCounter != 7: #If reached the end
                    self.deathCounter += 1
                else:
                    self.deathCounter == 7
                #endif
            #endif
        #endif
    #endmethod
    def EnemyAttackDetection(self, leftAttack_list, rightAttack_list):
        playerGetHit1_list = pygame.sprite.spritecollide(self, leftAttack_list, False)#If get hit
        for attack in playerGetHit1_list:
            if not self.hurt and not self.reduceHealth and not self.death and not self.blocked and not self.freezeAnimation:
                if self.block:
                    if self.lastHoriSpeed > 0:
                        if self.shield > 0:
                            self.blocked = True
                            self.shield-=1
                        else:
                            self.blocked = False
                            self.block = False
                            self.hurt = True
                            self.reduceHealth = True
                        #endif
                    else:
                        self.blocked = False
                        self.block = False
                        self.hurt = True
                        self.reduceHealth = True
                    #endif
                elif not self.block and not self.roll:
                    self.hurt = True
                    self.reduceHealth = True
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                    self.attackStep = 1
                    self.attacked = False
                    self.attackCounter1 = 0
                    self.attackCounter2 = 0
                    self.attackCounter3 = 0
                #endif
            #endif
        #endfor
        playerGetHit2_list = pygame.sprite.spritecollide(self, rightAttack_list, False)#If get hit
        for attack in playerGetHit2_list:
            if not self.hurt and not self.reduceHealth and not self.death and not self.blocked and not self.freezeAnimation:
                if self.block:
                    if self.lastHoriSpeed < 0:
                        if self.shield > 0:
                            self.blocked = True
                            self.shield-=1
                        else:
                            self.blocked = False
                            self.block = False
                            self.hurt = True
                            self.reduceHealth = True
                        #endif
                    else:
                        self.blocked = False
                        self.block = False
                        self.hurt = True
                        self.reduceHealth = True
                    #endif
                elif not self.block and not self.roll:
                    self.hurt = True
                    self.reduceHealth = True
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                    self.attackStep = 1
                    self.attacked = False
                    self.attackCounter1 = 0
                    self.attackCounter2 = 0
                    self.attackCounter3 = 0
                #endif
            #endif
        #endfor
    #endmethod
    def RogueDetection(self,attack_list):
        playerGetHit_list = pygame.sprite.spritecollide(self, attack_list, False)#If get hit
        for attack in playerGetHit_list:
            if not self.hurt and not self.death and not self.freezeAnimation:
                self.hurt = True
                self.reduceHealth = True
                self.block = False
                self.hp2 = -1
                self.playerAttackLeft.rect.x = -1000
                self.playerAttackRight.rect.x = -1000
                self.attackStep = 1
                self.attacked = False
                self.attackCounter1 = 0
                self.attackCounter2 = 0
                self.attackCounter3 = 0
            #endif
        #endfor
    #endmethod
    def ShadowBoltDetection(self, shadowBolt_list, levelThree_list):
        playerGetHit_list = pygame.sprite.spritecollide(self, shadowBolt_list, False)#If get hit
        for attack in playerGetHit_list:
            if not self.hurt and not self.death and not self.freezeAnimation and attack.rect.y >= self.rect.y:
                self.hurt = True
                self.reduceHealth = True
                self.block = False
                self.playerAttackLeft.rect.x = -1000
                self.playerAttackRight.rect.x = -1000
                self.attackStep = 1
                self.attacked = False
                self.attackCounter1 = 0
                self.attackCounter2 = 0
                self.attackCounter3 = 0
                attack.DeleteSelf(levelThree_list, shadowBolt_list)
            #endif
        #endfor
    #endmethod
    def MushroomDetection(self,attack_list):
        playerGetHit_list = pygame.sprite.spritecollide(self, attack_list, False)#If get hit
        for attack in playerGetHit_list:
            if not self.hurt and not self.death and not self.freezeAnimation:
                self.hurt = True
                self.reduceHealth = True
                self.block = False
                self.playerAttackLeft.rect.x = -1000
                self.playerAttackRight.rect.x = -1000
                self.attackStep = 1
                self.attacked = False
                self.attackCounter1 = 0
                self.attackCounter2 = 0
                self.attackCounter3 = 0
            #endif
        #endfor
    #endmethod
    def JavelinAttackDetection(self, leftJavelin_list, rightJavelin_list, levelTwo_list):
        playerGetHit1_list = pygame.sprite.spritecollide(self, leftJavelin_list, False)#If get hit
        for javelin in playerGetHit1_list:
            if not self.hurt and not self.death and not self.freezeAnimation and not self.roll and not self.blocked:
                if self.block:
                    if self.lastHoriSpeed > 0:
                        if self.shield > 0:
                            self.blocked = True
                            self.shield-=1
                        else:
                            self.blocked = False
                            self.block = False
                            self.hurt = True
                            self.reduceHealth = True
                        #endif
                        leftJavelin_list.remove(javelin)
                        levelTwo_list.remove(javelin)
                    else:
                        self.blocked = False
                        self.block = False
                        self.hurt = True
                        self.reduceHealth = True
                        leftJavelin_list.remove(javelin)
                        levelTwo_list.remove(javelin)
                    #endif
                elif not self.block and not self.roll:
                    self.hurt = True
                    self.reduceHealth = True
                    self.block = False
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                    self.attackStep = 1
                    self.attacked = False
                    self.attackCounter1 = 0
                    self.attackCounter2 = 0
                    self.attackCounter3 = 0
                    leftJavelin_list.remove(javelin)
                    levelTwo_list.remove(javelin)
                #endif
            #endif
        #endfor
        playerGetHit2_list = pygame.sprite.spritecollide(self, rightJavelin_list, False)#If get hit
        for javelin in playerGetHit2_list:
            if not self.hurt and not self.death and not self.freezeAnimation and not self.roll and not self.blocked:
                if self.block:
                    if self.lastHoriSpeed < 0:
                        if self.shield > 0:
                            self.blocked = True
                            self.shield-=1
                        else:
                            self.blocked = False
                            self.block = False
                            self.hurt = True
                            self.reduceHealth = True
                        #endif
                        rightJavelin_list.remove(javelin)
                        levelTwo_list.remove(javelin)
                    else:
                        self.blocked = False
                        self.block = False
                        self.hurt = True
                        self.reduceHealth = True
                        rightJavelin_list.remove(javelin)
                        levelTwo_list.remove(javelin)
                    #endif
                elif not self.block and not self.roll:
                    self.hurt = True
                    self.reduceHealth = True
                    self.block = False
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                    self.attackStep = 1
                    self.attacked = False
                    self.attackCounter1 = 0
                    self.attackCounter2 = 0
                    self.attackCounter3 = 0
                    rightJavelin_list.remove(javelin)
                    levelTwo_list.remove(javelin)
                #endif
            #endif
        #endfor
    #endmethod
    def Jump(self):
        if not self.freeze and not self.blocked and not self.hurt and not self.attacked and not self.roll and not self.death and not self.spell:
            if not self.jumped: #If player has not jumped yet
                self.block = False
                self.vertSpeed = 15
                self.jumped = True
                self.doubleJumped = False
                self.jumpCounter = 0
                self.fallCounter = 0
            elif self.jumped and not self.doubleJumped: #If double jump
                if self.vertSpeed >= 0:
                    self.vertSpeed += 12
                    if self.vertSpeed > 17:
                        self.vertSpeed = 17
                    #endif
                else:
                    self.vertSpeed = 12
                #endif
                self.doubleJumped = True
                self.jumpCounter = 0
                self.fallCounter = 0
            #endif
        #endif
    #endmethod
    def MoveVert(self, block_list):
        if not self.freezeAnimation:
            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif
            if self.rect.y >= 700 and self.vertSpeed <= 0: #If sinks into the ground
                self.rect.y = 700 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False
            elif self.rect.y <= 0 and self.vertSpeed > 0:
                self.rect.y = 0
                self.vertSpeed = 0
            #endif
            self.rect.y -= self.vertSpeed #Move
            playerVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in playerVertBlock_list:
                if self.vertSpeed <= 0: #If player is falling
                    self.rect.bottom = block.rect.top
                    self.jumped = False
                elif self.vertSpeed >= 0: #If player is jumping
                    self.rect.top = block.rect.bottom
                #endif
                self.vertSpeed = 0 #Stop player
            #endfor
        #endif
    #endmethod
    def RollTrigger(self):
        if self.attacked == False and self.jumped == False and self.blocked == False and self.hurt == False and not self.death and not self.freeze and not self.spell:
            self.block = False
            self.roll = True
        #endif
    #endmethod
    def BlockTrigger(self,num):
        if self.attacked == False and self.jumped == False and num == 1 and self.hurt == False and not self.death and not self.freeze and not self.spell:
            self.horiSpeed = 0
            self.block = True
            self.unblock = False
        elif num == 0 and not self.freezeAnimation:
            self.block = False
            self.unblock = True
            if not self.blocked:
                if not self.keepMoving:
                    self.horiSpeed = 0
                else:
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -self.speedX
                    elif self.lastHoriSpeed > 0:
                        self.horiSpeed = self.speedX
                    #endif
                #endif
            #endif
        #endif
    #endmethod
    def Blocked(self, live, shieldNum):
        if self.blocked and not self.freezeAnimation:
            self.horiSpeed = 0
            if self.blockedCounter == 4:
                shieldNum[0] = self.shield
                self.blocked = False
                self.blockedCounter = 0
                self.getAttack = False
                if self.unblock:
                    self.block = False
                    self.unblock = False
                #endif
                if self.hp < 5:
                    self.hp += 1
                    self.playerHealth.Update(self.hp)
                    live[0] = self.hp
                #endif
            #endif
        #endif
        if not self.freezeAnimation:
            if self.lvl == 3:
                if self.startAddShield == 0: #If start timer has not started yet
                    self.startAddShield = pygame.time.get_ticks() #Record current time
                #endif
                self.endAddShield = pygame.time.get_ticks() #Get current time for end time
                if self.endAddShield - self.startAddShield >= 5000:
                    self.startAddShield = self.endAddShield
                    if self.shield < 8:
                        self.shield += 1
                        shieldNum[0] = self.shield
                        if self.shield == 8:
                            self.playerShield8.ShieldUpdate(1)
                        elif self.shield == 7:
                            self.playerShield7.ShieldUpdate(1)
                        elif self.shield == 6:
                            self.playerShield6.ShieldUpdate(1)
                        elif self.shield == 5:
                            self.playerShield5.ShieldUpdate(1)
                        elif self.shield == 4:
                            self.playerShield4.ShieldUpdate(1)
                        elif self.shield == 3:
                            self.playerShield3.ShieldUpdate(1)
                        elif self.shield == 2:
                            self.playerShield2.ShieldUpdate(1)
                        elif self.shield == 1:
                            self.playerShield1.ShieldUpdate(1)
                        #endif
                    #endif
                #endif
            #endif
        #endif
    #endmethod
    def Health(self, live):
        if self.lvl >= 1:
            if self.star < 3:
                if self.startStar == 0: #If start timer has not started yet
                    self.startStar = pygame.time.get_ticks() #Record current time
                #endif
                self.endStar = pygame.time.get_ticks() #Get current time for end time
                if self.endStar - self.startStar >= 8000:
                    self.startStar = 0
                    self.endStar = 0
                    self.star += 1
                    self.playerStar.StarUpdate(self.star)
                #endif
            #endif
        #endif
        if self.reduceHealth == True and not self.freezeAnimation:
            self.reduceHealth = False
            if not self.invincible:
                if self.hp > 0:
                    self.hp -= 1
                    self.hp += self.hp2
                    self.hp2 = 0
                    if self.hp < 0:
                        self.hp = 0
                    #endif
                    self.playerHealth.Update(self.hp)
                if self.hp == 0:
                    self.death = True
                #endif
                live[0] = self.hp
            #endif
        #endif
        if self.hp > 0 and self.hp < 5:
            if self.startRecover == 0: #If start timer has not started yet
                self.startRecover = pygame.time.get_ticks() #Record current time
            #endif
            self.endRecover = pygame.time.get_ticks() #Get current time for end time
            if self.endRecover - self.startRecover >= 25000:
                self.startRecover = 0
                self.endRecover = 0
                self.hp+=1
                self.playerHealth.Update(self.hp)
            #endif
        #endif
    #endmethod
    def Death(self):
        if self.death == True:
            self.horiSpeed = 0
        #endif
    #endmethod
    def Revive(self, live):
        if self.death == True:
            self.horiSpeed = 0
            if self.startDeath == 0:
                self.startDeath = pygame.time.get_ticks()
            #endif
            self.endDeath = pygame.time.get_ticks()
            if self.endDeath - self.startDeath > 3000:
                self.endDeath = 0
                self.startDeath = 0
                self.death = False
                self.deathCounter = 0
                live[0] = 5
                self.hp = 5
                self.playerHealth.Update(self.hp)
            #endif
        #endif
    #endmethod
    def Hurt(self):
        if self.hurt == True and self.death == False and not self.freezeAnimation:
            self.horiSpeed = 0
            if self.startHurt == 0:
                self.startHurt = pygame.time.get_ticks()
            #endif
            self.endHurt = pygame.time.get_ticks()
            if self.endHurt - self.startHurt > 250:
                self.endHurt = 0
                self.startHurt = 0
                self.hurt = False
                self.hurtCounter = 0
                self.getAttack = False
                if not self.keepMoving:
                    self.horiSpeed = 0
                else:
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -self.speedX
                    elif self.lastHoriSpeed > 0:
                        self.horiSpeed = self.speedX
                    #endif
                #endif
            #endif
        #endif
    #endmethod
    def AttackTrigger(self):
        if self.attacked == False and self.jumped == False and self.roll == False and self.hurt == False and self.blocked == False and self.death == False and not self.freeze and not self.spell:
            self.endRest = pygame.time.get_ticks()
            if self.endRest - self.startRest >= 100 and self.resetAttack:
                self.block = False
                self.attacked = True
                self.startRest = 0
                self.endRest = 0
            else:
                self.block = False
                self.attacked = True
                self.endRest = 0
                self.startRest = 0
            #endif
        #endif
    #endmethod
    def SpellTrigger(self):
        if not self.spell and not self.hurt and not self.blocked and not self.death and not self.freeze and not self.attacked and self.star > 0 and self.lvl >= 1:
            self.star -= 1
            self.playerStar.StarUpdate(self.star)
            self.spell = True
            self.block = False
            self.jumpCounter = 0
            self.fallCounter = 0
            self.horiSpeed = 0
        #endif
    #endmethod
    def Spell(self, fireBall_list, levelThree_list):
        if self.spell and not self.freezeAnimation:
            if self.spellCounter == 3 and not self.fired:
                self.fired = True
                if self.lastHoriSpeed > 0:
                    fireball = EffectClass(2, self.rect.x, self.rect.y+8, 1, 0, levelThree_list)
                elif self.lastHoriSpeed < 0:
                    fireball = EffectClass(2, self.rect.x-45, self.rect.y+8, -1, 0, levelThree_list)
                #endif
                fireBall_list.add(fireball)
            elif self.spellCounter == 4:
                self.fired = False
                self.spell = False
                self.spellCounter = 0
                if not self.keepMoving: #If keep going
                    self.horiSpeed = 0
                else:
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -self.speedX
                    elif self.lastHoriSpeed > 0:
                        self.horiSpeed = self.speedX
                    #endif
                #endif
            #endif
        #endif
    #endmethod
    def KeepMove(self, speed):
        if self.freeze == False:
            if speed == 0:
                self.keepMoving = False
            else:
                self.keepMoving = True
            #endif
        #endif
    #endmethod
    def AttackChecker(self):
        if self.stopSelf and not self.freezeAnimation: #If the player should stop
            if not self.keepMoving:
                self.horiSpeed = 0
            else:
                if self.lastHoriSpeed < 0:
                    self.horiSpeed = -self.speedX
                elif self.lastHoriSpeed > 0:
                    self.horiSpeed = self.speedX
                #endif
            #endif
            self.stopSelf = False
        #endif
    #endmethod
    def Roll(self):
        if self.roll == True and not self.freezeAnimation:
            if self.lastHoriSpeed < 0:
                self.horiSpeed = -self.speedX
            else:
                self.horiSpeed = self.speedX
            #endif
            if self.rollCounter == 8:
                self.roll = False
                if not self.keepMoving: #If keep going
                    self.horiSpeed = 0
                elif not self.freeze:
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -self.speedX
                    elif self.lastHoriSpeed > 0:
                        self.horiSpeed = self.speedX
                    #endif
                #endif
                self.rollCounter = 0
            #endif
        #endif
    #endmethod
    def Attack(self):
        if self.attacked == False:
            self.endCombo = pygame.time.get_ticks()
            if self.startCombo == 0:
                self.startCombo = pygame.time.get_ticks()
            #endif
            if self.endCombo - self.startCombo >= 500:
                self.attackStep = 1
                self.startCombo = 0
                self.endCombo = 0
            #endif
        elif self.attacked == True and not self.freezeAnimation:
            self.horiSpeed = 0
            self.endCombo = 0
            self.startCombo = 0
            if self.attackStep == 1: #Attack 1
                if self.attackCounter1 == 2 or self.attackCounter1 == 3:
                    if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                        self.playerAttackRight.rect.x = self.rect.x + 35
                        self.playerAttackRight.rect.y = self.rect.y - 30
                    elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                        self.playerAttackLeft.rect.x = self.rect.x - 105
                        self.playerAttackLeft.rect.y = self.rect.y - 30
                    #endif
                elif self.attackCounter1 != 2 and self.attackCounter1 != 3:
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                elif self.hurt or self.death:
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                #endif
                if self.attackCounter1 == 5:
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -7
                    else:
                        self.horiSpeed = 7
                    #endif
                    self.stopSelf = True
                    self.attackStep = 2
                    self.attacked = False
                    self.attackCounter1 = 0
                #endif
            elif self.attackStep == 2: #Attack 2
                if self.attackCounter2 == 2 or self.attackCounter2 == 1:
                    if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                        self.playerAttackRight.rect.x = self.rect.x + 35
                        self.playerAttackRight.rect.y = self.rect.y - 30
                    elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                        self.playerAttackLeft.rect.x = self.rect.x - 105
                        self.playerAttackLeft.rect.y = self.rect.y - 30
                    #endif
                elif self.attackCounter2 != 2 and self.attackCounter2 != 1:
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                elif self.hurt or self.death:
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                #endif
                if self.attackCounter2 == 5:
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -7
                    else:
                        self.horiSpeed = 7
                    #endif
                    self.stopSelf = True
                    self.attackStep = 3
                    self.attacked = False
                    self.attackCounter2 = 0
                #endif
            elif self.attackStep == 3: #Attack 3
                if self.attackCounter3 == 2 or self.attackCounter3 == 3:
                    if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                        self.playerAttackRight.rect.x = self.rect.x + 35
                        self.playerAttackRight.rect.y = self.rect.y - 30
                    elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                        self.playerAttackLeft.rect.x = self.rect.x - 105
                        self.playerAttackLeft.rect.y = self.rect.y - 30
                    #endif
                elif self.attackCounter3 != 2 and self.attackCounter3 != 3:
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                elif self.hurt:
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                #endif
                if self.attackCounter3 == 7:
                    self.playerAttackLeft.rect.x = -1000
                    self.playerAttackRight.rect.x = -1000
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -9
                    else:
                        self.horiSpeed = 9
                    #endif
                    self.stopSelf = True
                    self.attackStep = 1
                    self.attacked = False
                    self.attackCounter3 = 0
                    self.startRest = pygame.time.get_ticks()
                    self.resetAttack = True
                #endif
            #endif
        #endif
    #endmethod
    def ChangeSpeed(self,num):
        if self.freeze == False and not self.blocked and not self.death and not self.spell:
            if num == 0:
                self.horiSpeed = -self.speedX
                self.block = False
                self.lastHoriSpeed = -1
            elif num == 1:
                self.horiSpeed = self.speedX
                self.block = False
                self.lastHoriSpeed = 1
            elif num == 2:
                self.horiSpeed = 0
            #endif
        #endif
    #endmethod
    def MoveHori2(self, block_list):
        if self.freezeAnimation == False:
            self.rect.x += self.horiSpeed
            for block in block_list:
                if self.rect.colliderect(block.rect): #If player hit block
                    if self.horiSpeed > 0:
                        self.rect.right = block.rect.left
                    else:
                        self.rect.left = block.rect.right
                    #endif
                #endif
            #endfor
            if self.rect.x <= 0: #If player reach the end of screen
                self.rect.x = 0
            #endif
        #endif
    #endmethod
    def MoveHori(self, block_list):
        if self.freezeAnimation == False:
            self.rect.x += self.horiSpeed
            for block in block_list:
                if self.rect.colliderect(block.rect): #If player hit block
                    if self.horiSpeed > 0:
                        self.rect.right = block.rect.left
                    else:
                        self.rect.left = block.rect.right
                    #endif
                #endif
            #endfor
            if self.rect.x <= 0: #If player reach the end of screen
                self.rect.x = 0
            elif self.rect.x >= 1450:
                self.rect.x = 1450
            #endif
            if self.limitX:
                if self.leftSide:
                    if self.rect.x >= 650:
                        self.rect.x = 650
                    #endif
                else:
                    if self.rect.x <= 800:
                        self.rect.x = 800
                    #endif
                #endif
            #endif
        #endif
    #endmethod
#endclass
#Player Animation Class
class PlayerAnimation(pygame.sprite.Sprite): #Class of player's animation
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([50, 100])
        self.rect = self.image.get_rect()
        self.rect.x = x #Set pos
        self.rect.y = y
        #Animation
        self.playerIdle = [] #Idle
        for x in range(8):
            add_str = str(x+1)
            self.playerIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroIdle" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerRun = [] #Run
        for x in range(10):
            add_str = str(x+1)
            self.playerRun.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroRun" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerJump = [] #Jump
        for x in range(3):
            add_str = str(x+1)
            self.playerJump.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroJump" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerFall = [] #Fall
        for x in range(4):
            add_str = str(x+1)
            self.playerFall.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroFall" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerAttack1 = [] #Attack 1
        for x in range(6):
            add_str = str(x+1)
            self.playerAttack1.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroAttack1-" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerAttack2 = [] #Attack 2
        for x in range(6):
            add_str = str(x+1)
            self.playerAttack2.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroAttack2-" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerAttack3 = [] #Attack 3
        for x in range(8):
            add_str = str(x+1)
            self.playerAttack3.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroAttack3-" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerSpell = [] #Spell
        for x in range(5):
            add_str = str(x+1)
            self.playerSpell.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroSpell" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerBlock = [] #Block
        for x in range(8):
            add_str = str(x+1)
            self.playerBlock.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroBlock" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerBlocked = [] #Blocked
        for x in range(5):
            add_str = str(x+1)
            self.playerBlocked.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroBlocked" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerRoll = [] #Roll
        for x in range(9):
            add_str = str(x+1)
            self.playerRoll.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroRoll" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerHurt = [] #Hurt
        for x in range(3):
            add_str = str(x+1)
            self.playerHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroHurt" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerDeath = [] #Death
        for x in range(8):
            add_str = str(x+1)
            self.playerDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroDeath" + add_str + ".png"), (250, 138)))
        #endfor
        self.image = self.playerIdle[0]
    #endmethod
    def PlayerIdle(self, speed, i): #When player not moving
        if speed > 0:
            self.image = self.playerIdle[i] #Right
        else:
            self.image = pygame.transform.flip(self.playerIdle[i],1,0) #Left
        #endif
    #endmethod
    def PlayerRun(self, speed, i):
        if speed > 0:
            self.image = self.playerRun[i]
        else:
            self.image = pygame.transform.flip(self.playerRun[i],1,0)
        #endif
    #endmethod
    def PlayerJump(self, speed, i):
        if speed > 0:
            self.image = self.playerJump[i]
        else:
            self.image = pygame.transform.flip(self.playerJump[i],1,0)
        #endif
    #endmethod
    def PlayerFall(self, speed, i):
        if speed > 0:
            self.image = self.playerFall[i]
        else:
            self.image = pygame.transform.flip(self.playerFall[i],1,0)
        #endif
    #endmethod
    def PlayerAttack1(self, speed, i):
        if speed > 0:
            self.image = self.playerAttack1[i]
        else:
            self.image = pygame.transform.flip(self.playerAttack1[i],1,0)
        #endif
    #endmethod
    def PlayerAttack2(self, speed, i):
        if speed > 0:
            self.image = self.playerAttack2[i]
        else:
            self.image = pygame.transform.flip(self.playerAttack2[i],1,0)
        #endif
    #endmethod
    def PlayerAttack3(self, speed, i):
        if speed > 0:
            self.image = self.playerAttack3[i]
        else:
            self.image = pygame.transform.flip(self.playerAttack3[i],1,0)
        #endif
    #endmethod
    def PlayerBlock(self, speed, i):
        if speed > 0:
            self.image = self.playerBlock[i]
        else:
            self.image = pygame.transform.flip(self.playerBlock[i],1,0)
        #endif
    #endmethod
    def PlayerSpell(self, speed, i):
        if speed > 0:
            self.image = self.playerSpell[i]
        else:
            self.image = pygame.transform.flip(self.playerSpell[i],1,0)
        #endif
    #endmethod
    def PlayerBlocked(self, speed, i):
        if speed > 0:
            self.image = self.playerBlocked[i]
        else:
            self.image = pygame.transform.flip(self.playerBlocked[i],1,0)
        #endif
    #endmethod
    def PlayerRoll(self, speed, i):
        if speed > 0:
            self.image = self.playerRoll[i]
        else:
            self.image = pygame.transform.flip(self.playerRoll[i],1,0)
        #endif
    #endmethod
    def PlayerHurt(self, speed, i):
        if speed > 0:
            self.image = self.playerHurt[i]
        else:
            self.image = pygame.transform.flip(self.playerHurt[i],1,0)
        #endif
    #endmethod
    def PlayerDeath(self, speed, i):
        if speed > 0:
            self.image = self.playerDeath[i]
        else:
            self.image = pygame.transform.flip(self.playerDeath[i],1,0)
        #endif
    #endmethod
#endclass
#Enemy Class----------------------------------------------------------------
#Bandit Class
class BanditClass(pygame.sprite.Sprite): #Class of the bandit
    def __init__(self, num , x, y, sprites_list, leftEnemyAttack_list, rightEnemyAttack_list, childNumber):
        super().__init__()
        self.image = pygame.Surface([50, 100])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.originalX = x
        self.originalY = y
        self.num = num
        if self.num == 1:
            self.banditAnimation = EnemyAnimation(1, 130, 130, self.rect.x, self.rect.y)
            self.hp = 3
            self.runningSpeed = 9
            self.jumpNum = randint(3,5)
            self.concentrateTime = randint(120,160)
            self.waitTime = randint(150,200)
            self.randomTime = randint(800,1000)
        elif self.num == 0:
            self.banditAnimation = EnemyAnimation(0, 130, 130, self.rect.x, self.rect.y)
            self.hp = 5
            self.runningSpeed = 10
            self.jumpNum = randint(2,4)
            self.concentrateTime = randint(50,70)
            self.waitTime = randint(70,100)
            self.randomTime = randint(500,700)
        #endif
        self.banditAttackLeft = AttackClass(65, 130, -1000, 0)
        self.banditAttackRight = AttackClass(65, 130, -1000, 0)
        leftEnemyAttack_list.add(self.banditAttackLeft)
        rightEnemyAttack_list.add(self.banditAttackRight)
        self.banditHealth = HealthClass(1, self.hp, 100, 20, self.rect.x - 5, self.rect.y - 25)
        self.coin1 = ItemClass(1, 20, 20, -200, 0)
        self.coin2 = ItemClass(1, 20, 20, -200, 0)
        sprites_list.add(self.banditAnimation, self.banditHealth)
        #Attributes
        self.childNum = childNumber
        if self.childNum >= 0:
            self.childNum -= 1
            xLuck = randint(0,1)
            if xLuck == 0:
                tempX = randint(-200,-100)
            else:
                tempX = randint(1550,1650)
            #endif
            self.childBandit = BanditClass(self.num, tempX, 700, sprites_list, leftEnemyAttack_list, rightEnemyAttack_list, self.childNum)
        #endif
        self.originalChild = self.childNum
        self.horiSpeed = 0
        self.lastHoriSpeed = -1
        self.vertSpeed = -0.4
        self.jumped = False
        self.attacked = False
        self.attackPhase = 1
        self.stopSelf = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.adle = False
        self.reduceHealth = False
        self.dropCoin = False
        self.random = False
        self.random2 = False
        self.jumpTime = 0
        self.attackDirectionAssign = False
        self.instantDeath = False
        self.reproduced = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -1500
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0
        self.startRandom2 = 0
        self.endRandom2 = 0
        self.startAbove = 0
        self.endAbove = 0
        #Counter
        self.idleCounter = randint(0,3)
        self.adleCounter = randint(0,3)
        self.runCounter = randint(0,7)
        self.jumpCounter = 0
        self.fallCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
    #endmethod
    def InstantKill(self, num):
        if num == 1:
            self.instantDeath = True
        else:
            self.instantDeath = False
        #endif
        if self.childNum >= 0:
            self.childBandit.InstantKill(num)
        #endif
    #endmethod
    def Freeze(self, num):
        if num == 1:
            self.freeze = True
        else:
            self.freeze = False
        #endif
        if self.childNum >= 0:
            self.childBandit.Freeze(num)
        #endif
    #endmethod
    def Reset(self):
        #Attributes
        self.rect.x = self.originalX
        self.rect.y = self.originalY
        self.horiSpeed = 0
        self.lastHoriSpeed = -1
        self.vertSpeed = -0.4
        self.jumped = False
        self.attacked = False
        self.attackPhase = 1
        self.stopSelf = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.adle = False
        self.reduceHealth = False
        self.dropCoin = False
        self.random = False
        self.random2 = False
        self.jumpTime = 0
        self.attackDirectionAssign = False
        self.reproduced = False
        self.childNum = self.originalChild
        if self.childNum >= 0:
            self.childBandit.Reset()
        #endif
        #Timers
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -1500
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0
        self.startRandom2 = 0
        self.endRandom2 = 0
        #Counter
        self.jumpCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.banditAttackLeft.rect.x = -1000
        self.banditAttackRight.rect.x = -1000
        if self.num == 1:
            self.hp = 3
            self.jumpNum = randint(3,5)
            self.concentrateTime = randint(120,160)
            self.waitTime = randint(150,200)
            self.randomTime = randint(800,1000)
            self.banditHealth.rect.x = self.rect.x - 5
        elif self.num == 0:
            self.hp = 5
            self.runningSpeed = 10
            self.jumpNum = randint(2,4)
            self.concentrateTime = randint(50,70)
            self.waitTime = randint(70,100)
            self.randomTime = randint(400,600)
            self.banditHealth.rect.x = self.rect.x - 25
        #endif
        self.banditHealth.Update(self.hp)
        self.banditHealth.rect.y = self.rect.y - 25
        self.Animation()
    #endmethod
    def Animation(self):
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        if self.num == 1:
            self.banditAnimation.rect.y = self.rect.y - 30
        elif self.num == 0:
            self.banditAnimation.rect.y = self.rect.y - 24.6
        #endif
        self.banditAnimation.rect.x = self.rect.x - 40
        if self.death == False and not self.freeze:
            if not self.hurt and self.attacked == False and self.horiSpeed == 0 and self.jumped == False and not self.adle:
                if self.endAnimation - self.startAnimation >= 160: #If next image
                    self.startAnimation = self.endAnimation #If player is idle
                    self.banditAnimation.Idle(-self.lastHoriSpeed, self.idleCounter)
                    if self.idleCounter != 3: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif
                #endif
            elif not self.hurt and self.attacked == False and self.horiSpeed == 0 and self.jumped == False and self.adle:
                if self.endAnimation - self.startAnimation >= 160: #If next image
                    self.startAnimation = self.endAnimation #If player is idle
                    self.banditAnimation.Adle(-self.lastHoriSpeed, self.adleCounter)
                    if self.adleCounter != 3: #If reached the end
                        self.adleCounter += 1
                    else:
                        self.adleCounter = 0
                    #endif
                #endif
            elif not self.hurt and self.attacked == False and self.horiSpeed != 0 and self.jumped == False:
                if self.endAnimation - self.startAnimation >= 80:
                    self.startAnimation = self.endAnimation #If player running
                    self.banditAnimation.Run(-self.lastHoriSpeed, self.runCounter)
                    if self.runCounter != 7: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif
                #endif
            elif self.jumped == True:
                if self.endAnimation - self.startAnimation >= 200:
                    self.startAnimation = self.endAnimation #If player jumping
                    self.banditAnimation.Jump(-self.lastHoriSpeed, self.jumpCounter)
                    self.jumpCounter = 0
                #endif
            elif self.hurt == True:
                if self.endAnimation - self.startAnimation >= 100:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.banditAnimation.Hurt(-self.lastHoriSpeed, self.hurtCounter)
                    if self.hurtCounter != 2: #If reached the end
                        self.hurtCounter += 1
                    else:
                        self.hurtCounter = 2
                    #endif
                #endif
            elif self.attacked == True:
                if self.endAnimation - self.startAnimation >= 50:
                    self.startAnimation = self.endAnimation
                    self.banditAnimation.Attack(-self.lastHoriSpeed, self.attackCounter)
                    if self.attackPhase == 1 and self.attackCounter != 3:
                        self.attackCounter += 1
                    elif self.attackPhase == 3 and self.attackCounter != 7:
                        self.attackCounter += 1
                    #endif
                #endif
            #endif
        elif self.death and not self.freeze:
            if self.endAnimation - self.startAnimation >= 50:
                self.startAnimation = self.endAnimation
                self.banditAnimation.Death(-self.lastHoriSpeed, self.deathCounter)
                self.deathCounter = 0
            #endif
        #endif
    #endmethod
    def Control(self, player_list):
        for player in player_list:
            if not self.random and not self.random2 and not self.freeze:
                if player.rect.y == self.rect.y:
                    self.ChangeSpeed(2)
                    self.startAbove = 0
                    self.endAbove = 0
                    if self.rect.x - player.rect.x < 90 and self.rect.x - player.rect.x > 0 and self.lastHoriSpeed < 0:
                        self.AttackTrigger()
                        self.random2 = True
                    elif player.rect.x - self.rect.x > 0 and player.rect.x - self.rect.x <= 90 and self.lastHoriSpeed > 0:
                        self.AttackTrigger()
                        self.random2 = True
                    elif player.rect.x <= self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(0)
                    elif player.rect.x > self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(1)
                    else:
                        self.ChangeSpeed(randint(0,1))
                    #endif
                elif player.rect.y > self.rect.y:
                    self.ChangeSpeed(2)
                    if self.startAbove == 0: #If start timer has not started yet
                        self.startAbove = pygame.time.get_ticks() #Record current time
                    #endif
                    self.endAbove = pygame.time.get_ticks()
                    if self.endAbove - self.startAbove >= 2000:
                        self.random2 = True
                        self.startAbove = 0
                        self.endAbove = 0
                    #endif
                    if player.rect.x <= self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(0)
                    elif player.rect.x > self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(1)
                    #endif
                elif player.rect.y < self.rect.y:
                    self.startAbove = 0
                    self.endAbove = 0
                    self.ChangeSpeed(2)
                    if player.rect.x <= self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(0)
                    elif player.rect.x > self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(1)
                    #endif
                    self.Jump()
                    if self.jumpTime > self.jumpNum:
                        self.random = True
                    #endif
                #endif
            elif self.random and not self.freeze:
                if self.startRandom == 0: #If start timer has not started yet
                    self.startRandom = pygame.time.get_ticks() #Record current time
                #endif
                self.jumpTime = 0
                self.endRandom = pygame.time.get_ticks()
                if self.endRandom - self.startRandom > 1500:
                    self.startRandom = self.endRandom
                    self.ChangeSpeed(randint(0,1))
                    self.Jump()
                #endif
                if player.rect.y >= self.rect.y:
                    self.startRandom = 0
                    self.endRandom = 0
                    self.random = False
                #endif
            elif self.random2 and not self.freeze:
                if self.startRandom2 == 0: #If start timer has not started yet
                    self.startRandom2 = pygame.time.get_ticks() #Record current time
                    self.ChangeSpeed(randint(0,1))
                #endif
                self.endRandom2 = pygame.time.get_ticks()
                if self.endRandom2 - self.startRandom2 > self.randomTime:
                    self.startRandom2 = 0
                    self.endRandom2 = 0
                    self.random2 = False
                #endif
            #endif
            if self.rect.x <= 0: #If player reach the end of screen
                self.rect.x = 0
            elif self.rect.x >= 1450:
                self.rect.x = 1450
            #endif
        #endfor
    #endmethod
    def AttackStance(self,num):
        if num == 1:
            self.adle = True
        else:
            self.adle = False
        #endif
    #endmethod
    def Reproduce(self, tempBandit_list):
        if self.death and not self.reproduced:
            self.reproduced = True
            if self.childNum >= 0:
                tempBandit_list.add(self.childBandit)
            #endif
        #endif
    #endmethod
    def Health(self, coin_list, sprite_list, level, gameLevel, enemyCount):
        if self.reduceHealth == True and not self.freeze:
            self.reduceHealth = False
            if self.hp > 0:
                if not self.instantDeath:
                    self.hp -= 1
                elif self.instantDeath:
                    self.hp = 0
                #endif
                self.banditHealth.Update(self.hp)
            #endif
            if self.hp == 0:
                self.death = True
                num = enemyCount[0]
                enemyCount[0] = num - 1
                if not self.dropCoin:
                    self.dropCoin = True
                    self.coin1.CoinSet(self.rect.x + 10, self.rect.y + 70)
                    self.coin2.CoinSet(self.rect.x + 10, self.rect.y + 70)
                    sprite_list.add(self.coin1, self.coin2)
                    coin_list.add(self.coin1, self.coin2)
                #endif
            #endif
        #endif
        if self.hp == 5:
            self.banditHealth.rect.x = self.rect.x - 25
        elif self.hp == 4:
            self.banditHealth.rect.x = self.rect.x - 15
        elif self.hp == 3:
            self.banditHealth.rect.x = self.rect.x - 5
        elif self.hp == 2:
            self.banditHealth.rect.x = self.rect.x + 5
        elif self.hp == 1:
            self.banditHealth.rect.x = self.rect.x + 15
        #endif
        self.banditHealth.rect.y = self.rect.y - 25
    #endmethod
    def EnemyAttackDetection(self,leftPlayerAttack_list, rightPlayerAttack_list):
        enemyGetHit1_list = pygame.sprite.spritecollide(self, leftPlayerAttack_list, False)#If get hit
        for attack in enemyGetHit1_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
                self.banditAttackLeft.rect.x = -1000
                self.banditAttackRight.rect.x = -1000
            #endif
        #endfor
        enemyGetHit2_list = pygame.sprite.spritecollide(self, rightPlayerAttack_list, False)#If get hit
        for attack in enemyGetHit2_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
                self.banditAttackLeft.rect.x = -1000
                self.banditAttackRight.rect.x = -1000
            #endif
        #endfor
    #endmethod
    def FireBallDetection(self, level_list, fireBall_list):
        enemyGetHit_list = pygame.sprite.spritecollide(self, fireBall_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
                self.banditAttackLeft.rect.x = -1000
                self.banditAttackRight.rect.x = -1000
            #endif
        #endfor
    #endmethod
    def Death(self):
        if self.death == True and not self.freeze:
            self.horiSpeed = 0
            if self.startDeath == 0:
                self.startDeath = pygame.time.get_ticks()
            #endif
            self.endDeath = pygame.time.get_ticks()
            if self.endDeath - self.startDeath > 3000:
                self.endDeath = 0
                self.startDeath = 0
                self.death = False
                self.deathCounter = 0
                self.hp = 3
                self.dropCoin = False
                self.banditHealth.Update(self.hp)
            #endif
        #endif
    #endmethod
    def Revive(self):
        if self.death == True:
            self.horiSpeed = 0
            if self.startDeath == 0:
                self.startDeath = pygame.time.get_ticks()
            #endif
            self.endDeath = pygame.time.get_ticks()
            if self.endDeath - self.startDeath > 3000:
                self.endDeath = 0
                self.startDeath = 0
                self.death = False
                self.deathCounter = 0
                if self.num == 1:
                    self.hp = 3
                else:
                    self.hp = 5
                #endif
                self.dropCoin = False
                self.banditHealth.Update(self.hp)
            #endif
        #endif
    #endmethod
    def Hurt(self):
        if self.hurt == True and not self.freeze:
            self.horiSpeed = 0
            if self.startHurt == 0:
                self.startHurt = pygame.time.get_ticks()
            #endif
            self.endHurt = pygame.time.get_ticks()
            if self.endHurt - self.startHurt > 300:
                self.endHurt = 0
                self.startHurt = 0
                self.hurt = False
                self.hurtCounter = 0
            #endif
        #endif
    #endmethod
    def Jump(self):
        if self.freeze == False and self.attacked == False and self.death == False:
            if self.jumped == False: #If player has not jumped yet
                self.jumpTime += 1
                self.vertSpeed = 18
                self.jumped = True
                self.jumpCounter = 0
                self.fallCounter = 0
            #endif
        #endif
    #endmethod
    def MoveVert(self, block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel):
        if self.freeze == False:
            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif
            if self.rect.y >= 700 and self.vertSpeed <= 0: #If sinks into the ground
                self.rect.y = 700 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False
            elif self.rect.y <= 0 and self.vertSpeed > 0:
                self.rect.y = 0
                self.vertSpeed = 0
            #endif
            self.rect.y -= self.vertSpeed #Move
            if level == 4:
                if gameLevel == 1:
                    selfVertBlock_list = pygame.sprite.spritecollide(self, block1_list, False)#If collide
                    for block in selfVertBlock_list:
                        if self.vertSpeed <= 0: #If player is falling
                            self.rect.bottom = block.rect.top
                            self.jumped = False
                            self.startRandom = 0
                            self.endRandom = 0
                            self.random = False
                        elif self.vertSpeed >= 0: #If player is jumping
                            self.rect.top = block.rect.bottom
                        #endif
                        self.vertSpeed = 0 #Stop player
                    #endfor
                elif gameLevel == 2:
                    selfVertBlock_list = pygame.sprite.spritecollide(self, block2_list, False)#If collide
                    for block in selfVertBlock_list:
                        if self.vertSpeed <= 0: #If player is falling
                            self.rect.bottom = block.rect.top
                            self.jumped = False
                            self.startRandom = 0
                            self.endRandom = 0
                            self.random = False
                        elif self.vertSpeed >= 0: #If player is jumping
                            self.rect.top = block.rect.bottom
                        #endif
                        self.vertSpeed = 0 #Stop player
                    #endfor
                #endif
            elif level == 2:
                selfVertBlock_list = pygame.sprite.spritecollide(self, tutorialBlock_list, False)#If collide
                for block in selfVertBlock_list:
                    if self.vertSpeed <= 0: #If player is falling
                        self.rect.bottom = block.rect.top
                        self.jumped = False
                        self.startRandom = 0
                        self.endRandom = 0
                        self.random = False
                    elif self.vertSpeed >= 0: #If player is jumping
                        self.rect.top = block.rect.bottom
                    #endif
                    self.vertSpeed = 0 #Stop player
                #endfor
            #endif
        #endif
    #endmethod
    def AttackTrigger(self):
        self.endAttackRest = pygame.time.get_ticks() #Get current time for end time
        if self.attacked == False and self.jumped == False and self.death == False and self.endAttackRest - self.startAttackRest >= 1500 and not self.freeze:
            self.attacked = True
            self.endAttackRest = 0
            self.startAttackRest = 0
        #endif
    #endmethod
    def AttackChecker(self):
        if self.stopSelf: #If the enemy should stop
            self.stopSelf = False
            self.horiSpeed = 0
        #endif
    #endmethod
    def Attack(self):
        if self.attacked == True and self.freeze == False:
            self.horiSpeed = 0
            if self.attackPhase == 1:
                if self.attackCounter == 3:
                    self.attackPhase = 2
                #endif
            elif self.attackPhase == 2:
                if self.startAttack == 0:
                    self.startAttack = pygame.time.get_ticks()
                #endif
                self.endAttack = pygame.time.get_ticks()
                if self.endAttack - self.startAttack >= self.concentrateTime:
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attackPhase = 3
                #endif
            elif self.attackPhase == 3:
                if self.lastHoriSpeed > 0 and not self.hurt and not self.death and self.attackCounter == 4:
                    self.banditAttackRight.rect.x = self.rect.x + 25
                    self.banditAttackRight.rect.y = self.rect.y - 30
                elif self.lastHoriSpeed < 0 and not self.hurt and not self.death and self.attackCounter == 4:
                    self.banditAttackLeft.rect.x = self.rect.x - 40
                    self.banditAttackLeft.rect.y = self.rect.y - 30
                elif self.attackCounter > 6:
                    self.banditAttackLeft.rect.x = -1000
                    self.banditAttackRight.rect.x = -1000
                elif self.hurt:
                    self.banditAttackLeft.rect.x = -1000
                    self.banditAttackRight.rect.x = -1000
                #endif
                if self.attackCounter == 7:
                    self.attackPhase = 4
                    self.banditAttackLeft.rect.x = -1000
                    self.banditAttackRight.rect.x = -1000
                #endif
            elif self.attackPhase == 4:
                if self.startAttack == 0:
                    self.startAttack = pygame.time.get_ticks()
                #endif
                self.endAttack = pygame.time.get_ticks()
                if self.endAttack - self.startAttack > self.waitTime:
                    self.attackDirectionAssign = False
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attacked = False
                    self.attackPhase = 1
                    self.attackCounter = 0
                    self.startAttackRest = pygame.time.get_ticks() #Record current time
                #endif
            #endif
        #endif
    #endmethod
    def ChangeSpeed(self,num):
        if self.freeze == False and self.attacked == False and not self.death:
            if num == 0:
                self.horiSpeed = -self.runningSpeed
                self.lastHoriSpeed = -1
            elif num == 1:
                self.horiSpeed = self.runningSpeed
                self.lastHoriSpeed = 1
            elif num == 2:
                self.horiSpeed = 0
            #endif
        #endif
    #endmethod
    def MoveHori(self, block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel):
        if self.freeze == False and not self.death:
            self.rect.x += self.horiSpeed
            if level == 2:
                for block in tutorialBlock_list:
                    if self.rect.colliderect(block.rect): #If player hit block
                        if self.horiSpeed > 0:
                            self.rect.right = block.rect.left
                        else:
                            self.rect.left = block.rect.right
                        #endif
                    #endif
                #endfor
            elif level == 4:
                if gameLevel == 1:
                    for block in block1_list:
                        if self.rect.colliderect(block.rect): #If player hit block
                            if self.horiSpeed > 0:
                                self.rect.right = block.rect.left
                            else:
                                self.rect.left = block.rect.right
                            #endif
                        #endif
                    #endfor
                elif gameLevel == 2:
                    for block in block2_list:
                        if self.rect.colliderect(block.rect): #If player hit block
                            if self.horiSpeed > 0:
                                self.rect.right = block.rect.left
                            else:
                                self.rect.left = block.rect.right
                            #endif
                        #endif
                    #endfor
                #endif
            #endif
        #endif
    #endmethod
#endclass
#Warlock Class
class WarlockClass(pygame.sprite.Sprite): #Class of the warlock
    def __init__(self, x, y, levelOne_list):
        super().__init__()
        self.image = pygame.Surface([80, 70])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.originalX = x
        self.originalY = y
        self.warlockAnimation = EnemyAnimation(2, 160, 160, self.rect.x - 40, self.rect.y - 90)
        self.warlockHealth = HealthClass(1, 5, 100, 20, self.rect.x - 10, self.rect.y - 35)
        levelOne_list.add(self.warlockAnimation, self.warlockHealth)
        #Attributes
        self.hp = 5
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.reduceHealth = False
        self.trigger = False
        self.immune = False
        self.skullAttack = False
        self.instantDeath = False
        self.escape = False
        self.appear = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startImmune = 0
        self.endImmune = 0
        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.escapeCounter = 0
        self.appearCounter = 0
    #endmethod
    def Face(self, posX):
        if posX >= self.rect.x:
            self.ChangeSpeed(1)
        else:
            self.ChangeSpeed(0)
        #endif
        self.ChangeSpeed(2)
    #endmethod
    def Turn(self, num):
        if num == 0:
            self.ChangeSpeed(0)
        elif num == 1:
            self.ChangeSpeed(1)
        #endif
        self.ChangeSpeed(2)
    #endmethod
    def InstantKill(self, num):
        if num == 1:
            self.instantDeath = True
        else:
            self.instantDeath = False
        #endif
    #endmethod
    def Reappear(self, posX):
        self.rect.y = 730
        if posX >= 670:
            self.AppearTrigger(randint(50, 150))
            self.lastHoriSpeed = 7
        elif posX < 670:
            self.AppearTrigger(randint(1270, 1370))
            self.lastHoriSpeed = -7
        #endif
        self.hp = 5
        self.vertSpeed = -0.4
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.reduceHealth = False
        self.trigger = False
        self.immune = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startImmune = 0
        self.endImmune = 0
        #Counter
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.warlockHealth.Update(5)
        self.warlockHealth.rect.x = self.rect.x - 10
        self.warlockHealth.rect.y = self.rect.y - 35
        self.Animation()
    #endif
    def Reset(self):
        #Attributes
        self.rect.x = self.originalX
        self.rect.y = self.originalY
        self.hp = 5
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.reduceHealth = False
        self.trigger = False
        self.immune = False
        self.skullAttack = False
        self.escape = False
        self.appear = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startImmune = 0
        self.endImmune = 0
        #Counter
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.escapeCounter = 0
        self.appearCounter = 0
        self.warlockHealth.Update(5)
        self.warlockHealth.rect.x = self.rect.x - 10
        self.warlockHealth.rect.y = self.rect.y - 35
        self.Animation()
    #endmethod
    def Freeze(self, num):
        if num == 1:
            self.freeze = True
        else:
            self.freeze = False
        #endif
    #endmethod
    def Animation(self):
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        self.warlockAnimation.rect.y = self.rect.y - 90
        self.warlockAnimation.rect.x = self.rect.x - 40
        if not self.death and not self.freeze:
            if not self.hurt and self.horiSpeed == 0 and not self.appear and not self.escape:
                if self.endAnimation - self.startAnimation >= 70: #If next image
                    self.startAnimation = self.endAnimation #If player is idle
                    self.warlockAnimation.Idle(self.lastHoriSpeed, self.idleCounter)
                    if self.idleCounter != 11: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif
                #endif
            elif not self.hurt and self.horiSpeed != 0 and not self.appear and not self.escape:
                if self.endAnimation - self.startAnimation >= 100:
                    self.startAnimation = self.endAnimation #If player running
                    self.warlockAnimation.Run(self.lastHoriSpeed, self.runCounter)
                    if self.runCounter != 7: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif
                #endif
            elif self.hurt and not self.appear and not self.escape:
                if self.endAnimation - self.startAnimation >= 100:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.warlockAnimation.Hurt(self.lastHoriSpeed, self.hurtCounter)
                    if self.hurtCounter != 3: #If reached the end
                        self.hurtCounter += 1
                    #endif
                #endif
            elif self.appear and not self.escape:
                if self.endAnimation - self.startAnimation >= 60:
                    self.startAnimation = self.endAnimation #If player is appearing
                    self.warlockAnimation.Appear(self.lastHoriSpeed, self.appearCounter)
                    if self.appearCounter != 8: #If reached the end
                        self.appearCounter += 1
                    #endif
                #endif
            elif self.escape and not self.appear:
                if self.endAnimation - self.startAnimation >= 60:
                    self.startAnimation = self.endAnimation #If player is escaping
                    self.warlockAnimation.Escape(self.lastHoriSpeed, self.escapeCounter)
                    if self.escapeCounter != 8: #If reached the end
                        self.escapeCounter += 1
                    #endif
                #endif
            #endif
        elif self.death and not self.freeze:
            if self.endAnimation - self.startAnimation >= 50:
                self.startAnimation = self.endAnimation
                self.warlockAnimation.Death(self.lastHoriSpeed, self.deathCounter)
                if self.deathCounter != 12:
                    self.deathCounter += 1
                #endif
            #endif
        #endif
    #endmethod
    def Health(self, odenHealth):
        if self.immune:
            self.endImmune = pygame.time.get_ticks()
            if self.endImmune - self.startImmune > 1500:
                self.endImmune = 0
                self.startImmune = 0
                self.immune = False
            #endif
        #endif
        if self.reduceHealth and not self.freeze and not self.death:
            self.startImmune = pygame.time.get_ticks()
            self.immune = True
            self.reduceHealth = False
            if self.hp > 0:
                self.hp -= 1
                if self.skullAttack:
                    self.hp = 0
                    self.skullAttack = False
                    self.death = True
                #endif
            #endif
            odenHealth[0] = self.hp
            self.warlockHealth.Update(self.hp)
        #endif
        if self.hp == 5:
            self.warlockHealth.rect.x = self.rect.x - 10
        elif self.hp == 4:
            self.warlockHealth.rect.x = self.rect.x
        elif self.hp == 3:
            self.warlockHealth.rect.x = self.rect.x + 10
        elif self.hp == 2:
            self.warlockHealth.rect.x = self.rect.x + 20
        elif self.hp == 1:
            self.warlockHealth.rect.x = self.rect.x + 30
        elif self.hp == 0:
            self.warlockHealth.rect.x = self.rect.x - 10
        #endif
        self.warlockHealth.rect.y = self.rect.y - 35
    #endmethod
    def EnemyAttackDetection(self,attack_list):
        enemyGetHit_list = pygame.sprite.spritecollide(self, attack_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze and not self.immune:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
    #endmethod
    def SkullAttackDetection(self,attack_list):
        enemyGetHit_list = pygame.sprite.spritecollide(self, attack_list, False)#If get hit
        for attack in enemyGetHit_list:
            if not self.death:
                self.hurt = True
                self.reduceHealth = True
                self.skullAttack = True
            #endif
        #endfor
    #endmethod
    def EscapeTrigger(self):
        self.escape = True
        self.escapeCounter = 0
    #endmethod
    def Escape(self):
        if self.escapeCounter == 8:
            self.rect.x = -500
            self.escapeCounter = 0
            self.escape = False
        #endif
    #endmethod
    def AppearTrigger(self, num):
        self.appear = True
        self.rect.x = num
    #endmethod
    def Appear(self):
        if self.appearCounter == 8:
            self.appearCounter = 0
            self.appear = False
        #endif
    #endmethod
    def Hurt(self):
        if self.hurt == True and not self.freeze:
            self.horiSpeed = 0
            if self.hurtCounter == 3:
                self.hurt = False
                self.hurtCounter = 0
            #endif
        #endif
    #endmethod
    def Death(self, warlockDead):
        if self.death and not self.trigger:
            self.trigger = True
            warlockDead[0] = 0
        #endif
    #endmethod
    def MoveVert(self, block_list):
        if self.freeze == False:
            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif
            if self.rect.y >= 730 and self.vertSpeed <= 0: #If sinks into the ground
                self.rect.y = 730 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False
            elif self.rect.y <= 0 and self.vertSpeed > 0:
                self.rect.y = 0
                self.vertSpeed = 0
            #endif
            self.rect.y -= self.vertSpeed #Move
            selfVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in selfVertBlock_list:
                if self.vertSpeed <= 0: #If player is falling
                    self.rect.bottom = block.rect.top
                    self.jumped = False
                elif self.vertSpeed >= 0: #If player is jumping
                    self.rect.top = block.rect.bottom
                #endif
                self.vertSpeed = 0 #Stop player
            #endfor
        #endif
    #endmethod
    def ChangeSpeed(self,num):
        if self.freeze == False and self.attacked == False and not self.death:
            if num == 0:
                self.horiSpeed = -7
                self.lastHoriSpeed = self.horiSpeed
            elif num == 1:
                self.horiSpeed = 7
                self.lastHoriSpeed = self.horiSpeed
            elif num == 2:
                self.horiSpeed = 0
            #endif
        #endif
    #endmethod
    def MoveHori(self, block_list):
        if self.freeze == False:
            self.rect.x += self.horiSpeed
            for block in block_list:
                if self.rect.colliderect(block.rect): #If player hit block
                    if self.horiSpeed > 0:
                        self.rect.right = block.rect.left
                    else:
                        self.rect.left = block.rect.right
                    #endif
                #endif
            #endfor
        #endif
    #endmethod
#endclass
#Rogue Class
class RogueClass(pygame.sprite.Sprite): #Class of the rogue
    def __init__(self, x, y, levelOne_list, leftEnemyAttack_list, rightEnemyAttack_list, rogueAttack_list):
        super().__init__()
        self.image = pygame.Surface([80, 90])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.originalX = x
        self.originalY = y
        self.rogueAnimation = EnemyAnimation(3, 160, 160, -1000, -1000)
        self.rogueAttackLeft = AttackClass(200, 70, -1000, 0)
        self.rogueAttackRight = AttackClass(200, 70, -1000, 0)
        self.rogueSaAttack = AttackClass(200, 70, -1000, 0)
        rogueAttack_list.add(self.rogueSaAttack)
        leftEnemyAttack_list.add(self.rogueAttackLeft)
        rightEnemyAttack_list.add(self.rogueAttackRight)
        self.rogueHealth1 = HealthClass(1, 5, 250, 50, 985, 10)
        self.rogueHealth2 = HealthClass(1, 5, 250, 50, 1235, 10)
        levelOne_list.add(self.rogueAnimation)
        self.coin_list = pygame.sprite.Group()
        #Attributes
        for i in range(10):
            coin = ItemClass(1, 20, 20, -200, 0)
            self.coin_list.add(coin)
        #endfor
        self.xDifference = -15
        self.xSize = 50
        self.hp = 10
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.sa = False
        self.saMove = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.spell = False
        self.reduceHealth = False
        self.preyPosX = 0
        self.random = False
        self.attackCount = 0
        self.skill = False
        self.dropCoin = False
        self.stopAttack = False
        self.trigger = False
        self.immune = False
        self.immuneFinish = False
        self.invincible = False
        self.instantDeath = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -750
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0
        self.startImmune = 0
        self.endImmune = 0
        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.saCounter = 0
    #endmethod
    def InstantKill(self, num):
        if num == 1:
            self.instantDeath = True
        else:
            self.instantDeath = False
        #endif
    #endmethod
    def FaceKing(self, xPos):
        if xPos > self.rect.x:
            self.ChangeSpeed(1)
        else:
            self.ChangeSpeed(0)
        #endif
        self.ChangeSpeed(2)
    #endmethod
    def InvincibleTrigger(self):
        self.invincible = True
    #endmethod
    def HealthDisplay(self, num, levelOne_list):
        if num == 1:
            levelOne_list.add(self.rogueHealth1, self.rogueHealth2)
        else:
            levelOne_list.remove(self.rogueHealth1, self.rogueHealth2)
        #endif
    #endmethod
    def Freeze(self, num):
        if num == 1:
            self.freeze = True
        elif num != 1:
            self.freeze = False
        #endif
    #endmethod
    def Unrandom(self):
        self.random = False
    #endmethod
    def SetDifference(self):
        self.xDifference = 85
        self.xSize = 250
    #endmethod
    def TurnAround(self):
        if self.rect.x > 750:
            self.ChangeSpeed(0)
        elif self.rect.x < 670:
            self.ChangeSpeed(1)
        #endif
        self.ChangeSpeed(2)
        self.hp = 1
        self.death = False
        self.reduceHealth = False
        self.trigger = False
    #endif
    def Turn(self, num):
        if num == 0:
            self.ChangeSpeed(0)
        elif num == 1:
            self.ChangeSpeed(1)
        #endif
        self.ChangeSpeed(2)
    #endmethod
    def Reset(self):
        #Attributes
        self.hp = 10
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.sa = False
        self.saMove = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.spell = False
        self.reduceHealth = False
        self.preyPosX = 0
        self.random = False
        self.attackCount = 0
        self.skill = False
        self.dropCoin = False
        self.stopAttack = False
        self.trigger = False
        self.rect.x = self.originalX
        self.rect.y = self.originalY
        self.immune = False
        self.immuneFinish = False
        self.invincible = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -750
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0
        self.startImmune = 0
        self.endImmune = 0
        #Counter
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.saCounter = 0
        self.rogueAttackLeft.rect.x = -1000
        self.rogueAttackRight.rect.x = -1000
        self.rogueSaAttack.rect.x = -1000
        self.rogueHealth1.Update(5)
        self.rogueHealth2.Update(5)
        self.rogueHealth1.rect.x = 985
        self.rogueHealth2.rect.x = 1235
        self.Animation()
    #endmethod
    def Animation(self):
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        if self.death == False and not self.freeze:
            self.rogueAnimation.rect.y = self.rect.y - 160
            self.rogueAnimation.rect.x = self.rect.x - 85
            if not self.hurt and self.horiSpeed == 0 and not self.attacked and not self.sa:
                if self.endAnimation - self.startAnimation >= 70: #If next image
                    self.startAnimation = self.endAnimation #If player is idle
                    self.rogueAnimation.Idle(self.lastHoriSpeed, self.idleCounter)
                    if self.idleCounter != 10: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif
                #endif
            elif not self.hurt and self.horiSpeed != 0 and not self.attacked and not self.sa:
                if self.endAnimation - self.startAnimation >= 60:
                    self.startAnimation = self.endAnimation #If player running
                    self.rogueAnimation.Run(self.lastHoriSpeed, self.runCounter)
                    if self.runCounter != 9: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif
                #endif
            elif self.sa and not self.attacked:
                if self.endAnimation - self.startAnimation >= 70:
                    self.saMove = True
                    self.startAnimation = self.endAnimation #If player is special attacking
                    self.rogueAnimation.SA(self.lastHoriSpeed, self.saCounter)
                    if self.saCounter != 17: #If reached the end
                        self.saCounter += 1
                    #endif
                #endif
            elif self.hurt:
                if self.endAnimation - self.startAnimation >= 100:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.rogueAnimation.Hurt(self.lastHoriSpeed, self.hurtCounter)
                    if self.hurtCounter != 2: #If reached the end
                        self.hurtCounter += 1
                    #endif
                #endif
            elif self.attacked and not self.hurt and not self.sa:
                if self.endAnimation - self.startAnimation >= 50:
                    self.startAnimation = self.endAnimation #If player is attacking
                    self.rogueAnimation.Attack(self.lastHoriSpeed, self.attackCounter)
                    if self.attackCounter != 9: #If reached the end
                        self.attackCounter += 1
                    #endif
                #endif
            elif self.spell and not self.hurt:
                if self.endAnimation - self.startAnimation >= 90:
                    self.startAnimation = self.endAnimation #If player is casting spell
                    self.rogueAnimation.Spell(self.lastHoriSpeed, self.spellCounter)
                    if self.spellCounter != 11: #If reached the end
                        self.spellCounter += 1
                    #endif
                #endif
            #endif
        elif self.death and not self.freeze:
            if self.endAnimation - self.startAnimation >= 70:
                self.startAnimation = self.endAnimation
                self.rogueAnimation.Death(self.lastHoriSpeed, self.deathCounter)
                if self.deathCounter != 13:
                    self.deathCounter += 1
                #endif
            #endif
        #endif
    #endmethod
    def AttackTrigger(self):
        self.endAttackRest = pygame.time.get_ticks() #Get current time for end time
        if not self.freeze and not self.attacked and not self.jumped and not self.death and self.endAttackRest - self.startAttackRest >= 750:
            self.attacked = True
            self.endAttackRest = 0
            self.startAttackRest = 0
            self.attackCount += 1
        #endif
    #endmethod
    def AttackChecker(self):
        if self.stopSelf: #If the enemy should stop
            self.stopSelf = False
            self.horiSpeed = 0
        #endif
    #endmethod
    def Attack(self):
        if self.attacked and not self.freeze:
            self.horiSpeed = 0
            if self.lastHoriSpeed > 0 and not self.hurt and not self.death and self.attackCounter == 4:
                self.rogueAttackRight.rect.x = self.rect.x - 50
                self.rogueAttackRight.rect.y = self.rect.y
            elif self.lastHoriSpeed < 0 and not self.hurt and not self.death and self.attackCounter == 4:
                self.rogueAttackLeft.rect.x = self.rect.x - 70
                self.rogueAttackLeft.rect.y = self.rect.y
            elif self.attackCounter != 4:
                self.rogueAttackLeft.rect.x = -1000
                self.rogueAttackRight.rect.x = -1000
            elif self.hurt or self.death:
                self.rogueAttackLeft.rect.x = -1000
                self.rogueAttackRight.rect.x = -1000
            #endif
            if self.attackCounter == 9:
                self.rogueAttackLeft.rect.x = -1000
                self.rogueAttackRight.rect.x = -1000
                self.attacked = False
                self.attackCounter = 0
                if self.attackCount == 3:
                    self.attackCount = 0
                    self.skill = True
                #endif
            #endif
        #endif
    #endmethod
    def Control(self, x):
        if not self.freeze and not self.stopAttack:
            if not self.random and not self.skill:
                self.ChangeSpeed(2)
                if self.rect.x - x < 100 and self.rect.x - x > 0:
                    self.AttackTrigger()
                elif x - self.rect.x > 0 and x - self.rect.x <= 130:
                    self.AttackTrigger()
                elif x <= self.rect.x and abs(x - self.rect.x) >= 100:
                    self.ChangeSpeed(0)
                elif x > self.rect.x and abs(x - self.rect.x) >= 130:
                    self.ChangeSpeed(1)
                #endif
            elif self.skill:
                self.ChangeSpeed(2)
                self.SATrigger(x)
            elif self.random:
                if self.startRandom == 0: #If start timer has not started yet
                    self.startRandom = pygame.time.get_ticks() #Record current time
                    self.ChangeSpeed(randint(0,1))
                #endif
                self.endRandom = pygame.time.get_ticks()
                if self.endRandom - self.startRandom > 400:
                    self.startRandom = 0
                    self.endRandom = 0
                    self.random = False
                #endif
            #endif
        #endif
        if self.rect.x <= 0: #If player reach the end of screen
            self.rect.x = 0
        elif self.rect.x >= 1420:
            self.rect.x = 1420
        #endif
    #endmethod
    def SATrigger(self, xPos):
        if not self.attacked and not self.hurt and not self.death and not self.freeze:
            self.sa = True
            self.preyPosX = xPos + self.xDifference
        #endif
    #endmethod
    def SA(self):
        if self.sa and not self.freeze:
            self.horiSpeed = 0
            self.vertSpeed = 0
            if self.saCounter == 8:
                self.rect.x = self.preyPosX
                self.rect.y = 110
            #endif
            if self.saCounter >= 9 and self.saCounter <= 12 and self.saMove:
                self.rect.y += 150
                self.saMove = False
            #endif
            if self.lastHoriSpeed > 0 and not self.hurt and not self.death and self.saCounter >= 13 and self.saCounter <= 14:
                self.rogueSaAttack.rect.x = self.rect.x - 35
                self.rogueSaAttack.rect.y = self.rect.y + 20
            elif self.lastHoriSpeed < 0 and not self.hurt and not self.death and self.saCounter >= 13 and self.saCounter <= 14:
                self.rogueSaAttack.rect.x = self.rect.x - 85
                self.rogueSaAttack.rect.y = self.rect.y + 20
            elif self.saCounter < 12 or self.saCounter > 14:
                self.rogueSaAttack.rect.x = -1000
            elif self.hurt or self.death:
                self.rogueSaAttack.rect.x = -1000
            #endif
            if self.saCounter == 17:
                self.sa = False
                self.rogueSaAttack.rect.x = -1000
                self.rect.y = 710
                self.saCounter = 0
                self.skill = False
                self.random = True
            #endif
        #endif
    #endmethod
    def Health(self, sprite_list, coin_list, enemyCount):
        if not self.immuneFinish and self.immune:
            if self.startImmune == 0: #If start timer has not started yet
                self.startImmune = pygame.time.get_ticks() #Record current time
            #endif
            self.endImmune = pygame.time.get_ticks() #Get current time for end time
            if self.endImmune - self.startImmune >= 3000:
                self.immune = False
                self.immuneFinish = True
            #endif
        #endif
        if self.reduceHealth == True and not self.freeze:
            self.reduceHealth = False
            if self.hp > 0:
                if not self.invincible:
                    if not self.instantDeath:
                        self.hp -= 1
                    elif self.instantDeath:
                        self.hp -= 9
                        if self.hp < 0:
                            self.hp = 0
                        #endif
                        self.rogueHealth2.Update(0)
                    #endif
                #endif
                if self.hp >= 5:
                    hpNum = self.hp - 5
                    self.rogueHealth2.Update(hpNum)
                else:
                    self.rogueHealth1.Update(self.hp)
                #endif
            #endif
            if self.hp == 1:
                num = enemyCount[0]
                enemyCount[0] = num - 1
                self.stopAttack = True
                self.attacked = False
                self.sa = False
                self.saMove = False
                self.spell = False
                self.ChangeSpeed(2)
                self.immune = True
            #endif
            if self.hp == 0:
                self.death = True
                if not self.dropCoin:
                    self.dropCoin = True
                    for coins in self.coin_list:
                        coins.CoinSet(self.rect.x+30,self.rect.y+70)
                        sprite_list.add(coins)
                        coin_list.add(coins)
                    #endfor
                #endif
            #endif
        #endif
        if self.hp == 9:
            self.rogueHealth1.rect.x = 1035
            self.rogueHealth2.rect.x = 1285
        elif self.hp == 8:
            self.rogueHealth1.rect.x = 1085
            self.rogueHealth2.rect.x = 1335
        elif self.hp == 7:
            self.rogueHealth1.rect.x = 1135
            self.rogueHealth2.rect.x = 1385
        elif self.hp == 6:
            self.rogueHealth1.rect.x = 1185
            self.rogueHealth2.rect.x = 1435
        elif self.hp == 5:
            self.rogueHealth1.rect.x = 1235
        elif self.hp == 4:
            self.rogueHealth1.rect.x = 1285
        elif self.hp == 3:
            self.rogueHealth1.rect.x = 1335
        elif self.hp == 2:
            self.rogueHealth1.rect.x = 1385
        elif self.hp == 1:
            self.rogueHealth1.rect.x = 1435
        #endif
    #endmethod
    def EnemyAttackDetection(self, leftAttack_list, rightAttack_list, player_list):
        enemyGetHit1_list = pygame.sprite.spritecollide(self, leftAttack_list, False)#If get hit
        for attack in enemyGetHit1_list:
            if self.hurt == False and not self.death and not self.freeze and not self.immune:
                if not self.instantDeath:
                    luckyNum = randint(0,1)
                    if luckyNum == 0:
                        self.hurt = True
                        self.reduceHealth = True
                        self.rogueAttackLeft.rect.x = -1000
                        self.rogueAttackRight.rect.x = -1000
                    else:
                        for player in player_list:
                            if player.rect.x <= 1370:
                                self.rect.x = player.rect.x + self.xSize
                                self.lastHoriSpeed = -1
                            else:
                                self.rect.x = player.rect.x - 180
                                self.lastHoriSpeed = 1
                            #endif
                        #endfor
                    #endif
                else:
                    self.hurt = True
                    self.reduceHealth = True
                    self.rogueAttackLeft.rect.x = -1000
                    self.rogueAttackRight.rect.x = -1000
                #endif
            #endif
        #endfor
        enemyGetHit2_list = pygame.sprite.spritecollide(self, rightAttack_list, False)#If get hit
        for attack in enemyGetHit2_list:
            if self.hurt == False and not self.death and not self.freeze and not self.immune:
                if not self.instantDeath:
                    luckyNum = randint(0,1)
                    if luckyNum == 0:
                        self.hurt = True
                        self.reduceHealth = True
                        self.rogueAttackLeft.rect.x = -1000
                        self.rogueAttackRight.rect.x = -1000
                    else:
                        for player in player_list:
                            if player.rect.x >= 80:
                                self.rect.x = player.rect.x - 80
                                self.lastHoriSpeed = 1
                            else:
                                self.rect.x = player.rect.x + self.xSize + 100
                                self.lastHoriSpeed = -1
                            #endif
                        #endfor
                    #endif
                else:
                    self.hurt = True
                    self.reduceHealth = True
                    self.rogueAttackLeft.rect.x = -1000
                    self.rogueAttackRight.rect.x = -1000
                #endif
            #endif
        #endfor
    #endmethod
    def FireBallDetection(self, level_list, fireBall_list):
        enemyGetHit_list = pygame.sprite.spritecollide(self, fireBall_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
                self.rogueAttackLeft.rect.x = -1000
                self.rogueAttackRight.rect.x = -1000
            #endif
        #endfor
    #endmethod
    def Hurt(self):
        if self.hurt == True and not self.freeze:
            self.horiSpeed = 0
            if self.startHurt == 0:
                self.startHurt = pygame.time.get_ticks()
            #endif
            self.endHurt = pygame.time.get_ticks()
            if self.endHurt - self.startHurt > 390:
                self.endHurt = 0
                self.startHurt = 0
                self.hurt = False
                self.hurtCounter = 0
                self.attackCount = 0
                self.skill = True
            #endif
        #endif
    #endmethod
    def Death(self, rogueDead):
        if self.death and not self.trigger:
            self.trigger = True
            rogueDead[0] = 0
        #endif
    #endmethod
    def MoveVert(self, block_list):
        if self.freeze == False and not self.sa:
            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif
            if self.rect.y >= 710 and self.vertSpeed <= 0: #If sinks into the ground
                self.rect.y = 710 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False
            elif self.rect.y <= 0 and self.vertSpeed > 0:
                self.rect.y = 0
                self.vertSpeed = 0
            #endif
            self.rect.y -= self.vertSpeed #Move
            selfVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in selfVertBlock_list:
                if self.vertSpeed <= 0: #If player is falling
                    self.rect.bottom = block.rect.top
                    self.jumped = False
                elif self.vertSpeed >= 0: #If player is jumping
                    self.rect.top = block.rect.bottom
                #endif
                self.vertSpeed = 0 #Stop player
            #endfor
        #endif
    #endmethod
    def ChangeSpeed(self,num):
        if self.freeze == False and self.attacked == False and not self.death:
            if num == 0:
                self.horiSpeed = -12
                self.lastHoriSpeed = self.horiSpeed
            elif num == 1:
                self.horiSpeed = 12
                self.lastHoriSpeed = self.horiSpeed
            elif num == 2:
                self.horiSpeed = 0
            #endif
        #endif
    #endmethod
    def MoveHori(self, block_list):
        if self.freeze == False:
            self.rect.x += self.horiSpeed
            for block in block_list:
                if self.rect.colliderect(block.rect): #If player hit block
                    if self.horiSpeed > 0:
                        self.rect.right = block.rect.left
                    else:
                        self.rect.left = block.rect.right
                    #endif
                #endif
            #endfor
        #endif
    #endmethod
#endclass
#Mushroom Class
class MushroomClass(pygame.sprite.Sprite): #Class of the mushroom
    def __init__(self, mType, x, y, levelTwo_list, enemyAttack_list):
        super().__init__()
        self.image = pygame.Surface([100, 80])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.originalX = x
        self.originalY = y
        if mType == 1:
            self.mColor = 5
        elif mType == 2:
            self.mColor = 6
        elif mType == 3:
            self.mColor = 7
        #endif
        self.mushroomAnimation = EnemyAnimation(self.mColor, 200, 160, self.rect.x, self.rect.y)
        self.mushroomHealth1 = HealthClass(1, 5, 100, 20, self.rect.x, self.rect.y - 25)
        self.mushroomHealth2 = HealthClass(1, 5, 100, 20, self.rect.x, self.rect.y - 50)
        self.mushroomAttack = AttackClass(190, 130, -1000, 0)
        enemyAttack_list.add(self.mushroomAttack)
        levelTwo_list.add(self.mushroomAnimation, self.mushroomHealth1, self.mushroomHealth2)
        #Attributes
        self.hp = 10
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.reduceHealth = False
        self.instantDeath = False
        self.burned = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startWalk = 0
        self.endWalk = 0
        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
    #endmethod
    def InstantKill(self, num):
        if num == 1:
            self.instantDeath = True
        else:
            self.instantDeath = False
        #endif
    #endmethod
    def Reset(self):
        #Attributes
        self.rect.x = self.originalX
        self.rect.y = self.originalY
        self.hp = 10
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.reduceHealth = False
        self.burned = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startWalk = 0
        self.endWalk = 0
        #Counter
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.mushroomHealth1.Update(5)
        self.mushroomHealth2.Update(5)
        self.mushroomHealth1.rect.x = self.rect.x
        self.mushroomHealth2.rect.x = self.rect.x
        self.Animation()
    #endmethod
    def Freeze(self, num):
        if num == 1:
            self.freeze = True
        else:
            self.freeze = False
        #endif
    #endmethod
    def Animation(self):
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        self.mushroomAnimation.rect.y = self.rect.y - 75
        self.mushroomAnimation.rect.x = self.rect.x - 50
        if self.death == False and self.freeze == False:
            if not self.hurt and self.horiSpeed == 0 and not self.attacked:
                if self.endAnimation - self.startAnimation >= 80: #If next image
                    self.startAnimation = self.endAnimation #If player is idle
                    self.mushroomAnimation.Idle(self.lastHoriSpeed, self.idleCounter)
                    if self.idleCounter != 7: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif
                #endif
            elif not self.hurt and self.horiSpeed != 0 and not self.attacked:
                if self.endAnimation - self.startAnimation >= 110:
                    self.startAnimation = self.endAnimation #If player running
                    self.mushroomAnimation.Run(self.lastHoriSpeed, self.runCounter)
                    if self.runCounter != 7: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif
                #endif
            elif self.hurt == True:
                if self.endAnimation - self.startAnimation >= 110:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.mushroomAnimation.Hurt(self.lastHoriSpeed, self.hurtCounter)
                    if self.hurtCounter != 2: #If reached the end
                        self.hurtCounter += 1
                    #endif
                #endif
            elif self.attacked == True and not self.hurt:
                if self.endAnimation - self.startAnimation >= 80:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.mushroomAnimation.Attack(self.lastHoriSpeed, self.attackCounter)
                    if self.attackCounter != 15: #If reached the end
                        self.attackCounter += 1
                    #endif
                #endif
            #endif
        elif self.death:
            if self.endAnimation - self.startAnimation >= 60:
                self.startAnimation = self.endAnimation
                self.mushroomAnimation.Death(self.lastHoriSpeed, self.deathCounter)
                if self.deathCounter != 10:
                    self.deathCounter += 1
                #endif
            #endif
        #endif
    #endmethod
    def Control(self):
        if not self.freeze:
            if self.startWalk == 0: #If start timer has not started yet
                self.startWalk = pygame.time.get_ticks() #Record current time
                if self.horiSpeed == 0:
                    self.ChangeSpeed(randint(0,1))
                #endif
            #endif
            self.endWalk = pygame.time.get_ticks() #Get current time for end time
            if self.endWalk - self.startWalk >= 5000:
                rollDice = randint(1,3)
                if rollDice == 3:
                    self.ChangeSpeed(2)
                    self.AttackTrigger()
                else:
                    self.ChangeSpeed(randint(0,1))
                #endif
                self.startWalk = 0
                self.endWalk = 0
            #endif
            if self.rect.x <= 0:
                self.rect.x = 0
                self.ChangeSpeed(1)
            elif self.rect.x >= 1400:
                self.rect.x = 1400
                self.ChangeSpeed(0)
            #endif
        #endif
    #endif
    def Health(self, enemyCount):
        if self.reduceHealth == True and not self.freeze:
            self.reduceHealth = False
            if self.hp > 0:
                self.hp -= 1
                if self.hp >= 5:
                    hpNum = self.hp - 5
                    self.mushroomHealth2.Update(hpNum)
                else:
                    self.mushroomHealth1.Update(self.hp)
                #endif
                if self.hp > 0 and self.burned:
                    self.hp -= 1
                    self.burned = False
                #endif
                if self.instantDeath:
                    self.hp = 0
                    self.mushroomHealth2.Update(0)
                #endif
                if self.hp >= 5:
                    hpNum = self.hp - 5
                    self.mushroomHealth2.Update(hpNum)
                else:
                    self.mushroomHealth1.Update(self.hp)
                #endif
            if self.hp == 0:
                self.death = True
                num = enemyCount[0]
                enemyCount[0] = num - 1
            #endif
        #endif
        if self.hp == 10:
            self.mushroomHealth2.rect.x = self.rect.x
            self.mushroomHealth1.rect.x = self.rect.x
        elif self.hp == 9:
            self.mushroomHealth2.rect.x = self.rect.x + 10
            self.mushroomHealth1.rect.x = self.rect.x
        elif self.hp == 8:
            self.mushroomHealth2.rect.x = self.rect.x + 20
            self.mushroomHealth1.rect.x = self.rect.x
        elif self.hp == 7:
            self.mushroomHealth2.rect.x = self.rect.x + 30
            self.mushroomHealth1.rect.x = self.rect.x
        elif self.hp == 6:
            self.mushroomHealth2.rect.x = self.rect.x + 40
            self.mushroomHealth1.rect.x = self.rect.x
        elif self.hp == 5:
            self.mushroomHealth1.rect.x = self.rect.x
        elif self.hp == 4:
            self.mushroomHealth1.rect.x = self.rect.x + 10
        elif self.hp == 3:
            self.mushroomHealth1.rect.x = self.rect.x + 20
        elif self.hp == 2:
            self.mushroomHealth1.rect.x = self.rect.x + 30
        elif self.hp == 1:
            self.mushroomHealth1.rect.x = self.rect.x + 40
        #endif
        self.mushroomHealth1.rect.y = self.rect.y - 25
        self.mushroomHealth2.rect.y = self.rect.y - 50
    #endmethod
    def AttackTrigger(self):
        self.endAttackRest = pygame.time.get_ticks() #Get current time for end time
        if not self.freeze and self.attacked == False and self.death == False:
            self.attacked = True
            self.endAttackRest = 0
            self.startAttackRest = 0
        #endif
    #endmethod
    def Attack(self):
        if self.attacked == True and self.freeze == False:
            self.horiSpeed = 0
            if not self.hurt and not self.death and self.attackCounter == 8:
                self.mushroomAttack.rect.x = self.rect.x - 45
                self.mushroomAttack.rect.y = self.rect.y - 50
            elif self.attackCounter != 8:
                self.mushroomAttack.rect.x = -1000
            elif self.death:
                self.mushroomAttack.rect.x = -1000
            #endif
            if self.attackCounter == 15:
                self.mushroomAttack.rect.x = -1000
                self.attacked = False
                self.attackCounter = 0
            #endif
        #endif
    #endmethod
    def EnemyAttackDetection(self, leftAttack_list, rightAttack_list):
        enemyGetHit1_list = pygame.sprite.spritecollide(self, leftAttack_list, False)#If get hit
        for attack in enemyGetHit1_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
        enemyGetHit2_list = pygame.sprite.spritecollide(self, rightAttack_list, False)#If get hit
        for attack in enemyGetHit2_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
    #endmethod
    def FireBallDetection(self, level_list, fireBall_list):
        enemyGetHit_list = pygame.sprite.spritecollide(self, fireBall_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
                self.burned = True
            #endif
        #endfor
    #endmethod
    def Hurt(self):
        if self.hurt == True and not self.freeze:
            self.horiSpeed = 0
            if self.hurtCounter == 2:
                self.hurt = False
                self.hurtCounter = 0
                rollDice = randint(1,3)
                if rollDice == 3:
                    self.ChangeSpeed(2)
                    self.AttackTrigger()
                else:
                    self.ChangeSpeed(randint(0,1))
                #endif
            #endif
        #endif
    #endmethod
    def MoveVert(self, block_list):
        if self.freeze == False:
            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif
            if self.rect.y >= 720 and self.vertSpeed <= 0: #If sinks into the ground
                self.rect.y = 720 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False
            elif self.rect.y <= 0 and self.vertSpeed > 0:
                self.rect.y = 0
                self.vertSpeed = 0
            #endif
            self.rect.y -= self.vertSpeed #Move
            selfVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in selfVertBlock_list:
                if self.vertSpeed <= 0: #If player is falling
                    self.rect.bottom = block.rect.top
                    self.jumped = False
                elif self.vertSpeed >= 0: #If player is jumping
                    self.rect.top = block.rect.bottom
                #endif
                self.vertSpeed = 0 #Stop player
            #endfor
        #endif
    #endmethod
    def ChangeSpeed(self,num):
        if self.freeze == False and self.attacked == False and not self.death:
            if num == 0:
                self.horiSpeed = -2
                self.lastHoriSpeed = self.horiSpeed
            elif num == 1:
                self.horiSpeed = 2
                self.lastHoriSpeed = self.horiSpeed
            elif num == 2:
                self.horiSpeed = 0
            #endif
        #endif
    #endmethod
    def MoveHori(self, block_list):
        if self.freeze == False:
            self.rect.x += self.horiSpeed
            for block in block_list:
                if self.rect.colliderect(block.rect): #If player hit block
                    if self.horiSpeed > 0:
                        self.rect.right = block.rect.left
                    else:
                        self.rect.left = block.rect.right
                    #endif
                #endif
            #endfor
        #endif
    #endmethod
#endclass
#Arun Swordsmith Class
class ArunClass(pygame.sprite.Sprite): #Class of the Arun Swordsmith
    def __init__(self, x, y, levelTwo_list, leftEnemyAttack_list, rightEnemyAttack_list):
        super().__init__()
        self.image = pygame.Surface([50, 100])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.originalX = x
        self.originalY = y
        self.coin_list = pygame.sprite.Group()
        #Attributes
        for i in range(20):
            coin = ItemClass(1, 20, 20, -200, 0)
            self.coin_list.add(coin)
        #endfor
        self.arunAnimation = EnemyAnimation(4, 320, 250, x-135, y-155)
        self.arunAttackLeft = AttackClass(170, 130, -1000, 0)
        self.arunAttackRight = AttackClass(170, 130, -1000, 0)
        leftEnemyAttack_list.add(self.arunAttackLeft)
        rightEnemyAttack_list.add(self.arunAttackRight)
        self.arunHealth1 = HealthClass(1, 5, 250, 50, 985, 10)
        self.arunHealth2 = HealthClass(1, 5, 250, 50, 1235, 10)
        self.arunHealth3 = HealthClass(1, 5, 250, 50, 985, 65)
        self.arunHealth4 = HealthClass(1, 5, 250, 50, 1235, 65)
        levelTwo_list.add(self.arunAnimation)
        #Attributes
        self.hp = 20
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.runSpeed = 8
        self.attacked = False
        self.throwed = False
        self.saMove = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.spell = False
        self.jumped = False
        self.jumpTime = 0
        self.jumpNum = 3
        self.reduceHealth = False
        self.preyPosX = 0
        self.random = False
        self.random2 = False
        self.randomTime = 700
        self.attackCount = 0
        self.skill = False
        self.throwTime = 1000
        self.stopSelf = False
        self.dropCoin = False
        self.rest = False
        self.javelinThrowed = False
        self.restTime = 900
        self.attackCountNum = 4
        self.immunity = False
        self.immune = False
        self.immuneFinish = False
        self.invincible = False
        self.instantDeath = False
        self.deathNum = 0
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -750
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0
        self.startRandom2 = 0
        self.endRandom2 = 0
        self.startAbove = 0
        self.endAbove = 0
        self.startThrow = 0
        self.endThrow = 0
        self.startRest = 0
        self.endRest = 0
        self.startImmune = 0
        self.endImmune = 0
        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.throwCounter = 0
        self.fallCounter = 0
        self.jumpCounter = 0
    #endmethod
    def SetDeathHp(self, num):
        if num == 1:
            self.deathNum = 1
        elif num == 0:
            self.deathNum = 0
        #endif
    #endmethod
    def InstantKill(self, num):
        if num == 1:
            self.instantDeath = True
        else:
            self.instantDeath = False
        #endif
    #endmethod
    def FaceKing(self, xPos):
        if xPos > self.rect.x:
            self.ChangeSpeed(1)
        else:
            self.ChangeSpeed(0)
        #endif
        self.ChangeSpeed(2)
    #endmethod
    def Turn(self, num):
        if num == 0:
            self.ChangeSpeed(0)
        elif num == 1:
            self.ChangeSpeed(1)
        #endif
        self.ChangeSpeed(2)
    #endmethod
    def HealthDisplay(self, num, levelTwo_list):
        if num == 1:
            levelTwo_list.add(self.arunHealth1, self.arunHealth2, self.arunHealth3, self.arunHealth4)
        else:
            levelTwo_list.remove(self.arunHealth1, self.arunHealth2, self.arunHealth3, self.arunHealth4)
        #endif
    #endmethod
    def Freeze(self, num):
        if num == 1:
            self.freeze = True
        elif num != 1:
            self.freeze = False
        #endif
    #endmethod
    def Unrandom(self):
        self.random = False
    #endmethod
    def Reset(self):
        #Attributes
        self.hp = 20
        self.horiSpeed = 0
        self.runSpeed = 8
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.throwed = False
        self.saMove = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.jumped = False
        self.jumpTime = 0
        self.reduceHealth = False
        self.preyPosX = 0
        self.random = False
        self.random2 = False
        self.randomTime = 600
        self.attackCount = 0
        self.throwTime = 1000
        self.dropCoin = False
        self.stopSelf = False
        self.rest = False
        self.rect.x = self.originalX
        self.rect.y = self.originalY
        self.javelinThrowed = False
        self.restTime = 900
        self.attackCountNum = 4
        self.immunity = False
        self.immune = False
        self.immuneFinish = False
        self.invincible = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -750
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0
        self.startRandom2 = 0
        self.endRandom2 = 0
        self.startAbove = 0
        self.endAbove = 0
        self.startThrow = 0
        self.endThrow = 0
        self.startRest = 0
        self.endRest = 0
        self.startImmune = 0
        self.endImmune = 0
        #Counter
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.throwCounter = 0
        self.fallCounter = 0
        self.jumpCounter = 0
        self.arunAttackLeft.rect.x = -1000
        self.arunAttackRight.rect.x = -1000
        self.arunHealth1.Update(5)
        self.arunHealth2.Update(5)
        self.arunHealth3.Update(5)
        self.arunHealth4.Update(5)
        self.arunHealth1.rect.x = 985
        self.arunHealth2.rect.x = 1235
        self.arunHealth3.rect.x = 985
        self.arunHealth4.rect.x = 1235
        self.Animation()
    #endmethod
    def Animation(self):
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        if self.death == False and not self.freeze:
            self.arunAnimation.rect.y = self.rect.y - 145
            self.arunAnimation.rect.x = self.rect.x - 135
            if not self.hurt and self.horiSpeed == 0 and not self.attacked and not self.throwed and not self.jumped:
                if self.endAnimation - self.startAnimation >= 70: #If next image
                    self.startAnimation = self.endAnimation #If player is idle
                    self.arunAnimation.Idle(self.lastHoriSpeed, self.idleCounter)
                    if self.idleCounter != 9: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif
                #endif
            elif not self.hurt and self.horiSpeed != 0 and not self.attacked and not self.throwed and not self.jumped:
                if self.endAnimation - self.startAnimation >= 60:
                    self.startAnimation = self.endAnimation #If player running
                    self.arunAnimation.Run(self.lastHoriSpeed, self.runCounter)
                    if self.runCounter != 9: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif
                #endif
            elif self.hurt == True:
                if self.endAnimation - self.startAnimation >= 75:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.arunAnimation.Hurt(self.lastHoriSpeed, self.hurtCounter)
                    if self.hurtCounter != 3: #If reached the end
                        self.hurtCounter += 1
                    #endif
                #endif
            elif self.attacked == True and not self.hurt and not self.throwed:
                if self.endAnimation - self.startAnimation >= 55:
                    self.startAnimation = self.endAnimation #If player is attacking
                    self.arunAnimation.Attack(self.lastHoriSpeed, self.attackCounter)
                    if self.attackCounter != 11: #If reached the end
                        self.attackCounter += 1
                    #endif
                #endif
            elif self.throwed == True and not self.attacked:
                if self.endAnimation - self.startAnimation >= 45:
                    self.startAnimation = self.endAnimation #If player is special attacking
                    self.arunAnimation.Throw(self.lastHoriSpeed, self.throwCounter)
                    if self.throwCounter != 9: #If reached the end
                        self.throwCounter += 1
                    #endif
                #endif
            elif self.jumped == True and self.vertSpeed >= 0 and not self.hurt:
                if self.endAnimation - self.startAnimation >= 200:
                    self.startAnimation = self.endAnimation #If player jumping
                    self.arunAnimation.Jump(self.lastHoriSpeed, self.jumpCounter)
                    if self.jumpCounter != 2: #If reached the end
                        self.jumpCounter += 1
                    else:
                        self.jumpCounter = 2 #Stay at the last frame
                    #endif
                #endif
            elif self.jumped == True and self.vertSpeed < 0 and not self.hurt:
                if self.endAnimation - self.startAnimation >= 200:
                    self.startAnimation = self.endAnimation #If player falling
                    self.arunAnimation.Fall(self.lastHoriSpeed, self.fallCounter)
                    if self.fallCounter != 2: #If reached the end
                        self.fallCounter += 1
                    else:
                        self.fallCounter = 2 #Stay at the last frame
                    #endif
                #endif
            #endif
        elif self.death and not self.freeze:
            if self.endAnimation - self.startAnimation >= 70:
                self.startAnimation = self.endAnimation
                self.arunAnimation.Death(self.lastHoriSpeed, self.deathCounter)
                if self.deathCounter != 16:
                    self.deathCounter += 1
                #endif
            #endif
        #endif
    #endmethod
    def InvincibleTrigger(self):
        self.invincible = True
    #endmethod
    def ImmuneTrigger(self):
        self.immunity = True
    #endmethod
    def AttackTrigger(self):
        self.endAttackRest = pygame.time.get_ticks() #Get current time for end time
        if not self.freeze and self.attacked == False and self.jumped == False and self.death == False and self.endAttackRest - self.startAttackRest >= 400:
            self.attacked = True
            self.endAttackRest = 0
            self.startAttackRest = 0
        #endif
    #endmethod
    def AttackChecker(self):
        if self.stopSelf: #If the enemy should stop
            self.stopSelf = False
            self.horiSpeed = 0
        #endif
    #endmethod
    def Attack(self):
        if self.attacked == True and self.freeze == False:
            self.horiSpeed = 0
            if self.attackCounter == 5 or self.attackCounter == 6:
                if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                    self.arunAttackRight.rect.x = self.rect.x
                    self.arunAttackRight.rect.y = self.rect.y - 30
                elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                    self.arunAttackLeft.rect.x = self.rect.x - 120
                    self.arunAttackLeft.rect.y = self.rect.y - 30
                #endif
            elif self.attackCounter != 5 or self.attackCounter != 6:
                self.arunAttackLeft.rect.x = -1000
                self.arunAttackRight.rect.x = -1000
            #endif
            if self.hurt or self.death:
                self.arunAttackLeft.rect.x = -1000
                self.arunAttackRight.rect.x = -1000
            #endif
            if self.attackCounter == 11:
                self.arunAttackLeft.rect.x = -1000
                self.arunAttackRight.rect.x = -1000
                self.attacked = False
                self.attackCounter = 0
                self.attackCount += 1
                if self.attackCount == self.attackCountNum:
                    self.attackCount = 0
                    self.rest = True
                #endif
            #endif
        #endif
    #endmethod
    def Control2(self, x):
        if not self.freeze:
            if not self.random and not self.random2 and not self.skill and not self.freeze and not self.attacked and not self.rest and not self.throwed:
                self.ChangeSpeed(2)
                if self.rect.x - x <= 160 and self.rect.x - x > 0 and self.lastHoriSpeed < 0:
                    self.AttackTrigger()
                elif x - self.rect.x > 0 and x - self.rect.x <= 160 and self.lastHoriSpeed > 0:
                    self.AttackTrigger()
                elif x <= self.rect.x:
                    self.ChangeSpeed(0)
                elif x > self.rect.x:
                    self.ChangeSpeed(1)
                #endif
                if abs(self.rect.x - x) > 500:
                    self.endThrow = pygame.time.get_ticks() #Get current time for end time
                    if self.endThrow - self.startThrow >= self.throwTime:
                        self.skill = True
                        self.endThrow = 0
                        self.startThrow = 0
                    #endif
                #endif
            elif self.random and not self.random2 and not self.skill and not self.freeze and not self.rest:
                if self.startRandom == 0: #If start timer has not started yet
                    self.startRandom = pygame.time.get_ticks() #Record current time
                    self.ChangeSpeed(randint(0,1))
                #endif
                self.endRandom = pygame.time.get_ticks()
                if self.endRandom - self.startRandom > 400:
                    self.startRandom = 0
                    self.endRandom = 0
                    self.random = False
                    self.rest = False
                    self.random2 = False
                #endif
            elif self.random2 and not self.freeze and not self.rest:
                if self.startRandom2 == 0: #If start timer has not started yet
                    self.startRandom2 = pygame.time.get_ticks() #Record current time
                    self.ChangeSpeed(randint(0,1))
                #endif
                self.endRandom2 = pygame.time.get_ticks()
                if self.endRandom2 - self.startRandom2 > self.randomTime:
                    self.startRandom2 = 0
                    self.endRandom2 = 0
                    self.random2 = False
                    self.rest = False
                    self.random = False
                #endif
            elif self.rest and not self.freeze and not self.random and not self.random2:
                if self.startRest == 0: #If start timer has not started yet
                    self.startRest = pygame.time.get_ticks() #Record current time
                #endif
                self.endRest = pygame.time.get_ticks()
                if self.endRest - self.startRest >= self.restTime:
                    self.startRest = 0
                    self.endRest = 0
                    self.rest = False
                    self.random2 = False
                    self.random = False
                #endif
            #endif
            if self.skill and not self.freeze and not self.rest:
                self.ChangeSpeed(2)
                self.ThrowTrigger()
            #endif
        #endif
        if self.rect.x <= 0: #If player reach the end of screen
            self.rect.x = 0
        elif self.rect.x >= 1450:
            self.rect.x = 1450
        #endif
    #endmethod
    def Control(self, x, y):
        if not self.freeze:
            if not self.random and not self.random2 and not self.skill and not self.freeze and not self.attacked and not self.rest and not self.throwed:
                if self.rect.y == y:
                    self.ChangeSpeed(2)
                    if self.rect.x - x <= 160 and self.rect.x - x > 0 and self.lastHoriSpeed < 0:
                        self.AttackTrigger()
                    elif x - self.rect.x > 0 and x - self.rect.x <= 160 and self.lastHoriSpeed > 0:
                        self.AttackTrigger()
                    elif x <= self.rect.x:
                        self.ChangeSpeed(0)
                    elif x > self.rect.x:
                        self.ChangeSpeed(1)
                    #endif
                elif y > self.rect.y:
                    self.ChangeSpeed(2)
                    if self.startAbove == 0: #If start timer has not started yet
                        self.startAbove = pygame.time.get_ticks() #Record current time
                    #endif
                    self.endAbove = pygame.time.get_ticks()
                    if self.endAbove - self.startAbove >= 1000:
                        self.random2 = True
                        self.startAbove = 0
                        self.endAbove = 0
                    #endif
                    if x <= self.rect.x and abs(x - self.rect.x) >= 90:
                        self.ChangeSpeed(0)
                    elif x > self.rect.x and abs(x - self.rect.x) >= 90:
                        self.ChangeSpeed(1)
                    #endif
                elif y < self.rect.y:
                    self.startAbove = 0
                    self.endAbove = 0
                    self.ChangeSpeed(2)
                    if x <= self.rect.x and abs(x - self.rect.x) >= 90:
                        self.ChangeSpeed(0)
                    elif x > self.rect.x and abs(x - self.rect.x) >= 90:
                        self.ChangeSpeed(1)
                    #endif
                    self.Jump()
                    if self.jumpTime > self.jumpNum:
                        self.random = True
                    #endif
                #endif
                if abs(self.rect.x - x) > 500 and self.rect.y + 20 >= y and self.rect.y + 20 <= y+100:
                    self.endThrow = pygame.time.get_ticks() #Get current time for end time
                    if self.endThrow - self.startThrow >= self.throwTime:
                        self.skill = True
                        self.endThrow = 0
                        self.startThrow = 0
                    #endif
                #endif
            elif self.random and not self.random2 and not self.skill and not self.freeze and not self.rest:
                if self.startRandom == 0: #If start timer has not started yet
                    self.startRandom = pygame.time.get_ticks() #Record current time
                    self.ChangeSpeed(randint(0,1))
                #endif
                self.endRandom = pygame.time.get_ticks()
                if self.endRandom - self.startRandom > 400:
                    self.startRandom = 0
                    self.endRandom = 0
                    self.random = False
                    self.rest = False
                    self.random2 = False
                #endif
            elif self.random2 and not self.freeze and not self.rest:
                if self.startRandom2 == 0: #If start timer has not started yet
                    self.startRandom2 = pygame.time.get_ticks() #Record current time
                    self.ChangeSpeed(randint(0,1))
                #endif
                self.endRandom2 = pygame.time.get_ticks()
                if self.endRandom2 - self.startRandom2 > self.randomTime:
                    self.startRandom2 = 0
                    self.endRandom2 = 0
                    self.random2 = False
                    self.rest = False
                    self.random = False
                #endif
            elif self.rest and not self.freeze and not self.random and not self.random2:
                if self.startRest == 0: #If start timer has not started yet
                    self.startRest = pygame.time.get_ticks() #Record current time
                #endif
                self.endRest = pygame.time.get_ticks()
                if self.endRest - self.startRest >= self.restTime:
                    self.startRest = 0
                    self.endRest = 0
                    self.rest = False
                    self.random2 = False
                    self.random = False
                #endif
            #endif
            if self.skill and not self.freeze and not self.rest:
                self.ChangeSpeed(2)
                self.ThrowTrigger()
            #endif
        #endif
        if self.rect.x <= 0: #If player reach the end of screen
            self.rect.x = 0
        elif self.rect.x >= 1450:
            self.rect.x = 1450
        #endif
    #endmethod
    def ThrowTrigger(self):
        if not self.attacked and not self.hurt and not self.death and not self.freeze:
            self.throwed = True
        #endif
    #endmethod
    def Throw(self, leftJavelin_list, rightJavelin_list, levelTwo_list):
        if self.throwed == True and self.freeze == False:
            if self.throwCounter == 3 and not self.javelinThrowed:
                self.javelinThrowed = True
                if self.lastHoriSpeed > 0:
                    javelin = ItemClass(4, 20, 40, self.rect.x-55, self.rect.y+20)
                    rightJavelin_list.add(javelin)
                elif self.lastHoriSpeed < 0:
                    javelin = ItemClass(4, -20, 40, self.rect.x-55, self.rect.y+20)
                    leftJavelin_list.add(javelin)
                #endif
                levelTwo_list.add(javelin)
            #endif
            if self.throwCounter == 9:
                self.javelinThrowed = False
                self.throwCounter = 0
                self.throwed = False
                self.skill = False
                self.random = False
                self.rest = False
                self.random2 = False
                self.startThrow = pygame.time.get_ticks() #Record current time
                self.attackCount += 1
                if self.attackCount == self.attackCountNum:
                    self.attackCount = 0
                    self.rest = True
                #endif
            #endif
        #endif
    #endmethod
    def Health(self, sprite_list, coin_list, enemyCount, mehiraDefeat):
        if not self.immuneFinish and self.immune:
            if self.startImmune == 0: #If start timer has not started yet
                self.startImmune = pygame.time.get_ticks() #Record current time
            #endif
            self.endImmune = pygame.time.get_ticks() #Get current time for end time
            if self.endImmune - self.startImmune >= 3000:
                self.immune = False
                self.immuneFinish = True
                self.immunity = False
            #endif
        #endif
        if self.reduceHealth == True and not self.freeze:
            self.reduceHealth = False
            if self.hp > self.deathNum:
                if not self.invincible:
                    self.hp -= 1
                    if self.instantDeath:
                        self.hp = self.deathNum
                        self.arunHealth4.Update(0)
                        self.arunHealth3.Update(0)
                        self.arunHealth2.Update(0)
                    #endif
                #endif
                if self.hp >= 15:
                    hpNum = self.hp - 15
                    self.arunHealth4.Update(hpNum)
                elif self.hp >= 10 and self.hp < 15:
                    hpNum = self.hp - 10
                    self.arunHealth3.Update(hpNum)
                elif self.hp >= 5 and self.hp < 10:
                    hpNum = self.hp - 5
                    self.arunHealth2.Update(hpNum)
                else:
                    self.arunHealth1.Update(self.hp)
                #endif
            if self.hp == 1:
                if self.immunity:
                    self.immune = True
                    self.attacked = False
                    self.throwed = False
                    self.saMove = False
                #endif
                mehiraDefeat[0] = 0
            #endif
            if self.hp == 0:
                num = enemyCount[0]
                enemyCount[0] = num - 1
                self.death = True
                if not self.dropCoin:
                    self.dropCoin = True
                    for coin in self.coin_list:
                        coin.CoinSet(self.rect.x+30,self.rect.y+70)
                        sprite_list.add(coin)
                        coin_list.add(coin)
                    #endfor
                #endif
            #endif
            if self.hp == 10:
                self.runSpeed = 10
                self.restTime = 700
                self.throwTime = 800
                self.attackCountNum = 6
                self.random = False
                self.rest = False
                self.random2 = False
            #endif
        #endif
        if self.hp == 19:
            self.arunHealth3.rect.x = 1035
            self.arunHealth4.rect.x = 1285
        elif self.hp == 18:
            self.arunHealth3.rect.x = 1085
            self.arunHealth4.rect.x = 1335
        elif self.hp == 17:
            self.arunHealth3.rect.x = 1135
            self.arunHealth4.rect.x = 1385
        elif self.hp == 16:
            self.arunHealth3.rect.x = 1185
            self.arunHealth4.rect.x = 1435
        elif self.hp == 15:
            self.arunHealth3.rect.x = 1235
        elif self.hp == 14:
            self.arunHealth3.rect.x = 1285
        elif self.hp == 13:
            self.arunHealth3.rect.x = 1335
        elif self.hp == 12:
            self.arunHealth3.rect.x = 1385
        elif self.hp == 11:
            self.arunHealth3.rect.x = 1435
        elif self.hp == 9:
            self.arunHealth1.rect.x = 1035
            self.arunHealth2.rect.x = 1285
        elif self.hp == 8:
            self.arunHealth1.rect.x = 1085
            self.arunHealth2.rect.x = 1335
        elif self.hp == 7:
            self.arunHealth1.rect.x = 1135
            self.arunHealth2.rect.x = 1385
        elif self.hp == 6:
            self.arunHealth1.rect.x = 1185
            self.arunHealth2.rect.x = 1435
        elif self.hp == 5:
            self.arunHealth1.rect.x = 1235
        elif self.hp == 4:
            self.arunHealth1.rect.x = 1285
        elif self.hp == 3:
            self.arunHealth1.rect.x = 1335
        elif self.hp == 2:
            self.arunHealth1.rect.x = 1385
        elif self.hp == 1:
            self.arunHealth1.rect.x = 1435
        #endif
    #endmethod
    def EnemyAttackDetection(self, leftAttack_list, rightAttack_list):
        enemyGetHit1_list = pygame.sprite.spritecollide(self, leftAttack_list, False)#If get hit
        for attack in enemyGetHit1_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
        enemyGetHit2_list = pygame.sprite.spritecollide(self, rightAttack_list, False)#If get hit
        for attack in enemyGetHit2_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
    #endmethod
    def FireBallDetection(self, level_list, fireBall_list):
        enemyGetHit_list = pygame.sprite.spritecollide(self, fireBall_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
    #endmethod
    def Hurt(self):
        if self.hurt == True and not self.freeze:
            self.horiSpeed = 0
            if self.hurtCounter == 3:
                self.hurt = False
                self.hurtCounter = 0
            #endif
        #endif
    #endmethod
    def Jump(self):
        if self.freeze == False and self.attacked == False and self.death == False and not self.throwed:
            if self.jumped == False: #If player has not jumped yet
                self.jumpTime += 1
                self.vertSpeed = 19
                self.jumped = True
                self.jumpCounter = 0
                self.fallCounter = 0
            #endif
        #endif
    #endmethod
    def MoveVert(self, block_list):
        if self.freeze == False:
            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif
            if self.rect.y >= 700 and self.vertSpeed <= 0: #If sinks into the ground
                self.rect.y = 700 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False
            elif self.rect.y <= 0 and self.vertSpeed > 0:
                self.rect.y = 0
                self.vertSpeed = 0
            #endif
            self.rect.y -= self.vertSpeed #Move
            selfVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in selfVertBlock_list:
                if self.vertSpeed <= 0: #If player is falling
                    self.rect.bottom = block.rect.top
                    self.jumped = False
                elif self.vertSpeed >= 0: #If player is jumping
                    self.rect.top = block.rect.bottom
                #endif
                self.vertSpeed = 0 #Stop player
            #endfor
        #endif
    #endmethod
    def ChangeSpeed(self,num):
        if self.freeze == False and self.attacked == False and not self.death:
            if num == 0:
                self.horiSpeed = -self.runSpeed
                self.lastHoriSpeed = self.horiSpeed
            elif num == 1:
                self.horiSpeed = self.runSpeed
                self.lastHoriSpeed = self.horiSpeed
            elif num == 2:
                self.horiSpeed = 0
            #endif
        #endif
    #endmethod
    def MoveHori(self, block_list):
        if self.freeze == False:
            self.rect.x += self.horiSpeed
            for block in block_list:
                if self.rect.colliderect(block.rect): #If player hit block
                    if self.horiSpeed > 0:
                        self.rect.right = block.rect.left
                    else:
                        self.rect.left = block.rect.right
                    #endif
                #endif
            #endfor
        #endif
    #endmethod
#endclass
#Skeleton Warrior Class
class SkeletonClass(pygame.sprite.Sprite): #Class of the skeleton
    def __init__(self, x, y, levelThree_list, leftEnemyAttack_list, rightEnemyAttack_list):
        super().__init__()
        self.image = pygame.Surface([80, 120])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.originalX = x
        self.originalY = y
        self.skeletonAnimation = EnemyAnimation(9, 350, 160, self.rect.x-135, self.rect.y-35)
        self.skeletonHealth = HealthClass(1, 0, 100, 20, self.rect.x, self.rect.y - 25)
        self.skeletonAttackLeft = AttackClass(250, 120, -1000, 0)
        self.skeletonAttackRight = AttackClass(250, 120, -1000, 0)
        leftEnemyAttack_list.add(self.skeletonAttackLeft)
        rightEnemyAttack_list.add(self.skeletonAttackRight)
        levelThree_list.add(self.skeletonAnimation, self.skeletonHealth)
        #Attributes
        self.hp = 0
        self.horiSpeed = 0
        self.speed = randint(2,4)
        self.attackTime = randint(60, 90)
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = True
        self.reduceHealth = False
        self.recover = True
        self.dice = 0
        self.rest = False
        self.reviveTime = randint(8000, 12000)
        self.instantDeath = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startWalk = 0
        self.endWalk = 0
        self.startRest = 0
        self.endRest = 0
        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.recoverCounter = 0
        self.Reset()
    #endmethod
    def InstantKill(self, num):
        if num == 1:
            self.instantDeath = True
        else:
            self.instantDeath = False
        #endif
    #endmethod
    def Reset(self):
        #Attributes
        self.rect.x = self.originalX
        self.rect.y = self.originalY
        self.hp = 5
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = True
        self.reduceHealth = False
        self.recover = True
        self.rest = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startWalk = 0
        self.endWalk = 0
        self.startRest = 0
        self.endRest = 0
        #Counter
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.recoverCounter = 0
        self.skeletonHealth.Update(0)
        self.skeletonHealth.rect.x = self.rect.x - 10
        self.skeletonAttackLeft.rect.x = -1000
        self.skeletonAttackRight.rect.x = -1000
        self.Animation()
    #endmethod
    def Freeze(self, num):
        if num == 1:
            self.freeze = True
        else:
            self.freeze = False
        #endif
    #endmethod
    def Animation(self):
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        self.skeletonAnimation.rect.y = self.rect.y - 35
        self.skeletonAnimation.rect.x = self.rect.x - 135
        if self.death == False and self.freeze == False:
            if not self.hurt and self.horiSpeed == 0 and not self.attacked and not self.recover:
                if self.endAnimation - self.startAnimation >= 80: #If next image
                    self.startAnimation = self.endAnimation #If player is idle
                    self.skeletonAnimation.Idle(self.lastHoriSpeed, self.idleCounter)
                    if self.idleCounter != 6: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif
                #endif
            elif not self.hurt and self.horiSpeed != 0 and not self.attacked and not self.recover:
                if self.endAnimation - self.startAnimation >= 80:
                    self.startAnimation = self.endAnimation #If player running
                    self.skeletonAnimation.Run(self.lastHoriSpeed, self.runCounter)
                    if self.runCounter != 9: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif
                #endif
            elif self.hurt == True and not self.recover:
                if self.endAnimation - self.startAnimation >= 110:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.skeletonAnimation.Hurt(self.lastHoriSpeed, self.hurtCounter)
                    if self.hurtCounter != 2: #If reached the end
                        self.hurtCounter += 1
                    #endif
                #endif
            elif self.attacked == True and not self.hurt:
                if self.endAnimation - self.startAnimation >= self.attackTime:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.skeletonAnimation.Attack(self.lastHoriSpeed, self.attackCounter)
                    if self.attackCounter != 16: #If reached the end
                        self.attackCounter += 1
                    #endif
                #endif
        elif self.death:
            if not self.recover:
                if self.endAnimation - self.startAnimation >= 70:
                    self.startAnimation = self.endAnimation
                    self.skeletonAnimation.Death(self.lastHoriSpeed, self.deathCounter)
                    if self.deathCounter != 12:
                        self.deathCounter += 1
                    #endif
                #endif
            else:
                if self.endAnimation - self.startAnimation >= 90:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.skeletonAnimation.Recover(self.lastHoriSpeed, self.recoverCounter)
                    if self.recoverCounter != 11: #If reached the end
                        self.recoverCounter += 1
                    #endif
                #endif
            #endif
        #endif
    #endmethod
    def Control(self, x, y):
        if not self.freeze and not self.recover and not self.death:
            if not self.rest:
                if self.rect.y == y:
                    self.ChangeSpeed(2)
                    if self.rect.x - x <= 135 and self.rect.x - x > 0 and self.lastHoriSpeed < 0:
                        self.AttackTrigger()
                        if self.dice == 9:
                            self.ChangeSpeed(2)
                            self.rest = True
                        #endif
                    elif x - self.rect.x > 0 and x - self.rect.x <= 135 and self.lastHoriSpeed > 0:
                        self.AttackTrigger()
                        self.dice = randint(0,9)
                        if self.dice == 9:
                            self.ChangeSpeed(2)
                            self.rest = True
                        #endif
                    elif x <= self.rect.x and abs(x - self.rect.x) >= 135:
                        self.ChangeSpeed(0)
                    elif x > self.rect.x and abs(x - self.rect.x) >= 135:
                        self.ChangeSpeed(1)
                    #endif
                else:
                    self.ChangeSpeed(2)
                    if x <= self.rect.x and abs(x - self.rect.x) >= 135:
                        self.ChangeSpeed(0)
                    elif x > self.rect.x and abs(x - self.rect.x) >= 135:
                        self.ChangeSpeed(1)
                    #endif
                #endif
            elif self.rest:
                if self.startRest == 0: #If start timer has not started yet
                    self.startRest = pygame.time.get_ticks() #Record current time
                #endif
                self.endRest = pygame.time.get_ticks() #Record current time
                if self.endRest - self.startRest >= 3000:
                    self.rest = False
                    self.endRest = 0
                    self.startRest = 0
                #endif
            #endif
        #endif
    #endmethod
    def Health(self):
        if self.reduceHealth == True and not self.freeze:
            self.reduceHealth = False
            if self.hp > 0:
                self.hp -= 1
                if self.instantDeath:
                    self.hp = 0
                #endif
                self.skeletonHealth.Update(self.hp)
            #endif
            if self.hp == 0:
                self.death = True
                self.hurt = False
                self.horiSpeed = 0
                self.attacked = False
                self.attackCounter = 0
                self.hurtCounter = 0
                self.deathCounter = 0
                self.recoverCounter = 0
            #endif
        #endif
        if self.hp == 5:
            self.skeletonHealth.rect.x = self.rect.x - 10
        elif self.hp == 4:
            self.skeletonHealth.rect.x = self.rect.x
        elif self.hp == 3:
            self.skeletonHealth.rect.x = self.rect.x + 10
        elif self.hp == 2:
            self.skeletonHealth.rect.x = self.rect.x + 20
        elif self.hp == 1:
            self.skeletonHealth.rect.x = self.rect.x + 30
        #endif
        self.skeletonHealth.rect.y = self.rect.y - 25
    #endmethod
    def AttackTrigger(self):
        self.endAttackRest = pygame.time.get_ticks() #Get current time for end time
        if not self.freeze and self.attacked == False and self.death == False:
            self.attacked = True
            self.endAttackRest = 0
            self.startAttackRest = 0
        #endif
    #endmethod
    def Recover(self, levelThree_list, enemyCount):
        if not self.freeze:
            if self.death and not self.recover and enemyCount[0] != 0:
                if self.startDeath == 0:
                    self.startDeath = pygame.time.get_ticks() #Get current time for start time
                #endif
                self.endDeath = pygame.time.get_ticks() #Get current time for end time
                if self.endDeath - self.startDeath >= self.reviveTime:
                    self.endDeath = 0
                    self.startDeath = 0
                    self.recover = True
                    self.recoverCounter = 0
                #endif
            elif self.recover and enemyCount[0] != 0:
                if self.recoverCounter == 11:
                    self.recover = False
                    self.death = False
                    self.hp = 5
                    self.skeletonHealth.Update(5)
                    self.deathCounter = 0
                    self.recoverCounter = 0
                #endif
            #endif
            if enemyCount[0] == 0 and not self.death:
                self.death = True
                self.hurt = False
                self.horiSpeed = 0
                self.attacked = False
                self.attackCounter = 0
                self.hurtCounter = 0
                self.deathCounter = 0
                self.recoverCounter = 0
                self.hp = 0
                self.skeletonHealth.Update(self.hp)
            #endif
        #endif
    #endmethod
    def Attack(self):
        if self.attacked == True and self.freeze == False:
            self.horiSpeed = 0
            if self.attackCounter == 6 or self.attackCounter == 7:
                if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                    self.skeletonAttackRight.rect.x = self.rect.x - 35
                    self.skeletonAttackRight.rect.y = self.rect.y
                elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                    self.skeletonAttackLeft.rect.x = self.rect.x - 135
                    self.skeletonAttackLeft.rect.y = self.rect.y
                #endif
            elif self.attackCounter != 6 or self.attackCounter != 7:
                self.skeletonAttackLeft.rect.x = -1000
                self.skeletonAttackRight.rect.x = -1000
            #endif
            if self.hurt or self.death:
                self.skeletonAttackLeft.rect.x = -1000
                self.skeletonAttackRight.rect.x = -1000
            #endif
            if self.attackCounter == 16:
                self.skeletonAttackLeft.rect.x = -1000
                self.skeletonAttackRight.rect.x = -1000
                self.attacked = False
                self.attackCounter = 0
            #endif
        #endif
    #endmethod
    def EnemyAttackDetection(self, leftAttack_list, rightAttack_list):
        enemyGetHit1_list = pygame.sprite.spritecollide(self, leftAttack_list, False)#If get hit
        for attack in enemyGetHit1_list:
            if self.hurt == False and not self.death and not self.freeze and not self.recover:
                self.hurt = True
                self.reduceHealth = True
                self.skeletonAttackLeft.rect.x = -1000
                self.skeletonAttackRight.rect.x = -1000
            #endif
        #endfor
        enemyGetHit2_list = pygame.sprite.spritecollide(self, rightAttack_list, False)#If get hit
        for attack in enemyGetHit2_list:
            if self.hurt == False and not self.death and not self.freeze and not self.recover:
                self.hurt = True
                self.reduceHealth = True
                self.skeletonAttackLeft.rect.x = -1000
                self.skeletonAttackRight.rect.x = -1000
            #endif
        #endfor
    #endmethod
    def FireBallDetection(self, level_list, fireBall_list):
        enemyGetHit_list = pygame.sprite.spritecollide(self, fireBall_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
                self.skeletonAttackLeft.rect.x = -1000
                self.skeletonAttackRight.rect.x = -1000
            #endif
        #endfor
    #endmethod
    def Hurt(self):
        if self.hurt == True and not self.freeze:
            self.horiSpeed = 0
            if self.hurtCounter == 2:
                self.hurt = False
                self.hurtCounter = 0
            #endif
        #endif
    #endmethod
    def MoveVert(self, block_list):
        if self.freeze == False:
            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif
            if self.rect.y >= 680 and self.vertSpeed <= 0: #If sinks into the ground
                self.rect.y = 680 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False
            elif self.rect.y <= 0 and self.vertSpeed > 0:
                self.rect.y = 0
                self.vertSpeed = 0
            #endif
            self.rect.y -= self.vertSpeed #Move
            selfVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in selfVertBlock_list:
                if self.vertSpeed <= 0: #If player is falling
                    self.rect.bottom = block.rect.top
                    self.jumped = False
                elif self.vertSpeed >= 0: #If player is jumping
                    self.rect.top = block.rect.bottom
                #endif
                self.vertSpeed = 0 #Stop player
            #endfor
        #endif
    #endmethod
    def ChangeSpeed(self,num):
        if self.freeze == False and self.attacked == False and not self.death:
            if num == 0:
                self.horiSpeed = -self.speed
                self.lastHoriSpeed = self.horiSpeed
            elif num == 1:
                self.horiSpeed = self.speed
                self.lastHoriSpeed = self.horiSpeed
            elif num == 2:
                self.horiSpeed = 0
            #endif
        #endif
    #endmethod
    def MoveHori(self, block_list):
        if self.freeze == False:
            self.rect.x += self.horiSpeed
            for block in block_list:
                if self.rect.colliderect(block.rect): #If player hit block
                    if self.horiSpeed > 0:
                        self.rect.right = block.rect.left
                    else:
                        self.rect.left = block.rect.right
                    #endif
                #endif
            #endfor
        #endif
    #endmethod
#endclass
#Necromancer Class
class NecromancerClass(pygame.sprite.Sprite): #Class of the Necromancer
    def __init__(self, x, y, levelThree_list, leftEnemyAttack_list, rightEnemyAttack_list):
        super().__init__()
        self.image = pygame.Surface([60, 100])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.originalX = x
        self.originalY = y
        self.necroAnimation = EnemyAnimation(12, 250, 160, x-95, y-60)
        self.necroAttackAnimation = EnemyAnimation(12, 250, 200, -1000, y-100)
        self.necroAttackLeft = AttackClass(240, 150, -1000, 0)
        self.necroAttackRight = AttackClass(240, 150, -1000, 0)
        leftEnemyAttack_list.add(self.necroAttackLeft)
        rightEnemyAttack_list.add(self.necroAttackRight)
        self.necroHealth1 = HealthClass(1, 5, 250, 50, 985, 10)
        self.necroHealth2 = HealthClass(1, 5, 250, 50, 1235, 10)
        self.necroHealth3 = HealthClass(1, 5, 250, 50, 985, 65)
        self.necroHealth4 = HealthClass(1, 5, 250, 50, 1235, 65)
        levelThree_list.add(self.necroAnimation, self.necroAttackAnimation)
        #Attributes
        self.hp = 20
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.runSpeed = 10
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.spell = False
        self.shadow = False
        self.jumped = False
        self.jumpTime = 0
        self.jumpNum = 3
        self.reduceHealth = False
        self.random = False
        self.random2 = False
        self.randomTime = 700
        self.attackCount = 0
        self.skill = False
        self.stopSelf = False
        self.dropCoin = False
        self.rest = False
        self.restTime = 1000
        self.attackCountNum = 4
        self.shadowNum = 0
        self.instantDeath = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -750
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0
        self.startRandom2 = 0
        self.endRandom2 = 0
        self.startAbove = 0
        self.endAbove = 0
        self.startThrow = 0
        self.endThrow = 0
        self.startRest = 0
        self.endRest = 0
        self.startShoot = 0
        self.endShoot = 0
        self.startTimer = 0
        self.endTimer = 0
        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.spellCounter = 0
        self.fallCounter = 0
        self.jumpCounter = 0
    #endmethod
    def InstantKill(self, num):
        if num == 1:
            self.instantDeath = True
        else:
            self.instantDeath = False
        #endif
    #endmethod
    def HealthDisplay(self, num, levelThree_list):
        if num == 1:
            levelThree_list.add(self.necroHealth1, self.necroHealth2, self.necroHealth3, self.necroHealth4)
        else:
            levelThree_list.remove(self.necroHealth1, self.necroHealth2, self.necroHealth3, self.necroHealth4)
        #endif
    #endmethod
    def Freeze(self, num):
        if num == 1:
            self.freeze = True
        elif num != 1:
            self.freeze = False
        #endif
    #endmethod
    def Unrandom(self):
        self.random = False
    #endmethod
    def Reset(self):
        #Attributes
        self.hp = 20
        self.horiSpeed = 0
        self.runSpeed = 8
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.spell = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.jumped = False
        self.jumpTime = 0
        self.reduceHealth = False
        self.random = False
        self.random2 = False
        self.randomTime = 600
        self.attackCount = 0
        self.dropCoin = False
        self.stopSelf = False
        self.rest = False
        self.rect.x = self.originalX
        self.rect.y = self.originalY
        self.restTime = 1000
        self.attackCountNum = 4
        self.shadowNun = 0
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -750
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0
        self.startRandom2 = 0
        self.endRandom2 = 0
        self.startAbove = 0
        self.endAbove = 0
        self.startThrow = 0
        self.endThrow = 0
        self.startRest = 0
        self.endRest = 0
        self.startShoot = 0
        self.endShoot = 0
        self.startTimer = 0
        self.endTimer = 0
        #Counter
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.spellCounter = 0
        self.fallCounter = 0
        self.jumpCounter = 0
        self.necroAttackLeft.rect.x = -1000
        self.necroAttackRight.rect.x = -1000
        self.necroHealth1.Update(5)
        self.necroHealth2.Update(5)
        self.necroHealth3.Update(5)
        self.necroHealth4.Update(5)
        self.necroHealth1.rect.x = 985
        self.necroHealth2.rect.x = 1235
        self.necroHealth3.rect.x = 985
        self.necroHealth4.rect.x = 1235
        self.Animation()
    #endmethod
    def Animation(self):
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        if not self.attacked or self.hurt:
            if self.death == False and not self.freeze:
                self.necroAnimation.rect.y = self.rect.y - 60
                self.necroAnimation.rect.x = self.rect.x - 95
                self.necroAttackAnimation.rect.x = -1000
                if not self.hurt and self.horiSpeed == 0 and not self.attacked and not self.spell and not self.jumped:
                    if self.endAnimation - self.startAnimation >= 70: #If next image
                        self.startAnimation = self.endAnimation #If player is idle
                        self.necroAnimation.Idle(self.lastHoriSpeed, self.idleCounter)
                        if self.idleCounter != 10: #If reached the end
                            self.idleCounter += 1
                        else:
                            self.idleCounter = 0
                        #endif
                    #endif
                elif not self.hurt and self.horiSpeed != 0 and not self.attacked and not self.spell and not self.jumped:
                    if self.endAnimation - self.startAnimation >= 60:
                        self.startAnimation = self.endAnimation #If player running
                        self.necroAnimation.Run(self.lastHoriSpeed, self.runCounter)
                        if self.runCounter != 7: #If reached the end
                            self.runCounter += 1
                        else:
                            self.runCounter = 0
                        #endif
                    #endif
                elif self.hurt == True:
                    if self.endAnimation - self.startAnimation >= 75:
                        self.startAnimation = self.endAnimation #If player is hurt
                        self.necroAnimation.Hurt(self.lastHoriSpeed, self.hurtCounter)
                        if self.hurtCounter != 3: #If reached the end
                            self.hurtCounter += 1
                        #endif
                    #endif
                elif self.spell == True and not self.attacked:
                    if self.endAnimation - self.startAnimation >= 40:
                        self.startAnimation = self.endAnimation #If player is special attacking
                        self.necroAnimation.Spell(self.lastHoriSpeed, self.spellCounter)
                        if self.spellCounter != 12: #If reached the end
                            self.spellCounter += 1
                        #endif
                    #endif
                elif self.jumped == True and self.vertSpeed >= 0 and not self.hurt:
                    if self.endAnimation - self.startAnimation >= 200:
                        self.startAnimation = self.endAnimation #If player jumping
                        self.necroAnimation.Jump(self.lastHoriSpeed, self.jumpCounter)
                        if self.jumpCounter != 2: #If reached the end
                            self.jumpCounter += 1
                        else:
                            self.jumpCounter = 2 #Stay at the last frame
                        #endif
                    #endif
                elif self.jumped == True and self.vertSpeed < 0 and not self.hurt:
                    if self.endAnimation - self.startAnimation >= 200:
                        self.startAnimation = self.endAnimation #If player falling
                        self.necroAnimation.Fall(self.lastHoriSpeed, self.fallCounter)
                        if self.fallCounter != 2: #If reached the end
                            self.fallCounter += 1
                        else:
                            self.fallCounter = 2 #Stay at the last frame
                        #endif
                    #endif
                #endif
            elif self.death and not self.freeze:
                self.necroAnimation.rect.y = self.rect.y - 60
                self.necroAnimation.rect.x = self.rect.x - 95
                self.necroAttackAnimation.rect.x = -1000
                if self.endAnimation - self.startAnimation >= 70:
                    self.startAnimation = self.endAnimation
                    self.necroAnimation.Death(self.lastHoriSpeed, self.deathCounter)
                    if self.deathCounter != 13:
                        self.deathCounter += 1
                    #endif
                #endif
            #endif
        elif self.attacked == True and not self.hurt and not self.death:
            if self.endAnimation - self.startAnimation >= 45:
                self.startAnimation = self.endAnimation #If player is attacking
                self.necroAttackAnimation.Attack(self.lastHoriSpeed, self.attackCounter)
                self.necroAttackAnimation.rect.x = self.rect.x - 95
                self.necroAttackAnimation.rect.y = self.rect.y - 100
                self.necroAnimation.rect.x = -1000
                if self.attackCounter != 14: #If reached the end
                    self.attackCounter += 1
                #endif
            #endif
        #endif
    #endmethod
    def AttackTrigger(self):
        self.endAttackRest = pygame.time.get_ticks() #Get current time for end time
        if not self.freeze and self.attacked == False and self.jumped == False and self.death == False and self.endAttackRest - self.startAttackRest >= 500:
            self.attacked = True
            self.endAttackRest = 0
            self.startAttackRest = 0
        #endif
    #endmethod
    def AttackChecker(self):
        if self.stopSelf: #If the enemy should stop
            self.stopSelf = False
            self.horiSpeed = 0
        #endif
    #endmethod
    def Attack(self):
        if self.attacked == True and self.freeze == False:
            self.horiSpeed = 0
            if self.attackCounter == 7 or self.attackCounter == 8:
                if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                    self.necroAttackRight.rect.x = self.rect.x - 90
                    self.necroAttackRight.rect.y = self.rect.y - 50
                elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                    self.necroAttackLeft.rect.x = self.rect.x - 90
                    self.necroAttackLeft.rect.y = self.rect.y - 50
                #endif
            elif self.attackCounter != 7 or self.attackCounter != 8:
                self.necroAttackLeft.rect.x = -1000
                self.necroAttackRight.rect.x = -1000
            #endif
            if self.hurt or self.death:
                self.necroAttackLeft.rect.x = -1000
                self.necroAttackRight.rect.x = -1000
            #endif
            if self.attackCounter == 14:
                self.necroAttackLeft.rect.x = -1000
                self.necroAttackRight.rect.x = -1000
                self.attacked = False
                self.attackCounter = 0
                self.attackCount += 1
                if self.attackCount >= self.attackCountNum:
                    self.attackCount = 0
                    self.rest = True
                #endif
            #endif
        #endif
    #endmethod
    def Control(self, x, y):
        if not self.freeze and not self.death:
            if not self.random and not self.random2 and not self.skill and not self.freeze and not self.attacked and not self.rest and not self.spell:
                if self.rect.y == y:
                    self.ChangeSpeed(2)
                    if self.rect.x - x <= 90 and self.rect.x - x > 0 and self.lastHoriSpeed < 0:
                        self.AttackTrigger()
                    elif x - self.rect.x > 0 and x - self.rect.x <= 90 and self.lastHoriSpeed > 0:
                        self.AttackTrigger()
                    elif x <= self.rect.x and abs(x - self.rect.x) >= 90:
                        self.ChangeSpeed(0)
                    elif x > self.rect.x and abs(x - self.rect.x) >= 90:
                        self.ChangeSpeed(1)
                    #endif
                elif y > self.rect.y:
                    self.ChangeSpeed(2)
                    if self.startAbove == 0: #If start timer has not started yet
                        self.startAbove = pygame.time.get_ticks() #Record current time
                    #endif
                    self.endAbove = pygame.time.get_ticks()
                    if self.endAbove - self.startAbove >= 800:
                        self.random2 = True
                        self.startAbove = 0
                        self.endAbove = 0
                    #endif
                    if x <= self.rect.x and abs(x - self.rect.x) >= 80:
                        self.ChangeSpeed(0)
                    elif x > self.rect.x and abs(x - self.rect.x) >= 80:
                        self.ChangeSpeed(1)
                    #endif
                elif y < self.rect.y:
                    self.startAbove = 0
                    self.endAbove = 0
                    self.ChangeSpeed(2)
                    if x <= self.rect.x and abs(x - self.rect.x) >= 80:
                        self.ChangeSpeed(0)
                    elif x > self.rect.x and abs(x - self.rect.x) >= 80:
                        self.ChangeSpeed(1)
                    #endif
                    self.Jump()
                    if self.jumpTime > self.jumpNum:
                        self.random = True
                    #endif
                #endif
                if self.startTimer == 0: #If start timer has not started yet
                    self.startTimer = pygame.time.get_ticks() #Record current time
                #endif
                self.endTimer = pygame.time.get_ticks()
                if self.endTimer - self.startTimer >= 7500:
                    self.skill = True
                    self.startTimer = 0
                    self.endTimer = 0
                #endif
            elif self.random and not self.random2 and not self.skill and not self.freeze and not self.rest and not self.death:
                if self.startRandom == 0: #If start timer has not started yet
                    self.startRandom = pygame.time.get_ticks() #Record current time
                    self.ChangeSpeed(randint(0,1))
                #endif
                self.endRandom = pygame.time.get_ticks()
                if self.endRandom - self.startRandom > 400:
                    self.startRandom = 0
                    self.endRandom = 0
                    self.random = False
                    self.rest = False
                    self.random2 = False
                #endif
            elif self.random2 and not self.freeze and not self.rest and not self.death:
                if self.startRandom2 == 0: #If start timer has not started yet
                    self.startRandom2 = pygame.time.get_ticks() #Record current time
                    self.ChangeSpeed(randint(0,1))
                #endif
                self.endRandom2 = pygame.time.get_ticks()
                if self.endRandom2 - self.startRandom2 > self.randomTime:
                    self.startRandom2 = 0
                    self.endRandom2 = 0
                    self.random2 = False
                    self.rest = False
                    self.random = False
                #endif
            elif self.rest and not self.freeze and not self.random and not self.random2 and not self.death:
                if self.startRest == 0: #If start timer has not started yet
                    self.startRest = pygame.time.get_ticks() #Record current time
                #endif
                self.endRest = pygame.time.get_ticks()
                if self.endRest - self.startRest >= self.restTime:
                    self.startRest = 0
                    self.endRest = 0
                    self.rest = False
                    self.random2 = False
                    self.random = False
                #endif
            #endif
            if self.skill and not self.freeze and not self.rest and not self.death:
                self.ChangeSpeed(2)
                self.SpellTrigger()
            #endif
        #endif
        if self.rect.x <= 0: #If player reach the end of screen
            self.rect.x = 0
        elif self.rect.x >= 1450:
            self.rect.x = 1450
        #endif
    #endmethod
    def SpellTrigger(self):
        if not self.attacked and not self.hurt and not self.death and not self.freeze and not self.shadow and not self.spell:
            self.spell = True
        #endif
    #endmethod
    def Spell(self, playerX, playerY, levelThree_list, shadowBolt_list):
        if self.spell and not self.freeze:
            if self.spellCounter == 12:
                self.spellCounter = 0
                self.shadow = True
                self.spell = False
                self.skill = False
                self.random = False
                self.rest = False
                self.random2 = False
            #endif
        #endif
        if self.shadow:
            if self.startShoot == 0: #If start timer has not started yet
                self.startShoot = pygame.time.get_ticks() #Record current time
            #endif
            self.endShoot = pygame.time.get_ticks() #Record current time
            if self.endShoot - self.startShoot >= 400:
                self.endShoot = 0
                self.startShoot = 0
                effect = EffectClass(1, 731, -160, playerX, playerY, levelThree_list)
                shadowBolt_list.add(effect)
                self.shadowNum += 1
                if self.shadowNum == 12:
                    self.shadow = False
                    self.shadowNum = 0
                #endif
            #endif
        #endif
    #endmethod
    def Health(self, sprite_list, coin_list, enemyCount):
        if self.reduceHealth == True and not self.freeze:
            self.reduceHealth = False
            if self.hp > 0:
                self.hp -= 1
                if self.instantDeath:
                    self.hp = 0
                    self.necroHealth4.Update(0)
                    self.necroHealth3.Update(0)
                    self.necroHealth2.Update(0)
                #endif
                if self.hp >= 15:
                    hpNum = self.hp - 15
                    self.necroHealth4.Update(hpNum)
                elif self.hp >= 10 and self.hp < 15:
                    hpNum = self.hp - 10
                    self.necroHealth3.Update(hpNum)
                elif self.hp >= 5 and self.hp < 10:
                    hpNum = self.hp - 5
                    self.necroHealth2.Update(hpNum)
                else:
                    self.necroHealth1.Update(self.hp)
                #endif
            if self.hp == 0:
                num = enemyCount[0]
                enemyCount[0] = num - 1
                self.death = True
            #endif
            if self.hp == 11:
                self.runSpeed = 10
                self.restTime = 700
                self.attackCountNum = 6
                self.random = False
                self.rest = False
                self.random2 = False
            #endif
        #endif
        if self.hp == 19:
            self.necroHealth3.rect.x = 1035
            self.necroHealth4.rect.x = 1285
        elif self.hp == 18:
            self.necroHealth3.rect.x = 1085
            self.necroHealth4.rect.x = 1335
        elif self.hp == 17:
            self.necroHealth3.rect.x = 1135
            self.necroHealth4.rect.x = 1385
        elif self.hp == 16:
            self.necroHealth3.rect.x = 1185
            self.necroHealth4.rect.x = 1435
        elif self.hp == 15:
            self.necroHealth3.rect.x = 1235
        elif self.hp == 14:
            self.necroHealth3.rect.x = 1285
        elif self.hp == 13:
            self.necroHealth3.rect.x = 1335
        elif self.hp == 12:
            self.necroHealth3.rect.x = 1385
        elif self.hp == 11:
            self.necroHealth3.rect.x = 1435
        elif self.hp == 9:
            self.necroHealth1.rect.x = 1035
            self.necroHealth2.rect.x = 1285
        elif self.hp == 8:
            self.necroHealth1.rect.x = 1085
            self.necroHealth2.rect.x = 1335
        elif self.hp == 7:
            self.necroHealth1.rect.x = 1135
            self.necroHealth2.rect.x = 1385
        elif self.hp == 6:
            self.necroHealth1.rect.x = 1185
            self.necroHealth2.rect.x = 1435
        elif self.hp == 5:
            self.necroHealth1.rect.x = 1235
        elif self.hp == 4:
            self.necroHealth1.rect.x = 1285
        elif self.hp == 3:
            self.necroHealth1.rect.x = 1335
        elif self.hp == 2:
            self.necroHealth1.rect.x = 1385
        elif self.hp == 1:
            self.necroHealth1.rect.x = 1435
        #endif
    #endmethod
    def EnemyAttackDetection(self, leftAttack_list, rightAttack_list):
        enemyGetHit1_list = pygame.sprite.spritecollide(self, leftAttack_list, False)#If get hit
        for attack in enemyGetHit1_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
        enemyGetHit2_list = pygame.sprite.spritecollide(self, rightAttack_list, False)#If get hit
        for attack in enemyGetHit2_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
    #endmethod
    def FireBallDetection(self, level_list, fireBall_list):
        enemyGetHit_list = pygame.sprite.spritecollide(self, fireBall_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
    #endmethod
    def Hurt(self):
        if self.hurt == True and not self.freeze:
            self.horiSpeed = 0
            if self.hurtCounter == 3:
                self.hurt = False
                self.hurtCounter = 0
            #endif
        #endif
    #endmethod
    def Jump(self):
        if self.freeze == False and self.attacked == False and self.death == False and not self.skill:
            if self.jumped == False: #If player has not jumped yet
                self.jumpTime += 1
                self.vertSpeed = 19
                self.jumped = True
                self.jumpCounter = 0
                self.fallCounter = 0
            #endif
        #endif
    #endmethod
    def MoveVert(self, block_list):
        if self.freeze == False:
            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif
            if self.rect.y >= 700 and self.vertSpeed <= 0: #If sinks into the ground
                self.rect.y = 700 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False
            elif self.rect.y <= 0 and self.vertSpeed > 0:
                self.rect.y = 0
                self.vertSpeed = 0
            #endif
            self.rect.y -= self.vertSpeed #Move
            selfVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in selfVertBlock_list:
                if self.vertSpeed <= 0: #If player is falling
                    self.rect.bottom = block.rect.top
                    self.jumped = False
                elif self.vertSpeed >= 0: #If player is jumping
                    self.rect.top = block.rect.bottom
                #endif
                self.vertSpeed = 0 #Stop player
            #endfor
        #endif
    #endmethod
    def ChangeSpeed(self,num):
        if self.freeze == False and self.attacked == False and not self.death:
            if num == 0:
                self.horiSpeed = -self.runSpeed
                self.lastHoriSpeed = self.horiSpeed
            elif num == 1:
                self.horiSpeed = self.runSpeed
                self.lastHoriSpeed = self.horiSpeed
            elif num == 2:
                self.horiSpeed = 0
            #endif
        #endif
    #endmethod
    def MoveHori(self, block_list):
        if self.freeze == False:
            self.rect.x += self.horiSpeed
            for block in block_list:
                if self.rect.colliderect(block.rect): #If player hit block
                    if self.horiSpeed > 0:
                        self.rect.right = block.rect.left
                    else:
                        self.rect.left = block.rect.right
                    #endif
                #endif
            #endfor
        #endif
    #endmethod
#endclass
#Abomination Class
class AbominationClass(pygame.sprite.Sprite): #Class of the Abomination AKA The King
    def __init__(self, x, y, levelThree_list, leftEnemyAttack_list, rightEnemyAttack_list):
        super().__init__()
        self.image = pygame.Surface([250, 236])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.originalX = x
        self.originalY = y
        self.kingAnimation = EnemyAnimation(11, 450, 450, x-100, y-207)
        self.kingAttackLeft = AttackClass(210, 300, -1000, 0)
        self.kingAttackRight = AttackClass(210, 300, -1000, 0)
        leftEnemyAttack_list.add(self.kingAttackLeft)
        rightEnemyAttack_list.add(self.kingAttackRight)
        self.kingHealth1 = HealthClass(1, 5, 250, 50, 985, 10)
        self.kingHealth2 = HealthClass(1, 5, 250, 50, 1235, 10)
        self.kingHealth3 = HealthClass(1, 5, 250, 50, 985, 65)
        self.kingHealth4 = HealthClass(1, 5, 250, 50, 1235, 65)
        self.kingHealth5 = HealthClass(1, 5, 250, 50, 985, 120)
        self.kingHealth6 = HealthClass(1, 5, 250, 50, 1235, 120)
        self.kingHealth7 = HealthClass(1, 5, 250, 50, 985, 175)
        self.kingHealth8 = HealthClass(1, 5, 250, 50, 1235, 175)
        levelThree_list.add(self.kingAnimation)
        #Attributes
        self.actualHp = 200
        self.hp = self.actualHp / 5
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.runSpeed = 8
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.reduceHealth = False
        self.random = False
        self.random2 = False
        self.randomTime = 700
        self.attackCount = 0
        self.stopSelf = False
        self.dropCoin = False
        self.rest = False
        self.restTime = 400
        self.attackCountNum = 8
        self.reduceTwice = False
        self.immune = False
        self.instantDeath = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -750
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startAbove = 0
        self.endAbove = 0
        self.startThrow = 0
        self.endThrow = 0
        self.startRest = 0
        self.endRest = 0
        self.startShoot = 0
        self.endShoot = 0
        self.startTimer = 0
        self.endTimer = 0
        self.startImmune = 0
        self.endImmune = 0
        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
    #endmethod
    def InstantKill(self, num):
        if num == 1:
            self.instantDeath = True
        else:
            self.instantDeath = False
        #endif
    #endmethod
    def HealthDisplay(self, num, levelThree_list):
        if num == 1:
            levelThree_list.add(self.kingHealth1, self.kingHealth2, self.kingHealth3, self.kingHealth4, self.kingHealth5, self.kingHealth6, self.kingHealth7, self.kingHealth8)
        else:
            levelThree_list.remove(self.kingHealth1, self.kingHealth2, self.kingHealth3, self.kingHealth4, self.kingHealth5, self.kingHealth6, self.kingHealth7, self.kingHealth8)
        #endif
    #endmethod
    def Freeze(self, num):
        if num == 1:
            self.freeze = True
        elif num != 1:
            self.freeze = False
        #endif
    #endmethod
    def Unrandom(self):
        self.random = False
    #endmethod
    def Reset(self):
        #Attributes
        self.actualHp = 200
        self.hp = 40
        self.horiSpeed = 0
        self.runSpeed = 8
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.reduceHealth = False
        self.random = False
        self.random2 = False
        self.randomTime = 600
        self.attackCount = 0
        self.dropCoin = False
        self.stopSelf = False
        self.rest = False
        self.rect.x = self.originalX
        self.rect.y = self.originalY
        self.restTime = 400
        self.attackCountNum = 8
        self.reduceTwice = False
        self.immune = False
        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -750
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0
        self.startRandom2 = 0
        self.endRandom2 = 0
        self.startAbove = 0
        self.endAbove = 0
        self.startThrow = 0
        self.endThrow = 0
        self.startRest = 0
        self.endRest = 0
        self.startShoot = 0
        self.endShoot = 0
        self.startTimer = 0
        self.endTimer = 0
        self.startImmune = 0
        self.endImmune = 0
        #Counter
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.kingAttackLeft.rect.x = -1000
        self.kingAttackRight.rect.x = -1000
        self.kingHealth1.Update(5)
        self.kingHealth2.Update(5)
        self.kingHealth3.Update(5)
        self.kingHealth4.Update(5)
        self.kingHealth5.Update(5)
        self.kingHealth6.Update(5)
        self.kingHealth7.Update(5)
        self.kingHealth8.Update(5)
        self.kingHealth1.rect.x = 985
        self.kingHealth2.rect.x = 1235
        self.kingHealth3.rect.x = 985
        self.kingHealth4.rect.x = 1235
        self.kingHealth5.rect.x = 985
        self.kingHealth6.rect.x = 1235
        self.kingHealth7.rect.x = 985
        self.kingHealth8.rect.x = 1235
        self.Animation()
    #endmethod
    def Animation(self):
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        self.kingAnimation.rect.y = self.rect.y - 207
        self.kingAnimation.rect.x = self.rect.x - 100
        if not self.death and not self.freeze:
            if not self.hurt and self.horiSpeed == 0 and not self.attacked:
                if self.endAnimation - self.startAnimation >= 110: #If next image
                    self.startAnimation = self.endAnimation #If player is idle
                    self.kingAnimation.Idle(self.lastHoriSpeed, self.idleCounter)
                    if self.idleCounter != 5: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif
                #endif
            elif not self.hurt and self.horiSpeed != 0 and not self.attacked:
                if self.endAnimation - self.startAnimation >= 50:
                    self.startAnimation = self.endAnimation #If player running
                    self.kingAnimation.Run(self.lastHoriSpeed, self.runCounter)
                    if self.runCounter != 7: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif
                #endif
            elif self.hurt == True:
                if self.endAnimation - self.startAnimation >= 80:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.kingAnimation.Hurt(self.lastHoriSpeed, self.hurtCounter)
                    if self.hurtCounter != 3: #If reached the end
                        self.hurtCounter += 1
                    #endif
                #endif
            elif self.attacked and not self.hurt:
                if self.endAnimation - self.startAnimation >= 60:
                    self.startAnimation = self.endAnimation #If player is hurt
                    self.kingAnimation.Attack(self.lastHoriSpeed, self.attackCounter)
                    if self.attackCounter != 13: #If reached the end
                        self.attackCounter += 1
                    #endif
                #endif
            #endif
        elif self.death:
            if self.endAnimation - self.startAnimation >= 100:
                self.startAnimation = self.endAnimation
                self.kingAnimation.Death(self.lastHoriSpeed, self.deathCounter)
                if self.deathCounter != 9:
                    self.deathCounter += 1
                #endif
            #endif
        #endif
    #endmethod
    def AttackTrigger(self):
        self.endAttackRest = pygame.time.get_ticks() #Get current time for end time
        if not self.freeze and self.attacked == False and self.death == False and self.endAttackRest - self.startAttackRest >= 200:
            self.attacked = True
            self.endAttackRest = 0
            self.startAttackRest = 0
        #endif
    #endmethod
    def AttackChecker(self):
        if self.stopSelf: #If the enemy should stop
            self.stopSelf = False
            self.horiSpeed = 0
        #endif
    #endmethod
    def Attack(self):
        if self.attacked == True and self.freeze == False:
            self.horiSpeed = 0
            if self.attackCounter == 7 or self.attackCounter == 8:
                if self.lastHoriSpeed > 0 and not self.death:
                    self.kingAttackRight.rect.x = self.rect.x + 125
                    self.kingAttackRight.rect.y = self.rect.y - 64
                elif self.lastHoriSpeed < 0 and not self.death:
                    self.kingAttackLeft.rect.x = self.rect.x - 85
                    self.kingAttackLeft.rect.y = self.rect.y - 64
                #endif
            elif self.attackCounter != 7 or self.attackCounter != 8:
                self.kingAttackLeft.rect.x = -1000
                self.kingAttackRight.rect.x = -1000
            #endif
            if self.death:
                self.kingAttackLeft.rect.x = -1000
                self.kingAttackRight.rect.x = -1000
                self.attacked = False
                self.attackCounter = 0
            #endif
            if self.attackCounter == 13:
                self.kingAttackLeft.rect.x = -1000
                self.kingAttackRight.rect.x = -1000
                self.attacked = False
                self.attackCounter = 0
                self.attackCount += 1
                if self.attackCount >= self.attackCountNum:
                    self.attackCount = 0
                    self.rest = True
                #endif
            #endif
        #endif
    #endmethod
    def Control(self, x):
        if not self.freeze and not self.death:
            if not self.freeze and not self.attacked and not self.rest:
                self.ChangeSpeed(2)
                if self.rect.x - x <= 40 and self.rect.x - x > 0 and self.lastHoriSpeed < 0:
                    self.AttackTrigger()
                elif x - self.rect.x > 0 and x - self.rect.x <= 290 and self.lastHoriSpeed > 0:
                    self.AttackTrigger()
                elif x <= self.rect.x:
                    self.ChangeSpeed(0)
                elif x > self.rect.x:
                    self.ChangeSpeed(1)
                #endif
            elif not self.freeze and not self.attacked and self.rest:
                if self.startTimer == 0: #If start timer has not started yet
                    self.startTimer = pygame.time.get_ticks() #Record current time
                #endif
                self.endTimer = pygame.time.get_ticks() #Get current time for end time
                if self.endTimer - self.startTimer >= 500:
                    self.rest = False
                    self.startTimer = 0
                    self.endTimer = 0
                #endif
            #endif
        #endif
        if self.rect.x <= 0: #If player reach the end of screen
            self.rect.x = 0
        elif self.rect.x >= 1250:
            self.rect.x = 1250
        #endif
    #endmethod
    def Health(self, sprite_list, coin_list, enemyCount):
        if self.reduceHealth == True and not self.freeze:
            self.reduceHealth = False
            if self.actualHp > 0:
                self.actualHp -= 1
                if self.instantDeath:
                    self.actualHp = 0
                    self.kingHealth8.Update(0)
                    self.kingHealth7.Update(0)
                    self.kingHealth6.Update(0)
                    self.kingHealth5.Update(0)
                    self.kingHealth4.Update(0)
                    self.kingHealth3.Update(0)
                    self.kingHealth2.Update(0)
                #endif
                if self.actualHp % 5 == 0:
                    self.hp = int(self.actualHp / 5)
                    if self.hp >= 35:
                        hpNum = self.hp - 35
                        self.kingHealth8.Update(hpNum)
                    elif self.hp >= 30 and self.hp < 35:
                        hpNum = self.hp - 30
                        self.kingHealth7.Update(hpNum)
                    elif self.hp >= 25 and self.hp < 30:
                        hpNum = self.hp - 25
                        self.kingHealth6.Update(hpNum)
                    elif self.hp >= 20 and self.hp < 25:
                        hpNum = self.hp - 20
                        self.kingHealth5.Update(hpNum)
                    elif self.hp >= 15 and self.hp < 20:
                        hpNum = self.hp - 15
                        self.kingHealth4.Update(hpNum)
                    elif self.hp >= 10 and self.hp < 15:
                        hpNum = self.hp - 10
                        self.kingHealth3.Update(hpNum)
                    elif self.hp >= 5 and self.hp < 10:
                        hpNum = self.hp - 5
                        self.kingHealth2.Update(hpNum)
                    elif self.hp < 5:
                        self.kingHealth1.Update(self.hp)
                    #endif
                #endif
                if self.reduceTwice and self.actualHp > 0:
                    self.actualHp -= 1
                    self.reduceTwice = False
                    if self.actualHp % 5 == 0:
                        self.hp = int(self.actualHp / 5)
                        if self.hp >= 35:
                            hpNum = self.hp - 35
                            self.kingHealth8.Update(hpNum)
                        elif self.hp >= 30 and self.hp < 35:
                            hpNum = self.hp - 30
                            self.kingHealth7.Update(hpNum)
                        elif self.hp >= 25 and self.hp < 30:
                            hpNum = self.hp - 25
                            self.kingHealth6.Update(hpNum)
                        elif self.hp >= 20 and self.hp < 25:
                            hpNum = self.hp - 20
                            self.kingHealth5.Update(hpNum)
                        elif self.hp >= 15 and self.hp < 20:
                            hpNum = self.hp - 15
                            self.kingHealth4.Update(hpNum)
                        elif self.hp >= 10 and self.hp < 15:
                            hpNum = self.hp - 10
                            self.kingHealth3.Update(hpNum)
                        elif self.hp >= 5 and self.hp < 10:
                            hpNum = self.hp - 5
                            self.kingHealth2.Update(hpNum)
                        elif self.hp < 5:
                            self.kingHealth1.Update(self.hp)
                        #endif
                    #endif
                #endif
            #endif
            if self.hp == 0:
                num = enemyCount[0]
                enemyCount[0] = num - 1
                self.death = True
                self.horiSpeed = 0
            #endif
            if self.hp == 20:
                self.runSpeed = 10
                self.restTime = 200
                self.attackCountNum = 12
                self.random = False
                self.rest = False
                self.random2 = False
            #endif
        #endif
        if self.hp == 39:
            self.kingHealth7.rect.x = 1035
            self.kingHealth8.rect.x = 1285
        elif self.hp == 38:
            self.kingHealth7.rect.x = 1085
            self.kingHealth8.rect.x = 1335
        elif self.hp == 37:
            self.kingHealth7.rect.x = 1135
            self.kingHealth8.rect.x = 1385
        elif self.hp == 36:
            self.kingHealth7.rect.x = 1185
            self.kingHealth8.rect.x = 1435
        elif self.hp == 35:
            self.kingHealth7.rect.x = 1235
        elif self.hp == 34:
            self.kingHealth7.rect.x = 1285
        elif self.hp == 33:
            self.kingHealth7.rect.x = 1335
        elif self.hp == 32:
            self.kingHealth7.rect.x = 1385
        elif self.hp == 31:
            self.kingHealth7.rect.x = 1435
        elif self.hp == 29:
            self.kingHealth5.rect.x = 1035
            self.kingHealth6.rect.x = 1285
        elif self.hp == 28:
            self.kingHealth5.rect.x = 1085
            self.kingHealth6.rect.x = 1335
        elif self.hp == 27:
            self.kingHealth5.rect.x = 1135
            self.kingHealth6.rect.x = 1385
        elif self.hp == 26:
            self.kingHealth5.rect.x = 1185
            self.kingHealth6.rect.x = 1435
        elif self.hp == 25:
            self.kingHealth5.rect.x = 1235
        elif self.hp == 24:
            self.kingHealth5.rect.x = 1285
        elif self.hp == 23:
            self.kingHealth5.rect.x = 1335
        elif self.hp == 22:
            self.kingHealth5.rect.x = 1385
        elif self.hp == 21:
            self.kingHealth5.rect.x = 1435
        elif self.hp == 19:
            self.kingHealth3.rect.x = 1035
            self.kingHealth4.rect.x = 1285
        elif self.hp == 18:
            self.kingHealth3.rect.x = 1085
            self.kingHealth4.rect.x = 1335
        elif self.hp == 17:
            self.kingHealth3.rect.x = 1135
            self.kingHealth4.rect.x = 1385
        elif self.hp == 16:
            self.kingHealth3.rect.x = 1185
            self.kingHealth4.rect.x = 1435
        elif self.hp == 15:
            self.kingHealth3.rect.x = 1235
        elif self.hp == 14:
            self.kingHealth3.rect.x = 1285
        elif self.hp == 13:
            self.kingHealth3.rect.x = 1335
        elif self.hp == 12:
            self.kingHealth3.rect.x = 1385
        elif self.hp == 11:
            self.kingHealth3.rect.x = 1435
        elif self.hp == 9:
            self.kingHealth1.rect.x = 1035
            self.kingHealth2.rect.x = 1285
        elif self.hp == 8:
            self.kingHealth1.rect.x = 1085
            self.kingHealth2.rect.x = 1335
        elif self.hp == 7:
            self.kingHealth1.rect.x = 1135
            self.kingHealth2.rect.x = 1385
        elif self.hp == 6:
            self.kingHealth1.rect.x = 1185
            self.kingHealth2.rect.x = 1435
        elif self.hp == 5:
            self.kingHealth1.rect.x = 1235
        elif self.hp == 4:
            self.kingHealth1.rect.x = 1285
        elif self.hp == 3:
            self.kingHealth1.rect.x = 1335
        elif self.hp == 2:
            self.kingHealth1.rect.x = 1385
        elif self.hp == 1:
            self.kingHealth1.rect.x = 1435
        #endif
    #endmethod
    def EnemyAttackDetection(self, leftAttack_list, rightAttack_list):
        enemyGetHit1_list = pygame.sprite.spritecollide(self, leftAttack_list, False)#If get hit
        for attack in enemyGetHit1_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
        enemyGetHit2_list = pygame.sprite.spritecollide(self, rightAttack_list, False)#If get hit
        for attack in enemyGetHit2_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
    #endmethod
    def TaleneAttackDetection(self, taleneAttack_list):
        enemyGetHit_list = pygame.sprite.spritecollide(self, taleneAttack_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
                self.reduceTwice = True
            #endif
        #endfor
    #endmethod
    def FireBallDetection(self, level_list, fireBall_list):
        enemyGetHit_list = pygame.sprite.spritecollide(self, fireBall_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor
    #endmethod
    def JavelinAttackDetection(self, leftJavelin_list, rightJavelin_list, levelThree_list):
        enemyGetHit_list = pygame.sprite.spritecollide(self, leftJavelin_list, False)#If get hit
        for javelin in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
                levelThree_list.remove(javelin)
                leftJavelin_list.remove(javelin)
            #endif
        #endfor
        enemyGetHit_list = pygame.sprite.spritecollide(self, rightJavelin_list, False)#If get hit
        for javelin in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
                levelThree_list.remove(javelin)
                rightJavelin_list.remove(javelin)
            #endif
        #endfor
    #endmethod
    def Hurt(self):
        if self.hurt and not self.freeze and not self.death:
            if self.hurtCounter == 3:
                self.hurt = False
                self.hurtCounter = 0
            #endif
        #endif
    #endmethod
    def MoveVert(self, block_list):
        if self.freeze == False:
            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif
            if self.rect.y >= 565 and self.vertSpeed <= 0: #If sinks into the ground
                self.rect.y = 565 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False
            elif self.rect.y <= 0 and self.vertSpeed > 0:
                self.rect.y = 0
                self.vertSpeed = 0
            #endif
            self.rect.y -= self.vertSpeed #Move
            selfVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in selfVertBlock_list:
                if self.vertSpeed <= 0: #If player is falling
                    self.rect.bottom = block.rect.top
                    self.jumped = False
                elif self.vertSpeed >= 0: #If player is jumping
                    self.rect.top = block.rect.bottom
                #endif
                self.vertSpeed = 0 #Stop player
            #endfor
        #endif
    #endmethod
    def ChangeSpeed(self,num):
        if self.freeze == False and self.attacked == False and not self.death:
            if num == 0:
                self.horiSpeed = -self.runSpeed
                self.lastHoriSpeed = self.horiSpeed
            elif num == 1:
                self.horiSpeed = self.runSpeed
                self.lastHoriSpeed = self.horiSpeed
            elif num == 2:
                self.horiSpeed = 0
            #endif
        #endif
    #endmethod
    def MoveHori(self, block_list):
        if self.freeze == False:
            self.rect.x += self.horiSpeed
            for block in block_list:
                if self.rect.colliderect(block.rect): #If player hit block
                    if self.horiSpeed > 0:
                        self.rect.right = block.rect.left
                    else:
                        self.rect.left = block.rect.right
                    #endif
                #endif
            #endfor
        #endif
    #endmethod
#endclass
#Enemy Animation Class
class EnemyAnimation(pygame.sprite.Sprite): #Class of player's animation
    def __init__(self, enemyType, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x #Set pos
        self.rect.y = y
        self.enemy = enemyType
        #Animation
        #Light Bandit
        self.banditIdle1 = [] #Idle
        for x in range(4):
            add_str = str(x+1)
            self.banditIdle1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditIdle" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditAdle1 = [] #Attack Idle
        for x in range(4):
            add_str = str(x+1)
            self.banditAdle1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditAdle" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditRun1 = [] #Run
        for x in range(8):
            add_str = str(x+1)
            self.banditRun1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditRun" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditJump1 = [] #Jump
        for x in range(1):
            add_str = str(x+1)
            self.banditJump1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditJump" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditAttack1 = [] #Attack 1
        for x in range(8):
            add_str = str(x+1)
            self.banditAttack1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditAttack" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditHurt1 = [] #Hurt 1
        for x in range(3):
            add_str = str(x+1)
            self.banditHurt1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditHurt" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditDeath1 = [] #Death 1
        for x in range(1):
            self.banditDeath1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditDeath" + str(1) + ".png"), (130, 130)))
        #endfor
        self.banditRecover1 = [] #Recover 1
        for x in range(8):
            add_str = str(x+1)
            self.banditRecover1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditRecover" + add_str + ".png"), (130, 130)))
        #endfor
        #Heavy Bandit
        self.banditIdle2 = [] #Idle
        for x in range(4):
            add_str = str(x)
            self.banditIdle2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Idle/HeavyBandit_Idle_" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditAdle2 = [] #Attack Idle
        for x in range(4):
            add_str = str(x)
            self.banditAdle2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Adle/HeavyBandit_CombatIdle_" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditRun2 = [] #Run
        for x in range(8):
            add_str = str(x)
            self.banditRun2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Run/HeavyBandit_Run_" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditJump2 = [] #Jump
        for x in range(1):
            add_str = str(x)
            self.banditJump2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Jump/HeavyBandit_Jump_0.png"), (130, 130)))
        #endfor
        self.banditAttack2 = [] #Attack 2
        for x in range(8):
            add_str = str(x)
            self.banditAttack2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Attack/HeavyBandit_Attack_" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditHurt2 = [] #Hurt 2
        for x in range(3):
            add_str = str(x)
            self.banditHurt2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Hurt/HeavyBandit_Hurt_" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditDeath2 = [] #Death 2
        for x in range(1):
            self.banditDeath2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Death/HeavyBandit_Death_0.png"), (130, 130)))
        #endfor
        self.banditRecover2 = [] #Recover 2
        for x in range(8):
            add_str = str(x)
            self.banditRecover2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Recover/HeavyBandit_Recover_" + add_str + ".png"), (130, 130)))
        #endfor
        #Mushrooms
        #Red
        self.mushroomIdle1 = [] #Idle
        for x in range(8):
            add_str = str(x)
            self.mushroomIdle1.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Red/Idle/MushroomRed_Idle_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomAttack1 = [] #Attack
        for x in range(16):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.mushroomAttack1.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Red/Attack/MushroomRed_Attack_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomDeath1 = [] #Death
        for x in range(11):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.mushroomDeath1.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Red/Death/MushroomRed_Death_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomRun1 = [] #Run
        for x in range(8):
            add_str = str(x)
            self.mushroomRun1.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Red/Walk/MushroomRed_Walk_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomHurt1 = [] #Hurt
        for x in range(3):
            add_str = str(x)
            self.mushroomHurt1.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Red/Hurt/MushroomRed_Hurt_" + add_str + ".png"), (200, 160)))
        #endfor
        #Orange
        self.mushroomIdle2 = [] #Idle
        for x in range(8):
            add_str = str(x)
            self.mushroomIdle2.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Orange/Idle/MushroomOrange_Idle_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomAttack2 = [] #Attack
        for x in range(16):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.mushroomAttack2.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Orange/Attack/MushroomOrange_Attack_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomDeath2 = [] #Death
        for x in range(11):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.mushroomDeath2.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Orange/Death/MushroomOrange_Death_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomRun2 = [] #Run
        for x in range(8):
            add_str = str(x)
            self.mushroomRun2.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Orange/Walk/MushroomOrange_Walk_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomHurt2 = [] #Hurt
        for x in range(3):
            add_str = str(x)
            self.mushroomHurt2.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Orange/Hurt/MushroomOrange_Hurt_" + add_str + ".png"), (200, 160)))
        #endfor
        #Purple
        self.mushroomIdle3 = [] #Idle
        for x in range(8):
            add_str = str(x)
            self.mushroomIdle3.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Purple/Idle/MushroomPurple_Idle_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomAttack3 = [] #Attack
        for x in range(16):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.mushroomAttack3.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Purple/Attack/MushroomPurple_Attack_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomDeath3 = [] #Death
        for x in range(11):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.mushroomDeath3.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Purple/Death/MushroomPurple_Death_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomRun3 = [] #Run
        for x in range(8):
            add_str = str(x)
            self.mushroomRun3.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Purple/Walk/MushroomPurple_Walk_" + add_str + ".png"), (200, 160)))
        #endfor
        self.mushroomHurt3 = [] #Hurt
        for x in range(3):
            add_str = str(x)
            self.mushroomHurt3.append(pygame.transform.scale(pygame.image.load("Game_Images/Mushroom Purple/Hurt/MushroomPurple_Hurt_" + add_str + ".png"), (200, 160)))
        #endfor
        #Arun Swordsmith
        self.arunIdle = [] #Idle
        for x in range(10):
            add_str = str(x)
            self.arunIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/Arun/Idle/ArunSwordsmith_Idle_" + add_str + ".png"), (320, 250)))
        #endfor
        self.arunRun = [] #Run
        for x in range(10):
            add_str = str(x)
            self.arunRun.append(pygame.transform.scale(pygame.image.load("Game_Images/Arun/Run/ArunSwordsmith_Run_" + add_str + ".png"), (320, 250)))
        #endfor
        self.arunAttack = [] #Attack
        for x in range(12):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.arunAttack.append(pygame.transform.scale(pygame.image.load("Game_Images/Arun/Attack/ArunSwordsmith_Attack_" + add_str + ".png"), (320, 250)))
        #endfor
        self.arunDeath = [] #Death
        for x in range(17):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.arunDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Arun/Death/ArunSwordsmith_Death_" + add_str + ".png"), (320, 250)))
        #endfor
        self.arunFall = [] #Fall
        for x in range(3):
            add_str = str(x)
            self.arunFall.append(pygame.transform.scale(pygame.image.load("Game_Images/Arun/Fall/ArunSwordsmith_Fall_" + add_str + ".png"), (320, 250)))
        #endfor
        self.arunHurt = [] #Hurt
        for x in range(4):
            add_str = str(x)
            self.arunHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/Arun/Hurt/ArunSwordsmith_Hurt_" + add_str + ".png"), (320, 250)))
        #endfor
        self.arunJump = [] #Jump
        for x in range(3):
            add_str = str(x)
            self.arunJump.append(pygame.transform.scale(pygame.image.load("Game_Images/Arun/Jump/ArunSwordsmith_Jump_" + add_str + ".png"), (320, 250)))
        #endfor
        self.arunThrow = [] #Throw
        for x in range(10):
            add_str = str(x)
            self.arunThrow.append(pygame.transform.scale(pygame.image.load("Game_Images/Arun/Throw/ArunSwordsmith_Throw_" + add_str + ".png"), (320, 250)))
        #endfor
        #Warlock
        self.warlockIdle = [] #Idle
        for x in range(12):
            add_str = str(x+1)
            self.warlockIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/Warlock/WarlockIdle" + add_str + ".png"), (160, 160)))
        #endfor
        self.warlockRun = [] #Run
        for x in range(8):
            add_str = str(x+1)
            self.warlockRun.append(pygame.transform.scale(pygame.image.load("Game_Images/Warlock/WarlockRun" + add_str + ".png"), (160, 160)))
        #endfor
        self.warlockDeath = [] #Death
        for x in range(13):
            add_str = str(x+1)
            self.warlockDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Warlock/WarlockDeath" + add_str + ".png"), (160, 160)))
        #endfor
        self.warlockHurt = [] #Hurt
        for x in range(4):
            add_str = str(x+1)
            self.warlockHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/Warlock/WarlockHurt" + add_str + ".png"), (160, 160)))
        #endfor
        self.warlockEscape = [] #Escape
        for x in range(9):
            add_str = str(x+1)
            self.warlockEscape.append(pygame.transform.scale(pygame.image.load("Game_Images/Warlock/WarlockEscape" + add_str + ".png"), (160, 160)))
        #endfor
        self.warlockAppear = [] #Appear
        for x in range(9):
            add_str = str(x+1)
            self.warlockAppear.append(pygame.transform.scale(pygame.image.load("Game_Images/Warlock/WarlockAppear" + add_str + ".png"), (160, 160)))
        #endfor
        #Rogue
        self.rogueIdle = [] #Idle
        for x in range(11):
            add_str = str(x+1)
            self.rogueIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueIdle" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueRun = [] #Run
        for x in range(10):
            add_str = str(x+1)
            self.rogueRun.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueRun" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueDeath = [] #Death
        for x in range(14):
            add_str = str(x+1)
            self.rogueDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueDeath" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueHurt = [] #Hurt
        for x in range(3):
            add_str = str(x+1)
            self.rogueHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueHurt" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueDeath = [] #Death
        for x in range(14):
            add_str = str(x+1)
            self.rogueDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueDeath" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueAttack = [] #Attack
        for x in range(10):
            add_str = str(x+1)
            self.rogueAttack.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueAttack" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueSA = [] #Special Attack
        for x in range(18):
            add_str = str(x+1)
            self.rogueSA.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueSA" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueSpell = [] #Spell
        for x in range(12):
            add_str = str(x+1)
            self.rogueSpell.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueSpell" + add_str + ".png"), (250, 250)))
        #endfor
        #Dark Knight
        self.knightIdle = [] #Idle
        for x in range(10):
            add_str = str(x)
            self.knightIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/DarkKnight/Idle/DarkKnight_Idle_" + add_str + ".png"), (250, 188)))
        #endfor
        self.knightRun = [] #Run
        for x in range(10):
            add_str = str(x)
            self.knightRun.append(pygame.transform.scale(pygame.image.load("Game_Images/DarkKnight/Walk/DarkKnight_Walk_" + add_str + ".png"), (250, 188)))
        #endfor
        self.knightAttack = [] #Attack
        for x in range(12):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.knightAttack.append(pygame.transform.scale(pygame.image.load("Game_Images/DarkKnight/Attack/DarkKnight_Attack_" + add_str + ".png"), (250, 188)))
        #endfor
        self.knightDeath = [] #Death
        for x in range(12):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.knightDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/DarkKnight/Death/DarkKnight_Death_" + add_str + ".png"), (250, 188)))
        #endfor
        self.knightFlameAttack = [] #Flame Attack
        for x in range(13):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.knightFlameAttack.append(pygame.transform.scale(pygame.image.load("Game_Images/DarkKnight/Flame Attack/DarkKnight_FlameAttack_" + add_str + ".png"), (250, 188)))
        #endfor
        self.knightBlock = [] #Block
        for x in range(10):
            add_str = str(x)
            self.knightBlock.append(pygame.transform.scale(pygame.image.load("Game_Images/DarkKnight/Block Idle/DarkKnight_Block Idle_" + add_str + ".png"), (250, 188)))
        #endfor
        self.knightBlocked = [] #Blocked
        for x in range(5):
            add_str = str(x)
            self.knightBlocked.append(pygame.transform.scale(pygame.image.load("Game_Images/DarkKnight/Block/DarkKnight_Block_" + add_str + ".png"), (250, 188)))
        #endfor
        self.knightHurt = [] #Hurt
        for x in range(3):
            add_str = str(x)
            self.knightHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/DarkKnight/Hurt/DarkKnight_Hurt_" + add_str + ".png"), (250, 188)))
        #endfor
        #Skeleton Warrior
        self.skeletonIdle = [] #Idle
        for x in range(7):
            add_str = str(x)
            self.skeletonIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/SkeletonWarrior/Idle/Skeleton_Idle_" + add_str + ".png"), (350, 160)))
        #endfor
        self.skeletonRun = [] #Walk
        for x in range(10):
            add_str = str(x)
            self.skeletonRun.append(pygame.transform.scale(pygame.image.load("Game_Images/SkeletonWarrior/Walk/Skeleton_Walk_" + add_str + ".png"), (350, 160)))
        #endfor
        self.skeletonHurt = [] #Hurt
        for x in range(3):
            add_str = str(x)
            self.skeletonHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/SkeletonWarrior/Hurt/Skeleton_Hurt_" + add_str + ".png"), (350, 160)))
        #endfor
        self.skeletonDeath = [] #Death
        for x in range(13):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.skeletonDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/SkeletonWarrior/Death/Skeleton_Death_" + add_str + ".png"), (350, 160)))
        #endfor
        self.skeletonAttack = [] #Attack
        for x in range(17):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.skeletonAttack.append(pygame.transform.scale(pygame.image.load("Game_Images/SkeletonWarrior/Attack/Skeleton_Attack_" + add_str + ".png"), (350, 160)))
        #endfor
        self.skeletonRecover = [] #Recover
        for x in range(12):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.skeletonRecover.append(pygame.transform.scale(pygame.image.load("Game_Images/SkeletonWarrior/Recover/Skeleton_Death_0" + add_str + ".png"), (350, 160)))
        #endfor
        #Abomination
        self.abominationIdle = [] #Idle
        for x in range(6):
            add_str = str(x)
            self.abominationIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/Abomination/Idle/Abomination_Idle_" + add_str + ".png"), (450, 450)))
        #endfor
        self.abominationHurt = [] #Hurt
        for x in range(4):
            add_str = str(x)
            self.abominationHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/Abomination/Hurt/Abomination_Hurt_" + add_str + ".png"), (450, 450)))
        #endfor
        self.abominationRun = [] #Run
        for x in range(8):
            add_str = str(x)
            self.abominationRun.append(pygame.transform.scale(pygame.image.load("Game_Images/Abomination/Walk/Abomination_Walk_" + add_str + ".png"), (450, 450)))
        #endfor
        self.abominationAttack = [] #Attack
        for x in range(14):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.abominationAttack.append(pygame.transform.scale(pygame.image.load("Game_Images/Abomination/Attack/Abomination_Attack_" + add_str + ".png"), (450, 450)))
        #endfor
        self.abominationDeath = [] #Death
        for x in range(10):
            add_str = str(x)
            self.abominationDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Abomination/Death/Abomination_Death_" + add_str + ".png"), (450, 450)))
        #endfor
        #Necromancer
        self.necromancerIdle = [] #Idle
        for x in range(11):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.necromancerIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/Necromancer/Idle/Necromancer_Idle_" + add_str + ".png"), (250, 160)))
        #endfor
        self.necromancerAttack = [] #Attack
        for x in range(15):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.necromancerAttack.append(pygame.transform.scale(pygame.image.load("Game_Images/Necromancer/Attack/Necromancer_Attack_" + add_str + ".png"), (250, 200)))
        #endfor
        self.necromancerDeath = [] #Death
        for x in range(14):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.necromancerDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Necromancer/Death/Necromancer_Death_" + add_str + ".png"), (250, 160)))
        #endfor
        self.necromancerSpell = [] #Spell
        for x in range(13):
            add_str = str(x)
            if x < 10:
                add_str = "0"+str(x)
            #endif
            self.necromancerSpell.append(pygame.transform.scale(pygame.image.load("Game_Images/Necromancer/Spellcast/Necromancer_Spellcast_" + add_str + ".png"), (250, 160)))
        #endfor
        self.necromancerRun = [] #Run
        for x in range(8):
            add_str = str(x)
            self.necromancerRun.append(pygame.transform.scale(pygame.image.load("Game_Images/Necromancer/Run/Necromancer_Run_" + add_str + ".png"), (250, 160)))
        #endfor
        self.necromancerJump = [] #Jump
        for x in range(3):
            add_str = str(x)
            self.necromancerJump.append(pygame.transform.scale(pygame.image.load("Game_Images/Necromancer/Jump/Necromancer_Jump_" + add_str + ".png"), (250, 160)))
        #endfor
        self.necromancerFall = [] #Fall
        for x in range(3):
            add_str = str(x)
            self.necromancerFall.append(pygame.transform.scale(pygame.image.load("Game_Images/Necromancer/Fall/Necromancer_Fall_" + add_str + ".png"), (250, 160)))
        #endfor
        self.necromancerHurt = [] #Hurt
        for x in range(4):
            add_str = str(x)
            self.necromancerHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/Necromancer/Hurt/Necromancer_Hurt_" + add_str + ".png"), (250, 160)))
        #endfor
        if self.enemy == 0:
            self.image = pygame.transform.flip(self.banditIdle2[0],1,0)
        elif self.enemy == 1: #Set
            self.image = pygame.transform.flip(self.banditIdle1[0],1,0)
        elif self.enemy == 2:
            self.image = pygame.transform.flip(self.warlockIdle[0],1,0)
        elif self.enemy == 3:
            self.image = pygame.transform.flip(self.rogueIdle[0],1,0)
        elif self.enemy == 4:
            self.image = pygame.transform.flip(self.arunIdle[0],1,0)
        elif self.enemy == 5:
            self.image = pygame.transform.flip(self.mushroomRun1[0],1,0)
        elif self.enemy == 6:
            self.image = pygame.transform.flip(self.mushroomRun2[0],1,0)
        elif self.enemy == 7:
            self.image = pygame.transform.flip(self.mushroomRun3[0],1,0)
        elif self.enemy == 8:
            self.image = pygame.transform.flip(self.knightIdle[0],1,0)
        elif self.enemy == 9:
            self.image = pygame.transform.flip(self.skeletonRecover[0],1,0)
        elif self.enemy == 11:
            self.image = pygame.transform.flip(self.abominationIdle[0],1,0)
        elif self.enemy == 12:
            self.image = pygame.transform.flip(self.necromancerIdle[0],1,0)
        #endif
    #endmethod
    def Idle(self, speed, i): #When enemy not moving
        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditIdle1[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditIdle1[i],1,0) #Left
            #endif
        elif self.enemy == 2:
            if speed > 0:
                self.image = self.warlockIdle[i] #Right
            else:
                self.image = pygame.transform.flip(self.warlockIdle[i],1,0) #Left
            #endif
        elif self.enemy == 3:
            if speed > 0:
                self.image = self.rogueIdle[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueIdle[i],1,0) #Left
            #endif
        elif self.enemy == 4:
            if speed > 0:
                self.image = self.arunIdle[i] #Right
            else:
                self.image = pygame.transform.flip(self.arunIdle[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditIdle2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditIdle2[i],1,0) #Left
            #endif
        elif self.enemy == 5:
            if speed > 0:
                self.image = self.mushroomIdle1[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomIdle1[i],1,0) #Left
            #endif
        elif self.enemy == 6:
            if speed > 0:
                self.image = self.mushroomIdle2[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomIdle2[i],1,0) #Left
            #endif
        elif self.enemy == 7:
            if speed > 0:
                self.image = self.mushroomIdle3[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomIdle3[i],1,0) #Left
            #endif
        elif self.enemy == 8:
            if speed > 0:
                self.image = self.knightIdle[i] #Right
            else:
                self.image = pygame.transform.flip(self.knightIdle[i],1,0) #Left
            #endif
        elif self.enemy == 9:
            if speed > 0:
                self.image = self.skeletonIdle[i] #Right
            else:
                self.image = pygame.transform.flip(self.skeletonIdle[i],1,0) #Left
            #endif
        elif self.enemy == 11:
            if speed > 0:
                self.image = self.abominationIdle[i] #Right
            else:
                self.image = pygame.transform.flip(self.abominationIdle[i],1,0) #Left
            #endif
        elif self.enemy == 12:
            if speed > 0:
                self.image = self.necromancerIdle[i] #Right
            else:
                self.image = pygame.transform.flip(self.necromancerIdle[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Adle(self, speed, i): #When enemy not moving 2
        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditAdle1[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditAdle1[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditAdle2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditAdle2[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Run(self, speed, i):
        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditRun1[i]
            else:
                self.image = pygame.transform.flip(self.banditRun1[i],1,0)
            #endif
        elif self.enemy == 2:
            if speed > 0:
                self.image = self.warlockRun[i] #Right
            else:
                self.image = pygame.transform.flip(self.warlockRun[i],1,0) #Left
            #endif
        elif self.enemy == 3:
            if speed > 0:
                self.image = self.rogueRun[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueRun[i],1,0) #Left
            #endif
        elif self.enemy == 4:
            if speed > 0:
                self.image = self.arunRun[i] #Right
            else:
                self.image = pygame.transform.flip(self.arunRun[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditRun2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditRun2[i],1,0) #Left
            #endif
        elif self.enemy == 5:
            if speed > 0:
                self.image = self.mushroomRun1[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomRun1[i],1,0) #Left
            #endif
        elif self.enemy == 6:
            if speed > 0:
                self.image = self.mushroomRun2[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomRun2[i],1,0) #Left
            #endif
        elif self.enemy == 7:
            if speed > 0:
                self.image = self.mushroomRun3[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomRun3[i],1,0) #Left
            #endif
        elif self.enemy == 8:
            if speed > 0:
                self.image = self.knightRun[i] #Right
            else:
                self.image = pygame.transform.flip(self.knightRun[i],1,0) #Left
            #endif
        elif self.enemy == 9:
            if speed > 0:
                self.image = self.skeletonRun[i] #Right
            else:
                self.image = pygame.transform.flip(self.skeletonRun[i],1,0) #Left
            #endif
        elif self.enemy == 11:
            if speed > 0:
                self.image = self.abominationRun[i] #Right
            else:
                self.image = pygame.transform.flip(self.abominationRun[i],1,0) #Left
            #endif
        elif self.enemy == 12:
            if speed > 0:
                self.image = self.necromancerRun[i] #Right
            else:
                self.image = pygame.transform.flip(self.necromancerRun[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Jump(self, speed, i):
        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditJump1[i]
            else:
                self.image = pygame.transform.flip(self.banditJump1[i],1,0)
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditJump2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditJump2[i],1,0) #Left
            #endif
        elif self.enemy == 4:
            if speed > 0:
                self.image = self.arunJump[i] #Right
            else:
                self.image = pygame.transform.flip(self.arunJump[i],1,0) #Left
            #endif
        elif self.enemy == 12:
            if speed > 0:
                self.image = self.necromancerJump[i] #Right
            else:
                self.image = pygame.transform.flip(self.necromancerJump[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Fall(self, speed, i):
        if self.enemy == 4:
            if speed > 0:
                self.image = self.arunFall[i]
            else:
                self.image = pygame.transform.flip(self.arunFall[i],1,0)
            #endif
        elif self.enemy == 12:
            if speed > 0:
                self.image = self.necromancerFall[i] #Right
            else:
                self.image = pygame.transform.flip(self.necromancerFall[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Attack(self, speed, i):
        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditAttack1[i]
            else:
                self.image = pygame.transform.flip(self.banditAttack1[i],1,0)
            #endif
        elif self.enemy == 3:
            if speed > 0:
                self.image = self.rogueAttack[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueAttack[i],1,0) #Left
            #endif
        elif self.enemy == 4:
            if speed > 0:
                self.image = self.arunAttack[i] #Right
            else:
                self.image = pygame.transform.flip(self.arunAttack[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditAttack2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditAttack2[i],1,0) #Left
            #endif
        elif self.enemy == 5:
            if speed > 0:
                self.image = self.mushroomAttack1[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomAttack1[i],1,0) #Left
            #endif
        elif self.enemy == 6:
            if speed > 0:
                self.image = self.mushroomAttack2[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomAttack2[i],1,0) #Left
            #endif
        elif self.enemy == 7:
            if speed > 0:
                self.image = self.mushroomAttack3[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomAttack3[i],1,0) #Left
            #endif
        elif self.enemy == 8:
            if speed > 0:
                self.image = self.knightAttack[i] #Right
            else:
                self.image = pygame.transform.flip(self.knightAttack[i],1,0) #Left
            #endif
        elif self.enemy == 9:
            if speed > 0:
                self.image = self.skeletonAttack[i] #Right
            else:
                self.image = pygame.transform.flip(self.skeletonAttack[i],1,0) #Left
            #endif
        elif self.enemy == 11:
            if speed > 0:
                self.image = self.abominationAttack[i] #Right
            else:
                self.image = pygame.transform.flip(self.abominationAttack[i],1,0) #Left
            #endif
        elif self.enemy == 12:
            if speed > 0:
                self.image = self.necromancerAttack[i] #Right
            else:
                self.image = pygame.transform.flip(self.necromancerAttack[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Hurt(self, speed, i):
        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditHurt1[i]
            else:
                self.image = pygame.transform.flip(self.banditHurt1[i],1,0)
            #endif
        elif self.enemy == 2:
            if speed > 0:
                self.image = self.warlockHurt[i] #Right
            else:
                self.image = pygame.transform.flip(self.warlockHurt[i],1,0) #Left
            #endif
        elif self.enemy == 3:
            if speed > 0:
                self.image = self.rogueHurt[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueHurt[i],1,0) #Left
            #endif
        elif self.enemy == 4:
            if speed > 0:
                self.image = self.arunHurt[i] #Right
            else:
                self.image = pygame.transform.flip(self.arunHurt[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditHurt2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditHurt2[i],1,0) #Left
            #endif
        elif self.enemy == 5:
            if speed > 0:
                self.image = self.mushroomHurt1[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomHurt1[i],1,0) #Left
            #endif
        elif self.enemy == 6:
            if speed > 0:
                self.image = self.mushroomHurt2[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomHurt2[i],1,0) #Left
            #endif
        elif self.enemy == 7:
            if speed > 0:
                self.image = self.mushroomHurt3[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomHurt3[i],1,0) #Left
            #endif
        elif self.enemy == 8:
            if speed > 0:
                self.image = self.knightHurt[i] #Right
            else:
                self.image = pygame.transform.flip(self.knightHurt[i],1,0) #Left
            #endif
        elif self.enemy == 9:
            if speed > 0:
                self.image = self.skeletonHurt[i] #Right
            else:
                self.image = pygame.transform.flip(self.skeletonHurt[i],1,0) #Left
            #endif
        elif self.enemy == 11:
            if speed > 0:
                self.image = self.abominationHurt[i] #Right
            else:
                self.image = pygame.transform.flip(self.abominationHurt[i],1,0) #Left
            #endif
        elif self.enemy == 12:
            if speed > 0:
                self.image = self.necromancerHurt[i] #Right
            else:
                self.image = pygame.transform.flip(self.necromancerHurt[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Recover(self, speed, i):
        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditRecover1[i]
            else:
                self.image = pygame.transform.flip(self.banditRecover1[i],1,0)
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditRecover2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditRecover2[i],1,0) #Left
            #endif
        elif self.enemy == 9:
            if speed > 0:
                self.image = self.skeletonRecover[i] #Right
            else:
                self.image = pygame.transform.flip(self.skeletonRecover[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Death(self, speed, i):
        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditDeath1[i]
            else:
                self.image = pygame.transform.flip(self.banditDeath1[i],1,0)
            #endif
        elif self.enemy == 2:
            if speed > 0:
                self.image = self.warlockDeath[i] #Right
            else:
                self.image = pygame.transform.flip(self.warlockDeath[i],1,0) #Left
            #endif
        elif self.enemy == 3:
            if speed > 0:
                self.image = self.rogueDeath[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueDeath[i],1,0) #Left
            #endif
        elif self.enemy == 4:
            if speed > 0:
                self.image = self.arunDeath[i] #Right
            else:
                self.image = pygame.transform.flip(self.arunDeath[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditDeath2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditDeath2[i],1,0) #Left
            #endif
        elif self.enemy == 5:
            if speed > 0:
                self.image = self.mushroomDeath1[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomDeath1[i],1,0) #Left
            #endif
        elif self.enemy == 6:
            if speed > 0:
                self.image = self.mushroomDeath2[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomDeath2[i],1,0) #Left
            #endif
        elif self.enemy == 7:
            if speed > 0:
                self.image = self.mushroomDeath3[i] #Right
            else:
                self.image = pygame.transform.flip(self.mushroomDeath3[i],1,0) #Left
            #endif
        elif self.enemy == 8:
            if speed > 0:
                self.image = self.knightDeath[i] #Right
            else:
                self.image = pygame.transform.flip(self.knightDeath[i],1,0) #Left
            #endif
        elif self.enemy == 9:
            if speed > 0:
                self.image = self.skeletonDeath[i] #Right
            else:
                self.image = pygame.transform.flip(self.skeletonDeath[i],1,0) #Left
            #endif
        elif self.enemy == 11:
            if speed > 0:
                self.image = self.abominationDeath[i] #Right
            else:
                self.image = pygame.transform.flip(self.abominationDeath[i],1,0) #Left
            #endif
        elif self.enemy == 12:
            if speed > 0:
                self.image = self.necromancerDeath[i] #Right
            else:
                self.image = pygame.transform.flip(self.necromancerDeath[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Spell(self, speed, i):
        if self.enemy == 3:
            if speed > 0:
                self.image = self.rogueSpell[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueSpell[i],1,0) #Left
            #endif
        elif self.enemy == 12:
            if speed > 0:
                self.image = self.necromancerSpell[i] #Right
            else:
                self.image = pygame.transform.flip(self.necromancerSpell[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def SA(self, speed, i):
        if self.enemy == 3:
            if speed > 0:
                self.image = self.rogueSA[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueSA[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Throw(self, speed, i):
        if self.enemy == 4:
            if speed > 0:
                self.image = self.arunThrow[i] #Right
            else:
                self.image = pygame.transform.flip(self.arunThrow[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def FlameAttack(self, speed, i):
        if self.enemy == 8:
            if speed > 0:
                self.image = self.knightFlameAttack[i] #Right
            else:
                self.image = pygame.transform.flip(self.knightFlameAttack[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Block(self, speed, i):
        if self.enemy == 8:
            if speed > 0:
                self.image = self.knightBlock[i] #Right
            else:
                self.image = pygame.transform.flip(self.knightBlock[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Blocked(self, speed, i):
        if self.enemy == 8:
            if speed > 0:
                self.image = self.knightBlocked[i] #Right
            else:
                self.image = pygame.transform.flip(self.knightBlocked[i],1,0) #Left
            #endif
        #endif
    #endmethod
    def Escape(self, speed, i):
        if speed > 0:
            self.image = self.warlockEscape[i] #Right
        else:
            self.image = pygame.transform.flip(self.warlockEscape[i],1,0) #Left
        #endif
    #endmethod
    def Appear(self, speed, i):
        if speed > 0:
            self.image = self.warlockAppear[i] #Right
        else:
            self.image = pygame.transform.flip(self.warlockAppear[i],1,0) #Left
        #endif
    #endmethod
#endclass
#Special Effect Class
class EffectClass(pygame.sprite.Sprite): #Class of effect's
    def __init__(self, effectType, x, y, playerX, playerY, level_list):
        super().__init__()
        if effectType == 1:
            width = 38
            height = 38
        elif effectType == 2:
            width = 92
            height = 32
        #endif
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x #Set pos
        self.rect.y = y
        self.scaleX = x*10
        self.scaleY = y*10
        self.effect = effectType
        if self.effect == 1:
            if self.rect.x + 19 > playerX + 25:
                self.angle = -1*180*math.atan((self.rect.x-playerX-6)/(playerY-self.rect.y+31))/math.pi
                self.xMove = -21+int(self.angle)*3
                self.yMove = 22+int(self.angle/5)
            elif self.rect.x + 19 < playerX + 25:
                self.angle = 180*math.atan((playerX-self.rect.x+6)/(playerY-self.rect.y+31))/math.pi
                self.xMove = -21+int(self.angle/1.5)
                self.yMove = 22-int(self.angle/5)
            #endif
            self.effectAnimation = EffectAnimation(1, 80, 160, x-21, y+61, self.angle)
            self.counterMax = 3
            self.speedX = int(float("{:.1f}".format((playerX - self.rect.x + 6)/50))*10)
            self.speedY = int(float("{:.1f}".format((playerY - self.rect.y + 31)/50))*10)
        elif self.effect == 2:
            self.effectAnimation = EffectAnimation(2, 160, 40, x-34, y+4, 0)
            self.xMove = -34
            self.yMove = 4
            self.counterMax = 3
            self.speedX = 150*playerX
            self.speedY = 0
        #endif
        level_list.add(self.effectAnimation)
        #Timers
        self.startAnimation = 0
        self.endAnimation = 0
        #Counters
        self.counter = 0
        self.effectAnimation.Animate(self.speedX, self.counter)
    #endmethod
    def EffectUpdate(self, level_list):
        if self.startAnimation == 0: #If start timer has not started yet
            self.startAnimation = pygame.time.get_ticks() #Record current time
        #endif
        self.endAnimation = pygame.time.get_ticks() #Record current time
        self.scaleX += self.speedX #Move x
        self.rect.x = self.scaleX/10
        self.scaleY += self.speedY #Move y
        self.rect.y = self.scaleY/10
        self.effectAnimation.rect.x = self.rect.x + self.xMove
        self.effectAnimation.rect.y = self.rect.y + self.yMove
        if self.endAnimation - self.startAnimation >= 40:
            self.endAnimation = 0
            self.startAnimation = 0
            if self.counter < self.counterMax:
                self.counter += 1
            else:
                self.counter = 0
            #endif
            self.effectAnimation.Animate(self.speedX, self.counter)
        #endif
        if self.effect == 1:
            if self.rect.y >= 1060:
                level_list.remove(self.effectAnimation)
            #endif
        elif self.effect == 2:
            if self.rect.x <= -160:
                level_list.remove(self.effectAnimation)
            elif self.rect.x >= 1660:
                level_list.remove(self.effectAnimation)
            #endif
        #endif
    #endmethod
    def DeleteSelf(self, level_list, effect_list):
        level_list.remove(self.effectAnimation)
        effect_list.remove(self)
    #endmethod
#endclass
#Special Effect Animation Class
class EffectAnimation(pygame.sprite.Sprite): #Class of effect's animation
    def __init__(self, effectType, width, height, x, y, angle):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x #Set pos
        self.rect.y = y
        self.effect = effectType
        self.angle = angle
        #Animation
        #Shadow Bolts - 1
        self.shadowBolt = [] #38, 60
        for x in range(4):
            add_str = str(x)
            self.shadowBolt.append(pygame.transform.scale(pygame.image.load("Game_Images/Effects1/Sprites/ShadowBolt/ShadowBolt_" + add_str + ".png"), (80, 160)))
        #endfor
        #Fireball - 2
        self.fireball = [] #92, 32
        for x in range(4):
            add_str = str(x)
            self.fireball.append(pygame.transform.scale(pygame.image.load("Game_Images/Effects1/Sprites/Fireball/Fireball_" + add_str + ".png"), (160, 40)))
        #endfor
    #endmethod
    def Animate(self, speed, i):
        if self.effect == 1:
            if speed > 0:
                self.image = self.shadowBolt[i] #Right
            else:
                self.image = pygame.transform.flip(self.shadowBolt[i],1,0) #Left
            #endif
            self.image = pygame.transform.rotate(self.image, self.angle)
        elif self.effect == 2:
            if speed > 0:
                self.image = self.fireball[i] #Right
            else:
                self.image = pygame.transform.flip(self.fireball[i],1,0) #Left
            #endif
        #endif
    #endmethod
#endclass
#Gameplay
def Game():
    game_over = False #Not finish
    clock = pygame.time.Clock()
    #Scripts
    script1 = []
    script2 = []
    script3 = []
    scriptExtra = []
    #Variables
    currency = [0,0,0,0] #Money
    live = [5] #Player's live
    shieldNum = [8] #Player's shield
    playerLevel = [0]
    loadedLive = [0] #Backup Live
    loadedShield = [0]
    loadedPlayerLevel = [0]
    timeUp = [0]
    enemyCount = [-1]
    gameMode = [0]
    gameDifficulty = 1
    gameLevel = 1 #Game Level
    gamePhase = 1
    gameChat = 1
    gameOver = False
    gamePause = False
    advanceLevel = False
    quitLevel = False
    gameUpgrade = False
    upgraded = False
    readyToUpgrade = False
    ReadyToClick = False
    startReadScript = 0
    endReadScript = 0
    timer = TimerClass()
    gameOverDisplay = False
    conversation = False
    warlockDead = [1]
    rogueDead = [1]
    mehiraDefeat = [1]
    warlockDodgeTime = 0
    odenHealth = [5]
    warlockMove = False
    playerInvincible = [0]
    instantKill = [0]
    posX = 0
    #Setting Variables
    difficulty = 0
    #Game Level Variable
    currentSpeed = 0 #Used to determine animation direction
    horiSpeed = 0#Used to determine background move
    level = -1 #Determines level
    tutorialReset = True
    #Tutorial Level Variable
    dummyStartAttack = 0
    dummyEndAttack = 0
    #Level Load Variables
    gameInitiated = False #If game has been intiated
    levelCreated = False #If level has been created
    loadNum = 0 #Animation Count
    startLoadTime = 0 #Timer
    endLoadTime = 0
    currentFile = 0 #The player's file
    fileLoaded = False #If file has been loaded
    crownChecked = False
    levelToGo = 0
    tutorialLevel = False
    startT = 0
    endT = 0
    #Sprites lists
    block1_list = pygame.sprite.Group() #Blocks list 1
    block2_list = pygame.sprite.Group() #Blocks list 2
    block3_list = pygame.sprite.Group() #Blocks list 3
    character1_list = pygame.sprite.Group()
    character2_list = pygame.sprite.Group()
    character3_list = pygame.sprite.Group()
    ground_list = pygame.sprite.Group()
    tutorialBlock_list = pygame.sprite.Group() #Block tutorial list
    player_list = pygame.sprite.Group() #Player's list
    enemy_list = pygame.sprite.Group() #Enemy's list
    warlock_list = pygame.sprite.Group() #Warlock
    warlock2_list = pygame.sprite.Group() #Walock 2
    warlock3_list = pygame.sprite.Group() #Warlock 3
    rogue_list = pygame.sprite.Group() #Rogue
    arun_list = pygame.sprite.Group() #Arun
    abomination_list = pygame.sprite.Group() #Abomination
    necromancer_list = pygame.sprite.Group() #Necromancer
    rogueAttack_list = pygame.sprite.Group() #Rogue Attack
    abominationAttack_list = pygame.sprite.Group() #Abomination Attack
    leftJavelin_list = pygame.sprite.Group() #Javelins
    rightJavelin_list = pygame.sprite.Group() #Javelins
    tutorialEnemy_list = pygame.sprite.Group() #Enemy's tutorial list
    banditGroup1_list = pygame.sprite.Group() #Bandits
    banditGroup2_list = pygame.sprite.Group()
    banditGroup3_list = pygame.sprite.Group()
    banditGroup4_list = pygame.sprite.Group()
    mushroomGroup1_list = pygame.sprite.Group() #Mushrooms
    mushroomGroup2_list = pygame.sprite.Group()
    mushroomGroup3_list = pygame.sprite.Group()
    skeleton1_list = pygame.sprite.Group() #Skeletons
    skeleton2_list = pygame.sprite.Group()
    darkKnight_list = pygame.sprite.Group()
    startEnd_list = pygame.sprite.Group() #The area determines the start and end of a level
    levelOne_list = pygame.sprite.Group() #All visible object lists in level one
    levelTwo_list = pygame.sprite.Group() #All visible object lists in level two
    levelThree_list = pygame.sprite.Group() #All visible object lists in level three
    menu_list = pygame.sprite.Group() #All visible objects in menu
    file_list = pygame.sprite.Group() #All visible objects in file
    leftPlayerAttack_list = pygame.sprite.Group() #Player's attack
    rightPlayerAttack_list = pygame.sprite.Group() #Player's attack
    skullAttack_list = pygame.sprite.Group()
    talene_list = pygame.sprite.Group()
    taleneAttack_list = pygame.sprite.Group()
    leftEnemyAttack_list = pygame.sprite.Group()
    rightEnemyAttack_list = pygame.sprite.Group()
    enemyAttack_list = pygame.sprite.Group() #Enemy's attack
    mushroomAttack_list = pygame.sprite.Group() #Mushroom's attack
    shadowBolt_list = pygame.sprite.Group() #Shadow Bolts
    fireBall_list = pygame.sprite.Group() #Fire Balls
    button_list = pygame.sprite.Group() #Buttons
    pauseButton_list = pygame.sprite.Group() #Pause Button
    optionBlock_list = pygame.sprite.Group()
    panelButton_list = pygame.sprite.Group()
    nextButton_list = pygame.sprite.Group() #Next Button
    upgradeButton_list = pygame.sprite.Group() #Upgrade Button
    upgradeTextButton_list = pygame.sprite.Group() #Upgrade Text Button
    okButton_list = pygame.sprite.Group() #Ok Button
    levelUp_list = pygame.sprite.Group()
    upgradeInstruction_list = pygame.sprite.Group()
    item_list = pygame.sprite.Group() #Group of items
    crown_list = pygame.sprite.Group() #Crown
    loading_list = pygame.sprite.Group() #Loading screen
    setting_list = pygame.sprite.Group() #Setting screen
    invincibleOn_list = pygame.sprite.Group() #Invincible on
    invincibleOff_list = pygame.sprite.Group() #Invincible off
    instantKillOn_list = pygame.sprite.Group() #Instant Kill on
    instantKillOff_list = pygame.sprite.Group() #Instant Kill off
    background1_list = pygame.sprite.Group() #Backgrounds
    background2_list = pygame.sprite.Group() #Backgrounds
    background3_list = pygame.sprite.Group() #Backgrounds
    cloud_list = pygame.sprite.Group() #Clouds
    tutorial_list = pygame.sprite.Group() #Tutorial
    coin_list = pygame.sprite.Group() #Coins
    thousand_list = pygame.sprite.Group()
    hundred_list = pygame.sprite.Group()
    ten_list = pygame.sprite.Group()
    one_list = pygame.sprite.Group()
    wordBox_list = pygame.sprite.Group() #WordBox
    currentLine_list = pygame.sprite.Group() #Current Line
    nextLevelBlock_list = pygame.sprite.Group() #Next level panel
    currentFileData_list = pygame.sprite.Group() #Current file data
    directionArrow_list = pygame.sprite.Group() #Arrow
    restartLevel_list = pygame.sprite.Group() #Restart level panel
    quitLevel_list = pygame.sprite.Group()
    upgradeBox_list = pygame.sprite.Group()
    yellowTriangle_list = pygame.sprite.Group()
    mehira_list = pygame.sprite.Group()
    talene2_list = pygame.sprite.Group()
    skull_list = pygame.sprite.Group()
    oden_list = pygame.sprite.Group() #Oden
    allBackgrounds_list = pygame.sprite.Group() #All backgrounds
    background_list = pygame.sprite.Group() #Backgrounds
    whiteScreen_list = pygame.sprite.Group() #White screen
    tempBandit_list = pygame.sprite.Group() #Temporary Bandits
    credit_list = pygame.sprite.Group() #Credit
    CreateLoad(loading_list)
    while not game_over:
    # -- User input and controls
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()#Track Mouse' Position
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN: #Mouse Click
                if level == 0 and pos[0] >= 595 and pos[1] >= 420 and pos[0] <= 904 and pos[1] <= 513: #Select save files
                    level = 3 #Start game
                    tutorialLevel = False
                    fileLoaded = False
                elif level == 0 and pos[0] >= 442 and pos[1] >= 560 and pos[0] <= 1057 and pos[1] <= 653: #Select Settings
                    level = 1 #Settings
                elif level == 0 and pos[0] >= 430 and pos[1] >= 700 and pos[0] <= 1069 and pos[1] <= 793: #Select tutorial
                    levelToGo = 2
                    level = -1 #Tutorial
                    tutorialLevel = True
                    for dummy in tutorialEnemy_list:
                        dummy.AttackStance(1)
                        dummy.ChangeSpeed(1)
                        dummy.ChangeSpeed(2)
                        dummy.rect.x = 295
                    #endfor
                    player.Freeze(0)
                    player.FreezeTrigger(0)
                    fileLoaded = True
                elif level == 1 and pos[0] >= 844 and pos[1] >= 390 and pos[0] <= 918 and pos[1] <= 430 and playerInvincible[0] == 1: #Turn Off Invincible
                    playerInvincible[0] = 0
                    for player in player_list:
                        player.Invincible(0)
                    #endfor
                    for on in invincibleOn_list:
                        setting_list.remove(on)
                    #endfor
                    for off in invincibleOff_list:
                        setting_list.add(off)
                    #endfor
                    f = open("Game_Files/Setting.txt","r+") #Open Setting
                    lines = f.readlines() #All data
                    f.close() #Close
                    f = open("Game_Files/Setting.txt","w+") #Modify Setting
                    f.write("0\n"+lines[1])
                    f.close() #Close
                elif level == 1 and pos[0] >= 844 and pos[1] >= 390 and pos[0] <= 944 and pos[1] <= 430 and playerInvincible[0] == 0: #Turn On Invincible
                    playerInvincible[0] = 1
                    for player in player_list:
                        player.Invincible(1)
                    #endfor
                    for on in invincibleOn_list:
                        setting_list.add(on)
                    #endfor
                    for off in invincibleOff_list:
                        setting_list.remove(off)
                    #endfor
                    f = open("Game_Files/Setting.txt","r+") #Open Setting
                    lines = f.readlines() #All data
                    f.close() #Close
                    f = open("Game_Files/Setting.txt","w+") #Modify Setting
                    f.write("1\n"+lines[1])
                    f.close() #Close
                elif level == 1 and pos[0] >= 844 and pos[1] >= 470 and pos[0] <= 918 and pos[1] <= 510 and instantKill[0] == 1: #Turn Off Instant Kill
                    instantKill[0] = 0
                    for character in character1_list:
                        character.InstantKill(0)
                    #endfor
                    for character in character2_list:
                        character.InstantKill(0)
                    #endfor
                    for character in character3_list:
                        character.InstantKill(0)
                    #endfor
                    for on in instantKillOn_list:
                        setting_list.remove(on)
                    #endfor
                    for off in instantKillOff_list:
                        setting_list.add(off)
                    #endfor
                    f = open("Game_Files/Setting.txt","r+") #Open Setting
                    lines = f.readlines() #All data
                    f.close() #Close
                    f = open("Game_Files/Setting.txt","w+") #Modify Setting
                    f.write(lines[0]+"0")
                    f.close() #Close
                elif level == 1 and pos[0] >= 844 and pos[1] >= 470 and pos[0] <= 944 and pos[1] <= 510 and instantKill[0] == 0: #Turn On Instant Kill
                    instantKill[0] = 1
                    for character in character1_list:
                        character.InstantKill(1)
                    #endfor
                    for character in character2_list:
                        character.InstantKill(1)
                    #endfor
                    for character in character3_list:
                        character.InstantKill(1)
                    #endfor
                    for on in instantKillOn_list:
                        setting_list.add(on)
                    #endfor
                    for off in instantKillOff_list:
                        setting_list.remove(off)
                    #endfor
                    f = open("Game_Files/Setting.txt","r+") #Open Setting
                    lines = f.readlines() #All data
                    f.close() #Close
                    f = open("Game_Files/Setting.txt","w+") #Modify Setting
                    f.write(lines[0]+"1")
                    f.close() #Close
                elif level == 3 and pos[0] >= 249 and pos[1] >= 680 and pos[0] <= 410 and pos[1] <= 711: #Select file 1
                    level = -1
                    levelToGo = 4
                    currentFile = 1
                    player.FreezeTrigger(0)
                elif level == 3 and pos[0] >= 669 and pos[1] >= 680 and pos[0] <= 830 and pos[1] <= 711: #Select file 2
                    level = -1
                    levelToGo = 4
                    currentFile = 2
                    player.FreezeTrigger(0)
                elif level == 3 and pos[0] >= 1089 and pos[1] >= 680 and pos[0] <= 1250 and pos[1] <= 711: #Select file 3
                    level = -1
                    levelToGo = 4
                    currentFile = 3
                    player.FreezeTrigger(0)
                elif level == 3 and pos[0] >= 284 and pos[1] >= 778 and pos[0] <= 376 and pos[1] <= 798: #Save Files Reset
                    ResetProgress(1)
                    ResetFile(file_list, currentFileData_list)
                    SetCrown(crown_list)
                elif level == 3 and pos[0] >= 704 and pos[1] >= 778 and pos[0] <= 796 and pos[1] <= 798:
                    ResetProgress(2)
                    ResetFile(file_list, currentFileData_list)
                    SetCrown(crown_list)
                elif level == 3 and pos[0] >= 1124 and pos[1] >= 778 and pos[0] <= 1216 and pos[1] <= 798:
                    ResetProgress(3)
                    ResetFile(file_list, currentFileData_list)
                    SetCrown(crown_list)
                elif level == 5 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851:
                    level = 1
                elif level == 1 and pos[0] >= 1315 and pos[1] >= 820 and pos[0] <= 1450 and pos[1] <= 851:
                    level = 5
                elif level == 3 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851: #Go back to menu
                    level = 0
                    fileLoaded = True
                elif level == 1 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851: #Go back to menu
                    level = 0
                elif level == 2 and pos[0] >= 1430 and pos[1] >= 10 and pos[0] <= 1490 and pos[1] <= 70: #Go back to menu
                    levelToGo = 0
                    tutorialLevel = True
                    fileLoaded = False
                    level = -1
                    player.ResetLive([5], shieldNum, playerLevel)
                    player.Reset()
                    currency[0] = 0
                    currency[1] = 0
                    currency[2] = 0
                    currency[3] = 0
                elif level == 4 and pos[0] >= 616 and pos[1] >= 503 and pos[0] <= 884 and pos[1] <= 543 and not gameUpgrade and not gamePause and not gameOver and not quitLevel and advanceLevel: #Advance Game Level
                    advanceLevel = False
                    enemyCount = [-1]
                    for triangle in yellowTriangle_list:
                        triangle.rect.x = -1000
                        triangle.rect.y = 670
                    #endfor
                    for bandit in tempBandit_list:#Remove Temporary Bandits
                        bandit.Reset()
                    #endfor
                    DrawOrRemove(0, tempBandit_list, tempBandit_list)
                    if gameLevel == 1:
                        DrawOrRemove(0, levelOne_list, nextLevelBlock_list)
                        for block in block1_list:
                            block.Reset()
                        #endfpr
                        for character in character1_list:
                            character.Reset()
                        #endfor
                        for button in pauseButton_list:
                            levelOne_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for rogue in rogue_list:
                            rogue.HealthDisplay(0, levelOne_list)
                        #endfor
                        DrawOrRemove(0, levelOne_list, nextButton_list)
                        DrawOrRemove(0, levelOne_list, currentLine_list)
                        DrawOrRemove(0, levelOne_list, wordBox_list)
                        DrawOrRemove(0, levelOne_list, whiteScreen_list)
                    elif gameLevel == 2:
                        DrawOrRemove(0, levelTwo_list, nextLevelBlock_list)
                        for block in block2_list:
                            block.Reset()
                        #endfpr
                        for character in character2_list:
                            character.Reset()
                        #endfor
                        for button in pauseButton_list:
                            levelTwo_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for arun in arun_list:
                            arun.HealthDisplay(0, levelTwo_list)
                        #endfor
                        DrawOrRemove(0, levelTwo_list, nextButton_list)
                        DrawOrRemove(0, levelTwo_list, currentLine_list)
                        DrawOrRemove(0, levelTwo_list, wordBox_list)
                        DrawOrRemove(0, levelTwo_list, leftJavelin_list)
                        DrawOrRemove(0, leftJavelin_list, leftJavelin_list)
                        DrawOrRemove(0, levelTwo_list, rightJavelin_list)
                        DrawOrRemove(0, rightJavelin_list, rightJavelin_list)
                    elif gameLevel == 3:
                        DrawOrRemove(0, levelThree_list, nextLevelBlock_list)
                        for block in block3_list:
                            block.Reset()
                        #endfpr
                        for character in character3_list:
                            character.Reset()
                        #endfor
                        for button in pauseButton_list:
                            levelThree_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for necro in necromancer_list:
                            necro.HealthDisplay(0, levelThree_list)
                        #endfor
                        DrawOrRemove(0, levelThree_list, shadowBolt_list)
                        DrawOrRemove(0, shadowBolt_list, shadowBolt_list)
                        DrawOrRemove(0, levelThree_list, nextButton_list)
                        DrawOrRemove(0, levelThree_list, currentLine_list)
                        DrawOrRemove(0, levelThree_list, wordBox_list)
                        DrawOrRemove(0, levelThree_list, coin_list)
                    #endif
                    if gameLevel < 3:
                        gameLevel += 1
                    #endif
                    gameOver = False
                    gamePause = False
                    timeUp[0] = 0
                    gamePhase = 1
                    gameChat = 1
                    startReadScript = 0
                    endReadScript = 0
                    player.Reset()
                    levelToGo = 4
                    level = -1
                elif level == 4 and pos[0] >= 700 and pos[1] >= 573 and pos[0] <= 800 and pos[1] <= 613 and not gameUpgrade and not gamePause and not gameOver and not quitLevel and advanceLevel: #Quit game level during completion
                    advanceLevel = False
                    enemyCount = [-1]
                    for triangle in yellowTriangle_list:
                        triangle.rect.x = -1000
                        triangle.rect.y = 670
                    #endfor
                    for bandit in tempBandit_list:#Remove Temporary Bandits
                        bandit.Reset()
                    #endfor
                    DrawOrRemove(0, tempBandit_list, tempBandit_list)
                    if gameLevel == 1:
                        DrawOrRemove(0, levelOne_list, nextLevelBlock_list)
                        for block in block1_list:
                            block.Reset()
                        #endfpr
                        for character in character1_list:
                            character.Reset()
                        #endfor
                        for button in pauseButton_list:
                            levelOne_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for rogue in rogue_list:
                            rogue.HealthDisplay(0, levelOne_list)
                        #endfor
                        DrawOrRemove(0, levelOne_list, nextButton_list)
                        DrawOrRemove(0, levelOne_list, currentLine_list)
                        DrawOrRemove(0, levelOne_list, wordBox_list)
                        DrawOrRemove(0, levelOne_list, whiteScreen_list)
                    elif gameLevel == 2:
                        DrawOrRemove(0, levelTwo_list, nextLevelBlock_list)
                        for block in block2_list:
                            block.Reset()
                        #endfpr
                        for character in character2_list:
                            character.Reset()
                        #endfor
                        for button in pauseButton_list:
                            levelTwo_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for arun in arun_list:
                            arun.HealthDisplay(0, levelTwo_list)
                        #endfor
                        DrawOrRemove(0, levelTwo_list, nextButton_list)
                        DrawOrRemove(0, levelTwo_list, currentLine_list)
                        DrawOrRemove(0, levelTwo_list, wordBox_list)
                        DrawOrRemove(0, levelTwo_list, leftJavelin_list)
                        DrawOrRemove(0, leftJavelin_list, leftJavelin_list)
                        DrawOrRemove(0, levelTwo_list, rightJavelin_list)
                        DrawOrRemove(0, rightJavelin_list, rightJavelin_list)
                    elif gameLevel == 3:
                        DrawOrRemove(0, levelThree_list, nextLevelBlock_list)
                        for block in block3_list:
                            block.Reset()
                        #endfpr
                        for character in character3_list:
                            character.Reset()
                        #endfor
                        for button in pauseButton_list:
                            levelThree_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for necro in necromancer_list:
                            necro.HealthDisplay(0, levelThree_list)
                        #endfor
                        DrawOrRemove(0, levelThree_list, shadowBolt_list)
                        DrawOrRemove(0, shadowBolt_list, shadowBolt_list)
                        DrawOrRemove(0, levelThree_list, nextButton_list)
                        DrawOrRemove(0, levelThree_list, currentLine_list)
                        DrawOrRemove(0, levelThree_list, wordBox_list)
                        DrawOrRemove(0, levelThree_list, coin_list)
                    #endif
                    if gameLevel < 3:
                        gameLevel += 1
                    #endif
                    levelToGo = 0
                    level = -1
                    fileLoaded = False
                    timeUp[0] = 0
                    gamePhase = 1
                    gameChat = 1
                    gameOver = False
                    gamePause = False
                    ReadyToClick = False
                    startReadScript = 0
                    endReadScript = 0
                    player.ResetLive([5], [8], [0])
                    player.Reset()
                    player.LevelSet([0])
                    live[0] = 5
                elif level == 4 and pos[0] >= 1360 and pos[1] >= 820 and pos[0] <= 1420 and pos[1] <= 880 and not gameUpgrade and not gamePause and not gameOver and not advanceLevel and readyToUpgrade: #Upgrade panel
                    gameUpgrade = True
                    if gameLevel == 1:
                        for character in character1_list:
                            character.Freeze(1)
                        #endfor
                        player.FreezeTrigger(1)
                        DrawOrRemove(1, levelOne_list, levelUp_list)
                        DrawOrRemove(0, levelOne_list, upgradeButton_list)
                        DrawOrRemove(0, levelOne_list, pauseButton_list)
                    elif gameLevel == 2:
                        for character in character2_list:
                            character.Freeze(1)
                        #endfor
                        player.FreezeTrigger(1)
                        DrawOrRemove(1, levelTwo_list, levelUp_list)
                        DrawOrRemove(0, levelTwo_list, upgradeButton_list)
                        DrawOrRemove(0, levelTwo_list, pauseButton_list)
                    elif gameLevel == 3:
                        for character in character3_list:
                            character.Freeze(1)
                        #endfor
                        player.FreezeTrigger(1)
                        DrawOrRemove(1, levelThree_list, levelUp_list)
                        DrawOrRemove(0, levelThree_list, upgradeButton_list)
                        DrawOrRemove(0, levelThree_list, pauseButton_list)
                    #endif
                elif level == 4 and pos[0] >= 670 and pos[1] >= 503 and pos[0] <= 830 and pos[1] <= 543 and gameUpgrade and not gamePause and not gameOver and not advanceLevel and not upgraded: #Upgrade
                    if currency[1] > 0 and currency[2] < 6:
                        currency[1] -= 1
                        currency[2] += 4
                        playerLevel[0] = playerLevel[0] + 1
                        for ten in ten_list:
                            ten.Update(currency[2])
                        #endfor
                        for hundred in hundred_list:
                            hundred.Update(currency[1])
                        #endfor
                        for player in player_list:
                            player.LevelSet(playerLevel)
                        #endfor
                        upgraded = True
                        if gameLevel == 1:
                            DrawOrRemove(1, levelOne_list, upgradeBox_list)
                        elif gameLevel == 2:
                            DrawOrRemove(1, levelTwo_list, upgradeBox_list)
                        elif gameLevel == 3:
                            DrawOrRemove(1, levelThree_list, upgradeBox_list)
                        #endif
                        for instruction in upgradeInstruction_list:
                            instruction.LevelUpdate(playerLevel[0])
                        #endfor
                    elif currency[2] >= 6:
                        currency[2] -= 6
                        playerLevel[0] = playerLevel[0] + 1
                        for ten in ten_list:
                            ten.Update(currency[2])
                        #endfor
                        for player in player_list:
                            player.LevelSet(playerLevel)
                        #endfor
                        upgraded = True
                        if gameLevel == 1:
                            DrawOrRemove(1, levelOne_list, upgradeBox_list)
                        elif gameLevel == 2:
                            DrawOrRemove(1, levelTwo_list, upgradeBox_list)
                        elif gameLevel == 3:
                            DrawOrRemove(1, levelThree_list, upgradeBox_list)
                        #endif
                        for instruction in upgradeInstruction_list:
                            instruction.LevelUpdate(playerLevel[0])
                        #endfor
                    #endif
                elif level == 4 and pos[0] >= 723 and pos[1] >= 503 and pos[0] <= 777 and pos[1] <= 533 and gameUpgrade and upgraded: #Exit Instruction of Upgrade
                    upgraded = False
                    if gameLevel == 1:
                        DrawOrRemove(0, levelOne_list, upgradeBox_list)
                    elif gameLevel == 2:
                        DrawOrRemove(0, levelTwo_list, upgradeBox_list)
                    elif gameLevel == 3:
                        DrawOrRemove(0, levelThree_list, upgradeBox_list)
                    #endif
                elif level == 4 and pos[0] >= 1430 and pos[1] >= 820 and pos[0] <= 1490 and pos[1] <= 880 and not gameUpgrade and not gamePause and not gameOver and not advanceLevel: #Pause game
                    gamePause = True
                    if gameLevel == 1:
                        for character in character1_list:
                            character.Freeze(1)
                        #endfor
                        player.FreezeTrigger(1)
                        DrawOrRemove(1, levelOne_list, optionBlock_list)
                        DrawOrRemove(1, levelOne_list, panelButton_list)
                        DrawOrRemove(0, levelOne_list, pauseButton_list)
                        DrawOrRemove(0, levelOne_list, upgradeButton_list)
                    elif gameLevel == 2:
                        for character in character2_list:
                            character.Freeze(1)
                        #endfor
                        player.FreezeTrigger(1)
                        DrawOrRemove(1, levelTwo_list, optionBlock_list)
                        DrawOrRemove(1, levelTwo_list, panelButton_list)
                        DrawOrRemove(0, levelTwo_list, pauseButton_list)
                        DrawOrRemove(0, levelTwo_list, upgradeButton_list)
                    elif gameLevel == 3:
                        for character in character3_list:
                            character.Freeze(1)
                        #endfor
                        player.FreezeTrigger(1)
                        DrawOrRemove(1, levelThree_list, optionBlock_list)
                        DrawOrRemove(1, levelThree_list, panelButton_list)
                        DrawOrRemove(0, levelThree_list, pauseButton_list)
                        DrawOrRemove(0, levelThree_list, upgradeButton_list)
                    #endif
                elif level == 4 and pos[0] >= 1068 and pos[1] >= 234 and pos[0] <= 1128 and pos[1] <= 294 and not gameUpgrade and gamePause and not gameOver and not quitLevel and not advanceLevel: #Continue during pause
                    gamePause = False
                    if gameLevel == 1:
                        for character in character1_list:
                            character.Freeze(0)
                        #endfor
                        if not conversation:
                            player.FreezeTrigger(0)
                        #endif
                        DrawOrRemove(0, levelOne_list, optionBlock_list)
                        DrawOrRemove(0, levelOne_list, panelButton_list)
                        DrawOrRemove(1, levelOne_list, pauseButton_list)
                        if readyToUpgrade:
                            DrawOrRemove(1, levelOne_list, upgradeButton_list)
                        #endif
                    elif gameLevel == 2:
                        for character in character2_list:
                            character.Freeze(0)
                        #endfor
                        if not conversation:
                            player.FreezeTrigger(0)
                        #endif
                        DrawOrRemove(0, levelTwo_list, optionBlock_list)
                        DrawOrRemove(0, levelTwo_list, panelButton_list)
                        DrawOrRemove(1, levelTwo_list, pauseButton_list)
                        if readyToUpgrade:
                            DrawOrRemove(1, levelTwo_list, upgradeButton_list)
                        #endif
                    elif gameLevel == 3:
                        for character in character3_list:
                            character.Freeze(0)
                        #endfor
                        if not conversation:
                            player.FreezeTrigger(0)
                        #endif
                        DrawOrRemove(0, levelThree_list, optionBlock_list)
                        DrawOrRemove(0, levelThree_list, panelButton_list)
                        DrawOrRemove(1, levelThree_list, pauseButton_list)
                        if readyToUpgrade:
                            DrawOrRemove(1, levelThree_list, upgradeButton_list)
                        #endif
                    #endif
                elif level == 4 and pos[0] >= 1068 and pos[1] >= 234 and pos[0] <= 1128 and pos[1] <= 294 and gameUpgrade and not gamePause and not gameOver and not quitLevel and not advanceLevel and not upgraded: #Continue during upgrade
                    gameUpgrade = False
                    if gameLevel == 1:
                        for character in character1_list:
                            character.Freeze(0)
                        #endfor
                        if not conversation:
                            player.FreezeTrigger(0)
                        #endif
                        DrawOrRemove(0, levelOne_list, levelUp_list)
                        if readyToUpgrade:
                            DrawOrRemove(1, levelOne_list, upgradeButton_list)
                        #endif
                        DrawOrRemove(1, levelOne_list, pauseButton_list)
                    elif gameLevel == 2:
                        for character in character2_list:
                            character.Freeze(0)
                        #endfor
                        if not conversation:
                            player.FreezeTrigger(0)
                        #endif
                        DrawOrRemove(0, levelTwo_list, levelUp_list)
                        if readyToUpgrade:
                            DrawOrRemove(1, levelTwo_list, upgradeButton_list)
                        #endif
                        DrawOrRemove(1, levelTwo_list, pauseButton_list)
                    elif gameLevel == 3:
                        for character in character3_list:
                            character.Freeze(0)
                        #endfor
                        if not conversation:
                            player.FreezeTrigger(0)
                        #endif
                        DrawOrRemove(0, levelThree_list, levelUp_list)
                        if readyToUpgrade:
                            DrawOrRemove(1, levelThree_list, upgradeButton_list)
                        #endif
                        DrawOrRemove(1, levelThree_list, pauseButton_list)
                    #endif
                elif level == 4 and pos[0] >= 654 and pos[1] >= 573 and pos[0] <= 845 and pos[1] <= 613 and not gameUpgrade and gamePause and not quitLevel and not gameOver and not advanceLevel: #Game Pause Restart
                    enemyCount = [-1]
                    levelToGo = 4
                    warlockMove = False
                    level = -1
                    timeUp[0] = 0
                    gamePhase = 1
                    gameChat = 1
                    gameOver = False
                    gamePause = False
                    ReadyToClick = False
                    advanceLevel = False
                    startReadScript = 0
                    endReadScript = 0
                    player.ResetLive(loadedLive, loadedShield, loadedPlayerLevel)
                    player.Reset()
                    live[0] = loadedLive[0]
                    DrawOrRemove(0, coin_list, coin_list)
                    for triangle in yellowTriangle_list:
                        triangle.rect.x = -1000
                        triangle.rect.y = 670
                    #endfor
                    for bandit in tempBandit_list:#Remove Temporary Bandits
                        bandit.Reset()
                    #endfor
                    DrawOrRemove(0, tempBandit_list, tempBandit_list)
                    if gameLevel == 1:
                        for block in block1_list:
                            block.Reset()
                        #endfpr
                        for character in character1_list:
                            character.Reset()
                        #endfor
                        for optionBlock in optionBlock_list:
                            levelOne_list.remove(optionBlock)
                        #endfor
                        for button in panelButton_list:
                            levelOne_list.remove(button)
                        #endfor
                        for button in pauseButton_list:
                            levelOne_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for rogue in rogue_list:
                            rogue.HealthDisplay(0, levelOne_list)
                        #endfor
                        for arrow in directionArrow_list:
                            arrow.ArrowReset(levelOne_list)
                        #endfor
                        DrawOrRemove(0, levelOne_list, nextButton_list)
                        DrawOrRemove(0, levelOne_list, currentLine_list)
                        DrawOrRemove(0, levelOne_list, wordBox_list)
                        DrawOrRemove(0, levelOne_list, coin_list)
                        DrawOrRemove(0, levelOne_list, whiteScreen_list)
                    elif gameLevel == 2:
                        for block in block2_list:
                            block.Reset()
                        #endfpr
                        for character in character2_list:
                            character.Reset()
                        #endfor
                        for optionBlock in optionBlock_list:
                            levelTwo_list.remove(optionBlock)
                        #endfor
                        for button in panelButton_list:
                            levelTwo_list.remove(button)
                        #endfor
                        for button in pauseButton_list:
                            levelTwo_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for arun in arun_list:
                            arun.HealthDisplay(0, levelTwo_list)
                        #endfor
                        for arrow in directionArrow_list:
                            arrow.ArrowReset(levelTwo_list)
                        #endfor
                        DrawOrRemove(0, levelTwo_list, nextButton_list)
                        DrawOrRemove(0, levelTwo_list, currentLine_list)
                        DrawOrRemove(0, levelTwo_list, wordBox_list)
                        DrawOrRemove(0, levelTwo_list, coin_list)
                        DrawOrRemove(0, levelTwo_list, leftJavelin_list)
                        DrawOrRemove(0, leftJavelin_list, leftJavelin_list)
                        DrawOrRemove(0, levelTwo_list, rightJavelin_list)
                        DrawOrRemove(0, rightJavelin_list, rightJavelin_list)
                    elif gameLevel == 3:
                        for block in block3_list:
                            block.Reset()
                        #endfpr
                        for character in character3_list:
                            character.Reset()
                        #endfor
                        for optionBlock in optionBlock_list:
                            levelThree_list.remove(optionBlock)
                        #endfor
                        for button in panelButton_list:
                            levelThree_list.remove(button)
                        #endfor
                        for button in pauseButton_list:
                            levelThree_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for necro in necromancer_list:
                            necro.HealthDisplay(0, levelThree_list)
                        #endfor
                        for skull in skull_list:
                            skull.SkullReset()
                            skull.SkullUpdate(0)
                        #endfor
                        DrawOrRemove(0, levelThree_list, shadowBolt_list)
                        DrawOrRemove(0, shadowBolt_list, shadowBolt_list)
                        DrawOrRemove(0, levelThree_list, nextButton_list)
                        DrawOrRemove(0, levelThree_list, currentLine_list)
                        DrawOrRemove(0, levelThree_list, wordBox_list)
                        DrawOrRemove(0, levelThree_list, coin_list)
                    #endif
                elif level == 4 and pos[0] >= 700 and pos[1] >= 503 and pos[0] <= 800 and pos[1] <= 543 and not gameUpgrade and gamePause and not quitLevel and not gameOver and not advanceLevel: #Quit game
                    enemyCount = [-1]
                    warlockMove = False
                    levelToGo = 0
                    level = -1
                    fileLoaded = False
                    timeUp[0] = 0
                    gamePhase = 1
                    gameChat = 1
                    gameOver = False
                    gamePause = False
                    ReadyToClick = False
                    startReadScript = 0
                    endReadScript = 0
                    player.ResetLive([5], [8], [0])
                    player.Reset()
                    live[0] = 5
                    for triangle in yellowTriangle_list:
                        triangle.rect.x = -1000
                        triangle.rect.y = 670
                    #endfor
                    for bandit in tempBandit_list:#Remove Temporary Bandits
                        bandit.Reset()
                    #endfor
                    DrawOrRemove(0, tempBandit_list, tempBandit_list)
                    DrawOrRemove(0, coin_list, coin_list)
                    if gameLevel == 1:
                        for block in block1_list:
                            block.Reset()
                        #endfpr
                        for character in character1_list:
                            character.Reset()
                        #endfor
                        for optionBlock in optionBlock_list:
                            levelOne_list.remove(optionBlock)
                        #endfor
                        for button in panelButton_list:
                            levelOne_list.remove(button)
                        #endfor
                        for button in pauseButton_list:
                            levelOne_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for rogue in rogue_list:
                            rogue.HealthDisplay(0, levelOne_list)
                        #endfor
                        for arrow in directionArrow_list:
                            arrow.ArrowReset(levelOne_list)
                        #endfor
                        DrawOrRemove(0, levelOne_list, nextButton_list)
                        DrawOrRemove(0, levelOne_list, currentLine_list)
                        DrawOrRemove(0, levelOne_list, wordBox_list)
                        DrawOrRemove(0, levelOne_list, coin_list)
                        DrawOrRemove(0, levelOne_list, whiteScreen_list)
                    elif gameLevel == 2:
                        for block in block2_list:
                            block.Reset()
                        #endfpr
                        for character in character2_list:
                            character.Reset()
                        #endfor
                        for optionBlock in optionBlock_list:
                            levelTwo_list.remove(optionBlock)
                        #endfor
                        for button in panelButton_list:
                            levelTwo_list.remove(button)
                        #endfor
                        for button in pauseButton_list:
                            levelTwo_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for arun in arun_list:
                            arun.HealthDisplay(0, levelTwo_list)
                        #endfor
                        for arrow in directionArrow_list:
                            arrow.ArrowReset(levelTwo_list)
                        #endfor
                        DrawOrRemove(0, levelTwo_list, nextButton_list)
                        DrawOrRemove(0, levelTwo_list, currentLine_list)
                        DrawOrRemove(0, levelTwo_list, wordBox_list)
                        DrawOrRemove(0, levelTwo_list, coin_list)
                        DrawOrRemove(0, levelTwo_list, leftJavelin_list)
                        DrawOrRemove(0, leftJavelin_list, leftJavelin_list)
                        DrawOrRemove(0, levelTwo_list, rightJavelin_list)
                        DrawOrRemove(0, rightJavelin_list, rightJavelin_list)
                    elif gameLevel == 3:
                        for block in block3_list:
                            block.Reset()
                        #endfpr
                        for character in character3_list:
                            character.Reset()
                        #endfor
                        for optionBlock in optionBlock_list:
                            levelThree_list.remove(optionBlock)
                        #endfor
                        for button in panelButton_list:
                            levelThree_list.remove(button)
                        #endfor
                        for button in pauseButton_list:
                            levelThree_list.add(button)
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for necro in necromancer_list:
                            necro.HealthDisplay(0, levelThree_list)
                        #endfor
                        DrawOrRemove(0, levelThree_list, shadowBolt_list)
                        DrawOrRemove(0, shadowBolt_list, shadowBolt_list)
                        DrawOrRemove(0, levelThree_list, nextButton_list)
                        DrawOrRemove(0, levelThree_list, currentLine_list)
                        DrawOrRemove(0, levelThree_list, wordBox_list)
                        DrawOrRemove(0, levelThree_list, coin_list)
                    #endif
                elif level == 4 and pos[0] >= 700 and pos[1] >= 533 and pos[0] <= 800 and pos[1] <= 573 and quitLevel and not gameUpgrade and not gamePause and not gameOver and not advanceLevel: #Quit Level in the End
                    quitLevel = False
                    enemyCount = [-1]
                    gameOverDisplay = False
                    levelToGo = 0
                    level = -1
                    fileLoaded = False
                    timeUp[0] = 0
                    gamePhase = 1
                    gameChat = 1
                    gameOver = False
                    gamePause = False
                    ReadyToClick = False
                    startReadScript = 0
                    endReadScript = 0
                    player.ResetLive([5], [8], [0])
                    player.Reset()
                    live[0] = 5
                    for triangle in yellowTriangle_list:
                        triangle.rect.x = -1000
                        triangle.rect.y = 670
                    #endfor
                    for bandit in tempBandit_list:#Remove Temporary Bandits
                        bandit.Reset()
                    #endfor
                    DrawOrRemove(0, tempBandit_list, tempBandit_list)
                    if gameLevel == 1:
                        for block in block1_list:
                            block.Reset()
                        #endfpr
                        for character in character1_list:
                            character.Reset()
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for rogue in rogue_list:
                            rogue.HealthDisplay(0, levelOne_list)
                        #endfor
                        DrawOrRemove(0, levelOne_list, nextButton_list)
                        DrawOrRemove(0, levelOne_list, currentLine_list)
                        DrawOrRemove(0, levelOne_list, wordBox_list)
                        DrawOrRemove(0, levelOne_list, restartLevel_list)
                        DrawOrRemove(1, levelOne_list, pauseButton_list)
                        DrawOrRemove(0, levelOne_list, coin_list)
                        DrawOrRemove(0, coin_list, coin_list)
                        DrawOrRemove(0, levelOne_list, whiteScreen_list)
                        DrawOrRemove(0, levelOne_list, quitLevel_list)
                    elif gameLevel == 2:
                        for block in block2_list:
                            block.Reset()
                        #endfpr
                        for character in character2_list:
                            character.Reset()
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for coin in coin_list:
                            levelTwo_list.remove(coin)
                        #endmethod
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for arun in arun_list:
                            arun.HealthDisplay(0, levelTwo_list)
                        #endfor
                        DrawOrRemove(0, levelTwo_list, nextButton_list)
                        DrawOrRemove(0, levelTwo_list, currentLine_list)
                        DrawOrRemove(0, levelTwo_list, wordBox_list)
                        DrawOrRemove(0, levelTwo_list, restartLevel_list)
                        DrawOrRemove(1, levelTwo_list, pauseButton_list)
                        DrawOrRemove(0, levelTwo_list, coin_list)
                        DrawOrRemove(0, coin_list, coin_list)
                        DrawOrRemove(0, levelTwo_list, leftJavelin_list)
                        DrawOrRemove(0, leftJavelin_list, leftJavelin_list)
                        DrawOrRemove(0, levelTwo_list, rightJavelin_list)
                        DrawOrRemove(0, rightJavelin_list, rightJavelin_list)
                        DrawOrRemove(0, levelTwo_list, quitLevel_list)
                    elif gameLevel == 3:
                        for block in block3_list:
                            block.Reset()
                        #endfpr
                        for character in character3_list:
                            character.Reset()
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for coin in coin_list:
                            levelThree_list.remove(coin)
                        #endmethod
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for necro in necromancer_list:
                            necro.HealthDisplay(0, levelThree_list)
                        #endfor
                        DrawOrRemove(0, levelThree_list, shadowBolt_list)
                        DrawOrRemove(0, shadowBolt_list, shadowBolt_list)
                        DrawOrRemove(0, levelThree_list, nextButton_list)
                        DrawOrRemove(0, levelThree_list, currentLine_list)
                        DrawOrRemove(0, levelThree_list, wordBox_list)
                        DrawOrRemove(0, levelThree_list, restartLevel_list)
                        DrawOrRemove(1, levelThree_list, pauseButton_list)
                        DrawOrRemove(0, levelThree_list, coin_list)
                        DrawOrRemove(0, coin_list, coin_list)
                        DrawOrRemove(0, levelThree_list, quitLevel_list)
                    #endif
                elif level == 4 and pos[0] >= 700 and pos[1] >= 573 and pos[0] <= 800 and pos[1] <= 613 and gameOver and not gameUpgrade: #Game Over Quit
                    enemyCount = [-1]
                    gameOverDisplay = False
                    levelToGo = 0
                    level = -1
                    fileLoaded = False
                    timeUp[0] = 0
                    gamePhase = 1
                    gameChat = 1
                    gameOver = False
                    gamePause = False
                    ReadyToClick = False
                    startReadScript = 0
                    endReadScript = 0
                    player.ResetLive([5], [8], [0])
                    player.Reset()
                    live[0] = 5
                    for triangle in yellowTriangle_list:
                        triangle.rect.x = -1000
                        triangle.rect.y = 670
                    #endfor
                    for bandit in tempBandit_list:#Remove Temporary Bandits
                        bandit.Reset()
                    #endfor
                    DrawOrRemove(0, tempBandit_list, tempBandit_list)
                    if gameLevel == 1:
                        for block in block1_list:
                            block.Reset()
                        #endfpr
                        for character in character1_list:
                            character.Reset()
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for rogue in rogue_list:
                            rogue.HealthDisplay(0, levelOne_list)
                        #endfor
                        DrawOrRemove(0, levelOne_list, nextButton_list)
                        DrawOrRemove(0, levelOne_list, currentLine_list)
                        DrawOrRemove(0, levelOne_list, wordBox_list)
                        DrawOrRemove(0, levelOne_list, restartLevel_list)
                        DrawOrRemove(1, levelOne_list, pauseButton_list)
                        DrawOrRemove(0, levelOne_list, coin_list)
                        DrawOrRemove(0, coin_list, coin_list)
                        DrawOrRemove(0, levelOne_list, whiteScreen_list)
                    elif gameLevel == 2:
                        for block in block2_list:
                            block.Reset()
                        #endfpr
                        for character in character2_list:
                            character.Reset()
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for coin in coin_list:
                            levelTwo_list.remove(coin)
                        #endmethod
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for arun in arun_list:
                            arun.HealthDisplay(0, levelTwo_list)
                        #endfor
                        DrawOrRemove(0, levelTwo_list, nextButton_list)
                        DrawOrRemove(0, levelTwo_list, currentLine_list)
                        DrawOrRemove(0, levelTwo_list, wordBox_list)
                        DrawOrRemove(0, levelTwo_list, restartLevel_list)
                        DrawOrRemove(1, levelTwo_list, pauseButton_list)
                        DrawOrRemove(0, levelTwo_list, coin_list)
                        DrawOrRemove(0, coin_list, coin_list)
                        DrawOrRemove(0, levelTwo_list, leftJavelin_list)
                        DrawOrRemove(0, leftJavelin_list, leftJavelin_list)
                        DrawOrRemove(0, levelTwo_list, rightJavelin_list)
                        DrawOrRemove(0, rightJavelin_list, rightJavelin_list)
                    elif gameLevel == 3:
                        for block in block3_list:
                            block.Reset()
                        #endfpr
                        for character in character3_list:
                            character.Reset()
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for coin in coin_list:
                            levelThree_list.remove(coin)
                        #endmethod
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for necro in necromancer_list:
                            necro.HealthDisplay(0, levelThree_list)
                        #endfor
                        DrawOrRemove(0, levelThree_list, shadowBolt_list)
                        DrawOrRemove(0, shadowBolt_list, shadowBolt_list)
                        DrawOrRemove(0, levelThree_list, nextButton_list)
                        DrawOrRemove(0, levelThree_list, currentLine_list)
                        DrawOrRemove(0, levelThree_list, wordBox_list)
                        DrawOrRemove(0, levelThree_list, restartLevel_list)
                        DrawOrRemove(1, levelThree_list, pauseButton_list)
                        DrawOrRemove(0, levelThree_list, coin_list)
                        DrawOrRemove(0, coin_list, coin_list)
                    #endif
                elif level == 4 and pos[0] >= 654 and pos[1] >= 503 and pos[0] <= 845 and pos[1] <= 543 and gameOver and not gameUpgrade and not gamePause: #Game Over Restart
                    enemyCount = [-1]
                    gameOverDisplay = False
                    levelToGo = 4
                    level = -1
                    timeUp[0] = 0
                    gamePhase = 1
                    gameChat = 1
                    gameOver = False
                    gamePause = False
                    ReadyToClick = False
                    advanceLevel = False
                    startReadScript = 0
                    endReadScript = 0
                    player.ResetLive(loadedLive, loadedShield, loadedPlayerLevel)
                    player.Reset()
                    live[0] = loadedLive[0]
                    for triangle in yellowTriangle_list:
                        triangle.rect.x = -1000
                        triangle.rect.y = 670
                    #endfor
                    for bandit in tempBandit_list:#Remove Temporary Bandits
                        bandit.Reset()
                    #endfor
                    DrawOrRemove(0, tempBandit_list, tempBandit_list)
                    if gameLevel == 1:
                        for block in block1_list:
                            block.Reset()
                        #endfpr
                        for character in character1_list:
                            character.Reset()
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for coin in coin_list:
                            levelOne_list.remove(coin)
                        #endmethod
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for rogue in rogue_list:
                            rogue.HealthDisplay(0, levelOne_list)
                        #endfor
                        DrawOrRemove(0, levelOne_list, nextButton_list)
                        DrawOrRemove(0, levelOne_list, currentLine_list)
                        DrawOrRemove(0, levelOne_list, wordBox_list)
                        DrawOrRemove(0, levelOne_list, restartLevel_list)
                        DrawOrRemove(1, levelOne_list, pauseButton_list)
                        DrawOrRemove(0, levelOne_list, coin_list)
                        DrawOrRemove(0, coin_list, coin_list)
                        DrawOrRemove(0, levelOne_list, whiteScreen_list)
                    elif gameLevel == 2:
                        for block in block2_list:
                            block.Reset()
                        #endfpr
                        for character in character2_list:
                            character.Reset()
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for coin in coin_list:
                            levelTwo_list.remove(coin)
                        #endmethod
                        for background in background_list:
                            background.Reset()
                        #endfor
                        for arun in arun_list:
                            arun.HealthDisplay(0, levelTwo_list)
                        #endfor
                        DrawOrRemove(0, levelTwo_list, nextButton_list)
                        DrawOrRemove(0, levelTwo_list, currentLine_list)
                        DrawOrRemove(0, levelTwo_list, wordBox_list)
                        DrawOrRemove(0, levelTwo_list, restartLevel_list)
                        DrawOrRemove(1, levelTwo_list, pauseButton_list)
                        DrawOrRemove(0, levelTwo_list, coin_list)
                        DrawOrRemove(0, coin_list, coin_list)
                        DrawOrRemove(0, levelTwo_list, leftJavelin_list)
                        DrawOrRemove(0, leftJavelin_list, leftJavelin_list)
                        DrawOrRemove(0, levelTwo_list, rightJavelin_list)
                        DrawOrRemove(0, rightJavelin_list, rightJavelin_list)
                    elif gameLevel == 3:
                        for block in block3_list:
                            block.Reset()
                        #endfpr
                        for character in character3_list:
                            character.Reset()
                        #endfor
                        for ground in ground_list:
                            ground.Update(0)
                        #endfor
                        for coin in coin_list:
                            levelThree_list.remove(coin)
                        #endmethod
                        for background in background_list:
                            background.Reset()
                        #endfor
                        DrawOrRemove(0, levelThree_list, shadowBolt_list)
                        DrawOrRemove(0, shadowBolt_list, shadowBolt_list)
                        DrawOrRemove(0, levelThree_list, nextButton_list)
                        DrawOrRemove(0, levelThree_list, currentLine_list)
                        DrawOrRemove(0, levelThree_list, wordBox_list)
                        DrawOrRemove(0, levelThree_list, restartLevel_list)
                        DrawOrRemove(1, levelThree_list, pauseButton_list)
                        DrawOrRemove(0, levelThree_list, coin_list)
                        DrawOrRemove(0, coin_list, coin_list)
                    #endif
                    for background in background_list:
                        background.Reset()
                    #endfor
                elif level == 4 and pos[0] >= 1195 and pos[1] >= 850 and pos[0] <= 1255 and pos[1] <= 870 and not gamePause and not gameUpgrade:
                    if ReadyToClick:
                        gameChat += 1
                        ReadyToClick = False
                        timeUp[0] = 0
                    #endif
                #endif
            elif level >= 2 and event.type == pygame.KEYDOWN: #Press Key Down
                if event.key == pygame.K_q:
                    for player in player_list:
                        player.AttackTrigger()
                    #endfor
                if event.key == pygame.K_SPACE:
                    for player in player_list:
                        player.Jump()
                    #endfor
                if event.key == pygame.K_LEFT:
                    for player in player_list:
                        player.ChangeSpeed(0)
                        player.KeepMove(1)
                    #endfor
                    currentSpeed = -1
                    horiSpeed = -1
                if event.key == pygame.K_RIGHT:
                    for player in player_list:
                        player.ChangeSpeed(1)
                        player.KeepMove(1)
                    #endfor
                    currentSpeed = 1
                    horiSpeed = 1
                if event.key == pygame.K_LSHIFT:
                    for player in player_list:
                        player.BlockTrigger(1)
                    #endfor
                if event.key == pygame.K_e:
                    for player in player_list:
                        player.RollTrigger()
                    #endfor
                if event.key == pygame.K_w:
                    for player in player_list:
                        player.SpellTrigger()
                    #endfor
                #endif
            elif level >= 2 and event.type == pygame.KEYUP: #Release Key
                if event.key == pygame.K_LEFT and currentSpeed < 0:
                    for player in player_list:
                        player.ChangeSpeed(2)
                        player.KeepMove(0)
                    #endfor
                    horiSpeed = 0
                if event.key == pygame.K_RIGHT and currentSpeed > 0:
                    for player in player_list:
                        player.ChangeSpeed(2)
                        player.KeepMove(0)
                    #endfor
                    horiSpeed = 0
                if event.key == pygame.K_LSHIFT:
                    for player in player_list:
                        player.BlockTrigger(0)
                    #endfor
                #endif
            #endif
        #endfor
        if level == 0:
            screen.fill(BLACK)
            for button in button_list:
                button.Change(pos, level)
            #endfor
            menu_list.draw(screen) #Display all visible objects
        elif level == -1:
            screen.fill(BLACK)
            if startLoadTime == 0: #If start timer has not started yet
                startLoadTime = pygame.time.get_ticks() #Record current time
                for load in loading_list:
                    load.Animation(loadNum)
                #endfor
            #endif
            if gameInitiated == False:
                endLoadTime = pygame.time.get_ticks() #Record current time
                if endLoadTime - startLoadTime >= 700:
                    startLoadTime = endLoadTime #Reset Timer
                    for load in loading_list:
                        load.Animation(loadNum) #Animation
                        loadNum += 1
                        if loadNum == 4: #If animation finished
                            gameInitiated = True #Reset Loading
                            loadNum = 0
                            startLoadTime = 0
                            endLoadTime = 0
                            fileLoaded = False
                            level = 0 #Go to menu
                        #endif
                    #endfor
                #endif
                loading_list.draw(screen) #Display objects
                if levelCreated == False:
                    levelCreated = True
                    CreateFile(file_list, button_list, item_list, crown_list, currentFileData_list)
                    CreateCredits(credit_list, button_list)
                    CreateMenu(menu_list, button_list)
                    CreateSettings(setting_list, button_list, invincibleOn_list, invincibleOff_list, instantKillOn_list, instantKillOff_list, playerInvincible, instantKill)
                    CreateBackgrounds(levelOne_list, levelTwo_list, levelThree_list, background1_list, background2_list, background3_list, cloud_list, ground_list, allBackgrounds_list, background_list, whiteScreen_list)#Backgrounds and ground
                    CreateLevelPlatform(block1_list, levelOne_list, block2_list, levelTwo_list) #Level One Platforms
                    CreatePanel(button_list, optionBlock_list, pauseButton_list, panelButton_list, levelOne_list, levelTwo_list, levelThree_list, nextLevelBlock_list, restartLevel_list, directionArrow_list, levelUp_list, upgradeButton_list, upgradeInstruction_list, upgradeTextButton_list, upgradeBox_list, okButton_list, quitLevel_list)
                    CreateTutorialPlatform(tutorialBlock_list, tutorial_list, button_list)
                    CreateCharacters0(oden_list, skull_list, skullAttack_list, character2_list, character3_list, mehira_list, talene2_list, yellowTriangle_list, player_list, leftPlayerAttack_list, rightPlayerAttack_list, tutorialEnemy_list, tutorial_list, levelOne_list, levelTwo_list, levelThree_list, leftEnemyAttack_list, rightEnemyAttack_list, character1_list, talene_list, taleneAttack_list)
                    CreateCharacters1(levelOne_list, enemy_list, warlock_list, wordBox_list, nextButton_list, rogue_list, leftEnemyAttack_list, rightEnemyAttack_list, rogueAttack_list, banditGroup1_list, banditGroup2_list, character1_list)
                    CreateCharacters2(levelTwo_list, enemyAttack_list, leftEnemyAttack_list, rightEnemyAttack_list, banditGroup3_list, banditGroup4_list, mushroomGroup1_list, mushroomGroup2_list, mushroomGroup3_list, character2_list, arun_list, mushroomAttack_list, warlock2_list)
                    CreateCharacters3(levelThree_list, leftEnemyAttack_list, rightEnemyAttack_list, character3_list, skeleton1_list, abomination_list, abominationAttack_list, necromancer_list, warlock3_list)
                    CreateMoney(tutorial_list, levelOne_list, levelTwo_list, levelThree_list, thousand_list, hundred_list, ten_list, one_list)
                    for player in player_list:
                        player.DrawOnCanvas(tutorial_list, levelOne_list, levelTwo_list, levelThree_list)
                        if playerInvincible[0] == 1:
                            player.Invincible(1)
                        #endif
                    #endfor
                    if instantKill[0] == 1:
                        for character in character1_list:
                            character.InstantKill(1)
                        #endfor
                        for character in character2_list:
                            character.InstantKill(1)
                        #endfor
                        for character in character3_list:
                            character.InstantKill(1)
                        #endfor
                    #endif
                    ReadScript(script1, script2, script3)
                #endif
            #endif
            elif gameInitiated == True and tutorialLevel == False:
                endLoadTime = pygame.time.get_ticks() #Record current time
                if endLoadTime - startLoadTime >= 700:
                    startLoadTime = endLoadTime #Reset Timer
                    for load in loading_list:
                        load.Animation(loadNum) #Animation
                        loadNum += 1
                        if loadNum == 4: #If animation finished
                            loadNum = 0
                            startLoadTime = 0
                            endLoadTime = 0
                            if levelToGo == 4:
                                for ground in ground_list:
                                    ground.ChangeTheme(gameLevel)
                                #endfor
                                for background in allBackgrounds_list:
                                    background.ChangeTheme(gameLevel)
                                #endfor
                                for player in player_list:
                                    player.FreezeTrigger(1)
                                #endfor
                            #endif
                            level = levelToGo #Go to gameplay
                            fileLoaded = False
                            crownChecked = False
                        #endif
                    #endfor
                #endif
                loading_list.draw(screen) #Display objects
                if crownChecked == False: #Crown
                    crownChecked = True
                    SetCrown(crown_list)
                #endif
                if not fileLoaded and not tutorialLevel:
                    fileLoaded = True
                    ResetFile(file_list, currentFileData_list)
                    if currentFile == 1:
                        #Open File 1
                        f = open("Game_Files/File1.txt","r+") #Open file 1
                        lines = f.readlines() #All data
                        f.close() #Close
                    elif currentFile == 2:
                        #Open File 2
                        f = open("Game_Files/File2.txt","r+") #Open file 2
                        lines = f.readlines() #All data
                        f.close() #Close
                    elif currentFile == 3:
                        #Open File 3
                        f = open("Game_Files/File3.txt","r+") #Open file 3
                        lines = f.readlines() #All data
                        f.close() #Close
                    #endif
                    #Set currency
                    currency[3] = int(lines[0][3])
                    currency[2] = int(lines[0][2])
                    currency[1] = int(lines[0][1])
                    currency[0] = int(lines[0][0])
                    #Set live
                    live[0] = int(lines[1].rstrip("\n"))
                    loadedLive[0] = int(lines[1].rstrip("\n"))
                    shieldNum[0] = int(lines[3].rstrip("\n"))
                    loadedShield[0] = int(lines[3].rstrip("\n"))
                    playerLevel[0] = int(lines[4].rstrip("\n"))
                    loadedPlayerLevel[0] = int(lines[4].rstrip("\n"))
                    for player in player_list:
                        player.ResetLive(live, shieldNum, playerLevel)
                        player.LevelSet(playerLevel)
                        player.FreezeTrigger(1)
                    #endfor
                    #Set Level
                    gameLevel = int(lines[2][0])
                    gameMode[0] = int(lines[5][0])
                #endif
            elif tutorialLevel == True:
                endLoadTime = pygame.time.get_ticks() #Record current time
                if endLoadTime - startLoadTime >= 500:
                    startLoadTime = endLoadTime #Reset Timer
                    for load in loading_list:
                        load.Animation(loadNum) #Animation
                        loadNum += 1
                        if loadNum == 4: #If animation finished
                            loadNum = 0
                            load.Animation(loadNum)
                            startLoadTime = 0
                            endLoadTime = 0
                            level = levelToGo #Go to gameplay
                            fileLoaded = False
                            crownChecked = False
                        #endif
                    #endfor
                #endif
                loading_list.draw(screen) #Display objects
            #endif
        elif level == 1: #Settings
            screen.fill(BLACK)
            for button in button_list:
                button.Change(pos, level)
            #endfor
            setting_list.draw(screen) #Display objects
        elif level == 2: #Tutorial
            screen.fill(BLACK)
            if tutorialReset == True:
                for cloud in cloud_list:
                    cloud.rect.x = 0
                #endfor
                tutorialReset = False
            #endif
            for thousand in thousand_list:
                thousand.Update(currency[0])
            #endfor
            for hundred in hundred_list:
                hundred.Update(currency[1])
            #endfor
            for ten in ten_list:
                ten.Update(currency[2])
            #endfor
            for one in one_list:
                one.Update(currency[3])
            #endfor
            for button in button_list: #Button Change
                button.Change(pos, level)
            #endfor
            for cloud in cloud_list:
                cloud.CloudUpdate()
            #endfor
            for coin in coin_list:
                coin.Change()
                coin.CoinUpdate(player_list, tutorialBlock_list, tutorial_list, coin_list, currency)
            #endfor
            for fireball in fireBall_list:
                fireball.EffectUpdate(tutorial_list)
                if fireball.rect.x > 1500 or fireball.rect.x < -160:
                    fireball.DeleteSelf(tutorial_list, fireBall_list)
                #endif
            #endfor
            #Enemy Movement
            for enemy in tutorialEnemy_list:
                dummyEndAttack = pygame.time.get_ticks()
                if dummyEndAttack - dummyStartAttack > 3000:
                    dummyStartAttack = dummyEndAttack
                    enemy.ChangeSpeed(1)
                    enemy.ChangeSpeed(2)
                    enemy.AttackTrigger()
                #endif
                enemy.Attack()
                enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                enemy.AttackChecker()
                enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                enemy.Revive()
                enemy.Hurt()
                enemy.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                enemy.FireBallDetection(tutorial_list, fireBall_list)
                enemy.Health(coin_list, tutorial_list, level, gameLevel, enemyCount)
                enemy.Animation()
            #endfor
            #Player Movement
            for player in player_list:
                #Detection
                player.EnemyAttackDetection(leftEnemyAttack_list, rightEnemyAttack_list)
                #Blocked
                player.Blocked(live, shieldNum)
                #Hurt
                player.Hurt()
                #Attack
                player.Attack()
                #Spell
                player.Spell(fireBall_list, tutorial_list)
                #Roll
                player.Roll()
                #Horizontal Movement
                player.MoveHori(tutorialBlock_list) #Player move horizontally
                #Attack Checker
                player.AttackChecker()
                #Vertical Movement
                player.MoveVert(tutorialBlock_list)
                #Death
                player.Revive(live)
                #Health
                player.Health(live)
                #Animation
                player.Animation()
            #endfor
            tutorial_list.draw(screen) #Display all visible objects
        elif level == 3: #Save Files
            screen.fill(BLACK)
            for button in button_list:
                button.Change(pos, level)
            #endfor
            for item in item_list:
                item.Change()
            #endfor
            file_list.draw(screen) #Display all visible objects
        elif level == 5: #Credit
            screen.fill(BLACK)
            for button in button_list: #Button Change
                button.Change(pos, level)
            #endfor
            credit_list.draw(screen) #Display objects
        elif level == 4: #Gameplay
            if not gamePause and not gameOver and not gameUpgrade: #If Game
                if gameLevel == 1: #level1fate------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    screen.fill(WHITE)
                    for cloud in cloud_list: #Cloud
                        cloud.CloudUpdate()
                    #endfor
                    for button in button_list: #Button Change
                        button.Change(pos, level)
                    #endfor
                    for coin in coin_list: #Coin
                        coin.Change()
                        coin.CoinUpdate(player_list, block1_list, levelOne_list, coin_list, currency)
                    #endfor
                    for fireball in fireBall_list: #Fire Ball
                        fireball.EffectUpdate(levelOne_list)
                        if fireball.rect.x > 1500 or fireball.rect.x < -160:
                            fireball.DeleteSelf(levelOne_list, fireBall_list)
                        #endif
                    #endfor
                    for thousand in thousand_list:
                        thousand.Update(currency[0])
                    #endfor
                    for hundred in hundred_list:
                        hundred.Update(currency[1])
                    #endfor
                    for ten in ten_list:
                        ten.Update(currency[2])
                    #endfor
                    for one in one_list:
                        one.Update(currency[3])
                    #endfor
                    #Warlock
                    if gamePhase <= 7 or gamePhase >= 20:
                        for warlock in warlock_list:
                            if gamePhase == 3 and warlockDodgeTime < 3 and warlockMove:
                                warlock.rect.x -= 60
                                warlockDodgeTime += 1
                            #endif
                            warlock.MoveHori(block1_list)
                            warlock.MoveVert(block1_list)
                            warlock.Hurt()
                            warlock.Health(odenHealth)
                            warlock.EnemyAttackDetection(leftPlayerAttack_list)
                            warlock.EnemyAttackDetection(rightPlayerAttack_list)
                            warlock.Appear()
                            warlock.Escape()
                            warlock.Animation()
                        #endfor
                    #endif
                    #Rogue
                    if gamePhase <= 5 or gamePhase >= 10:
                        for rogue in rogue_list:
                            if gamePhase == 19 and not gameOver:
                                rogue.Control(player.rect.x)
                            #endif
                            rogue.MoveHori(block1_list)
                            rogue.MoveVert(block1_list)
                            rogue.Hurt()
                            rogue.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list, player_list)
                            rogue.FireBallDetection(levelOne_list, fireBall_list)
                            rogue.Attack()
                            rogue.Health(levelOne_list, coin_list, enemyCount)
                            rogue.SA()
                            rogue.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 5 and gamePhase <= 8:
                        #Bandit Movement
                        for enemy in banditGroup1_list:
                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            if gamePhase == 8 and not gameOver:
                                enemy.Control(player_list)
                            #endif
                            enemy.Hurt()
                            enemy.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            enemy.FireBallDetection(levelOne_list, fireBall_list)
                            enemy.Health(coin_list, levelOne_list, level, gameLevel, enemyCount)
                            enemy.Reproduce(tempBandit_list)
                            enemy.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 10 and gamePhase <= 15:
                        #Bandit Movement
                        for enemy in banditGroup2_list:
                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            if gamePhase == 15 and not gameOver:
                                enemy.Control(player_list)
                            #endif
                            enemy.Hurt()
                            enemy.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            enemy.FireBallDetection(levelOne_list, fireBall_list)
                            enemy.Health(coin_list, levelOne_list, level, gameLevel, enemyCount)
                            enemy.Reproduce(tempBandit_list)
                            enemy.Animation()
                        #endfor
                    #endif
                    if gamePhase == 8 or gamePhase == 15:
                        for enemy in tempBandit_list:
                            if enemy.rect.x < 0:
                                enemy.ChangeSpeed(1)
                                enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                enemy.Animation()
                            elif enemy.rect.x > 1500:
                                enemy.ChangeSpeed(0)
                                enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                enemy.Animation()
                            else:
                                enemy.Attack()
                                enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                enemy.AttackChecker()
                                enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                if not gameOver:
                                    enemy.Control(player_list)
                                #endif
                                enemy.Hurt()
                                enemy.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                                enemy.FireBallDetection(levelOne_list, fireBall_list)
                                enemy.Health(coin_list, levelOne_list, level, gameLevel, enemyCount)
                                enemy.Reproduce(tempBandit_list)
                                enemy.Animation()
                            #endif
                        #endfor
                    #endif
                    #Player Movement
                    for player in player_list:
                        #Detection
                        player.EnemyAttackDetection(leftEnemyAttack_list, rightEnemyAttack_list)
                        if gamePhase == 19:
                            player.RogueDetection(rogueAttack_list)
                        #endif
                        #Blocked
                        player.Blocked(live, shieldNum)
                        #Hurt
                        player.Hurt()
                        #Attack
                        player.Attack()
                        #Roll
                        player.Roll()
                        #Horizontal Movement
                        if gamePhase != 9 and gamePhase != 10 and gamePhase != 16 and gamePhase != 17 and gamePhase != 25 and gamePhase != 26 and gamePhase != 27 and gamePhase != 28 and gamePhase != 34 and gamePhase != 35 and gamePhase != 36 and gamePhase != 37:
                            player.MoveHori(block1_list) #Player move horizontally
                        else:
                            player.MoveHori2(block1_list)
                        #endif
                        #Spell
                        player.Spell(fireBall_list, levelOne_list)
                        #Attack Checker
                        player.AttackChecker()
                        #Vertical Movement
                        player.MoveVert(block1_list)
                        #Health
                        player.Health(live)
                        #Animation
                        player.Animation()
                    #endfor
                    if gamePhase == 1:
                        conversation = True
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = 165
                            #endfor
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[0], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[1], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[2], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gamePhase = 2
                            gameChat = 1
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                            for warlock in warlock_list:
                                warlock.ChangeSpeed(1)
                            #endfor
                            for rogue in rogue_list:
                                rogue.ChangeSpeed(0)
                            #endfor
                        #endif
                    elif gamePhase == 2:
                        if warlock.rect.x >= 675:
                            warlock.rect.x = 675
                            for warlock in warlock_list:
                                warlock.ChangeSpeed(2)
                            #endfor
                            for rogue in rogue_list:
                                rogue.ChangeSpeed(2)
                                rogue.SATrigger(690)
                            #endfor
                            gamePhase = 3
                        #endif
                    elif gamePhase == 3:#1900
                        if not warlockMove:
                            if timeUp[0] == 0:
                                timer.Counter(900, timeUp)
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                warlockMove = True
                            #endif
                        elif warlockMove:
                            if timeUp[0] == 0:
                                timer.Counter(1000, timeUp)
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                warlockMove = False
                                gamePhase = 4
                            #endif
                        #endif
                    elif gamePhase == 4:
                        if gameChat == 1:
                            warlockDodgeTime = 0
                            for triangle in yellowTriangle_list:
                                for rogue in rogue_list:
                                    triangle.rect.x = rogue.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[3], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            for triangle in yellowTriangle_list:
                                for warlock in warlock_list:
                                    triangle.rect.x = warlock.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[25], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[26], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[27], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 8
                        elif gameChat == 8:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 9:
                            for triangle in yellowTriangle_list:
                                for rogue in rogue_list:
                                    triangle.rect.x = rogue.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[28], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 10
                        elif gameChat == 10:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 11:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                            gameChat = 0
                            gamePhase = 5
                            gameChat = 1
                        #endif
                    elif gamePhase == 5:
                        for bandit in banditGroup1_list:
                            bandit.ChangeSpeed(0)
                        #endfor
                        for rogue in rogue_list:
                            rogue.ChangeSpeed(1)
                        #endfor
                        for rogue in rogue_list:
                            if rogue.rect.x >= 1700:
                                timeUp[0] = 0
                                gamePhase = 6
                                endTimer = 0
                                startTimer = 0
                                for bandit in banditGroup1_list:
                                    bandit.ChangeSpeed(2)
                                #endfor
                                for warlock in warlock_list:
                                    warlock.ChangeSpeed(2)
                                #endfor
                                rogue.ChangeSpeed(0)
                                rogue.ChangeSpeed(2)
                                rogue.rect.x = 2210
                                rogue.rect.y = 290
                                rogue.Animation()
                            #endif
                        #endfor
                    elif gamePhase == 6:
                        if timeUp[0] == 0:
                            timer.Counter(600, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 7
                            endTimer = 0
                            startTimer = 0
                            for enemy in banditGroup1_list:
                                enemy.AttackStance(1)
                            #endfor
                            for warlock in warlock_list:
                                warlock.EscapeTrigger()
                            #endfor
                        #endif
                    elif gamePhase == 7:
                        if timeUp[0] == 0:
                            timer.Counter(1200, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 8
                            enemyCount = [12]
                            for player in player_list:
                                player.FreezeTrigger(0)
                                conversation = False
                            #endfor
                        #endif
                    elif gamePhase == 8:
                        if enemyCount == [0] and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                timer.Counter(1200, timeUp)
                                conversation = True
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                gamePhase = 9
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    conversation = False
                                #endfor
                                readyToUpgrade = True
                                DrawOrRemove(1, levelOne_list, upgradeButton_list)
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 9:
                        if player.rect.x < 1550:
                            for arrow in directionArrow_list:
                                arrow.ArrowUpdate(levelOne_list)
                            #endfor
                        elif player.rect.x >= 1550:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                    player.ResetForTransition()
                                #endfor
                                timer.Counter(1000, timeUp)
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for arrow in directionArrow_list:
                                    arrow.ArrowReset(levelOne_list)
                                #endfor
                                readyToUpgrade = False
                                DrawOrRemove(0, levelOne_list, upgradeButton_list)
                                player.rect.x = 1550
                                gamePhase = 10
                                for coin in coin_list:
                                    levelOne_list.remove(coin)
                                    coin_list.remove(coin)
                                    currency[3] += 1
                                    if currency[3] == 10:
                                        currency[2] += 1
                                        currency[3] = 0
                                    #endif
                                    if currency[2] == 10:
                                        currency[1] += 1
                                        currency[2] = 0
                                    #endif
                                    if currency[1] == 10:
                                        currency[0] += 1
                                        currency[1] = 0
                                    #endif
                                    if currency[0] == 10:
                                        currency[0] = 0
                                        currency[1] = 0
                                        currency[2] = 0
                                        currency[3] = 0
                                    #endif
                                #endfor
                            #endif
                        #endif
                    elif gamePhase == 10:
                        if player.rect.x > 50:
                            for player in player_list:
                                player.FreezeTrigger(1)
                            #endfor
                            player.rect.x -= 10
                            for block in block1_list:
                                block.rect.x -= 10
                            #endfor
                            for warlock in warlock_list:
                                warlock.rect.x -= 10
                                warlock.Animation()
                            #endfor
                            for enemy in banditGroup1_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for enemy in tempBandit_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for rogue in rogue_list:
                                rogue.rect.x -= 10
                                rogue.Animation()
                            #endfor
                            for bandit in banditGroup2_list:
                                bandit.rect.x -= 10
                            #endfor
                            for background in background1_list:
                                background.BackUpdate()
                            #endfor
                            for ground in ground_list:
                                ground.Update(1)
                            #endfor
                        elif player.rect.x == 50:
                            gamePhase = 11
                            for ground in ground_list:
                                ground.Update(0)
                            #endfor
                        #endif
                    elif gamePhase == 11:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = 725
                                for rogue in rogue_list:
                                    triangle.rect.y = rogue.rect.y - 40
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[4], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gameChat = 0
                            gamePhase = 12
                            gameChat = 1
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                                triangle.rect.y = 670
                            #endfor
                        #endif
                    elif gamePhase == 12:
                        for rogue in rogue_list:
                            rogue.SATrigger(1800)
                        #endfor
                        gamePhase = 13
                    elif gamePhase == 13:
                        if timeUp[0] == 0:
                            timer.Counter(1000, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 14
                            for enemy in banditGroup2_list:
                                enemy.AttackStance(1)
                            #endfor
                        #endif
                    elif gamePhase == 14:
                        if timeUp[0] == 0:
                            timer.Counter(600, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 15
                            enemyCount = [30]
                            for player in player_list:
                                player.FreezeTrigger(0)
                                conversation = False
                            #endfor
                        #endif
                    elif gamePhase == 15:
                        if enemyCount == [0] and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                timer.Counter(1200, timeUp)
                                conversation = True
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                gamePhase = 16
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    conversation = False
                                #endfor
                                readyToUpgrade = True
                                DrawOrRemove(1, levelOne_list, upgradeButton_list)
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 16:
                        if player.rect.x < 1550:
                            for arrow in directionArrow_list:
                                arrow.ArrowUpdate(levelOne_list)
                            #endfor
                        elif player.rect.x >= 1550:
                            if timeUp[0] == 0:
                                timer.Counter(1000, timeUp)
                                for player in player_list:
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                    player.ResetForTransition()
                                #endfor
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for arrow in directionArrow_list:
                                    arrow.ArrowReset(levelOne_list)
                                #endfor
                                readyToUpgrade = False
                                DrawOrRemove(0, levelOne_list, upgradeButton_list)
                                player.rect.x = 1550
                                for rogue in rogue_list:
                                    rogue.ChangeSpeed(0)
                                    rogue.ChangeSpeed(2)
                                    rogue.Unrandom()
                                    rogue.rect.x = 2870
                                    rogue.rect.y = 710
                                #endfor
                                gamePhase = 17
                                for coin in coin_list:
                                    levelOne_list.remove(coin)
                                    coin_list.remove(coin)
                                    currency[3] += 1
                                    if currency[3] == 10:
                                        currency[2] += 1
                                        currency[3] = 0
                                    #endif
                                    if currency[2] == 10:
                                        currency[1] += 1
                                        currency[2] = 0
                                    #endif
                                    if currency[1] == 10:
                                        currency[0] += 1
                                        currency[1] = 0
                                    #endif
                                    if currency[0] == 10:
                                        currency[0] = 0
                                        currency[1] = 0
                                        currency[2] = 0
                                        currency[3] = 0
                                    #endif
                                #endfor
                            #endif
                        #endif
                    elif gamePhase == 17:
                        if player.rect.x > 50:
                            player.rect.x -= 10
                            for block in block1_list:
                                block.rect.x -= 10
                            #endfor
                            for rogue in rogue_list:
                                rogue.rect.x -= 10
                                rogue.Animation()
                            #endfor
                            for bandit in banditGroup2_list:
                                bandit.rect.x -= 10
                                bandit.Animation()
                            #endfor
                            for enemy in tempBandit_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for background in background1_list:
                                background.BackUpdate()
                            #endfor
                            for ground in ground_list:
                                ground.Update(1)
                            #endfor
                        elif player.rect.x == 50:
                            gamePhase = 18
                            for ground in ground_list:
                                ground.Update(0)
                            #endfor
                        #endif
                    elif gamePhase == 18:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for rogue in rogue_list:
                                    triangle.rect.x = rogue.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[5], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[6], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gamePhase = 19
                            gameChat = 1
                            enemyCount = [1]
                            player.FreezeTrigger(0)
                            conversation = False
                            for rogue in rogue_list:
                                rogue.HealthDisplay(1, levelOne_list)
                            #endfor
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 19:
                        if enemyCount == [0] and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                conversation = True
                                timer.Counter(500, timeUp)
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                gamePhase = 20
                                enemyCount[0] = -1
                            #endif
                        #endif
                        if live[0] <= 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 20:
                        for rogue in rogue_list:
                            posX = rogue.rect.x
                        #endfor
                        for warlock in warlock_list:
                            warlock.Reappear(posX)
                        #endfor
                        gamePhase = 21
                    elif gamePhase == 21:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for warlock in warlock_list:
                                    triangle.rect.x = warlock.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[8], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[9], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 4
                            for rogue in rogue_list:
                                rogue.TurnAround()
                            #endfor
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[10], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gamePhase = 22
                            gameChat = 1
                            for player in player_list:
                                player.FreezeTrigger(0)
                            #endfor
                            conversation = False
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 22:
                        for rogue in rogue_list:
                            rogue.Death(rogueDead)
                        #endfor
                        if odenHealth[0] == 4:
                            gameMode[0] = 1
                            gamePhase = 29
                            conversation = True
                            for player in player_list:
                                player.ChangeSpeed(2)
                                player.FreezeTrigger(1)
                                player.LimitMovement(1)
                            #endfor
                        elif rogueDead[0] == 0:
                            rogueDead[0] = 1
                            gameMode[0] = 0
                            gamePhase = 23
                            conversation = True
                            for player in player_list:
                                player.ChangeSpeed(2)
                                player.FreezeTrigger(1)
                            #endfor
                        #endif
                    elif gamePhase == 23:
                        if gameChat == 1:
                            for player in player_list:
                                player.FreezeTrigger(0)
                                player.ChangeSpeed(2)
                                player.FreezeTrigger(1)
                            #endfor
                            for triangle in yellowTriangle_list:
                                for warlock in warlock_list:
                                    triangle.rect.x = warlock.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[11], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[12], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[13], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[14], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 8
                        elif gameChat == 8:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 9:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gamePhase = 24
                            gameChat = 1
                            for warlock in warlock_list:
                                warlock.ChangeSpeed(1)
                            #endfor
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 24:
                        for warlock in warlock_list:
                            if warlock.rect.x >= 1550:
                                warlock.ChangeSpeed(2)
                                gamePhase = 25
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                #endfor
                                conversation = False
                                readyToUpgrade = True
                                DrawOrRemove(1, levelOne_list, upgradeButton_list)
                            #endif
                        #endfor
                    elif gamePhase == 25:
                        if player.rect.x < 1550:
                            for arrow in directionArrow_list:
                                arrow.ArrowUpdate(levelOne_list)
                            #endfor
                        elif player.rect.x >= 1550:
                            if timeUp[0] == 0:
                                timer.Counter(1000, timeUp)
                                for player in player_list:
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                    player.ResetForTransition()
                                #endfor
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for arrow in directionArrow_list:
                                    arrow.ArrowReset(levelOne_list)
                                #endfor
                                player.rect.x = 1600
                                for rogue in rogue_list:
                                    rogue.HealthDisplay(0, levelOne_list)
                                #endfor
                                gamePhase = 26
                                readyToUpgrade = False
                                DrawOrRemove(0, levelOne_list, upgradeButton_list)
                                for coin in coin_list:
                                    levelOne_list.remove(coin)
                                    coin_list.remove(coin)
                                    currency[3] += 1
                                    if currency[3] == 10:
                                        currency[2] += 1
                                        currency[3] = 0
                                    #endif
                                    if currency[2] == 10:
                                        currency[1] += 1
                                        currency[2] = 0
                                    #endif
                                    if currency[1] == 10:
                                        currency[0] += 1
                                        currency[1] = 0
                                    #endif
                                    if currency[0] == 10:
                                        currency[0] = 0
                                        currency[1] = 0
                                        currency[2] = 0
                                        currency[3] = 0
                                    #endif
                                #endfor
                                DrawOrRemove(0, levelOne_list, pauseButton_list)
                            #endif
                        #endif
                    elif gamePhase == 26:
                        if gameChat == 1:
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[7], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gamePhase = 27
                            gameChat = 1
                        #endif
                    elif gamePhase == 27:
                        DrawOrRemove(1, levelOne_list, nextLevelBlock_list)
                        gamePhase = 28
                        SaveProgress(currentFile, currency,live,gameLevel+1, shieldNum, playerLevel, gameMode)
                        advanceLevel = True
                    elif gamePhase == 29:
                        gamePhase = 30
                    elif gamePhase == 30: #If Warlock gets killed
                        if gameChat == 1:
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[22], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 2
                            for player in player_list:
                                player.FreezeTrigger(1)
                            #endfor
                            conversation = True
                        elif gameChat == 2:
                            if timeUp[0] == 0:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                DrawOrRemove(0, levelOne_list, currentLine_list)
                                DrawOrRemove(0, levelOne_list, wordBox_list)
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                #endfor
                                conversation = False
                                gameChat = 3
                            #endif
                        elif gameChat == 3:
                            if odenHealth[0] == 3:
                                DrawOrRemove(1, levelOne_list, wordBox_list)
                                WriteWords(1, script1[23], 0, 815, levelOne_list, currentLine_list)
                                gameChat = 4
                                for player in player_list:
                                    player.FreezeTrigger(1)
                                #endfor
                                conversation = True
                            #endif
                        elif gameChat == 4:
                            if timeUp[0] == 0:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                DrawOrRemove(0, levelOne_list, currentLine_list)
                                DrawOrRemove(0, levelOne_list, wordBox_list)
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                #endfor
                                conversation = False
                                gameChat = 5
                            #endif
                        elif gameChat == 5:
                            if odenHealth[0] == 2:
                                DrawOrRemove(1, levelOne_list, wordBox_list)
                                WriteWords(1, script1[24], 0, 815, levelOne_list, currentLine_list)
                                gameChat = 6
                                for player in player_list:
                                    player.FreezeTrigger(1)
                                #endfor
                                conversation = True
                            #endif
                        elif gameChat == 6:
                            if timeUp[0] == 0:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                DrawOrRemove(0, levelOne_list, currentLine_list)
                                DrawOrRemove(0, levelOne_list, wordBox_list)
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                #endfor
                                conversation = False
                                gameChat = 8
                            #endif
                        elif gameChat == 8:
                            if odenHealth[0] == 1:
                                gameChat = 9
                                conversation = True
                                for player in player_list:
                                    player.FreezeTrigger(1)
                                    player.LimitMovement(0)
                                #endfor
                            #endif
                        elif gameChat == 9:
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[30], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 10
                        elif gameChat == 10:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 11:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[31], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 12
                        elif gameChat == 12:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 13:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[32], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 14
                        elif gameChat == 14:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 15:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[33], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 16
                        elif gameChat == 16:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 17:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[34], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 18
                        elif gameChat == 18:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 19:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gamePhase = 31
                            for warlock in warlock_list:
                                warlock.EscapeTrigger()
                            #endfor
                            gameChat = 1
                        #endif
                    elif gamePhase == 31:
                        if timeUp[0] == 0:
                            timer.Counter(1000, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            for rogue in rogue_list:
                                posX = rogue.rect.x
                            #endfor
                            for player in player_list:
                                player.TurnAround(posX)
                            #endfor
                            gamePhase = 32
                        #endif
                    elif gamePhase == 32:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for rogue in rogue_list:
                                    triangle.rect.x = rogue.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[15], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[16], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[17], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[18], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 8
                        elif gameChat == 8:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 9:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[19], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 10
                        elif gameChat == 10:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 11:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[20], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 12
                        elif gameChat == 12:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 13:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[21], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 14
                        elif gameChat == 14:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 15:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gamePhase = 33
                            gameChat = 1
                            for rogue in rogue_list:
                                rogue.ChangeSpeed(1)
                            #endfor
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 33:
                        for rogue in rogue_list:
                            if rogue.rect.x >= 1550:
                                rogue.ChangeSpeed(2)
                                gamePhase = 34
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                #endfor
                                conversation = False
                                readyToUpgrade = True
                                DrawOrRemove(1, levelOne_list, upgradeButton_list)
                            #endif
                        #endfor
                    elif gamePhase == 34:
                        if player.rect.x < 1550:
                            for arrow in directionArrow_list:
                                arrow.ArrowUpdate(levelOne_list)
                            #endfor
                        elif player.rect.x >= 1550:
                            if timeUp[0] == 0:
                                timer.Counter(1000, timeUp)
                                for player in player_list:
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                    player.ResetForTransition()
                                #endfor
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for arrow in directionArrow_list:
                                    arrow.ArrowReset(levelOne_list)
                                #endfor
                                player.rect.x = 1600
                                for rogue in rogue_list:
                                    rogue.HealthDisplay(0, levelOne_list)
                                #endfor
                                gamePhase = 35
                                readyToUpgrade = False
                                DrawOrRemove(0, levelOne_list, upgradeButton_list)
                                for coin in coin_list:
                                    levelOne_list.remove(coin)
                                    coin_list.remove(coin)
                                    currency[3] += 1
                                    if currency[3] == 10:
                                        currency[2] += 1
                                        currency[3] = 0
                                    #endif
                                    if currency[2] == 10:
                                        currency[1] += 1
                                        currency[2] = 0
                                    #endif
                                    if currency[1] == 10:
                                        currency[0] += 1
                                        currency[1] = 0
                                    #endif
                                    if currency[0] == 10:
                                        currency[0] = 0
                                        currency[1] = 0
                                        currency[2] = 0
                                        currency[3] = 0
                                    #endif
                                #endfor
                                DrawOrRemove(0, levelOne_list, pauseButton_list)
                            #endif
                        #endif
                    elif gamePhase == 35:
                        if gameChat == 1:
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[7], 0, 815, levelOne_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gamePhase = 36
                            gameChat = 1
                        #endif
                    elif gamePhase == 36:
                        DrawOrRemove(1, levelOne_list, nextLevelBlock_list)
                        gamePhase = 37
                        SaveProgress(currentFile, currency,live,gameLevel+1, shieldNum, playerLevel, gameMode)
                        advanceLevel = True
                    #endif
                    levelOne_list.draw(screen) #Display all visible objects
                elif gameLevel == 2 and gameMode[0] == 0: #Level2 Genocide--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    screen.fill(FORESTWHITE)
                    for button in button_list: #Button Change
                        button.Change(pos, level)
                    #endfor
                    for coin in coin_list:#Coins
                        coin.Change()
                        coin.CoinUpdate(player_list, block2_list, levelTwo_list, coin_list, currency)
                    #endfor
                    for fireball in fireBall_list:#Fire Ball
                        fireball.EffectUpdate(levelTwo_list)
                        if fireball.rect.x > 1500 or fireball.rect.x < -160:
                            fireball.DeleteSelf(levelTwo_list, fireBall_list)
                        #endif
                    #endfor
                    for thousand in thousand_list:
                        thousand.Update(currency[0])
                    #endfor
                    for hundred in hundred_list:
                        hundred.Update(currency[1])
                    #endfor
                    for ten in ten_list:
                        ten.Update(currency[2])
                    #endfor
                    for one in one_list:
                        one.Update(currency[3])
                    #endfor
                    #Player Movement
                    for player in player_list:
                        #Detection
                        player.EnemyAttackDetection(leftEnemyAttack_list, rightEnemyAttack_list)
                        #Javelin Detection
                        player.JavelinAttackDetection(leftJavelin_list, rightJavelin_list, levelTwo_list)
                        #Mushroom Detection
                        player.MushroomDetection(mushroomAttack_list)
                        #Blocked
                        player.Blocked(live, shieldNum)
                        #Hurt
                        player.Hurt()
                        #Spell
                        player.Spell(fireBall_list, levelTwo_list)
                        #Attack
                        player.Attack()
                        #Roll
                        player.Roll()
                        #Horizontal Movement
                        if gamePhase != 6 and gamePhase != 7 and gamePhase != 13 and gamePhase != 14 and gamePhase != 20 and gamePhase != 21 and gamePhase != 22 and gamePhase != 23:
                            player.MoveHori(block2_list) #Player move horizontally
                        else:
                            player.MoveHori2(block2_list)
                        #endif
                        #Attack Checker
                        player.AttackChecker()
                        #Vertical Movement
                        player.MoveVert(block2_list)
                        #Health
                        player.Health(live)
                        #Animation
                        player.Animation()
                    #endfor
                    if gamePhase >= 17:
                        for warlock in warlock2_list:
                            if gamePhase == 20:
                                for player in player_list:
                                    warlock.Face(player.rect.x)
                                #endfor
                            #endif
                            warlock.MoveHori(block2_list)
                            warlock.MoveVert(block2_list)
                            warlock.Health(odenHealth)
                            warlock.Escape()
                            warlock.Appear()
                            warlock.Animation()
                        #endfor
                    #endif
                    if gamePhase <= 5 or (gamePhase >= 7 and gamePhase <= 10) or (gamePhase >= 14 and gamePhase <= 17):
                        for arun in arun_list:
                            if gamePhase == 17:
                                arun.Control(player.rect.x, player.rect.y)
                            #endif
                            arun.Attack()
                            arun.MoveHori(block2_list)
                            arun.AttackChecker()
                            arun.MoveVert(block2_list)
                            arun.Hurt()
                            arun.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            arun.Health(levelTwo_list, coin_list, enemyCount, mehiraDefeat)
                            arun.FireBallDetection(levelTwo_list, fireBall_list)
                            arun.Throw(leftJavelin_list, rightJavelin_list, levelTwo_list)
                            arun.Animation()
                        #endfor
                    #endif
                    if gamePhase <= 5:
                        for mushroom in mushroomGroup1_list:
                            if gamePhase == 5:
                                mushroom.Control()
                            #endif
                            mushroom.Attack()
                            mushroom.MoveHori(block2_list)
                            mushroom.MoveVert(block2_list)
                            mushroom.Hurt()
                            mushroom.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            mushroom.Health(enemyCount)
                            mushroom.FireBallDetection(levelTwo_list, fireBall_list)
                            mushroom.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 7 and gamePhase <= 12:
                        for mushroom in mushroomGroup2_list:
                            if gamePhase == 12:
                                mushroom.Control()
                            #endif
                            mushroom.Attack()
                            mushroom.MoveHori(block2_list)
                            mushroom.MoveVert(block2_list)
                            mushroom.Hurt()
                            mushroom.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            mushroom.FireBallDetection(levelTwo_list, fireBall_list)
                            mushroom.Health(enemyCount)
                            mushroom.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 14 and gamePhase <= 17:
                        for mushroom in mushroomGroup3_list:
                            if gamePhase == 17:
                                mushroom.Control()
                            #endif
                            mushroom.Attack()
                            mushroom.MoveHori(block2_list)
                            mushroom.MoveVert(block2_list)
                            mushroom.Hurt()
                            mushroom.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            mushroom.FireBallDetection(levelTwo_list, fireBall_list)
                            mushroom.Health(enemyCount)
                            mushroom.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 1 and gamePhase <= 5:
                        #Bandit Movement
                        for enemy in banditGroup3_list:
                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            if gamePhase == 5 and not gameOver:
                                enemy.Control(player_list)
                            #endif
                            enemy.Hurt()
                            enemy.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            enemy.FireBallDetection(levelTwo_list, fireBall_list)
                            enemy.Health(coin_list, levelTwo_list, level, gameLevel, enemyCount)
                            enemy.Reproduce(tempBandit_list)
                            enemy.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 7 and gamePhase <= 12:#Bandit Group 4
                        #Bandit Movement
                        for enemy in banditGroup4_list:
                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            if gamePhase == 12 and not gameOver:
                                enemy.Control(player_list)
                            #endif
                            enemy.Hurt()
                            enemy.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            enemy.FireBallDetection(levelTwo_list, fireBall_list)
                            enemy.Health(coin_list, levelTwo_list, level, gameLevel, enemyCount)
                            enemy.Reproduce(tempBandit_list)
                            enemy.Animation()
                        #endfor
                    #endif
                    if gamePhase == 5 or gamePhase == 12:#Temporary Bandit
                        for enemy in tempBandit_list:
                            if enemy.rect.x < 0:
                                enemy.ChangeSpeed(1)
                                enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                enemy.Animation()
                            elif enemy.rect.x > 1500:
                                enemy.ChangeSpeed(0)
                                enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                enemy.Animation()
                            else:
                                enemy.Attack()
                                enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                enemy.AttackChecker()
                                enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                if not gameOver:
                                    enemy.Control(player_list)
                                #endif
                                enemy.Hurt()
                                enemy.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                                enemy.FireBallDetection(levelTwo_list, fireBall_list)
                                enemy.Health(coin_list, levelTwo_list, level, gameLevel, enemyCount)
                                enemy.Reproduce(tempBandit_list)
                                enemy.Animation()
                            #endif
                        #endfor
                    #endif
                    if gamePhase == 17:
                        for javelin in leftJavelin_list:
                            javelin.JavelinUpdate(leftJavelin_list, rightJavelin_list, levelTwo_list)
                        #endfor
                        for javelin in rightJavelin_list:
                            javelin.JavelinUpdate(leftJavelin_list, rightJavelin_list, levelTwo_list)
                        #endfor
                    #endif
                    if gamePhase == 1:
                        conversation = True
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for arun in arun_list:
                                    triangle.rect.x = arun.rect.x
                                #endfor
                            #endfor
                            for arun in arun_list:
                                arun.SetDeathHp(0)
                            #endfor
                            for player in player_list:
                                player.FreezeTrigger(0)
                                player.ChangeSpeed(2)
                                player.FreezeTrigger(1)
                            #endfor
                            DrawOrRemove(1, levelTwo_list, wordBox_list)
                            WriteWords(1, script2[0], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[1], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            DrawOrRemove(0, levelTwo_list, wordBox_list)
                            gamePhase = 2
                            gameChat = 1
                            for arun in arun_list:
                                arun.ChangeSpeed(1)
                            #endfor
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 2:
                        for arun in arun_list:
                            if arun.rect.x >= 1600:
                                arun.ChangeSpeed(0)
                                arun.ChangeSpeed(2)
                                arun.rect.x = 2900
                                gamePhase = 3
                            #endif
                        #endfor
                    elif gamePhase == 3:
                        if timeUp[0] == 0:
                            timer.Counter(900, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 4
                            endTimer = 0
                            startTimer = 0
                            for enemy in banditGroup3_list:
                                enemy.AttackStance(1)
                            #endfor
                        #endif
                    elif gamePhase == 4:
                        if timeUp[0] == 0:
                            timer.Counter(1000, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 5
                            endTimer = 0
                            startTimer = 0
                            enemyCount[0] = 14
                            for player in player_list:
                                player.FreezeTrigger(0)
                                conversation = False
                            #endfor
                        #endif
                    elif gamePhase == 5:
                        if enemyCount == [0] and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                timer.Counter(1200, timeUp)
                                conversation = True
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                gamePhase = 6
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                #endfor
                                conversation = False
                                readyToUpgrade = True
                                DrawOrRemove(1, levelTwo_list, upgradeButton_list)
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 6:
                        if player.rect.x < 1550:
                            for arrow in directionArrow_list:
                                arrow.ArrowUpdate(levelTwo_list)
                            #endfor
                        elif player.rect.x >= 1550:
                            if timeUp[0] == 0:
                                timer.Counter(1000, timeUp)
                                for player in player_list:
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                    player.ResetForTransition()
                                #endfor
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for arrow in directionArrow_list:
                                    arrow.ArrowReset(levelTwo_list)
                                #endfor
                                readyToUpgrade = False
                                DrawOrRemove(0, levelTwo_list, upgradeButton_list)
                                player.rect.x = 1550
                                gamePhase = 7
                                for coin in coin_list:
                                    levelTwo_list.remove(coin)
                                    coin_list.remove(coin)
                                    currency[3] += 1
                                    if currency[3] == 10:
                                        currency[2] += 1
                                        currency[3] = 0
                                    #endif
                                    if currency[2] == 10:
                                        currency[1] += 1
                                        currency[2] = 0
                                    #endif
                                    if currency[1] == 10:
                                        currency[0] += 1
                                        currency[1] = 0
                                    #endif
                                    if currency[0] == 10:
                                        currency[0] = 0
                                        currency[1] = 0
                                        currency[2] = 0
                                        currency[3] = 0
                                    #endif
                                #endfor
                            #endif
                        #endif
                    elif gamePhase == 7:
                        if player.rect.x > 50:
                            player.rect.x -= 10
                            for block in block2_list:
                                block.rect.x -= 10
                            #endfor
                            for arun in arun_list:
                                arun.rect.x -= 10
                                arun.Animation()
                            #endfor
                            for enemy in banditGroup4_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for enemy in tempBandit_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for mushroom in mushroomGroup2_list:
                                mushroom.rect.x -= 10
                                mushroom.Animation()
                            #endfor
                            for mushroom in mushroomGroup1_list:
                                mushroom.rect.x -= 10
                                mushroom.Animation()
                            #endfor
                            for bandit in banditGroup3_list:
                                bandit.rect.x -= 10
                                bandit.Animation()
                            #endfor
                            for background in background2_list:
                                background.BackUpdate()
                            #endfor
                            for ground in ground_list:
                                ground.Update(1)
                            #endfor
                        elif player.rect.x == 50:
                            gamePhase = 8
                            for ground in ground_list:
                                ground.Update(0)
                            #endfor
                        #endif
                    elif gamePhase == 8:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for arun in arun_list:
                                    triangle.rect.x = arun.rect.x
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelTwo_list, wordBox_list)
                            WriteWords(1, script2[2], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[3], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            DrawOrRemove(0, levelTwo_list, wordBox_list)
                            gamePhase = 9
                            gameChat = 1
                            for arun in arun_list:
                                arun.ChangeSpeed(1)
                            #endfor
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 9:
                        for arun in arun_list:
                            if arun.rect.x >= 1600:
                                arun.ChangeSpeed(0)
                                arun.ChangeSpeed(2)
                                arun.rect.x = 2900
                                gamePhase = 10
                            #endif
                        #endfor
                    elif gamePhase == 10:
                        if timeUp[0] == 0:
                            timer.Counter(900, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 11
                            endTimer = 0
                            startTimer = 0
                            for enemy in banditGroup4_list:
                                enemy.AttackStance(1)
                            #endfor
                        #endif
                    elif gamePhase == 11:
                        if timeUp[0] == 0:
                            timer.Counter(1000, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 12
                            endTimer = 0
                            startTimer = 0
                            enemyCount[0] = 24
                            for player in player_list:
                                player.FreezeTrigger(0)
                                conversation = False
                            #endfor
                        #endif
                    elif gamePhase == 12:
                        if enemyCount == [0] and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                timer.Counter(1200, timeUp)
                                conversation = True
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                gamePhase = 13
                                readyToUpgrade = True
                                DrawOrRemove(1, levelTwo_list, upgradeButton_list)
                                conversation = False
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                #endfor
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 13:
                        if player.rect.x < 1550:
                            for arrow in directionArrow_list:
                                arrow.ArrowUpdate(levelTwo_list)
                            #endfor
                        elif player.rect.x >= 1550:
                            if timeUp[0] == 0:
                                timer.Counter(1000, timeUp)
                                for player in player_list:
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                    player.ResetForTransition()
                                #endfor
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for arrow in directionArrow_list:
                                    arrow.ArrowReset(levelTwo_list)
                                #endfor
                                readyToUpgrade = False
                                DrawOrRemove(0, levelTwo_list, upgradeButton_list)
                                player.rect.x = 1550
                                gamePhase = 14
                                for mushroom in mushroomGroup3_list:
                                    mushroom.rect.x = randint(1700, 2800)
                                #endfor
                                for coin in coin_list:
                                    levelTwo_list.remove(coin)
                                    coin_list.remove(coin)
                                    currency[3] += 1
                                    if currency[3] == 10:
                                        currency[2] += 1
                                        currency[3] = 0
                                    #endif
                                    if currency[2] == 10:
                                        currency[1] += 1
                                        currency[2] = 0
                                    #endif
                                    if currency[1] == 10:
                                        currency[0] += 1
                                        currency[1] = 0
                                    #endif
                                    if currency[0] == 10:
                                        currency[0] = 0
                                        currency[1] = 0
                                        currency[2] = 0
                                        currency[3] = 0
                                    #endif
                                #endfor
                            #endif
                        #endif
                    elif gamePhase == 14:
                        if player.rect.x > 50:
                            player.rect.x -= 10
                            for block in block2_list:
                                block.rect.x -= 10
                            #endfor
                            for arun in arun_list:
                                arun.rect.x -= 10
                                arun.Animation()
                            #endfor
                            for enemy in banditGroup4_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for enemy in tempBandit_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for mushroom in mushroomGroup2_list:
                                mushroom.rect.x -= 10
                                mushroom.Animation()
                            #endfor
                            for mushroom in mushroomGroup3_list:
                                mushroom.rect.x -= 10
                                mushroom.Animation()
                            #endfor
                            for background in background2_list:
                                background.BackUpdate()
                            #endfor
                            for ground in ground_list:
                                ground.Update(1)
                            #endfor
                        elif player.rect.x == 50:
                            gamePhase = 15
                            for ground in ground_list:
                                ground.Update(0)
                            #endfor
                        #endif
                    elif gamePhase == 15:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for arun in arun_list:
                                    triangle.rect.x = arun.rect.x
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelTwo_list, wordBox_list)
                            WriteWords(1, script2[4], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            DrawOrRemove(0, levelTwo_list, wordBox_list)
                            gamePhase = 16
                            gameChat = 1
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 16:
                        if timeUp[0] == 0:
                            timer.Counter(1000, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 17
                            endTimer = 0
                            startTimer = 0
                            enemyCount[0] = 3
                            for arun in arun_list:
                                arun.HealthDisplay(1, levelTwo_list)
                            #endfor
                            for player in player_list:
                                player.FreezeTrigger(0)
                                conversation = False
                            #endfor
                        #endif
                    elif gamePhase == 17:
                        if enemyCount == [0] and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                #endfor
                                timer.Counter(1200, timeUp)
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                gamePhase = 18
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 18:
                        for warlock in warlock2_list:
                            for player in player_list:
                                if player.rect.x <= 1350:
                                    warlock.ChangeSpeed(2)
                                    warlock.AppearTrigger(player.rect.x + 70)
                                    warlock.Turn(0)
                                    player.Turn(1)
                                    gamePhase = 19
                                elif player.rect.x >= 1350:
                                    warlock.ChangeSpeed(2)
                                    warlock.AppearTrigger(player.rect.x - 100)
                                    player.Turn(0)
                                    gamePhase = 19
                                #endif
                            #endfor
                        #endfor
                    elif gamePhase == 19:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for warlock in warlock2_list:
                                    triangle.rect.x = warlock.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelTwo_list, wordBox_list)
                            WriteWords(1, script2[23], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[24], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[25], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            DrawOrRemove(0, levelTwo_list, wordBox_list)
                            gamePhase = 20
                            gameChat = 1
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                            conversation = False
                            for player in player_list:
                                player.FreezeTrigger(0)
                            #endfor
                            readyToUpgrade = True
                            DrawOrRemove(1, levelTwo_list, upgradeButton_list)
                        #endif
                    elif gamePhase == 20:
                        if player.rect.x < 1550:
                            for arrow in directionArrow_list:
                                arrow.ArrowUpdate(levelTwo_list)
                            #endfor
                        elif player.rect.x >= 1550:
                            if timeUp[0] == 0:
                                timer.Counter(1000, timeUp)
                                for player in player_list:
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                    player.ResetForTransition()
                                #endfor
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for arrow in directionArrow_list:
                                    arrow.ArrowReset(levelTwo_list)
                                #endfor
                                readyToUpgrade = False
                                DrawOrRemove(0, levelTwo_list, upgradeButton_list)
                                player.rect.x = 1600
                                for arun in arun_list:
                                    arun.HealthDisplay(0, levelTwo_list)
                                #endfor
                                gamePhase = 21
                                DrawOrRemove(0, levelTwo_list, pauseButton_list)
                                for coin in coin_list:
                                    levelTwo_list.remove(coin)
                                    coin_list.remove(coin)
                                    currency[3] += 1
                                    if currency[3] == 10:
                                        currency[2] += 1
                                        currency[3] = 0
                                    #endif
                                    if currency[2] == 10:
                                        currency[1] += 1
                                        currency[2] = 0
                                    #endif
                                    if currency[1] == 10:
                                        currency[0] += 1
                                        currency[1] = 0
                                    #endif
                                    if currency[0] == 10:
                                        currency[0] = 0
                                        currency[1] = 0
                                        currency[2] = 0
                                        currency[3] = 0
                                    #endif
                                #endfor
                                for warlock in warlock2_list:
                                    warlock.EscapeTrigger()
                                #endfor
                            #endif
                        #endif
                    elif gamePhase == 21:
                        if gameChat == 1:
                            DrawOrRemove(1, levelTwo_list, wordBox_list)
                            WriteWords(1, script2[5], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            DrawOrRemove(0, levelTwo_list, wordBox_list)
                            gamePhase = 22
                            gameChat = 1
                        #endif
                    elif gamePhase == 22:
                        DrawOrRemove(1, levelTwo_list, nextLevelBlock_list)
                        gamePhase = 23
                        SaveProgress(currentFile, currency,live,gameLevel+1, shieldNum, playerLevel, gameMode)
                        advanceLevel = True
                    #endif
                    levelTwo_list.draw(screen) #Display all visible objects
                elif gameLevel == 2 and gameMode[0] == 1: #Level2 Version 2--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    screen.fill(FORESTWHITE)
                    for button in button_list: #Button Change
                        button.Change(pos, level)
                    #endfor
                    for coin in coin_list:
                        coin.Change()
                        coin.CoinUpdate(player_list, block2_list, levelTwo_list, coin_list, currency)
                    #endfor
                    for fireball in fireBall_list:
                        fireball.EffectUpdate(levelTwo_list)
                        if fireball.rect.x > 1500 or fireball.rect.x < -160:
                            fireball.DeleteSelf(levelTwo_list, fireBall_list)
                        #endif
                    #endfor
                    for thousand in thousand_list:
                        thousand.Update(currency[0])
                    #endfor
                    for hundred in hundred_list:
                        hundred.Update(currency[1])
                    #endfor
                    for ten in ten_list:
                        ten.Update(currency[2])
                    #endfor
                    for one in one_list:
                        one.Update(currency[3])
                    #endfor
                    #Player Movement
                    for player in player_list:
                        #Detection
                        player.EnemyAttackDetection(leftEnemyAttack_list, rightEnemyAttack_list)
                        #Javelin Detection
                        player.JavelinAttackDetection(leftJavelin_list, rightJavelin_list, levelTwo_list)
                        #Mushroom Detection
                        player.MushroomDetection(mushroomAttack_list)
                        #Blocked
                        player.Blocked(live, shieldNum)
                        #Hurt
                        player.Hurt()
                        #Spell
                        player.Spell(fireBall_list, levelTwo_list)
                        #Attack
                        player.Attack()
                        #Roll
                        player.Roll()
                        #Horizontal Movement
                        if gamePhase != 6 and gamePhase != 7 and gamePhase != 13 and gamePhase != 14 and gamePhase != 17 and gamePhase != 21 and gamePhase != 22 and gamePhase != 23 and gamePhase != 24:
                            player.MoveHori(block2_list) #Player move horizontally
                        else:
                            player.MoveHori2(block2_list)
                        #endif
                        #Attack Checker
                        player.AttackChecker()
                        #Vertical Movement
                        player.MoveVert(block2_list)
                        #Health
                        player.Health(live)
                        #Animation
                        player.Animation()
                    #endfor
                    if gamePhase >= 1:
                        for talene in talene_list:
                            talene.MoveHori(block2_list)
                            talene.MoveVert(block2_list)
                            talene.Hurt()
                            talene.Attack()
                            talene.Health(levelTwo_list, coin_list, enemyCount)
                            talene.SA()
                            talene.Animation()
                        #endfor
                    #endif
                    if gamePhase <= 5 or (gamePhase >= 7 and gamePhase <= 10) or (gamePhase >= 14 and gamePhase <= 21):
                        for arun in arun_list:
                            if gamePhase == 17:
                                arun.Control(player.rect.x, player.rect.y)
                            #endif
                            arun.Attack()
                            arun.MoveHori(block2_list)
                            arun.AttackChecker()
                            arun.MoveVert(block2_list)
                            arun.Hurt()
                            arun.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            arun.Health(levelTwo_list, coin_list, enemyCount, mehiraDefeat)
                            arun.FireBallDetection(levelTwo_list, fireBall_list)
                            arun.Throw(leftJavelin_list, rightJavelin_list, levelTwo_list)
                            arun.Animation()
                        #endfor
                    #endif
                    if gamePhase <= 5:
                        for mushroom in mushroomGroup1_list:
                            if gamePhase == 5:
                                mushroom.Control()
                            #endif
                            mushroom.Attack()
                            mushroom.MoveHori(block2_list)
                            mushroom.MoveVert(block2_list)
                            mushroom.Hurt()
                            mushroom.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            mushroom.Health(enemyCount)
                            mushroom.FireBallDetection(levelTwo_list, fireBall_list)
                            mushroom.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 7 and gamePhase <= 12:
                        for mushroom in mushroomGroup2_list:
                            if gamePhase == 12:
                                mushroom.Control()
                            #endif
                            mushroom.Attack()
                            mushroom.MoveHori(block2_list)
                            mushroom.MoveVert(block2_list)
                            mushroom.Hurt()
                            mushroom.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            mushroom.FireBallDetection(levelTwo_list, fireBall_list)
                            mushroom.Health(enemyCount)
                            mushroom.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 14 and gamePhase <= 24:
                        for mushroom in mushroomGroup3_list:
                            if gamePhase == 17:
                                mushroom.Control()
                            #endif
                            mushroom.Attack()
                            mushroom.MoveHori(block2_list)
                            mushroom.MoveVert(block2_list)
                            mushroom.Hurt()
                            mushroom.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            mushroom.FireBallDetection(levelTwo_list, fireBall_list)
                            mushroom.Health(enemyCount)
                            mushroom.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 1 and gamePhase <= 5:
                        #Bandit Movement
                        for enemy in banditGroup3_list:
                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            if gamePhase == 5 and not gameOver:
                                enemy.Control(player_list)
                            #endif
                            enemy.Hurt()
                            enemy.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            enemy.FireBallDetection(levelTwo_list, fireBall_list)
                            enemy.Health(coin_list, levelTwo_list, level, gameLevel, enemyCount)
                            enemy.Reproduce(tempBandit_list)
                            enemy.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 7 and gamePhase <= 12:
                        #Bandit Movement
                        for enemy in banditGroup4_list:
                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            if gamePhase == 12 and not gameOver:
                                enemy.Control(player_list)
                            #endif
                            enemy.Hurt()
                            enemy.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            enemy.FireBallDetection(levelTwo_list, fireBall_list)
                            enemy.Health(coin_list, levelTwo_list, level, gameLevel, enemyCount)
                            enemy.Reproduce(tempBandit_list)
                            enemy.Animation()
                        #endfor
                    #endif
                    if gamePhase == 5 or gamePhase == 12:#Temporary Bandit
                        for enemy in tempBandit_list:
                            if enemy.rect.x < 0:
                                enemy.ChangeSpeed(1)
                                enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                enemy.Animation()
                            elif enemy.rect.x > 1500:
                                enemy.ChangeSpeed(0)
                                enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                enemy.Animation()
                            else:
                                enemy.Attack()
                                enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                enemy.AttackChecker()
                                enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                                if not gameOver:
                                    enemy.Control(player_list)
                                #endif
                                enemy.Hurt()
                                enemy.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                                enemy.FireBallDetection(levelTwo_list, fireBall_list)
                                enemy.Health(coin_list, levelTwo_list, level, gameLevel, enemyCount)
                                enemy.Reproduce(tempBandit_list)
                                enemy.Animation()
                            #endif
                        #endfor
                    #endif
                    if gamePhase == 17:
                        for javelin in leftJavelin_list:
                            javelin.JavelinUpdate(leftJavelin_list, rightJavelin_list, levelTwo_list)
                        #endfor
                        for javelin in rightJavelin_list:
                            javelin.JavelinUpdate(leftJavelin_list, rightJavelin_list, levelTwo_list)
                        #endfor
                    #endif
                    if gamePhase == 1:
                        conversation = True
                        for talene in talene_list:
                            talene.rect.x = 120
                            talene.Turn(1)
                        #endfor
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for talene in talene_list:
                                    triangle.rect.x = talene.rect.x + 15
                                #endfor
                            #endfor
                            for player in player_list:
                                player.FreezeTrigger(0)
                                player.ChangeSpeed(2)
                                player.FreezeTrigger(1)
                            #endfor
                            DrawOrRemove(1, levelTwo_list, wordBox_list)
                            WriteWords(1, script2[6], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 2
                            for arun in arun_list:
                                arun.SetDeathHp(1)
                            #endfor
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[7], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            for triangle in yellowTriangle_list:
                                for arun in arun_list:
                                    triangle.rect.x = arun.rect.x
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[8], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[9], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 8
                        elif gameChat == 8:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 9:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[10], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 10
                        elif gameChat == 10:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 11:
                            for triangle in yellowTriangle_list:
                                for talene in talene_list:
                                    triangle.rect.x = talene.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[11], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 12
                        elif gameChat == 12:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 13:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            DrawOrRemove(0, levelTwo_list, wordBox_list)
                            gamePhase = 2
                            gameChat = 1
                            for arun in arun_list:
                                arun.ChangeSpeed(1)
                            #endfor
                            for talene in talene_list:
                                talene.ChangeSpeed(0)
                            #endfor
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 2:
                        for talene in talene_list:
                            if talene.rect.x <= -120:
                                talene.ChangeSpeed(1)
                                talene.ChangeSpeed(2)
                                for arun in arun_list:
                                    arun.ChangeSpeed(0)
                                    arun.ChangeSpeed(2)
                                    arun.rect.x = 2900
                                #endfor
                                gamePhase = 3
                            #endif
                        #endfor
                    elif gamePhase == 3:
                        if timeUp[0] == 0:
                            timer.Counter(900, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 4
                            endTimer = 0
                            startTimer = 0
                            for enemy in banditGroup3_list:
                                enemy.AttackStance(1)
                            #endfor
                        #endif
                    elif gamePhase == 4:
                        if timeUp[0] == 0:
                            timer.Counter(1000, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 5
                            endTimer = 0
                            startTimer = 0
                            enemyCount[0] = 14
                            for player in player_list:
                                player.FreezeTrigger(0)
                                conversation = False
                            #endfor
                        #endif
                    elif gamePhase == 5:
                        if enemyCount == [0] and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                timer.Counter(1200, timeUp)
                                conversation = True
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                gamePhase = 6
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                #endfor
                                conversation = False
                                readyToUpgrade = True
                                DrawOrRemove(1, levelTwo_list, upgradeButton_list)
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 6:
                        if player.rect.x < 1550:
                            for arrow in directionArrow_list:
                                arrow.ArrowUpdate(levelTwo_list)
                            #endfor
                        elif player.rect.x >= 1550:
                            if timeUp[0] == 0:
                                timer.Counter(1000, timeUp)
                                for player in player_list:
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                    player.ResetForTransition()
                                #endfor
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for arrow in directionArrow_list:
                                    arrow.ArrowReset(levelTwo_list)
                                #endfor
                                for talene in talene_list:
                                    talene.rect.x = 1620
                                    talene.Turn(1)
                                #endfor
                                readyToUpgrade = False
                                DrawOrRemove(0, levelTwo_list, upgradeButton_list)
                                player.rect.x = 1550
                                gamePhase = 7
                                for coin in coin_list:
                                    levelTwo_list.remove(coin)
                                    coin_list.remove(coin)
                                    currency[3] += 1
                                    if currency[3] == 10:
                                        currency[2] += 1
                                        currency[3] = 0
                                    #endif
                                    if currency[2] == 10:
                                        currency[1] += 1
                                        currency[2] = 0
                                    #endif
                                    if currency[1] == 10:
                                        currency[0] += 1
                                        currency[1] = 0
                                    #endif
                                    if currency[0] == 10:
                                        currency[0] = 0
                                        currency[1] = 0
                                        currency[2] = 0
                                        currency[3] = 0
                                    #endif
                                #endfor
                            #endif
                        #endif
                    elif gamePhase == 7:
                        if player.rect.x > 50:
                            player.FreezeTrigger(1)
                            player.rect.x -= 10
                            for talene in talene_list:
                                talene.rect.x -= 10
                            #endfor
                            for block in block2_list:
                                block.rect.x -= 10
                            #endfor
                            for arun in arun_list:
                                arun.rect.x -= 10
                                arun.Animation()
                            #endfor
                            for enemy in banditGroup4_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for mushroom in mushroomGroup2_list:
                                mushroom.rect.x -= 10
                                mushroom.Animation()
                            #endfor
                            for mushroom in mushroomGroup1_list:
                                mushroom.rect.x -= 10
                                mushroom.Animation()
                            #endfor
                            for bandit in banditGroup3_list:
                                bandit.rect.x -= 10
                                bandit.Animation()
                            #endfor
                            for enemy in tempBandit_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for background in background2_list:
                                background.BackUpdate()
                            #endfor
                            for ground in ground_list:
                                ground.Update(1)
                            #endfor
                        elif player.rect.x == 50:
                            gamePhase = 8
                            for ground in ground_list:
                                ground.Update(0)
                            #endfor
                        #endif
                    elif gamePhase == 8:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for talene in talene_list:
                                    triangle.rect.x = talene.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelTwo_list, wordBox_list)
                            WriteWords(1, script2[12], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[13], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[14], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[15], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 8
                        elif gameChat == 8:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 9:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[16], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 10
                        elif gameChat == 10:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 11:
                            for triangle in yellowTriangle_list:
                                for arun in arun_list:
                                    triangle.rect.x = arun.rect.x
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[22], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 12
                        elif gameChat == 12:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 13:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            DrawOrRemove(0, levelTwo_list, wordBox_list)
                            gamePhase = 9
                            gameChat = 1
                            for arun in arun_list:
                                arun.ChangeSpeed(1)
                            #endfor
                            for talene in talene_list:
                                talene.ChangeSpeed(0)
                            #endfor
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 9:
                        for arun in arun_list:
                            if arun.rect.x >= 1600:
                                arun.ChangeSpeed(0)
                                arun.ChangeSpeed(2)
                                arun.rect.x = 2900
                                gamePhase = 10
                                for talene in talene_list:
                                    talene.ChangeSpeed(1)
                                    talene.ChangeSpeed(2)
                                #endfor
                            #endif
                        #endfor
                    elif gamePhase == 10:
                        if timeUp[0] == 0:
                            timer.Counter(900, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 11
                            endTimer = 0
                            startTimer = 0
                            for enemy in banditGroup4_list:
                                enemy.AttackStance(1)
                            #endfor
                        #endif
                    elif gamePhase == 11:
                        if timeUp[0] == 0:
                            timer.Counter(1000, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 12
                            endTimer = 0
                            startTimer = 0
                            enemyCount[0] = 24
                            for player in player_list:
                                player.FreezeTrigger(0)
                                conversation = False
                            #endfor
                        #endif
                    elif gamePhase == 12:
                        if enemyCount == [0] and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                timer.Counter(1200, timeUp)
                                conversation = True
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                gamePhase = 13
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                #endfor
                                conversation = False
                                readyToUpgrade = True
                                DrawOrRemove(1, levelTwo_list, upgradeButton_list)
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 13:
                        if player.rect.x < 1550:
                            for arrow in directionArrow_list:
                                arrow.ArrowUpdate(levelTwo_list)
                            #endfor
                        elif player.rect.x >= 1550:
                            if timeUp[0] == 0:
                                timer.Counter(1000, timeUp)
                                for player in player_list:
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                    player.ResetForTransition()
                                #endfor
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for arrow in directionArrow_list:
                                    arrow.ArrowReset(levelTwo_list)
                                #endfor
                                readyToUpgrade = False
                                DrawOrRemove(0, levelTwo_list, upgradeButton_list)
                                player.rect.x = 1550
                                gamePhase = 14
                                for talene in talene_list:
                                    talene.rect.x = 1620
                                    talene.Turn(1)
                                #endfor
                                for mushroom in mushroomGroup3_list:
                                    mushroom.rect.x = randint(1700, 2800)
                                #endfor
                                for coin in coin_list:
                                    levelTwo_list.remove(coin)
                                    coin_list.remove(coin)
                                    currency[3] += 1
                                    if currency[3] == 10:
                                        currency[2] += 1
                                        currency[3] = 0
                                    #endif
                                    if currency[2] == 10:
                                        currency[1] += 1
                                        currency[2] = 0
                                    #endif
                                    if currency[1] == 10:
                                        currency[0] += 1
                                        currency[1] = 0
                                    #endif
                                    if currency[0] == 10:
                                        currency[0] = 0
                                        currency[1] = 0
                                        currency[2] = 0
                                        currency[3] = 0
                                    #endif
                                #endfor
                            #endif
                        #endif
                    elif gamePhase == 14:
                        if player.rect.x > 50:
                            player.rect.x -= 10
                            for talene in talene_list:
                                talene.rect.x -= 10
                            #endfor
                            for block in block2_list:
                                block.rect.x -= 10
                            #endfor
                            for arun in arun_list:
                                arun.rect.x -= 10
                                arun.Animation()
                            #endfor
                            for enemy in banditGroup4_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for mushroom in mushroomGroup2_list:
                                mushroom.rect.x -= 10
                                mushroom.Animation()
                            #endfor
                            for mushroom in mushroomGroup3_list:
                                mushroom.rect.x -= 10
                                mushroom.Animation()
                            #endfor
                            for enemy in tempBandit_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for background in background2_list:
                                background.BackUpdate()
                            #endfor
                            for ground in ground_list:
                                ground.Update(1)
                            #endfor
                        elif player.rect.x == 50:
                            gamePhase = 15
                            for ground in ground_list:
                                ground.Update(0)
                            #endfor
                        #endif
                    elif gamePhase == 15:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for arun in arun_list:
                                    triangle.rect.x = arun.rect.x
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelTwo_list, wordBox_list)
                            WriteWords(1, script2[4], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            for triangle in yellowTriangle_list:
                                for talene in talene_list:
                                    triangle.rect.x = talene.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[21], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            DrawOrRemove(0, levelTwo_list, wordBox_list)
                            gamePhase = 16
                            gameChat = 1
                            for talene in talene_list:
                                talene.ChangeSpeed(0)
                            #endfor
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 16:
                        if timeUp[0] == 0:
                            timer.Counter(1000, timeUp)
                        elif timeUp[0] == 1:
                            for talene in talene_list:
                                talene.ChangeSpeed(2)
                            #endfor
                            timeUp[0] = 0
                            gamePhase = 17
                            endTimer = 0
                            startTimer = 0
                            enemyCount[0] = 3
                            for arun in arun_list:
                                arun.HealthDisplay(1, levelTwo_list)
                            #endfor
                            for player in player_list:
                                player.FreezeTrigger(0)
                                conversation = False
                            #endfor
                        #endif
                    elif gamePhase == 17:
                        if mehiraDefeat == [0] and live[0] > 0:
                            if timeUp[0] == 0:
                                conversation = True
                                timer.Counter(500, timeUp)
                            elif timeUp[0] == 1:
                                gamePhase = 18
                                conversation = True
                                DrawOrRemove(1, levelTwo_list, whiteScreen_list)
                                timeUp[0] = 0
                                mehiraDefeat[0] = 1
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    for talene in talene_list:
                                        if player.rect.x <= talene.rect.x:
                                            player.Turn(1)
                                        else:
                                            player.Turn(0)
                                        #endif
                                    #endfor
                                #endfor
                                for talene in talene_list:
                                    talene.rect.x = -100
                                #endfor
                                if arun.rect.x < 80:
                                    arun.rect.x = 80
                                #endif
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 18:
                        if timeUp[0] == 0:
                            timer.Counter(2000, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 19
                            for player in player_list:
                                player.FreezeTrigger(0)
                                player.ChangeSpeed(2)
                                player.FreezeTrigger(1)
                            #endfor
                            DrawOrRemove(0, levelTwo_list, whiteScreen_list)
                        #endif
                    elif gamePhase == 19:
                        if gameChat == 1:
                            for talene in talene_list:
                                for arun in arun_list:
                                    if talene.rect.x < arun.rect.x - 80:
                                        talene.ChangeSpeed(1)
                                    else:
                                        talene.rect.x = arun.rect.x - 80
                                        talene.ChangeSpeed(2)
                                        gameChat = 2
                                    #endif
                                #endfor
                            #endfor
                        elif gameChat == 2:
                            for arun in arun_list:
                                arun.ChangeSpeed(0)
                                arun.ChangeSpeed(2)
                            #endfor
                            for talene in talene_list:
                                talene.ChangeSpeed(1)
                                talene.ChangeSpeed(2)
                            #endfor
                            gameChat = 3
                        elif gameChat == 3:
                            for triangle in yellowTriangle_list:
                                for arun in arun_list:
                                    triangle.rect.x = arun.rect.x
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelTwo_list, wordBox_list)
                            WriteWords(1, script2[17], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[18], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            for triangle in yellowTriangle_list:
                                for talene in talene_list:
                                    triangle.rect.x = talene.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[19], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 8
                        elif gameChat == 8:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 9:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            WriteWords(1, script2[20], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 10
                        elif gameChat == 10:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 11:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            DrawOrRemove(0, levelTwo_list, wordBox_list)
                            gamePhase = 20
                            gameChat = 1
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                            for arun in arun_list:
                                arun.ChangeSpeed(1)
                            #endfor
                            for talene in talene_list:
                                talene.ChangeSpeed(1)
                            #endfor
                        #endif
                    elif gamePhase == 20:
                        for arun in arun_list:
                            if arun.rect.x >= 1600:
                                arun.ChangeSpeed(2)
                                gamePhase = 21
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                #endfor
                                for talene in talene_list:
                                    talene.ChangeSpeed(2)
                                #endfor
                                conversation = False
                                readyToUpgrade = True
                                DrawOrRemove(1, levelTwo_list, upgradeButton_list)
                            #endif
                        #endfor
                    elif gamePhase == 21:
                        if player.rect.x < 1550:
                            for arrow in directionArrow_list:
                                arrow.ArrowUpdate(levelTwo_list)
                            #endfor
                        elif player.rect.x >= 1550:
                            if timeUp[0] == 0:
                                timer.Counter(1000, timeUp)
                                for player in player_list:
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                    player.ResetForTransition()
                                #endfor
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for arrow in directionArrow_list:
                                    arrow.ArrowReset(levelTwo_list)
                                #endfor
                                readyToUpgrade = False
                                DrawOrRemove(0, levelTwo_list, upgradeButton_list)
                                player.rect.x = 1600
                                for arun in arun_list:
                                    arun.HealthDisplay(0, levelTwo_list)
                                #endfor
                                gamePhase = 22
                                DrawOrRemove(0, levelTwo_list, pauseButton_list)
                                for coin in coin_list:
                                    levelTwo_list.remove(coin)
                                    coin_list.remove(coin)
                                    currency[3] += 1
                                    if currency[3] == 10:
                                        currency[2] += 1
                                        currency[3] = 0
                                    #endif
                                    if currency[2] == 10:
                                        currency[1] += 1
                                        currency[2] = 0
                                    #endif
                                    if currency[1] == 10:
                                        currency[0] += 1
                                        currency[1] = 0
                                    #endif
                                    if currency[0] == 10:
                                        currency[0] = 0
                                        currency[1] = 0
                                        currency[2] = 0
                                        currency[3] = 0
                                    #endif
                                #endfor
                            #endif
                        #endif
                    elif gamePhase == 22:
                        if gameChat == 1:
                            DrawOrRemove(1, levelTwo_list, wordBox_list)
                            WriteWords(1, script2[5], 0, 815, levelTwo_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelTwo_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelTwo_list, nextButton_list)
                            DrawOrRemove(0, levelTwo_list, currentLine_list)
                            DrawOrRemove(0, levelTwo_list, wordBox_list)
                            gamePhase = 23
                            gameChat = 1
                        #endif
                    elif gamePhase == 23:
                        DrawOrRemove(1, levelTwo_list, nextLevelBlock_list)
                        gamePhase = 24
                        SaveProgress(currentFile, currency,live,gameLevel+1, shieldNum, playerLevel, gameMode)
                        advanceLevel = True
                    #endif
                    levelTwo_list.draw(screen) #Display all visible objects
                elif gameLevel == 3 and gameMode[0] == 0: #Level3 Genocide------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    for button in button_list: #Button Change
                        button.Change(pos, level)
                    #endfor
                    for coin in coin_list:
                        coin.Change()
                        coin.CoinUpdate(player_list, block3_list, levelThree_list, coin_list, currency)
                    #endfor
                    for fireball in fireBall_list:
                        fireball.EffectUpdate(levelThree_list)
                        if fireball.rect.x > 1500 or fireball.rect.x < -160:
                            fireball.DeleteSelf(levelThree_list, fireBall_list)
                        #endif
                    #endfor
                    for thousand in thousand_list:
                        thousand.Update(currency[0])
                    #endfor
                    for hundred in hundred_list:
                        hundred.Update(currency[1])
                    #endfor
                    for ten in ten_list:
                        ten.Update(currency[2])
                    #endfor
                    for one in one_list:
                        one.Update(currency[3])
                    #endfor
                    #Player Movement
                    for player in player_list:
                        #Detection
                        player.EnemyAttackDetection(leftEnemyAttack_list, rightEnemyAttack_list)
                        #Detection Shadow Bolt
                        player.ShadowBoltDetection(shadowBolt_list, levelThree_list)
                        #Blocked
                        player.Blocked(live, shieldNum)
                        #Hurt
                        player.Hurt()
                        #Attack
                        player.Attack()
                        #Spell
                        player.Spell(fireBall_list, levelThree_list)
                        #Roll
                        player.Roll()
                        #Horizontal Movement
                        if gamePhase != 3 and gamePhase != 4 and gamePhase != 5 and gamePhase != 6:
                            player.MoveHori(block3_list) #Player move horizontally
                        else:
                            player.MoveHori2(block3_list)
                        #endif
                        #Attack Checker
                        player.AttackChecker()
                        #Vertical Movement
                        player.MoveVert(block3_list)
                        #Health
                        player.Health(live)
                        #Animation
                        player.Animation()
                    #endfor
                    if gamePhase >= 1:
                        for necro in necromancer_list:
                            if gamePhase == 2:
                                necro.Control(player.rect.x, player.rect.y)
                            #endif
                            necro.Attack()
                            necro.MoveHori(block3_list)
                            necro.AttackChecker()
                            necro.MoveVert(block3_list)
                            necro.Hurt()
                            necro.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            necro.FireBallDetection(levelThree_list, fireBall_list)
                            necro.Health(levelThree_list, coin_list, enemyCount)
                            necro.Spell(player.rect.x, player.rect.y, levelThree_list, shadowBolt_list)
                            necro.Animation()
                        #endfor
                        for skeleton in skeleton1_list:
                            if gamePhase == 2:
                                skeleton.Control(player.rect.x, player.rect.y - 20)
                            #endif
                            if gamePhase <= 2:
                                skeleton.Recover(levelThree_list, enemyCount)
                            #endif
                            skeleton.Attack()
                            skeleton.MoveHori(block3_list)
                            skeleton.MoveVert(block3_list)
                            skeleton.Hurt()
                            skeleton.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            skeleton.FireBallDetection(levelThree_list, fireBall_list)
                            skeleton.Health()
                            skeleton.Animation()
                        #endfor
                        for warlock in warlock3_list:
                            warlock.MoveHori(block3_list)
                            warlock.MoveVert(block3_list)
                            warlock.Health(odenHealth)
                            warlock.Escape()
                            warlock.Appear()
                            warlock.Animation()
                        #endfor
                        for stuff in shadowBolt_list:
                            if gamePhase == 2:
                                stuff.EffectUpdate(levelThree_list)
                            #endif
                        #endfor
                    #endif
                    if gamePhase == 1:
                        conversation = True
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for necro in necromancer_list:
                                    triangle.rect.x = necro.rect.x
                                #endfor
                            #endfor
                            for player in player_list:
                                player.FreezeTrigger(0)
                                player.ChangeSpeed(2)
                                player.FreezeTrigger(1)
                            #endfor
                            DrawOrRemove(1, levelThree_list, wordBox_list)
                            WriteWords(1, script3[0], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 2
                            enemyCount[0] = -1
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[1], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[2], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            DrawOrRemove(0, levelThree_list, wordBox_list)
                            gamePhase = 2
                            gameChat = 1
                            player.FreezeTrigger(0)
                            conversation = False
                            enemyCount[0] = 1
                            for necro in necromancer_list:
                                necro.HealthDisplay(1, levelThree_list)
                            #endfor
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 2:
                        if enemyCount == [0] and live[0] > 0:
                            DrawOrRemove(0, levelThree_list, shadowBolt_list)
                            DrawOrRemove(0, shadowBolt_list, shadowBolt_list)
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                timer.Counter(1200, timeUp)
                                conversation = True
                            elif timeUp[0] == 1:
                                player.FreezeTrigger(1)
                                timeUp[0] = 0
                                gamePhase = 3
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 3:
                        for warlock in warlock3_list:
                            for player in player_list:
                                if player.rect.x <= 1350:
                                    warlock.AppearTrigger(player.rect.x + 70)
                                    warlock.Turn(0)
                                    player.Turn(1)
                                elif player.rect.x >= 1350:
                                    warlock.AppearTrigger(player.rect.x - 100)
                                    warlock.Turn(1)
                                    player.Turn(0)
                                #endif
                            #endfor
                        #endfor
                        gamePhase = 4
                    elif gamePhase == 4:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for warlock in warlock3_list:
                                    triangle.rect.x = warlock.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelThree_list, wordBox_list)
                            WriteWords(1, script3[3], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 2
                            enemyCount[0] = -1
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[26], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[27], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            DrawOrRemove(0, levelThree_list, wordBox_list)
                            gamePhase = 5
                            gameChat = 1
                            enemyCount[0] = 1
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                        #endif
                    elif gamePhase == 5:
                        if gameChat == 1:
                            DrawOrRemove(1, levelThree_list, wordBox_list)
                            WriteWords(1, script3[25], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            DrawOrRemove(0, levelThree_list, wordBox_list)
                            gamePhase = 6
                            gameChat = 1
                            for warlock in warlock3_list:
                                warlock.EscapeTrigger()
                            #endfor
                        #endif
                    elif gamePhase == 6:
                        DrawOrRemove(1, levelThree_list, quitLevel_list)
                        gamePhase = 7
                        quitLevel = True
                    #endif
                    levelThree_list.draw(screen) #Display all visible objects
                elif gameLevel == 3 and gameMode[0] == 1: #Level3 Version2------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    for button in button_list: #Button Change
                        button.Change(pos, level)
                    #endfor
                    for coin in coin_list:
                        coin.Change()
                        coin.CoinUpdate(player_list, block3_list, levelThree_list, coin_list, currency)
                    #endfor
                    for fireball in fireBall_list:
                        fireball.EffectUpdate(levelThree_list)
                        if fireball.rect.x > 1500 or fireball.rect.x < -160:
                            fireball.DeleteSelf(levelThree_list, fireBall_list)
                        #endif
                    #endfor
                    for thousand in thousand_list:
                        thousand.Update(currency[0])
                    #endfor
                    for hundred in hundred_list:
                        hundred.Update(currency[1])
                    #endfor
                    for ten in ten_list:
                        ten.Update(currency[2])
                    #endfor
                    for one in one_list:
                        one.Update(currency[3])
                    #endfor
                    #Player Movement
                    for player in player_list:
                        #Detection
                        player.EnemyAttackDetection(leftEnemyAttack_list, rightEnemyAttack_list)
                        #Blocked
                        player.Blocked(live, shieldNum)
                        #Hurt
                        player.Hurt()
                        #Attack
                        player.Attack()
                        #Roll
                        player.Roll()
                        #Spell
                        player.Spell(fireBall_list, levelThree_list)
                        #Horizontal Movement
                        if gamePhase != 6 and gamePhase != 7:
                            player.MoveHori(block3_list) #Player move horizontally
                        else:
                            player.MoveHori2(block3_list)
                        #endif
                        #Attack Checker
                        player.AttackChecker()
                        #Vertical Movement
                        player.MoveVert(block3_list)
                        #Health
                        player.Health(live)
                        #Animation
                        player.Animation()
                    #endfor
                    #Skull AKA God Of Souls
                    if gamePhase == 8:
                        for skull in skull_list:
                            skull.SkullMove()
                        #endfor
                    #endif
                    #Warlock
                    if gamePhase <= 3 or gamePhase >= 7:
                        for oden in oden_list:
                            oden.MoveHori(block3_list)
                            oden.MoveVert(block3_list)
                            oden.Hurt()
                            oden.Health(odenHealth)
                            oden.Animation()
                            oden.SkullAttackDetection(skullAttack_list)
                            oden.Escape()
                            oden.Appear()
                        #endfor
                    #endif
                    if gamePhase >= 1:
                        for talene in talene2_list:
                            if gamePhase == 3:
                                for king in abomination_list:
                                    talene.Control(king.rect.x)
                                #endfor
                            #endif
                            talene.MoveHori(block3_list)
                            talene.MoveVert(block3_list)
                            talene.Hurt()
                            talene.Attack()
                            talene.Health(levelThree_list, coin_list, enemyCount)
                            talene.EnemyAttackDetection(leftEnemyAttack_list, rightEnemyAttack_list, abomination_list)
                            talene.SA()
                            talene.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 1:
                        for mehira in mehira_list:
                            if gamePhase == 3:
                                for king in abomination_list:
                                    mehira.Control2(king.rect.x)
                                #endfor
                            #endif
                            mehira.Attack()
                            mehira.MoveHori(block3_list)
                            mehira.AttackChecker()
                            mehira.MoveVert(block3_list)
                            mehira.Hurt()
                            mehira.EnemyAttackDetection(leftEnemyAttack_list, rightEnemyAttack_list)
                            mehira.Health(levelThree_list, coin_list, enemyCount, mehiraDefeat)
                            mehira.Throw(leftJavelin_list, rightJavelin_list, levelThree_list)
                            mehira.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 1 and gamePhase <= 5:
                        for king in abomination_list:
                            if gamePhase == 3:
                                for player in player_list:
                                    king.Control(player.rect.x)
                                #endfor
                            #endif
                            king.MoveHori(block3_list)
                            king.Attack()
                            king.AttackChecker()
                            king.MoveVert(block3_list)
                            king.Hurt()
                            king.EnemyAttackDetection(leftPlayerAttack_list, rightPlayerAttack_list)
                            king.TaleneAttackDetection(taleneAttack_list)
                            king.Health(levelThree_list, coin_list, enemyCount)
                            king.FireBallDetection(levelThree_list, fireBall_list)
                            king.JavelinAttackDetection(leftJavelin_list, rightJavelin_list, levelThree_list)
                            king.Animation()
                        #endfor
                    #endif
                    if gamePhase == 3:
                        for javelin in leftJavelin_list:
                            javelin.JavelinUpdate(leftJavelin_list, rightJavelin_list, levelThree_list)
                        #endfor
                        for javelin in rightJavelin_list:
                            javelin.JavelinUpdate(leftJavelin_list, rightJavelin_list, levelThree_list)
                        #endfor
                    #endif
                    if gamePhase == 1:
                        for skeleton in skeleton1_list:
                            skeleton.rect.x = -1000
                            skeleton.Animation()
                        #endfor
                        for necromancer in necromancer_list:
                            necromancer.rect.x = -1000
                            necromancer.Animation()
                        #endfor
                        for talene in talene2_list:
                            talene.Turn(1)
                            talene.rect.x = 120
                            talene.InvincibleTrigger()
                            talene.SetDifference()
                        #endfor
                        for mehira in mehira_list:
                            mehira.Turn(1)
                            mehira.rect.x = 210
                            mehira.InvincibleTrigger()
                        #endfor
                        for king in abomination_list:
                            king.rect.x = 1220
                        #endfor
                        for oden in oden_list:
                            oden.rect.x = 1120
                        #endfor
                        conversation = True
                        if gameChat == 1:
                            for player in player_list:
                                player.FreezeTrigger(0)
                                player.ChangeSpeed(2)
                                player.FreezeTrigger(1)
                            #endfor
                            DrawOrRemove(1, levelThree_list, wordBox_list)
                            WriteWords(1, script3[4], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 2
                            enemyCount[0] = -1
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            for triangle in yellowTriangle_list:
                                for mehira in mehira_list:
                                    triangle.rect.x = mehira.rect.x
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[5], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            for triangle in yellowTriangle_list:
                                for oden in oden_list:
                                    triangle.rect.x = oden.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[6], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[7], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 8
                        elif gameChat == 8:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 9:
                            for triangle in yellowTriangle_list:
                                for talene in talene2_list:
                                    triangle.rect.x = talene.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[8], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 10
                        elif gameChat == 10:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 11:
                            for triangle in yellowTriangle_list:
                                for oden in oden_list:
                                    triangle.rect.x = oden.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[9], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 12
                        elif gameChat == 12:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 13:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            DrawOrRemove(0, levelThree_list, wordBox_list)
                            gamePhase = 2
                            gameChat = 1
                            player.FreezeTrigger(0)
                            conversation = False
                            enemyCount[0] = 1
                            for king in abomination_list:
                                king.HealthDisplay(1, levelThree_list)
                            #endfor
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                            for oden in oden_list:
                                oden.EscapeTrigger()
                            #endfor
                        #endif
                    elif gamePhase == 2:
                        if timeUp[0] == 0:
                            timer.Counter(600, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            for oden in oden_list:
                                oden.ChangeSpeed(0)
                                oden.ChangeSpeed(2)
                                oden.rect.x = 2870
                                gamePhase = 3
                            #endfor
                        #endif
                    elif gamePhase == 3:
                        if enemyCount == [0] and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                timer.Counter(1200, timeUp)
                                conversation = True
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                gamePhase = 4
                                for king in abomination_list:
                                    for talene in talene2_list:
                                        talene.FaceKing(king.rect.x)
                                    #endfor
                                    for mehira in mehira_list:
                                        mehira.FaceKing(king.rect.x)
                                    #endfor
                                #endfor
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 4:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for mehira in mehira_list:
                                    triangle.rect.x = mehira.rect.x
                                #endfor
                            #endfor
                            for player in player_list:
                                player.FreezeTrigger(0)
                                player.ChangeSpeed(2)
                                player.FreezeTrigger(1)
                            #endfor
                            DrawOrRemove(1, levelThree_list, wordBox_list)
                            WriteWords(1, script3[10], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 2
                            enemyCount[0] = -1
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            for triangle in yellowTriangle_list:
                                for talene in talene2_list:
                                    triangle.rect.x = talene.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[11], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            DrawOrRemove(0, levelThree_list, wordBox_list)
                            gamePhase = 5
                            gameChat = 1
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                            for talene in talene2_list:
                                talene.ChangeSpeed(1)
                            #endfor
                            for mehira in mehira_list:
                                mehira.ChangeSpeed(1)
                            #endfor
                        #endif
                    elif gamePhase == 5:
                        for mehira in mehira_list:
                            if mehira.rect.x >= 1900:
                                mehira.ChangeSpeed(2)
                                for talene in talene2_list:
                                    talene.ChangeSpeed(2)
                                #endfor
                                gamePhase = 6
                                player.FreezeTrigger(0)
                                conversation = False
                                readyToUpgrade = True
                                DrawOrRemove(1, levelThree_list, upgradeButton_list)
                            #endif
                        #endfor
                    elif gamePhase == 6:
                        if player.rect.x < 1550:
                            for arrow in directionArrow_list:
                                arrow.ArrowUpdate(levelThree_list)
                            #endfor
                        elif player.rect.x >= 1550:
                            if timeUp[0] == 0:
                                timer.Counter(1000, timeUp)
                                for player in player_list:
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                    conversation = True
                                    player.ResetForTransition()
                                #endfor
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for arrow in directionArrow_list:
                                    arrow.ArrowReset(levelThree_list)
                                #endfor
                                readyToUpgrade = False
                                DrawOrRemove(0, levelThree_list, upgradeButton_list)
                                player.rect.x = 1550
                                for king in abomination_list:
                                    king.HealthDisplay(0, levelThree_list)
                                #endfor
                                for mehira in mehira_list:
                                    mehira.rect.x = 1710
                                #endfor
                                for talene in talene2_list:
                                    talene.rect.x = 1620
                                #endfor
                                gamePhase = 7
                            #endif
                        #endif
                    elif gamePhase == 7:
                        if player.rect.x > 50:
                            player.FreezeTrigger(1)
                            player.rect.x -= 10
                            for talene in talene2_list:
                                talene.rect.x -= 10
                            #endfor
                            for mehira in mehira_list:
                                mehira.rect.x -= 10
                            #endfor
                            for king in abomination_list:
                                king.rect.x -= 10
                                king.Animation()
                            #endfor
                            for background in background2_list:
                                background.BackUpdate()
                            #endfor
                            for oden in oden_list:
                                oden.rect.x -= 10
                            #endfor
                            for ground in ground_list:
                                ground.Update(1)
                            #endfor
                        elif player.rect.x == 50:
                            gamePhase = 8
                            for ground in ground_list:
                                ground.Update(0)
                            #endfor
                        #endif
                    elif gamePhase == 8:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for oden in oden_list:
                                    triangle.rect.x = oden.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelThree_list, wordBox_list)
                            WriteWords(1, script3[12], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            for triangle in yellowTriangle_list:
                                for mehira in mehira_list:
                                    triangle.rect.x = mehira.rect.x
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[13], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            for triangle in yellowTriangle_list:
                                for talene in talene2_list:
                                    triangle.rect.x = talene.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[14], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(1, levelThree_list, whiteScreen_list)
                            gameChat = 8
                        elif gameChat == 8:
                            if timeUp[0] == 0:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                for skull in skull_list:
                                    skull.rect.x = 550
                                #endfor
                                DrawOrRemove(0, levelThree_list, whiteScreen_list)
                                gameChat = 9
                            #endif
                        elif gameChat == 9:
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = 725
                                triangle.rect.y = 40
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[15], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 10
                        elif gameChat == 10:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 11:
                            for skull in skull_list:
                                skull.SkullUpdate(1)
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[16], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 12
                        elif gameChat == 12:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 13:
                            for triangle in yellowTriangle_list:
                                for oden in oden_list:
                                    triangle.rect.y = 670
                                    triangle.rect.x = oden.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[17], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 14
                        elif gameChat == 14:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 15:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            DrawOrRemove(0, levelThree_list, wordBox_list)
                            gamePhase = 9
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                            for skull in skull_list:
                                skull.SkullResetY()
                            #endfor
                            gameChat = 1
                        #endif
                    elif gamePhase == 9:
                        if odenHealth[0] != 0:
                            for skull in skull_list:
                                skull.SkullCrush()
                            #endfor
                        else:
                            if timeUp[0] == 0:
                                timer.Counter(400, timeUp)
                                for skull in skull_list:
                                    skull.SkullCrush()
                                #endfor
                            elif timeUp[0] == 1:
                                timeUp[0] = 0
                                gamePhase = 10
                                for skull in skull_list:
                                    skull.SkullReset()
                                    skull.SkullUpdate(0)
                                #endfor
                            #endif
                        #endif
                    elif gamePhase == 10:
                        if timeUp[0] == 0:
                            timer.Counter(1000, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 11
                            for talene in talene2_list:
                                talene.Turn(0)
                            #endfor
                            for mehira in mehira_list:
                                mehira.Turn(0)
                            #endfor
                        #endif
                    elif gamePhase == 11:
                        if gameChat == 1:
                            for triangle in yellowTriangle_list:
                                for talene in talene2_list:
                                    triangle.rect.x = talene.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(1, levelThree_list, wordBox_list)
                            WriteWords(1, script3[18], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[19], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            for triangle in yellowTriangle_list:
                                for mehira in mehira_list:
                                    triangle.rect.x = mehira.rect.x
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[20], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            for triangle in yellowTriangle_list:
                                for talene in talene2_list:
                                    triangle.rect.x = talene.rect.x + 15
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[21], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 8
                        elif gameChat == 8:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 9:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[22], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 10
                        elif gameChat == 10:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 11:
                            for triangle in yellowTriangle_list:
                                for mehira in mehira_list:
                                    triangle.rect.x = mehira.rect.x
                                #endfor
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[23], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 12
                        elif gameChat == 12:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 13:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[24], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 14
                        elif gameChat == 14:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 15:
                            for triangle in yellowTriangle_list:
                                triangle.rect.x = -1000
                            #endfor
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            WriteWords(1, script3[25], 0, 815, levelThree_list, currentLine_list)
                            gameChat = 16
                        elif gameChat == 16:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelThree_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 17:
                            DrawOrRemove(0, levelThree_list, nextButton_list)
                            DrawOrRemove(0, levelThree_list, currentLine_list)
                            DrawOrRemove(0, levelThree_list, wordBox_list)
                            gamePhase = 12
                            gameChat = 1
                        #endif
                    elif gamePhase == 12:
                        DrawOrRemove(0, levelThree_list, pauseButton_list)
                        DrawOrRemove(1, levelThree_list, quitLevel_list)
                        gamePhase = 13
                        quitLevel = True
                    #endif
                    levelThree_list.draw(screen) #Display all visible objects
                #endif
            elif gameUpgrade:
                for button in panelButton_list:
                    button.Change(pos, level)
                #endfor
                for button in upgradeTextButton_list:
                    button.Change(pos, level)
                #endfor
                if upgraded:
                    for button in okButton_list:
                        button.Change(pos, level)
                    #endfor
                #endif
                if gameLevel == 1:
                    levelOne_list.draw(screen) #Display all visible objects
                elif gameLevel == 2:
                    levelTwo_list.draw(screen)
                elif gameLevel == 3:
                    levelThree_list.draw(screen)
                #endif
            elif gamePause:
                for button in panelButton_list:
                    button.Change(pos, level)
                #endfor
                if gameLevel == 1:
                    levelOne_list.draw(screen) #Display all visible objects
                elif gameLevel == 2:
                    levelTwo_list.draw(screen)
                elif gameLevel == 3:
                    levelThree_list.draw(screen)
                #endif
            elif gameOver:
                if not gameOverDisplay:
                    gameOverDisplay = True
                    if gameLevel == 1:
                        DrawOrRemove(1, levelOne_list, restartLevel_list)
                        DrawOrRemove(0, levelOne_list, pauseButton_list)
                        for character in character1_list:
                            character.ChangeSpeed(2)
                        #endfor
                    elif gameLevel == 2:
                        DrawOrRemove(1, levelTwo_list, restartLevel_list)
                        DrawOrRemove(0, levelTwo_list, pauseButton_list)
                        for character in character2_list:
                            character.ChangeSpeed(2)
                        #endfor
                    elif gameLevel == 3:
                        DrawOrRemove(1, levelThree_list, restartLevel_list)
                        DrawOrRemove(0, levelThree_list, pauseButton_list)
                        for character in character3_list:
                            character.ChangeSpeed(2)
                        #endfor
                    #endif
                #endif
                for button in button_list: #Button Change
                    button.Change(pos, level)
                #endfor
                if gameLevel == 1:
                    for cloud in cloud_list: #Cloud
                        cloud.CloudUpdate()
                    #endfor
                    for coin in coin_list:
                        coin.Change()
                        coin.CoinUpdate(player_list, block1_list, levelOne_list, coin_list, currency)
                    #endfor
                    for player in player_list:
                        #Hurt
                        player.Hurt()
                        #Attack
                        player.Attack()
                        #Attack Checker
                        player.AttackChecker()
                        #Vertical Movement
                        player.MoveVert(block1_list)
                        #Health
                        player.Health(live)
                        #Animation
                        player.Animation()
                    #endfor
                    if gamePhase <= 5 or gamePhase >= 10:
                        for rogue in rogue_list:
                            rogue.MoveHori(block1_list)
                            rogue.MoveVert(block1_list)
                            rogue.Hurt()
                            rogue.Attack()
                            rogue.Health(levelOne_list, coin_list, enemyCount)
                            rogue.SA()
                            rogue.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 5 and gamePhase <= 8:
                        #Bandit Movement
                        for enemy in banditGroup1_list:
                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.Hurt()
                            enemy.Health(coin_list, levelOne_list, level, gameLevel, enemyCount)
                            enemy.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 10 and gamePhase <= 15:
                        #Bandit Movement
                        for enemy in banditGroup2_list:
                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.Hurt()
                            enemy.Health(coin_list, levelOne_list, level, gameLevel, enemyCount)
                            enemy.Animation()
                        #endfor
                    #endif
                    levelOne_list.draw(screen) #Display all visible objects
                elif gameLevel == 2:
                    for coin in coin_list:
                        coin.Change()
                        coin.CoinUpdate(player_list, block2_list, levelTwo_list, coin_list, currency)
                    #endfor
                    #Player Movement
                    for player in player_list:
                        #Hurt
                        player.Hurt()
                        #Attack
                        player.Attack()
                        #Attack Checker
                        player.AttackChecker()
                        #Vertical Movement
                        player.MoveVert(block2_list)
                        #Health
                        player.Health(live)
                        #Animation
                        player.Animation()
                    #endfor
                    if gamePhase <= 5 or (gamePhase >= 7 and gamePhase <= 10) or (gamePhase >= 14 and gamePhase <= 17):
                        for arun in arun_list:
                            arun.Attack()
                            arun.MoveHori(block2_list)
                            arun.AttackChecker()
                            arun.MoveVert(block2_list)
                            arun.Hurt()
                            arun.Health(levelTwo_list, coin_list, enemyCount, mehiraDefeat)
                            arun.Throw(leftJavelin_list, rightJavelin_list, levelTwo_list)
                            arun.Animation()
                        #endfor
                    #endif
                    if gamePhase <= 5:
                        for mushroom in mushroomGroup1_list:
                            mushroom.Attack()
                            mushroom.MoveHori(block2_list)
                            mushroom.MoveVert(block2_list)
                            mushroom.Hurt()
                            mushroom.Health(enemyCount)
                            mushroom.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 7 and gamePhase <= 12:
                        for mushroom in mushroomGroup2_list:
                            mushroom.Attack()
                            mushroom.MoveHori(block2_list)
                            mushroom.MoveVert(block2_list)
                            mushroom.Hurt()
                            mushroom.Health(enemyCount)
                            mushroom.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 14 and gamePhase <= 17:
                        for mushroom in mushroomGroup3_list:
                            mushroom.Attack()
                            mushroom.MoveHori(block2_list)
                            mushroom.MoveVert(block2_list)
                            mushroom.Hurt()
                            mushroom.Health(enemyCount)
                            mushroom.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 1 and gamePhase <= 5:
                        #Bandit Movement
                        for enemy in banditGroup3_list:
                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.Hurt()
                            enemy.Health(coin_list, levelTwo_list, level, gameLevel, enemyCount)
                            enemy.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 7 and gamePhase <= 12:
                        #Bandit Movement
                        for enemy in banditGroup4_list:
                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.Hurt()
                            enemy.Health(coin_list, levelTwo_list, level, gameLevel, enemyCount)
                            enemy.Animation()
                        #endfor
                    #endif
                    if gamePhase == 17:
                        for javelin in leftJavelin_list:
                            javelin.JavelinUpdate(leftJavelin_list, rightJavelin_list, levelTwo_list)
                        #endfor
                        for javelin in rightJavelin_list:
                            javelin.JavelinUpdate(leftJavelin_list, rightJavelin_list, levelTwo_list)
                        #endfor
                    #endif
                    levelTwo_list.draw(screen) #Display all visible objects
                elif gameLevel == 3 and gameMode[0] == 0:
                    for coin in coin_list:
                        coin.Change()
                        coin.CoinUpdate(player_list, block3_list, levelThree_list, coin_list, currency)
                    #endfor
                    #Player Movement
                    for player in player_list:
                        #Hurt
                        player.Hurt()
                        #Attack
                        player.Attack()
                        #Attack Checker
                        player.AttackChecker()
                        #Vertical Movement
                        player.MoveVert(block3_list)
                        #Health
                        player.Health(live)
                        #Animation
                        player.Animation()
                    #endfor
                    for skeleton in skeleton1_list:
                        skeleton.Attack()
                        skeleton.MoveVert(block3_list)
                        skeleton.Hurt()
                        skeleton.Health()
                        skeleton.Animation()
                        skeleton.Recover(levelThree_list, enemyCount)
                    #endfor
                    for necro in necromancer_list:
                        necro.Attack()
                        necro.AttackChecker()
                        necro.MoveVert(block3_list)
                        necro.Hurt()
                        necro.Spell(player.rect.x, player.rect.y, levelThree_list, shadowBolt_list)
                        necro.Animation()
                    #endfor
                    for stuff in shadowBolt_list:
                        stuff.EffectUpdate(levelThree_list)
                    #endfor
                    levelThree_list.draw(screen) #Display all visible objects
                elif gameLevel == 3 and gameMode[0] == 1:
                    for coin in coin_list:
                        coin.Change()
                        coin.CoinUpdate(player_list, block3_list, levelThree_list, coin_list, currency)
                    #endfor
                    if gamePhase >= 1:
                        for talene in talene2_list:
                            talene.ChangeSpeed(2)
                            talene.MoveHori(block3_list)
                            talene.MoveVert(block3_list)
                            talene.Hurt()
                            talene.Attack()
                            talene.SA()
                            talene.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 1:
                        for mehira in mehira_list:
                            mehira.ChangeSpeed(2)
                            mehira.Attack()
                            mehira.MoveHori(block3_list)
                            mehira.AttackChecker()
                            mehira.MoveVert(block3_list)
                            mehira.Hurt()
                            mehira.Throw(leftJavelin_list, rightJavelin_list, levelThree_list)
                            mehira.Animation()
                        #endfor
                    #endif
                    if gamePhase >= 1 and gamePhase <= 5:
                        for king in abomination_list:
                            king.ChangeSpeed(2)
                            king.MoveHori(block3_list)
                            king.Attack()
                            king.AttackChecker()
                            king.MoveVert(block3_list)
                            king.Hurt()
                            king.Health(levelThree_list, coin_list, enemyCount)
                            king.Animation()
                        #endfor
                    #endif
                    if gamePhase == 3:
                        for javelin in leftJavelin_list:
                            javelin.JavelinUpdate(leftJavelin_list, rightJavelin_list, levelThree_list)
                        #endfor
                        for javelin in rightJavelin_list:
                            javelin.JavelinUpdate(leftJavelin_list, rightJavelin_list, levelThree_list)
                        #endfor
                    #endif
                    levelThree_list.draw(screen) #Display all visible objects
                #endif
            #endif
        #endif
        pygame.display.flip() #Flip the images
        clock.tick(60) #Tick
    #endwhile
#endfunction
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (1500,900)
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("HEROTALE")
### -- Game Loop
#Start Game
Game() #Calls game
#Quit
pygame.quit()