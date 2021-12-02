import pygame
import math
import sys
import random

#Initial settings
pygame.init()

#Window dimensions
window = pygame.display.set_mode((725,500))
pygame.display.set_caption("Hangman")

#Font sizes
LetterFont = pygame.font.SysFont('comicsans',38)
WordFont = pygame.font.SysFont('comicsans',60)

#Color variables
WHITE = (255,255,255)
BLACK = (0, 0 , 0)

#Uploading the hangman images
folderimages = []
for i in range(9): #loops from 0 to 8, adding the 8 numerically-ordered hangman images
    image = pygame.image.load("Hangman_Images!/Hangman_Images! (" +  str(1+i) + ").png")
    folderimages.append(image)

#Computer's words
wordList = ["PYTHON", "PIZZA", "JAMES", "APPLE", "BANANA", "BLANKET", "EYE", "DOG", "CAT", "SHOE", "MAT", "PIZZA", "CUP",
            "YELLOW", "RED", "GREEN", "BLUE", "SELECT", "CAP", "USA", "FEUD", "UTAH", "PANTS", "FACE", "ADVANCED", "THERAPY",
             "PROVEN", "HEALTHY", "TEACHER", "STUDENT", "HOT", "COLD", "TISSUE", "SWEATER",
              "PUSH", "HAIR", "BLONDE", "BLOCK", "WORK", "MASK", "ROBOT", "TOUCH", "HAT", "ENTER", "TABLE", "CHAIR", "HORSE","COFFEE", "TEA",
            "FLAG", "EGG", "HAMMER", "BELL", "SHOP", "SPONGE", "TRAVEL", "SNAKE", "CAMERA", "COMB", "BOOK", "MOUSE", "SONG", "ICE",
            "CAR", "GLUE", "TREE", "BEE", "FIRE", "PENCIL", "VOTE", "ROCKET", "KNIFE", "SONG", "MONEY", "PAINT",
            "HOLD", "JUNIOR", "SENIOR", "STANDS", "NOTE", "WORD", "EVERY", "DRIVE", "MARCH", "TREE", "MEN", "WOMEN", "HENCE", "STAIR", "LOWER", "HERE",
            "SPITE", "SOFT", "SPEAK", "JAZZ", "SQUISH", "SQUASH"
            ]

#Functions
def selectRandomWord(wordList):#this function chooses a random word
    indexOfWord = random.randint(0, len(wordList) - 1)
    return wordList[indexOfWord]

def main():#this is the main hangman function
    letters = [] #list stores created buttons [x, y, chr(A+i), True]
    for i in range(26): #stores all 26 charaters of the alphabet,their respective position, and state into a letter
        x = 40 + 55 * (i % 13) #x position of each letter button - 2 rows of 13
        y = 400 + 55 * (i // 13) #y position of each letter button
        letters.append([x, y, chr(65 + i),True])

    hangman_status = 0 #user has not guessed any incorrect letters
    guessedletters = []#list keeps track of guessed letters
    word = selectRandomWord(wordList)
    run = True

    while run: #runs while user wants to play the game and does NOT click quit
        for event in pygame.event.get(): #this loop checks if events are occuring
            if event.type == pygame.QUIT: #if the user clicks the close button
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: #if user clicks on the screen
                mouseXpos, mouseYpos = pygame.mouse.get_pos() #x and y coordinates of cursor position
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible: #if it is true that the letter IS visible
                        xDistance = x-mouseXpos #x distance between center of button and mouse position
                        yDistance = y-mouseYpos #y distance between center of button and mouse position
                        totalDis = math.sqrt((xDistance)**2 + (yDistance)**2) #total distance between center of button and mouse position
                        if totalDis < 20: #if you have pressed a button (radius of button = 20)
                            guessedletters.append(ltr)
                            letter[3] = False
                            if ltr not in word: #if you guess a letter that is NOT in the word
                                hangman_status += 1
        window.fill(WHITE)

        #draw the word
        displayWord = ""
        for letter in word: #Traverses through each letter in the computer-selected word
            if letter in guessedletters: #if the letter has been guessed
                displayWord += letter + " "
            else: #if the letter has NOT been guessed
                displayWord += "_ "
        text = WordFont.render(displayWord, True, BLACK)
        window.blit(text, (350, 200))

        #draw the buttons
        for letter in letters: #Traverses through each letter that has been guessed
            x, y, ltr, visible = letter
            if visible:#if the letter IS visible, draw a circular button
                pygame.draw.circle(window, BLACK, (x, y), 20, 3)#black circle at position (x,y) w/ radius = 20 and circle thickness = 3
                text = LetterFont.render(ltr, True, BLACK)
                window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))
        window.blit(folderimages[hangman_status],(0, 0))
        pygame.display.update()

    #Code displays if the player has won or lost
        won = True
        for letter in word:#loops through every letter in the computer selected word
            #if all letters of word are guessed,user will win
            if letter not in guessedletters: #if a letter in word has NOT been guessed
                won = False
                break

        if won: #if user has won
             pygame.time.delay(1000)
             window.fill(WHITE)
             text = WordFont.render("You Won!", True, BLACK)
             window.blit(text, (250, 200))
             pygame.display.update()
             pygame.time.delay(4000)
             break

        if hangman_status == 8: #if user has lost and hangman has all its limbs
            pygame.time.delay(1000)
            window.fill(WHITE)
            message = "You Lost!"
            message2 = "Your word was " + word
            text = WordFont.render(message, True, BLACK)
            text2 = WordFont.render(message2, True, BLACK)
            window.blit(text,(250, 200))
            window.blit(text2,(170, 275))
            pygame.display.update()
            pygame.time.delay(4000)
            break

def replay():#this is the replay function
    buttonNotPressed = True
    while buttonNotPressed: #while a key has NOT been pressed
        window.fill(WHITE)
        message = "Press enter to play again!"
        message2 = "Press the red X (top left corner) to quit!"
        text3 = LetterFont.render(message, True, BLACK)
        text4 = LetterFont.render(message2, True, BLACK)
        window.blit(text3, (20, 200))
        window.blit(text4, (20, 250))
        pygame.display.update()

        for event in pygame.event.get():#this loop checks if events are occuring
            if event.type == pygame.QUIT:#if user clicks the close button
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #if user presses a key, main hangman code will re-run
                buttonNotPressed = False
                main()

#The actual hangman code
#Welcome screen
keynotpressed = True
while keynotpressed: #while it is TRUE that a computer key has NOT been pressed
    window.fill(WHITE)
    message = "Welcome to Hangman! You have 8 tries to guess the"
    message2 = "computer's selected word. Please press enter to begin."
    text = LetterFont.render(message, True, BLACK)
    text2 = LetterFont.render(message2, True, BLACK)
    window.blit(text,(20, 200))
    window.blit(text2,(20,250))
    pygame.display.update()

    for event in pygame.event.get():#this loop checks if events are occuring
        if event.type == pygame.QUIT:#if user clicks the close button
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:#if user presses a key, the code will proceed
            keynotpressed = False
            break

#Main hangman function
main()

#Replay function
again = True
while again:
    replay()


