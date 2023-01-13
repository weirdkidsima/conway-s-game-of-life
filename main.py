import pygame as pg
from random import randint
from copy import deepcopy
from tkinter import messagebox as mb

RESOLUTION = WIDTH, HEIGHT = 1280, 720 
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

# RANDOM VARIATION
variations = [
    [[1 if i == WQTY // 2 or j == HQTY // 2 else 0 for i in range(WQTY)] for j in range(HQTY)],
    [[randint(0, 1) for i in range(WQTY)] for j in range(HQTY)],
    [[1 if not i % 9 else 0 for i in range(WQTY)] for j in range(HQTY)],
    [[1 if not (2 * i + j) % 4 else 0 for i in range(WQTY)] for j in range(HQTY)],
    [[1 if not (i * j) % 22 else 0 for i in range(WQTY)] for j in range(HQTY)],
    [[1 if not i % 7 else randint(0, 1) for i in range(WQTY)] for j in range(HQTY)]
]
existField = variations[randint(0,len(variations) - 1)]

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
        keys = pg.key.get_pressed()
        if keys[pg.K_i]:
            mb.showinfo(
                "Информация",
                "Создал Ступников М.А 22ИП2Б"
            )

    # DRAW  CELLS
    for x in range(1, WQTY - 1):
        for y in range(1, HQTY - 1):
            if existField[y][x]:
                pg.draw.rect(surface, pg.Color('white'), (x * CELL + 2, y * CELL + 2, CELL - 2, CELL - 2))
            nextField[y][x] = check_cell(existField, x, y)

    existField = deepcopy(nextField)

    # print(clock.get_fps())
    pg.display.flip()
    clock.tick(FPS)
