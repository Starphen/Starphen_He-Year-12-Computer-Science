import pygame
import random
import math
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
 
class Block(pygame.sprite.Sprite):
    """ This class represents the ball that moves in a circle. """
 
    def __init__(self, color, width, height):
        """ Constructor that create's the ball's image. """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
        self.center_x = 0
        self.center_y = 0
 
        self.angle = 0
 
        self.radius = 0
 
        self.speed = 0.05
 
    def update(self):
        """ Update the ball's position. """
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y
 
        self.angle += self.speed
 
 
class Player(pygame.sprite.Sprite):
    """ Class to represent the player. """
    def __init__(self, color, width, height):
        """ Create the player image. """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
    def update(self):
        """Set the user to be where the mouse is. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
pygame.init()
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
block_list = pygame.sprite.Group()
 
all_sprites_list = pygame.sprite.Group()
 
for i in range(5000):
    block = Block(WHITE, 5, 5)

    block.center_x = random.randrange(SCREEN_WIDTH)
    block.center_y = random.randrange(SCREEN_HEIGHT)
    block.radius = random.randrange(10, 200)
    block.angle = random.random() * 2 * math.pi
    block.speed = 0.008
    block_list.add(block)
    all_sprites_list.add(block)
 
player = Player(BLUE, 300, 300)
all_sprites_list.add(player)
 
done = False
 
clock = pygame.time.Clock()
 
score = 0
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    all_sprites_list.update()
 
    screen.fill(BLACK)
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    for block in blocks_hit_list:
        score += 3
        print( score )
    
    all_sprites_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
