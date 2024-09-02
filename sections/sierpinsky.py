import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT


WIDTH, HEIGHT = 900, 900
MARGIN = 20
SCREEN_BG_COLOR = (102, 14, 120)
SIER_SKELTON_COLOR = (155, 66, 173)
SIER_CURVE_COLOR = (209, 194, 25)

base_points = [
    (MARGIN, MARGIN), 
    (WIDTH - MARGIN, MARGIN),
    (MARGIN, HEIGHT - MARGIN),
    (WIDTH - MARGIN, HEIGHT - MARGIN),
]

def cal_triangle_median(pt1, pt2, pt3):
    return (pt1[0] + pt2[0] + pt3[0])/3, (pt1[1] + pt2[1] + pt3[1])/3


def cal_points_median(*pts):
    coor0 = 0
    for i in pts: coor0 += i[0]
    coor1 = 0
    for i in pts: coor1 += i[1]
    coor0 //= len(pts)
    coor1 //= len(pts)
    return (coor0, coor1)


def sier_triangles(n):
    if n == 1:
        global base_points
        return [(base_points[0], base_points[1], base_points[2]), (base_points[3], base_points[2], base_points[1])]
    prev_tris = sier_triangles(n-1)
    tris = []
    for tri in prev_tris:
        is_even = (n+1) % 2
        tri1 = (cal_points_median(tri[1], tri[2]), tri[2], tri[0])
        tri2 = (cal_points_median(tri[1], tri[2]), tri[0], tri[1])
        if is_even:
            tris.append(tri1)
            tris.append(tri2)
        else:
            tris.append(tri2)
            tris.append(tri1)
    return tris


def find_sier_curve_pts(triangles):
    pts = []
    for tri in triangles:
        pts.append(cal_points_median(*tri))
    return pts


def start_sier_curve(level):
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    screen.fill(SCREEN_BG_COLOR)
    tris = sier_triangles(level)
    for t in tris:
        pygame.draw.lines(screen, SIER_SKELTON_COLOR, True, t)
    pygame.draw.lines(screen, SIER_CURVE_COLOR, True, find_sier_curve_pts(tris))
    pygame.display.update()

    while True:
        event = pygame.event.poll()
        if (event.type == QUIT or
            (event.type == KEYDOWN and event.key == K_ESCAPE)):
            break
