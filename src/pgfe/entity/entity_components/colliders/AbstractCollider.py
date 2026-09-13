
import abc
import pygame as pg

from pgfe import Enum
from pgfe.entity.entity_components.AbstractComponent import AbstractComponent
from pgfe.entity.entity_components.CollisionExceptions import CollisionExceptions


class AbstractCollider(AbstractComponent, abc.ABC):
    def __init__(self):
        super().__init__()

        self.collision_exceptions = CollisionExceptions()

    def get_collides(self, sprite_group):
        for sprite in sprite_group.sprites():
            if sprite != self and self.rect.colliderect(sprite.rect):
                yield sprite

    @abc.abstractmethod
    def collide(self, sprite: pg.sprite.Sprite, axis: Enum.Axis) -> tuple[bool, bool]:
        pass

    def collides(self, sprite_group):
        directions = {"top": False, "left": False, "bottom": False, "right": False}

        newgroup = pg.sprite.Group(*sprite_group.sprites())

        # Remove unwanted sprites
        for sprite in newgroup.sprites():
            if sprite != self and type(sprite) in self.collision_exceptions.unconditional:
                newgroup.remove(sprite)

        self.move_x()
        for sprite in self.get_collides(newgroup):
            right, left = self.collide(sprite, Enum.Axis.X)
            directions.update({
                "left": left,
                "right": right
            })

        self.move_y()
        for sprite in self.get_collides(newgroup):
            top, bottom = self.collide(sprite, Enum.Axis.Y)
            directions.update({
                "top": top,
                "bottom": bottom
            })

        return directions

    @abc.abstractmethod
    def move_x(self):
        pass

    @abc.abstractmethod
    def move_y(self):
        pass