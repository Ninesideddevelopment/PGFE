
import abc
import pygame as pg

from pgfe.entity.entity_controllers.AbstractController import AbstractController


class AbstractEntity(pg.sprite.Sprite, abc.ABC):

    def __init__(self, *groups, x: int, y: int, image: pg.Surface) -> None:
        pg.sprite.Sprite.__init__(self, *groups)
        self.controller: AbstractController|None = None

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity: pg.Vector2 = pg.Vector2()

    def update_velocity(self, x: float = 0.0, y: float = 0.0) -> None:
        self.velocity.x += x
        self.velocity.y += y

    def move_x(self):
        self.rect.x += self.velocity.x

    def move_y(self):
        self.rect.y += self.velocity.y
