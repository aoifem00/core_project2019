import sys
import pygame
import Card

# Goals:
#     **Screen designs
#         **Buttons
#         **Cards - Group of rects around pics - Need matrix - Have to get
#           code from backend about where the cards have been randomized
#           If any of group has been touched and then the specific card
#             **Assign card rects to certain numbers? - Need a matrix
#             **Flip animations
#             **Disappearing
#     **Score display
#     **Time display
#     **From video to gifs of Baxter - Teach self
#     **Levels

class Controller:
    def __init__(self,width = 800, height = 600):
        self.screen = pygame.display.set_mode((width,height))
        #self.bkgd = pygame.Surface(self.screen.get_size()).convert()
            #Might change the sets for the self.bkgd and then blit onto self.screen
        #self.card = Group
        pygame.init()
        """Create the screen"""
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((160,82,173)) #purple

        """Create the button"""
        self.startBtnImg = pygame.image.load("assets/start Button.png").convert()
        self.startBtnImg.set_colorkey((0,0,0))
        self.startBtnImg = pygame.transform.scale(self.startBtnImg, (self.width//2, self.height//2))
        self.startBtn = self.startBtnImg.get_rect()
        self.startBtn.x = self.startBtn.centerx
        self.startBtn.y = self.startBtn.centery

        #pygame.mixer.music.load()      #This is where to put music
        #pygame.mixer.music.play(-1)

        pygame.font.init()  #you have to call this at the start,
        #if you want to us this module.

        """Load the sprites that we need"""
        #Cards
        self.card = pygame.sprite.Group()
        num_cards = 10
        for i in range(num_cards):
            self.card.add(Card.Card("Card", i*30, i*20, 'assets/card.jpg'))

        #Adds the sprites
        self.all_sprites = pygame.sprite.Group((tuple(self.card)))
        self.state = "GAME"

    def mainloop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        """This is the Main Loop of the Game"""
        #pygame.key.set_repeat(1,50)  #what does this do?
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.startBtnImg, (self.startBtn.x,self.startBtn.y))
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    if (self.startBtn.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN):
                        self.background.fill((245,10,57))


            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.startBtnImg, (self.startBtn.x,self.startBtn.y))
            pygame.display.flip()


        # def setStartScreen(self):
        #     self.screen.fill((245,10,57)) #red

        #def setGameScreen(self):

        #def setGameOverScreen(self):
        #    self.screen.fill((55,111,200)) #blue

        #def setInstructionsScreen(self):
            #self.screen.fill((255,255,255)) #white

        done = False
        while (not done):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        setStartScreen(self)
                    elif event.key == pygame.K_a:
                        setGameScreen(self)
                    elif event.key == pygame.K_TAB:
                        setGameOverScreen(self)
                    elif event.key == pygame.K_b:
                        setInstructionsScreen(self)
            if done:
                break

            self.screen
            pygame.display.flip()
            
        #done = False
        #while (not done):
        #    for event in pygame.event.get():
        #        if event.type == pygame.QUIT:
        #            done = True
        #            break
        #        elif event.type == pygame.KEYDOWN:
        #            if event.key == pygame.K_SPACE:
        #                setStartScreen(self)
        #            elif event.key == pygame.K_a:
        #                setGameScreen(self)
        #            elif event.key == pygame.K_TAB:
        #                setGameOverScreen(self)
        #            elif event.key == pygame.K_b:
        #                setInstructionsScreen(self)
        #    if done:
        #        break

        #    self.screen

            pygame.display.update()
