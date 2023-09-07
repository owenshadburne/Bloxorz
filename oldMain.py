# Imports, screen dimensions, maps -- all initializations
import pygame, tkinter
from tkinter import messagebox
pygame.init()
screen_width = 550
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DEBUG MODE -- PRESS A NUMBER TO PLAY THAT LEVEL")
clock = pygame.time.Clock()
global map
global mapCount
mapCount = 1

root = tkinter.Tk()
root.title('Connect4')
# root.iconbitmap('c:/gui/codemy.ico')

# Create menu
my_menu= tkinter.Menu(root)
root.config(menu=my_menu)

def reset():
    pass

# Maps spaces with n are blank, it's there purely there for spacing reasons
mapOne = (("1", "O", "1", "1"),
          ("1", "1", "1", "1"),
          ("1", "1", "1", "1"),
          ("1", "1", "X", "1"))

mapTwo = (("O", "1", "1", "1"),
          ("1", "1", "1", "1"),
          ("1", "X", "1", "1"))

mapThree = (("n", "n", "n", "1", "X", "1"),
            ("O", "1", "1", "1", "1", "1"),
            ("n", "n", "n", "1", "1", "1"))

mapFour = (("1", "1", "1", "1", "1", "1", "1", "1", "1"),
           ("1", "1", "1", "n", "1", "O", "n", "1", "1"),
           ("n", "n", "1", "1", "X", "1", "1", "1", "1"),
           ("n", "n", "1", "1", "n", "1", "1", "1", "n"),
           ("n", "n", "n", "1", "1", "1", "1", "n", "n"))

mapFive = (("n", "O", "1", "n", "1", "1", "n"),
           ("n", "1", "1", "n", "1", "1", "1"),
           ("1", "1", "1", "1", "1", "1", "X"),
           ("1", "1", "1", "n", "1", "1", "1"))

mapSix = (("1", "1", "1"),
          ("X", "O", "1"),
          ("1", "1", "1"),
          ("n", "1", "1"))

# Class for the block which takes the starting x and y cordinates
class Block():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.orientation = ""
        self.width, self.height = self.blockOrientation(pygame.K_SPACE)

    # Determines the current orientation and changes it according to the press received
    def blockOrientation(self, key):

        # When the block is standing
        if self.orientation == "standing":
            if key == "w":
                self.orientation = "flatNS"
                self.y -= 100
                self.height = 100
            if key == "a":
                self.orientation = "flatEW"
                self.x -= 100
                self. width = 100
            if key == "s":
                self.orientation = "flatNS"
                self.y += 50
                self.height = 100
            if key == "d":
                self.orientation = "flatEW"
                self.x += 50
                self.width = 100

        # When the block is flatNS
        elif self.orientation == "flatNS":
            if key == "w":
                self.orientation = "standing"
                self.y -= 50
                self.height = 50
            if key == "a":
                # No change in orientation
                self.x -= 50
            if key == "s":
                self.orientation = "standing"
                self.y += 100
                self.height = 50
            if key == "d":
                # No change in orientation
                self.x += 50

        # When the block is flatEW
        elif self.orientation == "flatEW":
            if key == "w":
                # No change in orientation
                self.y -= 50
            if key == "a":
                self.orientation = "standing"
                self.x -= 50
                self.width = 50
            if key == "s":
                # No change in orientation
                self.y += 50
            if key == "d":
                self.orientation = "standing"
                self.x += 100
                self.width = 50

        else:
            self.orientation = "standing"
            return [50, 50]

    # Takes the keys and feeds it to the orientation function
    def move(self, keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.blockOrientation("w")
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.blockOrientation("s")
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.blockOrientation("a")
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.blockOrientation("d")

    # Updates "sprite"
    def update(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def position(self):
        return (self.orientation, self.x, self.y)

# Class for the map, intakes a map index (map number) then sets the offset and self.map of the index
class Map():
    def __init__(self, mapIndex):
        # Offset only works if both are the same and are multiples of 50.
        # Someone please change it so that the offsets does not need to be equal for X and Y.
        self.offsetX, self.offsetY = 50, 50
        if mapIndex == 1:
            self.offsetX, self.offsetY = 150, 150
            self.map = mapOne
        if mapIndex == 2:
            self.offsetX, self.offsetY = 150, 150
            self.map = mapTwo
        if mapIndex == 3:
            self.offsetX, self.offsetY = 100, 100
            self.map = mapThree
        if mapIndex == 4:
            self.map = mapFour
        if mapIndex == 5:
            self.map = mapFive
        if mapIndex == 6:
            self.offsetX, self.offsetY = 150, 150
            self.map = mapSix

    # Paints tiles in the 2D array (maps are flipped x and y compared to the array)
    # "1" is ground, "O" is start, "X" is end
    def draw(self, win):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "1":
                    pygame.draw.rect(win, (125, 75, 75), (self.offsetX * (j + 1) - ((self.offsetX - 50) * j), self.offsetY * (i + 1) - ((self.offsetX - 50) * i), 50, 50))
                if self.map[i][j] == "O":
                    pygame.draw.rect(win, (0, 0, 255), (self.offsetX * (j + 1) - ((self.offsetX - 50) * j), self.offsetY * (i + 1) - ((self.offsetX - 50) * i), 50, 50))
                if self.map[i][j] == "X":
                    pygame.draw.rect(win, (0, 255, 0), (self.offsetX * (j + 1) - ((self.offsetX - 50) * j), self.offsetY * (i + 1) - ((self.offsetX - 50) * i), 50, 50))

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

    def hasWon(self, block, map):
        self.blockList = block.position()
        self.mapList = self.getEnd()
        global winner
        winner = False
        if self.blockList[0] == "standing" and self.blockList[1] == self.mapList[0] and self.blockList[2] == self.mapList[1]:
            winner = True
        if winner:
            pass
            # messagebox.showinfo("Bloxorz", "Level Complete")
            # mapCount += 1
            # map = Map(self.mapCount)


# Activates the redraw for the map and the block
def redraw(drawCount):
    win.fill((50 + drawCount, 0, 0))
    map.draw(win)
    block.update(win)
    map.hasWon(block, map)
    pygame.display.update()


# Main Loop
drawCount = 0
neg = 1
# Change the number here to change the map shown
map = Map(1)
startingPos = map.getStart()
block = Block(startingPos[0], startingPos[1])
run = True


def raw_input():
    menu = {}
    menu['1'] = "Add Student."
    menu['2'] = "Delete Student."
    menu['3'] = "Find Student"
    menu['4'] = "Exit"
    while True:
        options = menu.keys()
        options.sort()
        for entry in options:
            print
            entry, menu[entry]

        selection = raw_input("Please Select:")
        if selection == '1':
            print
            "add"
        elif selection == '2':
            print
            "delete"
        elif selection == '3':
            print
            "find"
        elif selection == '4':
            break
        else:
            print
            "Unknown Option Selected!"

while run:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    # Some nice background pulse to spice things up
    if drawCount >= 50:
        neg = -1
    elif drawCount <= 0:
        neg = 1
    drawCount += 0.25 * neg
    redraw(drawCount)

    # Debug -- press number to switch level
    if keys[pygame.K_1]:
        map = Map(1)
        startingPos = map.getStart()
        block = Block(startingPos[0], startingPos[1])
    if keys[pygame.K_2]:
        map = Map(2)
        startingPos = map.getStart()
        block = Block(startingPos[0], startingPos[1])
    if keys[pygame.K_3]:
        map = Map(3)
        startingPos = map.getStart()
        block = Block(startingPos[0], startingPos[1])
    if keys[pygame.K_4]:
        map = Map(4)
        startingPos = map.getStart()
        block = Block(startingPos[0], startingPos[1])
    if keys[pygame.K_5]:
        map = Map(5)
        startingPos = map.getStart()
        block = Block(startingPos[0], startingPos[1])
    if keys[pygame.K_6]:
        map = Map(6)
        startingPos = map.getStart()
        block = Block(startingPos[0], startingPos[1])

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            block.move(keys)
        if event.type == pygame.QUIT:
            run = False

    # Create menu
    my_menu = tkinter.Menu(root)
    root.config(menu=my_menu)

    # Create Options Menu
    options_menu = tkinter.Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Reset Game", command=reset)

    reset()


pygame.quit()
