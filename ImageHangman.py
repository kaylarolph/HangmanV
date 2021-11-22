import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 1500, 1000 #defining the dimensions of the screen #725, 500
win = pygame.display.set_mode((WIDTH,HEIGHT)) #set the window to this width and height
pygame.display.set_caption("Let's play Hangman!")

#Various fonts with different sizes
LETTER_FONT = pygame.font.SysFont('comicsans',40)
WORD_FONT = pygame.font.SysFont('comicsans',60)
TITLE_FONT = pygame.font.SysFont('comicsans',70)

#Colors and corresponding coordinates
WHITE = (255,255,255)
BLACK = (0, 0 , 0)

#Setting up the buttons for letters A-Z
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

#Loading the hangman images - 7 of them
images = []
for i in range(7): #loop 0,1,2,3,4,5
    image = pygame.image.load("HangmanImages/IMG_" + str(7521 + i) + ".jpg") #first image is IMG_7521.jpg, second is 7522..
    images.append(image)

#Game variables
hangman_status = 0
words = ["PYTHON", "PIZZA", "JAMES"]
word = random.choice(words) #selects a random word from word list
guessed = [] #list that keeps track of letters guessed so far

#Set up game loop
FPS = 60 #maximum FPS 60 frames/second
clock = pygame.time.Clock()
run = True #boolean that is important!

def draw(): #drawing function,need to call draw() to do this
    win.fill(WHITE) #fill the window with white!
    #draw title
    text = TITLE_FONT.render("HANGMAN!", 1, BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2, 20)) #text, (x, y) positions

    #draw word
    display_word = ""
    for letter in word: #eg. in DEVELOPER, D, E, V,E L...
        if letter in guessed:
            display_word += letter + "  "
        else: #do not display it, if not in word
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text,(900, 200)) #400, 200

    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible: #by default, all buttons are visible (cause true)
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3) #3 thick
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text,(x - text.get_width()/2,y - text.get_height()/2))
        #you want to draw the letters in the middle of button- go backwards and up
    win.blit(images[hangman_status],(50,60))  # blit stands for draw image, surface
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000) #wait one sec. bf drawing anything
    win.fill(WHITE)  # override everything on the screen
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width() / 2), HEIGHT/2 - text.get_height() / 2)
    pygame.display.update()
    pygame.time.delay(3000)  # 3 seconds


while run:
    clock.tick(FPS) #tick at this speed
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
        display_message("You WON!")
        break

    if hangman_status == 6: #full limbs - you have lost! may need to change this number
        display_message("You LOST!")
        break

pygame.quit()

#26 total buttons, 2 rows of 13 buttons
#(Width - ((Gap + radius * 2)*13))/2
