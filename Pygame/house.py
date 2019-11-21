import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
pygame.init()
# -- Blank Screen
size = (640,480)

x = 320
y = 240

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
# -- Exit game flag set to false
done = False

while not done:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#End If
    #Next event

    # -- Game logic goes after this comment
    if x > size[0]:
        x = 0
    else:
        x = x + 313
    if y > size[0]:
        y = 0
    else:
        y = y + 313




ball_width = 20

x_val = 150
y_val = 200

x_val = x_val + 1
y_val = y_val + 1

x_val = x_val + x_direction
y_val = y_val + y_direction

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True
         #End If
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_UP:
        # - write logic that happens on key press hereelif event.key == pygame.K_DOWN:# - write logic that happens on key press here #End If#End If#Next event

    # -- Screen background is white
    screen.fill (WHITE)
    # -- flip display to reveal new position of objects
    pygame.display.flip()


    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop

pygame.quit()
          

