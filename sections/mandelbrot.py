import pygame
from pygame.locals import DOUBLEBUF, K_ESCAPE, KEYDOWN, QUIT

WIDTH, HEIGHT = 900,900


def paletize(cl, p_mode):
    if p_mode == 1:
        return (cl[2], cl[1], cl[0])
    if p_mode == 2:
        return (cl[2], cl[0], cl[1])
    return cl


def get_color(v, p_mode):
    if v > 510:
        color = (255, 255, v%255)
    elif v > 255:
        color = (255, v%255, 0)
    else:
        color = (v%255, 0, 0)
    return paletize(color, p_mode)


def mandel_sequence(n_lim, c):
    z = 0 + 0j
    for _ in range(n_lim):
        yield z 
        z = z**2 + c


def start_mandelbrot_sets(iteration_num, p_mode):    
    screen = pygame.display.set_mode((WIDTH,HEIGHT),DOUBLEBUF)
    xaxis = WIDTH/1.5 + 140
    yaxis = HEIGHT / 2
    scale = 400
    for iy in range(HEIGHT//2 + 1):
        for ix in range(WIDTH):
            z = 0 + 0j
            c = complex((ix-xaxis) / scale, (iy-yaxis) / scale)
            color = (0, 0, 0)
            for i, z in enumerate(mandel_sequence(iteration_num, c)):
                if abs(z) > 2: # Not stable
                    v = 765 * i / iteration_num
                    color = get_color(v, p_mode)
                    break
            screen.set_at((ix, iy), color)
            screen.set_at((ix, HEIGHT-iy), color)

    pygame.display.update()

    while True:
        event = pygame.event.poll()
        if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
            break

