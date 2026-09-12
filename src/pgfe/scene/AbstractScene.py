
from __future__ import annotations

import abc
import typing
import dataclasses
import pygame as pg

if typing.TYPE_CHECKING:
    from pgfe.game.AbstractGame import AbstractGame


@dataclasses.dataclass
class SceneColors:

    BG: pg.Color = dataclasses.field(
        default_factory=lambda: pg.Color("black")
    )

    FG: pg.Color = dataclasses.field(
        default_factory=lambda: pg.Color("grey")
    )

    extra: dict[str, pg.Color] = dataclasses.field(default_factory=dict)

    def add_color(self, name: str, color: pg.Color):
        self.extra[name] = color


class AbstractScene(abc.ABC):

    def __init__(self, game: AbstractGame, colors: SceneColors = SceneColors(), **groups: pg.sprite.Group):

        self.game: AbstractGame = game

        self.colors: SceneColors = colors

        self.groups: dict[str, pg.sprite.Group] = groups

    @abc.abstractmethod
    def load(self):
        pass

    def reset(self):
        for group in self.groups.values():
            group.empty()

    def update(self, *args, **kwargs):
        for group in self.groups.values():
            group.update(*args, **kwargs)

    def render(self, surface: pg.Surface):
        for group in self.groups.values():
            group.draw(surface)
