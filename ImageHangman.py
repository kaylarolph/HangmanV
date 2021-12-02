import pygame
import math
import sys
import random
import time

#Initial Settings and baseline Variables
pygame.init()
clock = pygame.time.Clock()

#Defining the dimensions of the screen
window = pygame.display.set_mode((725,500)) #the window has the dimensions defined
pygame.display.set_caption("Hangman")

#Various fonts with varying sizes
LetterFont = pygame.font.SysFont('comicsans',38)
WordFont = pygame.font.SysFont('comicsans',60)

#Colors and their corresponding coordinates
WHITE = (255,255,255)
BLACK = (0, 0 , 0)

    #Loading the hangman images from the uploaded folder
folderimages = []
for i in range(9): #loops from 0 to 8, adding the 9 hangman images (ordered numerically) from the folder
    image = pygame.image.load("Hangman_Images!/Hangman_Images! (" +  str(1+i) + ").png")
    folderimages.append(image)

        #Computer generated words
wordList = ["PYTHON", "PIZZA", "JAMES", "APPLE", "BANANA", "BLANKET", "EYE", "DOG", "CAT", "SHOE", "MAT", "PIZZA", "CUP",
            "YELLOW", "RED", "GREEN", "BLUE", "SELECT", "CAP", "USA", "FEUD", "UTAH", "PANTS", "FACE", "ADVANCED", "THERAPY",
             "PROVEN", "HEALTHY", "TEACHER", "STUDENT", "HOT", "COLD", "TISSUE", "SWEATER",
              "PUSH", "HAIR", "BLONDE", "BLOCK", "WORK", "MASK", "ROBOT", "TOUCH", "HAT", "ENTER", "TABLE", "CHAIR", "HORSE","COFFEE", "TEA",
            "FLAG", "EGG", "HAMMER", "BELL", "SHOP", "SPONGE", "TRAVEL", "SNAKE", "CAMERA", "COMB", "BOOK", "MOUSE", "SONG", "ICE",
            "CAR", "GLUE", "TREE", "BEE", "FIRE", "PENCIL", "VOTE", "ROCKET", "KNIFE", "SONG", "MONEY", "PAINT",
            "HOLD", "JUNIOR", "SENIOR", "STANDS", "NOTE", "WORD", "EVERY", "DRIVE", "MARCH", "TREE", "MEN", "WOMEN", "HENCE", "STAIR", "LOWER", "HERE",
            "SPITE", "SOFT", "SPEAK"
            ]

def selectRandomWord(wordList): #this function selects a random string from the the list of available strings
    indexOfWord = random.randint(0, len(wordList) - 1)
    return wordList[indexOfWord]

    #Code for the welcome screen
keynotpressed = True #key has not been pressed
while keynotpressed:
    window.fill(WHITE)
    message = "Welcome to Hangman! You have 8 tries to guess the" #two messages bc it does not all fit in one line
    message2 = "computer generated word. Please press enter to begin."
    text = LetterFont.render(message, True, BLACK)
    text2 = LetterFont.render(message2, True, BLACK)
    window.blit(text,(20, 200))
    window.blit(text2,(20,250))
    pygame.display.update()

    for event in pygame.event.get(): #this loop checks if events are occuring
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #if a key has been pressed down, the code will proceed & show the hangman display
            keynotpressed = False
            break

def main():
    letters = []  # List that stores created buttons [x, y, chr(A+i), True]
    for i in range(26):  # for the 26 letters of the alphabet, store where it should be positioned
        x = 40 + 55 * (i % 13)  # x position of each letter button - 2 rows of 13
        y = 400 + 55 * (i // 13)  # y position of each letter button
        letters.append([x, y, chr(65 + i),
                        True])  # stores pairs of x, y values into the list, letters A(65), B(66), C(67), and boolean (default = true) in each letter

    #Code for the actual Hangman game
    hangman_status = 0
    guessedletters = [] #list that keeps track of letters guessed so far
    word = selectRandomWord(wordList)
    run = True

    while run: #while the user wants to play the game and does NOT click quit
        for event in pygame.event.get(): #Check for keyboard and mouse events
            if event.type == pygame.QUIT: #if you click the close button at the top left of the screen
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: #if you click on the screen
                mouseXpos, mouseYpos = pygame.mouse.get_pos() #x and y coordinates of position clicked on screen
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        xDistance = x-mouseXpos #x distance between center of button and mouse position
                        yDistance = y-mouseYpos #y distance between center of button and mouse position
                        totalDis = math.sqrt((xDistance)**2 + (yDistance)**2) #total distance between center of button and mouse position
                        if totalDis < 20: #if you have pressed a button (radius = 20)
                            guessedletters.append(ltr) #adds the letter to the screen if it is in word
                            letter[3] = False #visible boolean is now false - no button or letter will show as an option anymore
                            if ltr not in word: #if you guess a letter that is NOT in the word
                                hangman_status += 1 #adds a body part to the hangman
        window.fill(WHITE)  # fill the window with white!

        #Draw the word
        displayWord = ""
        for letter in word: #Traverses through each letter in the computer-selected word
            if letter in guessedletters: #if the letter has been guessed, display it
                displayWord += letter + " "
            else: #if the letter has not been guessed, do NOT display it
                displayWord += "_ "
        text = WordFont.render(displayWord, True, BLACK) #draw what should be displayed to the screen
        window.blit(text, (350, 200))

        #Draw the buttons
        for letter in letters: #Traverses through each letter that has been guessed
            x, y, ltr, visible = letter
            if visible: #if the button is visible
                pygame.draw.circle(window, BLACK, (x, y), 20, 3) #draw a black circle at position (x,y) w/ radius = 20 and circle thickness = 3
                text = LetterFont.render(ltr, True, BLACK) #before True was 1?
                window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))
            # you want to draw the letters in the middle of button- go backwards and up
        window.blit(folderimages[hangman_status],(0, 0))
        pygame.display.update()

    #Code displays if the player has won or lost on the screen
        won = True
        for letter in word: #if we loop through every letter in word and all are in guessed, won stays True
            if letter not in guessedletters:
                won = False
                break

        if won:
             pygame.time.delay(1000)  # wait one sec. bf drawing anything
             window.fill(WHITE)  # override everything on the screen
             text = WordFont.render("You Won!", True, BLACK)
             window.blit(text, (250, 200))
             pygame.display.update()
             pygame.time.delay(4000) #4 seconds
             #done = True
             break

        if hangman_status == 8: #full limbs - you have lost! may need to change this number
            pygame.time.delay(1000)  # wait one sec. bf drawing anything
            window.fill(WHITE)  # override everything on the screen
            message = "You Lost!"
            message2 = "Your word was " + word
            text = WordFont.render(message, True, BLACK)
            text2 = WordFont.render(message2, True, BLACK)
            window.blit(text,(250, 200))
            window.blit(text2,(170, 275))
            pygame.display.update()
            pygame.time.delay(4000) #4 seconds
            break #new

def replay():
    buttonNotPressed = True #key has not been pressed
    while buttonNotPressed:
        window.fill(WHITE)
        message = "Press enter to play again!"  # two messages bc it does not all fit in one line
        message2 = "Press the red X (top left corner) to quit!"
        text3 = LetterFont.render(message, True, BLACK)
        text4 = LetterFont.render(message2, True, BLACK)
        window.blit(text3, (20, 200))
        window.blit(text4, (20, 250))
        pygame.display.update()

        for event in pygame.event.get():# this loop checks if events are occuring
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #if a key has been pressed down
                buttonNotPressed = False #button has been pressed
                main()

           # else: #nothing is pressed - can set it with time
               # pygame.quit()
               # sys.exit()
main()

again = True
while again:
    replay()


