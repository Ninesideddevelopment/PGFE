
import pygame as pg
from pygame import Surface, FRect, Rect

from pgfe.camera import Camera2D


class GameObject(pg.sprite.Sprite):

    def __init__(self, *groups, image_varients: dict[str, pg.Surface]):
        super().__init__(*groups)

        self.image = list(image_varients.values())[0]
        self.rect = pg.FRect(self.image.get_rect())


class ObjectGroup(pg.sprite.Group):

    def draw(
            self,
            surface: Surface,
            bgd: Surface | None = None,
            special_flags: int = 0,
            camera: Camera2D = None,
    ) -> list[FRect | Rect]:
        if camera is None:
            return super().draw(surface, bgd, special_flags)

        sprites = self.sprites()
        if hasattr(surface, "blits"):
            self.spritedict.update(
                zip(
                    sprites,
                    surface.blits(
                        (
                            spr.image,
                            pg.Rect(spr.rect.x - spr.rect.width / 2 + camera.x, spr.rect.y - spr.rect.height / 2 + camera.y, spr.rect.w, spr.rect.h),
                            None,
                            special_flags
                        ) for spr in sprites
                    ),
                )
            )
        else:
            for spr in sprites:
                self.spritedict[spr] = surface.blit(
                    spr.image, spr.rect, None, special_flags
                )
        self.lostsprites = []
        dirty = self.lostsprites

        return dirty
