import pygame

class Desktop:
    def __init__(self, id: int, size: (int, int)) -> None:
        self.id = id
        self.surface = pygame.Surface(size)

    def events(self, event) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self, output_surface: pygame.Surface) -> None:
        output_surface.blit(self.surface, (0, 0))


class DesktopHandler:
    def __init__(self) -> None:
        self.desktops = []
        self.active_desktop_index = 0

    def add_desktop(self, desktop: Desktop) -> None:
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
