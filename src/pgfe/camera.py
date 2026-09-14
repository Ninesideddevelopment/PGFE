
import pygame as pg


class Camera2D:

    def __init__(self, x: int|float = 0, y: int|float = 0):
        self.x: int|float = x
        self.y: int|float = y

    def follow_position(self, window: Window, target: pg.Vector2):
        self.x += ((window.get_surface().get_width() / 2) - self.x - target.x) / 20
        self.y += ((window.get_surface().get_height() / 2) - self.y - target.y) / 20

    def set_position(self, window: CustomWindow, target: pg.Vector2):
        self.x += ((window.get_surface().get_width() / 2) - self.x - target.x)
        self.y += ((window.get_surface().get_height() / 2) - self.y - target.y)

    @property
    def position(self) -> pg.Vector2:
        return pg.Vector2(self.x, self.y)