
from typing import Literal

import pygame as pg

class Window(pg.Window):

    def __init__(
            self,
            title: str = "pygame window",
            size: Point = (640, 480),
            position: int | Point = pg.WINDOWPOS_UNDEFINED,
            *,
            fullscreen: bool = False,
            fullscreen_desktop: bool = False,
            opengl: bool = False,
            vulkan: bool = False,
            hidden: bool = False,
            borderless: bool = False,
            resizable: bool = False,
            minimized: bool = False,
            maximized: bool = False,
            mouse_grabbed: bool = False,
            keyboard_grabbed: bool = False,
            input_focus: bool = False,
            mouse_focus: bool = False,
            allow_high_dpi: bool = False,
            mouse_capture: bool = False,
            always_on_top: bool = False,
            utility: bool = False,
    ) -> None:
        super().__init__(
            title=title,
            size=size,
            position=position,
            fullscreen=fullscreen,
            fullscreen_desktop=fullscreen_desktop,
            opengl=opengl,
            vulkan=vulkan,
            hidden=hidden,
            borderless=borderless,
            resizable=resizable,
            minimized=minimized,
            maximized=maximized,
            mouse_grabbed=mouse_grabbed,
            keyboard_grabbed=keyboard_grabbed,
            input_focus=input_focus,
            mouse_focus=mouse_focus,
            allow_high_dpi=allow_high_dpi,
            mouse_capture=mouse_capture,
            always_on_top=always_on_top,
            utility=utility,
        )

        self.fullscreen_mode: Literal["windowed", "fullscreen_desktop"] = "windowed"
        if fullscreen_desktop:
            self.fullscreen_mode = "fullscreen_desktop"

    def toggle_fullscreen(self) -> None:
        if self.fullscreen_mode == "windowed":
            self.fullscreen_mode = "fullscreen_desktop"
            self.set_fullscreen(desktop=True)

        elif self.fullscreen_mode == "fullscreen_desktop":
            self.fullscreen_mode = "windowed"
            self.set_windowed()