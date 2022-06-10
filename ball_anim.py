import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT


WIDTH, HEIGHT = 900,900
FPS = 10
SCREEN_BG_COLOR = (116, 214, 130)
BALL_COLOR = (117, 22, 22)
HORIZONTAL_DIRECTION = +1
VERTICAL_DIRECTION = +1
BALL_POSITION = [WIDTH//2, HEIGHT//2]
BALL_RADIUS = 50
HORIZONTAL_STEP = 1
VERTICAL_STEP = 2


def start_ball_animation():
    global HORIZONTAL_DIRECTION, VERTICAL_DIRECTION

    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    screen.fill(SCREEN_BG_COLOR)
    clock = pygame.time.Clock()


    while True:
        screen.fill(SCREEN_BG_COLOR)
        if not (0 <= BALL_POSITION[0] + HORIZONTAL_DIRECTION*HORIZONTAL_STEP <= WIDTH):
            HORIZONTAL_DIRECTION *= -1
        BALL_POSITION[0] += HORIZONTAL_DIRECTION*HORIZONTAL_STEP
        if not (0 <= BALL_POSITION[1] + VERTICAL_DIRECTION*VERTICAL_STEP <= HEIGHT):
            VERTICAL_DIRECTION *= -1
        BALL_POSITION[1] += VERTICAL_DIRECTION*VERTICAL_STEP
        pygame.draw.circle(screen, BALL_COLOR, BALL_POSITION, BALL_RADIUS)
        pygame.display.update()
        event = pygame.event.poll()
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
            break
    clock.tick(FPS)
