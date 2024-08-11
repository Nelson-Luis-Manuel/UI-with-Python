#Importing packages/modules/libraries
import pygame, sys

#Getting the pygame modules ready
pygame.init()

#Variables
mMainScreenSize = (1200,600)
mDrawingScreenSize = (1000,500)
mComponentsScreenSize = (145,500)
clock = pygame.time.Clock()
running = True

## Setting up the screens:

#Main Sreen
mMainScreen = pygame.display.set_mode(size = mMainScreenSize)
mMainScreen.fill(pygame.Color('gray'))


#Main loop:
while running:

    #Listener for exit intent
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  
            sys.exit()

   
    #Drawing screen
    mDrawingScreen = pygame.Surface(mDrawingScreenSize)
    mDrawingScreen.fill(pygame.Color('white'))
    mMainScreen.blit(mDrawingScreen,(180,85))

    #Components screen
    mComponentscreen = pygame.Surface(mComponentsScreenSize)
    mComponentscreen.fill(pygame.Color('white'))

    mResistance = pygame.Rect(40,50,60,20)
    pygame.draw.rect(mComponentscreen,(255,0,0),mResistance)

    mSource = pygame.draw.circle(mComponentscreen,(255,0,0),(69,150),25)

    mConductor = pygame.draw.line(mComponentscreen,(255,0,0),(40,50),(40,150))

    mMainScreen.blit(mComponentscreen,(20,85))

#Horizontal Conductor
    

    mMousePosition = pygame.mouse.get_pos()
    print(mMousePosition)

    
    #Telling pygame to upgrade the screen
    pygame.display.update()
    clock.tick(60)