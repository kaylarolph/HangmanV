import random
import pygame

mistakes = 0

# pygame.mixer.init()
pygame.init()
BACKGROUND_COLOR = (236, 255, 245)
window = pygame.display.set_mode([600, 600])
window.fill(BACKGROUND_COLOR)
pygame.display.flip()


# Functions needed

# pickedLetters = [])
#  "apple"
# correctnessMap = {
#  'a': False,
#  'p': False,
#  'p': False,
#  'l': False,
#  'e': False


# }
# startGame()
# choose a random word from words array
# type a letter
# letter = input("What is your letter")
# if letter in pickedLetters array:
# letter = input("pick another letter")
# else:
# pickedLetters.append(letter)
# if checkIfWrong(letter) == True:
#   mistakes += 1
#   drawNextWrongPiece(mistakes)


# drawNextWrongPiece(mistakes)
# draw next hangman piece of we were wrong
# mistakesToPieceMap[mistakes]


# checkIfWrong(letter) - return true/false
# if a letter that a player picked is not inside the word, then they got it wrong
# try again
# if they got something wrong startPygame()


# if they got it right, correctnessMap["p"]= True


# checkIfWon()
# if correctnessMap is all True, then return True
# otherwise return False


# PyGame stuff:
# startPygame()

# drawHead()
# drawBody()
# drawArm()
# ..draw other pieces Functions

# drawUnderscores()
# drawAlphabet()

def chooseRandomWord(words):
    # choose random word from words array
    # return word
    index = random.randint(0, len(words) - 1)
    return words[index]


def checkIfLetterIsInWord(letter, word):
    # here you will check if letter is in
    # the word
    # if the letter is in the words
    # return True
    # return False
    index2 = 0
    while index2 < len(word):
        if letter == word[index2]:
            return True
        index2 += 1
    return False


def drawHead():
    print("drawing head")
    pygame.draw.circle(window, (48, 20, 0), (300, 200), 50, 1)
    pygame.draw.circle(window, (48, 20, 0), (280, 190), 3, 3)
    pygame.draw.circle(window, (48, 20, 0), (320, 190), 3, 3)
    pygame.draw.line(window, (0, 0, 0), (290, 215), (310, 215), 1)
    pygame.display.flip()


def drawBody():
    print("drawing body")
    pygame.draw.line(window, (0, 0, 0), (300, 250), (300, 400), 1)
    pygame.display.flip()


def drawArm1():
    print("drawing arm 1")
    pygame.draw.line(window, (0, 0, 0), (300, 300), (240, 240), 1)
    pygame.display.flip()


def drawLeg1():
    print("drawing leg 1")
    pygame.draw.line(window, (0, 0, 0), (300, 400), (400, 520), 1)
    pygame.display.flip()


def drawArm2():
    print("drawing arm 2 ")
    pygame.draw.line(window, (0, 0, 0), (300, 300), (360, 240), 1)
    pygame.display.flip()


def drawLeg2():
    print("drawing leg 2")
    pygame.draw.line(window, (0, 0, 0), (300, 400), (200, 520), 1)
    pygame.display.flip()


# start integrating pygame
# draw this function
# verify that it's 6 body parts
def drawBodyPart(mistakes):
    if mistakes == 1:
        drawHead()
    elif mistakes == 2:
        drawBody()
    elif mistakes == 3:
        drawArm1()
    elif mistakes == 4:
        drawArm2()
    elif mistakes == 5:
        drawLeg1()
    elif mistakes == 6:
        drawLeg2()


def initializeUnderscores(num):
    # underscores = []
    # fill up underscoes with num number of underscores
    # return underscores array
    underscores = []
    marker = 1
    while marker <= num:
        underscores.append("_")
        marker += 1
    return underscores


def changeUnderscoresToLetter(underscores, word, letter):
    # not much direction here, but you should
    # return a new array with the letter in place
    # of the underscore
    index3 = 0
    while index3 < len(word):
        if word[index3] == letter:
            underscores[index3] = word[index3]
        index3 += 1

    return underscores


def displayUnderscores(underscores):
    # display the underscores array so that the
    # user can see more and more of the word
    index = 0
    while index < len(underscores):
        print(underscores[index], end=' ')
        index += 1


def youWon(mistakes, underscores):
    # 0 means we lost  -- done
    # 1 means we won
    # 2 means we are still going
    if mistakes >= 6:
        return 0

    index = 0
    while index < len(underscores):
        if underscores[index] == "_":
            return 2
        index += 1

    return 1


def printPickedLetters(pickedLetters):
    index = 0
    print("Already chosen: ", end=" ")
    while index < len(pickedLetters):
        print(pickedLetters[index], end=" ")
        index += 1
    print("\n")


def drawCheckmark():
    rect = pygame.Rect(-170, 360, 350, 570)
    pygame.draw.ellipse(window, (57, 255, 20), rect, 50)
    pygame.draw.line(window, (57, 255, 20), (175, 600), (600, 0), 30)
    pygame.display.flip()


def drawX():
    pygame.draw.line(window, (255, 126, 126), (0, 0), (600, 600), 20)
    pygame.draw.line(window, (255, 126, 126), (0, 600), (600, 0), 20)
    pygame.display.flip()


def openWordList(catagory):
    wordlist = []
    fileName = ""
    if catagory == "food":
        fileName = "foodlist.txt"
    elif catagory == "movies":
        fileName = "movies.txt"
    else:
        fileName = "everything.txt"
    file = open(fileName, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        wordlist.append(line.strip())
    return wordlist


def startGame():
    # pygame.mixer.music.load("music1.mp3")

    # add some logic to take user input
    # what category do you want?  Type 1 for Food,
    # type 2 for Movies, type 3 for everything
    wordlist = []
    catagory = input("Pick a catagory: food, everything, movies ")
    wordlist = openWordList(catagory)

    word = chooseRandomWord(wordlist)
    pickedLetters = []
    mistakes = 0
    underscores = initializeUnderscores(len(word))
    while 1:
        displayUnderscores(underscores)
        letter = input("\nChoose a letter: ")
        while letter in pickedLetters or len(letter) != 1:
            letter = input("\nPick another letter: ")
        pickedLetters.append(letter)
        printPickedLetters(pickedLetters)
        isInWord = checkIfLetterIsInWord(letter, word)
        if isInWord == False:
            mistakes += 1
            drawBodyPart(mistakes)
        else:
            underscores = changeUnderscoresToLetter(underscores, word, letter)

        what = youWon(mistakes, underscores)
        if what == 0:
            print("You Lost :(")
            drawX()
            break
        if what == 1:
            print("You Won :)")
            drawCheckmark()
            displayUnderscores(underscores)
            break


# call start game
startGame()
