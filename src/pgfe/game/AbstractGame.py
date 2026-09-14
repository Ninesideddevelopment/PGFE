
import abc
import pygame as pg

from pgfe.camera import Camera2D
from pgfe.scene.AbstractScene import AbstractScene
from pgfe import events_manager


def quit(event: int):
    pg.quit()
    raise SystemExit


class AbstractGame(abc.ABC):

    def __init__(self, framerate: int = 60, tickrate: int = 60, camera: Camera2D|None = None, **window_args):
        self.window: pg.Window = pg.Window(**window_args)
        self.window.get_surface()

        self.clock: pg.time.Clock = pg.time.Clock()

        self.framerate: int = framerate
        self.tickrate: int = tickrate

        self.dt: float = 0
        self.frame_dt: float = 0

        self.scene: AbstractScene|None = None
        self.camera: Camera2D|None = camera

        events_manager.add(pg.QUIT, quit)

    def set_scene(self, scene: AbstractScene):
        self.scene = scene
        self.scene.load()

    def tick(self):
        self.dt = self.clock.tick(self.tickrate) / 1000
        self.frame_dt = self.dt * self.framerate

    def update_idle_tasks(self):
        self.scene.render(self.window.get_surface(), camera=self.camera)
        events_manager.update_events()
        self.window.flip()

    def play(self):
        while True:
            self.tick()

            self.window.get_surface().fill(self.scene.colors.BG)

            self.scene.update()

            self.update_idle_tasks()
