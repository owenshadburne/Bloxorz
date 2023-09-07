# Imports, screen dimensions, maps -- all initializations
import pygame, Block, Map, Menu
pygame.init()
screen_width = 550
screen_height = 500
global win
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bloxorz")
clock = pygame.time.Clock()

global Menu
menu = Menu.Menu(win)
global map
map = Map.Map(1)
startingPos = map.getStart()
global block
block = Block.Block(startingPos[0], startingPos[1])


class Main():

    # Main Loop
    def __init__(self):
        self.instructions = False
        self.inLevel = False
        self.menu = menu
        self.map = map
        self.block = block
        self.secret = False
        self.drawCount1 = 0
        self.drawCount2, self.drawCount3 = 170, 170

        self.drawCount = 0
        self.neg = 1

        run = True
        while run:
            clock.tick(60)
            self.keys = pygame.key.get_pressed()
            self.mouse = pygame.mouse.get_pos()


            self.redraw()

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    self.block.move(self.keys)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.menu.click(self.mouse)
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()

    # Activates the redraw for the map and the block
    def redraw(self):

        # Some nice background pulse to spice things up


        if self.drawCount >= 50:
            self.neg = -1
        elif self.drawCount <= 0:
            self.neg = 1
        self.drawCount += 0.25 * self.neg
        if not self.secret:
            win.fill((50 + self.drawCount, 0, 0))
        else:
            if self.drawCount1 < 170 and self.drawCount3 >= 170:
                self.drawCount1 += .5
                self.drawCount2 -= .5
            elif self.drawCount2 < 170:
                self.drawCount2 += .5
                self.drawCount3 -= .5
            elif self.drawCount3 < 170:
                self.drawCount3 += .5
                self.drawCount1 -= .5
            win.fill((self.drawCount1, self.drawCount2, self.drawCount3))


        # Redraw Assets
        if self.instructions:
            self.instructionsDisplay()
            self.menu.update(self.mouse, self, win, self.drawCount, self.instructions)
            pygame.display.update()

        elif (not self.inLevel and not self.instructions):
            self.menu.update(self.mouse, self, win, self.drawCount, self.instructions)
            pygame.display.update()

        elif self.inLevel:
            self.map.draw(win, self.drawCount)
            self.block.update(win)
            self.checkWin()
            self.map.death(self.block, self)
            pygame.display.update()

    # Receives a level from Menu and generates that level
    def levelSelected(self, levelNum):
        self.levelNum = levelNum
        self.inLevel = True
        if self.levelNum == 1:
            self.map = Map.Map(1)
            self.startingPos = self.map.getStart()
            self.block = Block.Block(self.startingPos[0], self.startingPos[1])
        if self.levelNum == 2:
            self.map = Map.Map(2)
            self.startingPos = self.map.getStart()
            self.block = Block.Block(self.startingPos[0], self.startingPos[1])
        if self.levelNum == 3:
            self.map = Map.Map(3)
            self.startingPos = self.map.getStart()
            self.block = Block.Block(self.startingPos[0], self.startingPos[1])
        if self.levelNum == 4:
            self.map = Map.Map(4)
            self.startingPos = self.map.getStart()
            self.block = Block.Block(self.startingPos[0], self.startingPos[1])
        if self.levelNum == 5:
            self.map = Map.Map(5)
            self.startingPos = self.map.getStart()
            self.block = Block.Block(self.startingPos[0], self.startingPos[1])
        if self.levelNum == 6:
            self.map = Map.Map(6)
            self.startingPos = self.map.getStart()
            self.block = Block.Block(self.startingPos[0], self.startingPos[1])
        if self.levelNum == 7:
            self.map = Map.Map(7)
            self.startingPos = self.map.getStart()
            self.block = Block.Block(self.startingPos[0], self.startingPos[1])

    def checkWin(self):
        self.blockPos = self.block.position()
        self.endPos = self.map.getEnd()

        if (self.blockPos[1:] == self.endPos and self.blockPos[0] == "standing") and self.levelNum == 7:
            self.secret = True
            clock.tick(5)
            self.inLevel = False

        elif (self.blockPos[1:] == self.endPos and self.blockPos[0] == "standing"):
            pygame.display.update()
            clock.tick(30)
            self.inLevel = False

    def closeInstructions(self):
        self.instructions = False

    def instructionsDisplay(self):
        self.instructions = True
        self.titleFont = pygame.font.SysFont('System', 60)
        self.title = self.titleFont.render('Instructions', True, (255, 255, 255))
        win.blit(self.title, (150, 30))

        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('1) This is a 2D version of the original game Bloxorz.', True, (255, 255, 255))
        win.blit(self.subtext, (10, 100))

        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('2) The aim of the game is to get the block to fall into the square hole at the end of', True,(255, 255, 255))
        win.blit(self.subtext, (10, 120))
        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('each stage. There are 6 stages to complete.', True, (255, 255, 255))
        win.blit(self.subtext, (27, 140))

        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('3) In order to move the block, you can press the up, down, right, and left keys on your', True, (255, 255, 255))
        win.blit(self.subtext, (10, 160))
        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('keyboard on the bottom right, or you can press the keys "w", "a", "s", and "d",', True, (255, 255, 255))
        win.blit(self.subtext, (27, 180))
        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('which preform the same functions.', True, (255, 255, 255))
        win.blit(self.subtext, (27, 200))

        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('4) The block orientation will be moving in directions: North, East, South, West.', True, (255, 255, 255))
        win.blit(self.subtext, (10, 220))

        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('5) When the block moves, it\'ll take up either one or two spaces depending on', True, (255, 255, 255))
        win.blit(self.subtext, (10, 240))
        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('whether the block is flat or upright.', True, (255, 255, 255))
        win.blit(self.subtext, (27, 260))

        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('6) If the block take up one space, it means it is standing upright.', True, (255, 255, 255))
        win.blit(self.subtext, (10, 280))

        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('7) If the block is taking up two spaces, it means it is flat on the map.', True, (255, 255, 255))
        win.blit(self.subtext, (10, 300))

        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('8) In order to win in Bloxorz, the block must be standing upright on the green square.', True, (255, 255, 255))
        win.blit(self.subtext, (10, 320))
        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('If it is not standing upright on the green square, the game will continue until it is.', True, (255, 255, 255))
        win.blit(self.subtext, (27, 340))
        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('This means the block should look like a single block on top of the green square.', True, (255, 255, 255))
        win.blit(self.subtext, (27, 360))

        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('9) Once you beat the level, the game will go to the starting page, and then you get to', True, (255, 255, 255))
        win.blit(self.subtext, (10, 380))
        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('pick the next level.', True, (255, 255, 255))
        win.blit(self.subtext, (27, 400))

        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('10) If you have beaten all 6 (7) levels of the game, Congratulations you\'re a', True, (255, 255, 255))
        win.blit(self.subtext, (10, 420))
        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render(' champion at 2D Bloxorz, if you want to try 3D Bloxorz, go to Cool Math Games', True, (255, 255, 255))
        win.blit(self.subtext, (27, 440))
        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('and try it yourself.', True, (255, 255, 255))
        win.blit(self.subtext, (27, 460))

        self.subtextFont = pygame.font.SysFont('System', 20)
        self.subtext = self.subtextFont.render('Enjoy!', True, (255, 255, 255))
        win.blit(self.subtext, (505, 480))

Main()
