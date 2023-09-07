import pygame


# Class for the block which takes the starting x and y cordinates
class Block():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xFlat = x
        self.yFlat = y
        self.orientation = ""
        self.width, self.height = self.blockOrientation(pygame.K_SPACE)

    # Determines the current orientation and changes it according to the press received
    def blockOrientation(self, key):

        # When the block is standing
        if self.orientation == "standing":
            if key == "w":
                self.orientation = "flatNS"
                self.y -= 100
                self.yFlat -= 50
                self.height = 100
            if key == "a":
                self.orientation = "flatEW"
                self.x -= 100
                self.xFlat -= 50
                self. width = 100
            if key == "s":
                self.orientation = "flatNS"
                self.y += 50
                self.yFlat += 100
                self.height = 100
            if key == "d":
                self.orientation = "flatEW"
                self.x += 50
                self.xFlat += 100
                self.width = 100

        # When the block is flatNS
        elif self.orientation == "flatNS":
            if key == "w":
                self.orientation = "standing"
                self.y -= 50
                self.yFlat -= 100
                self.height = 50
            if key == "a":
                # No change in orientation
                self.x -= 50
                self.xFlat = self.x
            if key == "s":
                self.orientation = "standing"
                self.y += 100
                self.yFlat += 50
                self.height = 50
            if key == "d":
                # No change in orientation
                self.x += 50
                self.xFlat = self.x

        # When the block is flatEW
        elif self.orientation == "flatEW":
            if key == "w":
                # No change in orientation
                self.y -= 50
                self.yFlat -= 50
            if key == "a":
                self.orientation = "standing"
                self.x -= 50
                self.xFlat -= 100
                self.width = 50
            if key == "s":
                # No change in orientation
                self.y += 50
                self.yFlat += 50
            if key == "d":
                self.orientation = "standing"
                self.x += 100
                self.xFlat += 50
                self.width = 50

        else:
            self.orientation = "standing"
            return [50, 50]

        # print("(" + str(self.x) + ", " + str(self.y) + ")" + " - " + "(" + str(self.xFlat) + ", " + str(self.yFlat) + ")")

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

    def flatposition(self):
        return (self.orientation, self.xFlat, self.yFlat)
