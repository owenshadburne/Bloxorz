import pygame, sys

class Menu():
    def __init__(self, win):
        self.width = win.get_width()
        self.height = win.get_height()
        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.text1 = self.smallfont.render('Level 1', True, (255, 255, 255))
        self.text2 = self.smallfont.render('Level 2', True, (255, 255, 255))
        self.text3 = self.smallfont.render('Level 3', True, (255, 255, 255))
        self.text4 = self.smallfont.render('Level 4', True, (255, 255, 255))
        self.text5 = self.smallfont.render('Level 5', True, (255, 255, 255))
        self.text6 = self.smallfont.render('Level 6', True, (255, 255, 255))
        self.text7 = self.smallfont.render('Instructions', True, (255, 255, 255))
        self.text8 = self.smallfont.render('Close', True, (255, 255, 255))

    def update(self, mouse, main, win, drawCount, instructions):
        self.mouse = mouse
        self.main = main
        self.instructions = False
        self.instructions = instructions

        if not self.instructions:
            self.titleFont = pygame.font.SysFont('System', int(75 + drawCount))
            self.title = self.titleFont.render('Bloxorz', True, (255, 255, 255))
            win.blit(self.title, (175 - drawCount, 65 - (drawCount / 3)))

            self.subtextFont = pygame.font.SysFont('System', 20)
            self.subtext = self.subtextFont.render('Press a Number to Play that Level', True, (255, 255, 255))
            win.blit(self.subtext, (165, 485))

        if self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 3 <= self.mouse[1] <= self.height / 3 + 40:
            if not self.instructions:
                pygame.draw.rect(win, self.color_light, [self.width / 2.6, self.height / 3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2.3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2 + 20, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 1.8 + 45, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 210, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 263, 140, 40])

                pygame.draw.rect(win, self.color_dark, [self.width / 18 - 10, self.height / 2, 175, 40])
            if self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 22 - 10, self.height / 19, 90, 40])



        elif self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 2.3 <= self.mouse[1] <= self.height / 2.3 + 40:
            if not self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3, 140, 40])
                pygame.draw.rect(win, self.color_light, [self.width / 2.6, self.height / 2.3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2 + 20, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 1.8 + 45, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 210, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 263, 140, 40])

                pygame.draw.rect(win, self.color_dark, [self.width / 18 - 10, self.height / 2, 175, 40])

            pygame.draw.rect(win, self.color_dark, [self.width / 22 - 10, self.height / 19, 90, 40])



        elif self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 2 + 20 <= self.mouse[1] <= self.height / 2 + 60:
            if not self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2.3, 140, 40])
                pygame.draw.rect(win, self.color_light, [self.width / 2.6, self.height / 2 + 20, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 1.8 + 45, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 210, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 263, 140, 40])

                pygame.draw.rect(win, self.color_dark, [self.width / 18 - 10, self.height / 2, 175, 40])
            if self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 22 - 10, self.height / 19, 90, 40])



        elif self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 1.8 + 45 <= self.mouse[1] <= self.height / 1.8 + 85:
            if not self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2.3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2 + 20, 140, 40])
                pygame.draw.rect(win, self.color_light, [self.width / 2.6, self.height / 1.8 + 45, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 210, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 263, 140, 40])

                pygame.draw.rect(win, self.color_dark, [self.width / 18 - 10, self.height / 2, 175, 40])
            if self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 22 - 10, self.height / 19, 90, 40])



        elif self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 3 + 210 <= self.mouse[1] <= self.height / 3 + 250:
            if not self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2.3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2 + 20, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 1.8 + 45, 140, 40])
                pygame.draw.rect(win, self.color_light, [self.width / 2.6, self.height / 3 + 210, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 263, 140, 40])

                pygame.draw.rect(win, self.color_dark, [self.width / 18 - 10, self.height / 2, 175, 40])
            if self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 22 - 10, self.height / 19, 90, 40])


        elif self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 3 + 263 <= self.mouse[1] <= self.height / 3 + 303:
            if not self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2.3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2 + 20, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 1.8 + 45, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 210, 140, 40])
                pygame.draw.rect(win, self.color_light, [self.width / 2.6, self.height / 3 + 263, 140, 40])

                pygame.draw.rect(win, self.color_dark, [self.width / 18 - 10, self.height / 2, 175, 40])
            if self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 22 - 10, self.height / 19, 90, 40])

        elif self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 3 + 263 <= self.mouse[1] <= self.height / 3 + 303:
            if not self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2.3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2 + 20, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 1.8 + 45, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 210, 140, 40])
                pygame.draw.rect(win, self.color_light, [self.width / 2.6, self.height / 3 + 263, 140, 40])

                pygame.draw.rect(win, self.color_dark, [self.width / 18 - 10, self.height / 2, 175, 40])
            if self.instructions:
                pygame.draw.rect(win, self.color_light, [self.width / 22 - 10, self.height / 19, 90, 40])

        elif self.width / 18 - 10 <= self.mouse[0] <= self.width / 18 + 165 and self.height / 2 <= self.mouse[1] <= self.height / 2 + 40:
            if not self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2.3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2 + 20, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 1.8 + 45, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 210, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 263, 140, 40])

                pygame.draw.rect(win, self.color_light, [self.width / 18 - 10, self.height / 2, 175, 40])
            if self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 22 - 10, self.height / 19, 90, 40])


        elif self.width / 22 - 10 <= self.mouse[0] <= self.width / 22 + 80 and self.height / 19 <= self.mouse[1] <= self.height / 19 + 40:
            if not self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2.3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2 + 20, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 1.8 + 45, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 210, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 263, 140, 40])

                pygame.draw.rect(win, self.color_dark, [self.width / 18 - 10, self.height / 2, 175, 40])
            if self.instructions:
                pygame.draw.rect(win, self.color_light, [self.width / 22 - 10, self.height / 19, 90, 40])



        else:
            if not self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2.3, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 2 + 20, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 1.8 + 45, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 210, 140, 40])
                pygame.draw.rect(win, self.color_dark, [self.width / 2.6, self.height / 3 + 263, 140, 40])

                pygame.draw.rect(win, self.color_dark, [self.width / 18 - 10, self.height / 2, 175, 40])
            if self.instructions:
                pygame.draw.rect(win, self.color_dark, [self.width / 22 - 10, self.height / 19, 90, 40])

        if not self.instructions:
            win.blit(self.text1, (self.width / 2.37, self.height / 3))
            win.blit(self.text2, (self.width / 2.37, self.height / 2.3))
            win.blit(self.text3, (self.width / 2.37, self.height / 2 + 20))
            win.blit(self.text4, (self.width / 2.37, self.height / 1.8 + 45))
            win.blit(self.text5, (self.width / 2.37, self.height / 3 + 210))
            win.blit(self.text6, (self.width / 2.37, self.height / 3 + 263))

            win.blit(self.text7, (self.width / 16 - 5, self.height / 2))
        if self.instructions:
            win.blit(self.text8, (self.width / 23, self.height / 19))


    def click(self, mouse):
        self.mouse = mouse
        if self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 3 <= self.mouse[1] <= self.height / 3 + 40:
            self.main.levelSelected(1)
        if self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 2.3 <= self.mouse[1] <= self.height / 2.3 + 40:
            self.main.levelSelected(2)
        if self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 2 + 20 <= self.mouse[1] <= self.height / 2 + 60:
            self.main.levelSelected(3)
        if self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 1.8 + 45 <= self.mouse[1] <= self.height / 1.8 + 85:
            self.main.levelSelected(4)
        if self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 3 + 210 <= self.mouse[1] <= self.height / 3 + 250:
            self.main.levelSelected(5)
        if self.width / 2.6 <= self.mouse[0] <= self.width / 2.6 + 140 and self.height / 3 + 263 <= self.mouse[1] <= self.height / 3 + 303:
            self.main.levelSelected(6)
        if self.width / 18-10 <= self.mouse[0] <= self.width / 18+165 and self.height / 2 <= self.mouse[1] <= self.height / 2 + 40:
            self.main.instructionsDisplay()
        if self.width / 22 - 10 <= self.mouse[0] <= self.width / 22 + 80 and self.height / 19 <= self.mouse[1] <= self.height / 19 + 40:
            self.main.closeInstructions()
