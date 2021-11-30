import pygame
import math
import sys
import random

done = False
while done == False: #while the user has not won the game, the code keeps running/will restart and let user play again
    #Initial Settings and baseline Variables
    pygame.init()

    #Defining the dimensions of the screen
    window = pygame.display.set_mode((725,500)) #the window has the dimensions defined
    pygame.display.set_caption("Hangman")

    #Various fonts with varying sizes
    LetterFont = pygame.font.SysFont('comicsans',38)
    WordFont = pygame.font.SysFont('comicsans',60)

    #Colors and their corresponding coordinates
    WHITE = (255,255,255)
    BLACK = (0, 0 , 0)

    #Buttons for letters A-Z
    RADIUS = 20 #move this to more releveant location

    letters = [] #List that stores created buttons [x, y, chr(A+i), True]
    for i in range(26): #for the 26 letters of the alphabet, store where it should be positioned
        x = 40 + 55 *(i % 13) #x position of each letter button - 2 rows of 13
        y = 400 + 55 * (i//13) #y position of each letter button
        letters.append([x,y,chr(65 + i), True]) #stores pairs of x, y values into the list, letters A(65), B(66), C(67), and boolean (default = true) in each letter

    #Loading the hangman images from the uploaded folder
    folderimages = []
    for i in range(9): #loops from 0 to 8, adding the 9 hangman images (ordered numerically) from the folder
        image = pygame.image.load("Hangman_Images!/Hangman_Images! (" +  str(1+i) + ").png")
        folderimages.append(image)

        #Computer generated words
    wordList = ["PYTHON", "PIZZA", "JAMES", "APPLE", "BANANA", "BLANKET", "EYE", "DOG", "CAT", "SHOE", "MAT", "PIZZA", "CUP",
            "YELLOW", "RED", "GREEN", "BLUE", "SELECT", "CAP", "USA", "FEUD", "UTAH", "PANTS", "FACE", "ADVANCED", "THERAPY",
             "PROVEN", "HEALTHY", "TEACHER", "STUDENT", "HOT", "COLD", "TISSUE", "SWEATER",
              "PUSH", "HAIR", "BLONDE", "BLOCK", "WORK", "MASK", "ROBOT", "TOUCH", "HAT", "ENTER", "TABLE", "CHAIR"
            ]
    def selectRandomWord(wordList): #this function selects a random string from the the list of available strings
        indexOfWord = random.randint(0, len(wordList) - 1)
        return wordList[indexOfWord]


#The actual code begins here

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

    #Code for the actual Hangman game
    hangman_status = 0
    guessedletters = [] #list that keeps track of letters guessed so far
    word = selectRandomWord(wordList)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #when you click red x button on window
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos() #position of the mouse
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2) #distance between center of button and mouse pos.
                        if dis < RADIUS: #if you have pressed a button
                            letter[3] = False #no button shows
                        #eg. letter[3] = false
                        #[3, 4,"A", False] - not true anymore
                            guessedletters.append(ltr) #adds the letter to the screen if its in the word
                            if ltr not in word: #if you guess a letter that is NOT in the word
                                hangman_status += 1
        window.fill(WHITE)  # fill the window with white!
        # draw word
        display_word = ""
        for letter in word:  # eg. in DEVELOPER, D, E, V,E L...
            if letter in guessedletters:
                display_word += letter + " "
            else:  # do not display it, if not in word
                display_word += "_ "
        text = WordFont.render(display_word, True, BLACK)
        window.blit(text, (350, 200))
        # draw buttons
        for letter in letters:
            x, y, ltr, visible = letter
            if visible:  # by default, all buttons are visible (cause true)
                pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)  # 3 thick
                text = LetterFont.render(ltr, 1, BLACK)
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
             pygame.time.delay(4000)  #4 seconds
             done = True
             break

        if hangman_status == 8: #full limbs - you have lost! may need to change this number
            pygame.time.delay(1000)  # wait one sec. bf drawing anything
            window.fill(WHITE)  # override everything on the screen
            text = WordFont.render("You Lost!", True, BLACK)
            window.blit(text, (250, 200))
            pygame.display.update()
            pygame.time.delay(4000)  # 4 seconds
            done = False
            break
    #this code is part of the while loop which makes the hangman game able to be replayed - or not.
    if done:
        pygame.quit()
