import pygame
import math
import sys
import random

#Initial Settings and baseline Variables
pygame.init()

    #Defining the dimensions of the screen
WIDTH = 725
HEIGHT = 500
window = pygame.display.set_mode((WIDTH,HEIGHT)) #the window has the dimensions defined
pygame.display.set_caption("Hangman")

    #Various fonts with varying sizes
LETTER_FONT = pygame.font.SysFont('comicsans',38)
WORD_FONT = pygame.font.SysFont('comicsans',60)
TITLE_FONT = pygame.font.SysFont('comicsans',70)

    #Colors and their corresponding coordinates
WHITE = (255,255,255)
BLACK = (0, 0 , 0)

    #Buttons for letters A-Z
RADIUS = 20
GAP = 15
letters = [] #List that stores created buttons [x, y, chr(A+i), True]
startx = round(WIDTH - ((RADIUS * 2 + GAP) * 13)) #Width of screen - (diameter of 13 buttons w/ gap's in between) = starting position
starty = 400
A = 65 #A = 65, B = 66, C = 67,  chr(A+i) - character that corresponds to 65, 66, 67...

for i in range(26): #for the 26 letters of the alphabet, store where it should be positioned
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP)* (i % 13))
    # each loop, i tells us what button we're on,
    #GAP * 2 so you are not directly on sides of screen, simulate having two rows with i%13, (RADIUS* 2 + GAP) = distance between each button
    y = starty + ((i // 13) * (GAP + RADIUS * 2)) #integer division with i//13
    letters.append([x,y,chr(A + i), True]) #pairs of x, y values into the list, store 4 things in each letter

#Loading the hangman images from the uploaded folder
images = []
for i in range(9): #loop 0,1,2,3,4,5,6,7,8,9
    image = pygame.image.load("Hangman_Images!/Hangman_Images! (" +  str(1+i) + ").png")
    #image = pygame.image.load("HangmanImages/IMG_" + str(7521 + i) + ".jpg") #first image is IMG_7521.jpg, second is 7522..
    images.append(image)

hangman_status = 0 #put this where it is more obviously relevant
guessed = [] #list that keeps track of letters guessed so far

    #Computer generated words
wordList = ["PYTHON", "PIZZA", "JAMES", "APPLE", "BANANA", "BLANKET", "COMPUTER", "EYE", "DOG", "CAT", "SHOE", "MAT", "PIZZA", "CUP",
         "YELLOW", "RED", "GREEN", "BLUE", "SELECT", "CAP", "USA", "FEUD", "VIRGINIA", "MARYLAND", "UTAH", "PANTS", "FACE", "ADVANCED", "THERAPY",
         "CLINICALLY", "PROVEN", "HEALTHY", "OINTMENT", "RECOMMENDED", "TEACHER", "STUDENT", "CARDIGAN", "HOT", "COLD", "TISSUE", "SWEATER",
         "INTEREST", "COMPUTER", "PUSH", "HAIR", "BLONDE", "BLOCK", "WORK", "MASK", "ROBOT", "PROFESSIONAL", "TOUCH", "HAT",
         ]


#Functions or methods - what are these called
def selectRandomWord(wordList): #this function selects a random string from the the list of available strings
    indexOfWord = random.randint(0, len(wordList) - 1)
    return wordList[indexOfWord]

def draw(): #this function draws the guessed letters and buttons onto the screen
    window.fill(WHITE) #fill the window with white!

    #draw word
    display_word = ""
    for letter in word: #eg. in DEVELOPER, D, E, V,E L...
        if letter in guessed:
            display_word += letter + " "
        else: #do not display it, if not in word
            display_word += "_ "
    text = WORD_FONT.render(display_word, True, BLACK)
    window.blit(text,(350, 200))

    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible: #by default, all buttons are visible (cause true)
            pygame.draw.circle(window, BLACK, (x,y), RADIUS, 3) #3 thick
            text = LETTER_FONT.render(ltr, 1, BLACK)
            window.blit(text,(x - text.get_width()/2,y - text.get_height()/2))
        #you want to draw the letters in the middle of button- go backwards and up
    window.blit(images[hangman_status],(0,0))  # blit stands for draw image, surface
    pygame.display.update()

def display_message(message): #This function overrides the screen and tells the user if they won or lost
    pygame.time.delay(1000) #wait one sec. bf drawing anything
    window.fill(WHITE)  # override everything on the screen
    text = WORD_FONT.render(message, True, BLACK)
    window.blit(text,(250, 200))
    pygame.display.update()
    pygame.time.delay(4000) #3 seconds



#The actual code begins here

keynotpressed = True #key has not been pressed
while keynotpressed:
    window.fill(WHITE)
    message = "Welcome to Hangman! You have 8 tries to guess the" #two messages bc it does not all fit in one line
    message2 = "computer generated word. Please press enter to begin."
    text = LETTER_FONT.render(message, True, BLACK)
    text2 = LETTER_FONT.render(message2, True, BLACK)
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
                        guessed.append(ltr) #adds the letter to the screen if its in the word
                        if ltr not in word: #if you guess a letter that is NOT in the word
                            hangman_status += 1
    draw() #will run the code in draw

    won = True
    for letter in word: #if we loop through every letter in word and all are in guessed, won stays True
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("You Won!")
        break

    if hangman_status == 8: #full limbs - you have lost! may need to change this number
        display_message("You Lost!")
        break

pygame.quit()

#26 total buttons, 2 rows of 13 buttons
#(Width - ((Gap + radius * 2)*13))/2
