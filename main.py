import pygame as pg
from random import randint
from copy import deepcopy

RESOLUTION = WIDTH, HEIGHT = 1500, 900
CELL = 10
WQTY = WIDTH // CELL
HQTY = HEIGHT // CELL
FPS = 10

pg.init()
pg.display.set_caption("Conway's Game of Life")
pg.display.set_icon(pg.image.load("resources/icon.png"))
surface = pg.display.set_mode(RESOLUTION)
clock = pg.time.Clock()

nextField = [[0 for i in range(WQTY)] for j in range(HQTY)]
#VARIATIONS
# existField = [[0 for i in range(WQTY)] for j in range(HQTY)]
# existField = [[1 if i == WQTY // 2 or j == HQTY // 2 else 0 for i in range(WQTY)] for j in range(HQTY)]
# existField = [[randint(0, 1) for i in range(WQTY)] for j in range(HQTY)]
# existField = [[1 if not i % 9 else 0 for i in range(WQTY)] for j in range(HQTY)]
# existField = [[1 if not (2 * i + j) % 4 else 0 for i in range(WQTY)] for j in range(HQTY)]
# existField = [[1 if not (i * j) % 22 else 0 for i in range(WQTY)] for j in range(HQTY)]
existField = [[1 if not i % 7 else randint(0, 1) for i in range(WQTY)] for j in range(HQTY)] #use one of the variations

def check_cell(existField, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if existField[j][i]:
                count += 1

    if existField[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:

    surface.fill(pg.Color('black'))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    # DRAW  CELLS
    for x in range(1, WQTY - 1):
        for y in range(1, HQTY - 1):
            if existField[y][x]:
                pg.draw.rect(surface, pg.Color('white'), (x * CELL + 2, y * CELL + 2, CELL - 2, CELL - 2))
            nextField[y][x] = check_cell(existField, x, y)

    existField = deepcopy(nextField)

    print(clock.get_fps())
    pg.display.flip()
    clock.tick(FPS)
