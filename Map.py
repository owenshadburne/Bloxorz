# Imports, screen dimensions, maps -- all initializations
import pygame

# Maps spaces with n are blank, it's there purely there for spacing reasons
mapOne = (("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "1", "O", "1", "1", "n", "n", "n", "n"),
          ("n", "n", "n", "1", "1", "1", "1", "n", "n", "n", "n"),
          ("n", "n", "n", "1", "1", "1", "1", "n", "n", "n", "n"),
          ("n", "n", "n", "1", "1", "X", "1", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"))

mapTwo = (("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "O", "1", "1", "1", "n", "n", "n", "n"),
          ("n", "n", "n", "1", "1", "1", "1", "n", "n", "n", "n"),
          ("n", "n", "n", "1", "X", "1", "1", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"))

mapThree = (("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "1", "X", "1", "n", "n", "n"),
            ("n", "n", "O", "1", "1", "1", "1", "1", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "1", "1", "1", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"))

mapFour = (("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
           ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
           ("n", "1", "1", "1", "1", "1", "1", "1", "1", "1", "n"),
           ("n", "1", "1", "1", "n", "1", "O", "n", "1", "1", "n"),
           ("n", "n", "n", "1", "1", "X", "1", "1", "1", "1", "n"),
           ("n", "n", "n", "1", "1", "n", "1", "1", "1", "n", "n"),
           ("n", "n", "n", "n", "1", "1", "1", "1", "n", "n", "n"),
           ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
           ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
           ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"))

mapFive = (("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
           ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
           ("n", "n", "n", "O", "1", "n", "1", "1", "n", "n", "n"),
           ("n", "n", "n", "1", "1", "n", "1", "1", "1", "n", "n"),
           ("n", "n", "1", "1", "1", "1", "1", "1", "X", "n", "n"),
           ("n", "n", "1", "1", "1", "n", "1", "1", "1", "n", "n"),
           ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
           ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
           ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
           ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"))

mapSix = (("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "1", "1", "1", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "X", "O", "1", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "1", "1", "1", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "1", "1", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "v", "n", "n"),
          ("n", "n", "n", "n", "n", "n", "n", "n", "v", "v", "s"))

mapSeven = (("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
            ("n", "1", "1", "n", "n", "n", "n", "n", "1", "1", "n"),
            ("n", "n", "1", "n", "n", "n", "n", "n", "n", "1", "n"),
            ("n", "n", "n", "n", "n", "n", "n", "n", "n", "1", "n"),
            ("n", "n", "n", "n", "O", "1", "n", "n", "1", "n", "n"),
            ("n", "n", "1", "n", "1", "X", "1", "n", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "1", "1", "n", "n", "1", "n"),
            ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"),
            ("n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"))


# Class for the map, intakes a map index (map number) then sets the offset and self.map of the index
class Map():
    def __init__(self, mapIndex):
        self.mapIndex = mapIndex
        # Offset only works if both are the same and are multiples of 50.
        # Someone please change it so that the offsets does not need to be equal for X and Y.
        self.offsetX, self.offsetY = 0, 0
        if self.mapIndex == 1:
            self.map = mapOne
        if self.mapIndex == 2:
            self.map = mapTwo
        if self.mapIndex == 3:
            self.map = mapThree
        if self.mapIndex == 4:
            self.map = mapFour
        if self.mapIndex == 5:
            self.map = mapFive
        if self.mapIndex == 6:
            self.map = mapSix
        if self.mapIndex == 7:
            self.map  = mapSeven

    # Paints tiles in the 2D array (maps are flipped x and y compared to the array)
    # "1" is ground, "O" is start, "X" is end
    def draw(self, win, drawCount):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "1":
                    pygame.draw.rect(win, (125, 75, 75), (self.offsetX * (j + 1) - ((self.offsetX - 50) * j), self.offsetY * (i + 1) - ((self.offsetX - 50) * i), 50, 50))
                if self.map[i][j] == "O":
                    pygame.draw.rect(win, (125, 75, 75), (self.offsetX * (j + 1) - ((self.offsetX - 50) * j), self.offsetY * (i + 1) - ((self.offsetX - 50) * i), 50, 50))
                if self.map[i][j] == "X":
                    pygame.draw.rect(win, (100, 255, 100), (self.offsetX * (j + 1) - ((self.offsetX - 50) * j), self.offsetY * (i + 1) - ((self.offsetX - 50) * i), 50, 50))
                # if self.map[i][j] == "n":
                #     pygame.draw.rect(win, (0, 0, 0), (self.offsetX * (j + 1) - ((self.offsetX - 50) * j), self.offsetY * (i + 1) - ((self.offsetX - 50) * i), 50, 50))

                # Secret Level
                if self.mapIndex == 6 and self.map[i][j] == "v":
                    pygame.draw.rect(win, (50 + (drawCount / 1.05), 0, 0), (self.offsetX * (j + 1) - ((self.offsetX - 50) * j), self.offsetY * (i + 1) - ((self.offsetX - 50) * i), 50, 50))
                if self.mapIndex == 6 and self.map[i][j] == "s":
                    pygame.draw.rect(win, (50 + (drawCount / 1.1), 0 + (drawCount / 1.9), 0), (self.offsetX * (j + 1) - ((self.offsetX - 50) * j), self.offsetY * (i + 1) - ((self.offsetX - 50) * i), 50, 50))

    def death(self, block, main):
        self.main = main
        self.block = block
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "n":
                    self.a = self.offsetY * (i + 1) - ((self.offsetX - 50) * i)
                    self.b = self.offsetX * (j + 1) - ((self.offsetX - 50) * j)
                    self.blockPos = self.block.position()
                    self.blockFlatPos = self.block.flatposition()
                    if self.blockPos[1] < 0 or self.blockPos[2] < 0 or self.blockFlatPos[1] < 0 or self.blockFlatPos[2] < 0:
                        main.levelSelected(self.mapIndex)
                    if self.mapIndex != 6:
                        if self.blockPos[1] >= 550 or self.blockPos[2] >= 500 or self.blockFlatPos[1] >= 550 or self.blockFlatPos[2] >= 500:
                            main.levelSelected(self.mapIndex)
                    if (self.blockPos[2], self.blockPos[1]) == (self.a, self.b) or (self.blockFlatPos[2], self.blockFlatPos[1]) == (self.a, self.b):
                        main.levelSelected(self.mapIndex)

                if self.map[i][j] == "s":
                    self.a = self.offsetY * (i + 1) - ((self.offsetX - 50) * i)
                    self.b = self.offsetX * (j + 1) - ((self.offsetX - 50) * j)
                    self.blockPos = self.block.position()
                    self.blockFlatPos = self.block.flatposition()
                    if (self.blockPos[2], self.blockPos[1]) == (self.a, self.b) and self.blockPos[0] == "standing":
                        main.levelSelected(7)

    # Locates "O" in the 2D array and returns it (maps are flipped x and y compared to the array)
    def getStart(self):
        for i in range(len(self.map)):
            if "O" in self.map[i]:
                j = self.map[i].index("O")
                return (self.offsetX * (j + 1) - ((self.offsetX - 50) * j), self.offsetY * (i + 1) - ((self.offsetX - 50) * i))

    def getEnd(self):
        for i in range(len(self.map)):
            if "X" in self.map[i]:
                j = self.map[i].index("X")
                return (self.offsetX * (j + 1) - ((self.offsetX - 50) * j), self.offsetY * (i + 1) - ((self.offsetX - 50) * i))
