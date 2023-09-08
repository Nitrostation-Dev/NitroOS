import pygame

from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.Events import Event
from src.drive_c.api.Window import Window, WindowNoDecorations, WindowNoDecorRounded


class Desktop:
    def __init__(self, id: int, size: (int, int), assets: AssetManager) -> None:
        self.id = id
        self.surface = pygame.Surface(size)
        self.assets = assets

        self.windows = []

    def final_init(self) -> None:
        for window in self.windows:
            window.final_init()

    def gen_id(self) -> int:
        return len(self.windows)

    def create_window(
        self,
        WindowClass: Window | WindowNoDecorations | WindowNoDecorRounded,
        **window_args
    ) -> None:
        self.windows.append(WindowClass(len(self.windows), self.assets, **window_args))

    def add_window(self, window: WindowNoDecorations | Window) -> None:
        self.windows.append(window)

    def events(self, event) -> None:
        for window in self.windows:
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

            mouse_pos_x -= window.rect.x
            mouse_pos_y -= window.rect.y

            if mouse_pos_x < 0:
                mouse_pos_x = 0

            if mouse_pos_y < 0:
                mouse_pos_y = 0

            window.events(Event(event, (mouse_pos_x, mouse_pos_y)))

    def update(self) -> None:
        for window in self.windows:
            window.update()

    def draw(self, output_surface: pygame.Surface) -> None:
        for window in self.windows:
            window.draw(self.surface)

        output_surface.blit(self.surface, (0, 0))


class DesktopHandler:
    def __init__(self) -> None:
        self.desktops = []
        self.active_desktop_index = 0

    def final_init(self) -> None:
        for desktop in self.desktops:
            desktop.final_init()

    def add_desktop(self, desktop: Desktop):
        self.desktops.append(desktop)

    def change_to_desktop(self, id: str) -> None:
        for i in range(len(self.desktops)):
            if self.desktops[i].id != id:
                continue

            self.active_desktop_index = i

    def events(self, event):
        if len(self.desktops) < 0:
            return

        self.desktops[self.active_desktop_index].events(event)

    def update(self) -> None:
        if len(self.desktops) < 0:
            return

        self.desktops[self.active_desktop_index].update()

    def draw(self, output_surface: pygame.Surface) -> None:
        if len(self.desktops) < 0:
            return

        self.desktops[self.active_desktop_index].draw(output_surface)
