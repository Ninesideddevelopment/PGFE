
import math
import pygame as pg


def get_cell(sheet: pg.Surface, start: tuple[int, int] = (0, 0), size: tuple[int, int] = (1, 1)) -> pg.Surface:
    return sheet.subsurface(start, size)

def get_cells(sheet: pg.Surface, start: tuple[int, int], size: tuple[int, int], interval: int) -> list[pg.Surface]:

    if interval < 0:
        raise ValueError('Interval cannot be negative.')

    sub_sheet = sheet.subsurface(start, size)

    cell_count = math.ceil(sub_sheet.get_width() / interval)
    cell_size = (
        interval,
        sub_sheet.get_height(),
    )

    return_list = []
    for i in range(cell_count):
        sub_start = (i * interval, 0)

        return_list.append(
            sub_sheet.subsurface(sub_start, cell_size)
        )

    return return_list
