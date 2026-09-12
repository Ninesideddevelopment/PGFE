
import abc
import pygame as pg


class AbstractComponent(abc.ABC):
    def __init__(self):
        self.rect: pg.FRect|Pg.Rect = None
        self.velocity: pg.Vector2|None = None
