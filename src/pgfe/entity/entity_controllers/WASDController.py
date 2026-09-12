
import pygame as pg

from pgfe.entity.entity_controllers.AbstractController import AbstractController


class WASDController(AbstractController):
    def __init__(self):
        super().__init__()

    def return_wasd(self) -> dict[str, float]:
        pressed = pg.key.get_pressed()

        return {
            "w": pressed[pg.K_w],
            "a": pressed[pg.K_a],
            "s": pressed[pg.K_s],
            "d": pressed[pg.K_d]
        }

    def return_movement(self) -> pg.Vector2:
        vector = pg.math.Vector2()
        wasd = self.return_wasd()

        if wasd["w"]:
            vector.x = 0
            vector.y -= 1
        if wasd["a"]:
            vector.y = 0
            vector.x -= 1
        if wasd["s"]:
            vector.x = 0
            vector.y += 1
        if wasd["d"]:
            vector.y = 0
            vector.x += 1

        return vector