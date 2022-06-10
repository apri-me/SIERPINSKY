import pygame
import pygame_menu
from sierpinsky import start_sier_curve
from mandelbrot import start_mandelbrot_sets
from ball_anim import start_ball_animation

THEME = pygame_menu.themes.THEME_SOLARIZED

MODE = 1
WIDTH, HEIGHT = 900, 900

SIERPINSKY_LEVEL = 8

MANDELBROT_ITERATIONS_NUM = 30
MANDELBROT_COLOR_PALET_MODE = 1


def select_mode(value, mode):
    global MODE
    MODE = mode


def choose_menu():
    if MODE == 1:
        start_sierpinsky_menu()
    elif MODE == 2:
        start_mandelbrot_menu()
    else:
        start_ball_animation()


def select_sierpinsky_level(value, level):
    global SIERPINSKY_LEVEL 
    SIERPINSKY_LEVEL = level


def help_sier_curve_start():
    global SIERPINSKY_LEVEL
    start_sier_curve(SIERPINSKY_LEVEL)


def select_mandelbrot_num_of_iterations(value, n):
    global MANDELBROT_ITERATIONS_NUM
    MANDELBROT_ITERATIONS_NUM = n


def select_mandelbrot_color_pallet(value, mode):
    global MANDELBROT_COLOR_PALET_MODE
    MANDELBROT_COLOR_PALET_MODE = mode


def help_mandelbrot_start():
    global MANDELBROT_ITERATIONS_NUM, MANDELBROT_COLOR_PALET_MODE
    start_mandelbrot_sets(MANDELBROT_ITERATIONS_NUM, MANDELBROT_COLOR_PALET_MODE)


def start_mandelbrot_menu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    menu = pygame_menu.Menu('Mandelbrot Sets', WIDTH, HEIGHT, theme=THEME)
    menu.add.selector('Select Num of iterations: ', [(str(i), i) for i in range(15, 61, 5)], default=5, onchange=select_mandelbrot_num_of_iterations)
    menu.add.selector('Select Color: ', [("Blue", 1), ("Green", 2), ("Red", 3)], default=0, onchange=select_mandelbrot_color_pallet)
    menu.add.button('Start', help_mandelbrot_start)
    menu.add.button('Back', start_main_menu)
    menu.mainloop(screen)


def start_sierpinsky_menu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    menu = pygame_menu.Menu('Sierpinsky', WIDTH, HEIGHT, theme=THEME)
    menu.add.selector('Select Level: ', [(str(i), i) for i in range(1, 17)], default=7, onchange=select_sierpinsky_level)
    menu.add.button('Start', help_sier_curve_start)
    menu.add.button('Back', start_main_menu)
    menu.mainloop(screen)


def start_main_menu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    menu = pygame_menu.Menu('Computer Graphics', WIDTH, HEIGHT, theme=THEME)
    menu.add.selector('Select Mode :', [('Serpinski curves', 1), ('Mandelbrot sets', 2), ('Ball Animation', 3)], onchange=select_mode)
    menu.add.button('Go', choose_menu)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)


if __name__ == '__main__':
    pygame.init()
    start_main_menu()