import pygame

from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.Window import Window, WindowNoDecorations


class Desktop:
    def __init__(self, id: int, size: (int, int), assets: AssetManager) -> None:
        self.id = id
        self.surface = pygame.Surface(size)

        self.windows = []

        self.assets = assets

    def gen_id(self) -> int:
        return len(self.windows)

    def add_window(self, window: WindowNoDecorations | Window) -> None:
        self.windows.append(window)

    def events(self, event) -> None:
        for window in self.windows:
            window.events(event)

    def update(self) -> None:
        for window in self.windows:
            window.update()

    def draw(self, output_surface: pygame.Surface) -> None:
        for window in self.windows:
            window.draw(self.surface)

        output_surface.blit(self.surface, (0, 0))


class DesktopHandler:
    def __init__(self, assets: AssetManager) -> None:
        self.desktops = []
        self.active_desktop_index = 0

        self.assets = assets

    def create_desktop(self, DesktopClass: Desktop):
        self.desktops.append(
            DesktopClass(
                len(self.desktops), self.assets.get_asset("monitor_size"), self.assets
            )
        )

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
