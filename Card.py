import pygame

class Card(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name + str(id(self))

    def flip(self):
        if self.flip == True:
            return True
        else:
            return False

    def disappear(self):
        if self.image == self.image:
            return True
        else:
            return False

    def update(self):
        print("'Update me,' says " + self.name)
