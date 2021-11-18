import pygame

#setup display
pygame.init() #initializing pygame
WIDTH, HEIGHT = 800, 500 #define the dimensions of our screen
win = pygame.display.set_mode((WIDTH, HEIGHT)) #capitals to represent constant values, this takes a tuple
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = [] #where you store created buttons
startx = round(WIDTH - ((RADIUS * 2 + GAP) * 13) / 2)
starty = 400
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP)* (i % 13)) #each loop, i tells us what button we're on,
    #GAP * 2 so you are not directly on sides of screen, simulate having two rows with i%13, (RADIUS* 2 + GAP) = distance between each button
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    #integer division with i//13
    letters.append([x,y]) #pairs of x, y values into the list


# load images
images = []
for i in range(7): #loop 0, 1,2,3,4,5,6
    image = pygame.image.load("images2/hangman" + str(i) + ".png")
    images.append(image)

#game variables
hangman_status = 0

#colors
WHITE = (255,255,255)
BLACK = (0, 0 , 0)

#set up game loop
FPS = 60 #maximum FPS 60 frames/second
clock = pygame.time.Clock()
run = True

def draw(): #drawing function,need to call draw() to do this
    win.fill(WHITE)

    #draw buttons
    for letter in letters:
        x, y = letter #letter is like [ 4, 5]
        pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3) #3 thick
    win.blit(images[hangman_status], (150, 100))  # blit stands for draw image, surface
    pygame.display.update()

while run:
    clock.tick(FPS) #tick at this speed
    draw() #will run the code in draw
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when you click red x button on window
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() #position of the mouse
            print(pos)
pygame.quit()

#26 total buttons, 2 rows of 13 buttons
#(Width - ((Gap + radius * 2)*13))/2
