import pygame


class WindowNoDecorations:
    def __init__(self, id: int, **kargs) -> None:
        self.name = "Undefined Title"
        self.id = id

        self.size = (600, 350)
        self.pos = (30, 30)

        self.__dict__.update(kargs)

        self.surface = pygame.Surface(self.size)
        self.rect = self.surface.get_rect(topleft=self.pos)

        # Rounded Corners functionalitiy

        del self.size
        del self.pos

    def events(self, event) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.fill((0, 0, 0))

        output_surface.blit(self.surface, self.rect)


class Window(WindowNoDecorations):
    def __init__(self, id: int, **kargs) -> None:
        self.border_radius = 8

        super().__init__(id, **kargs)

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.fill((0, 0, 0))

        # Rounded Corners
        rect_image = pygame.Surface(self.surface.get_size(), pygame.SRCALPHA)
        pygame.draw.rect(
            rect_image,
            (255, 255, 255),
            (0, 0, *self.surface.get_size()),
            border_radius=self.border_radius,
        )

        image = self.surface.copy().convert_alpha()
        image.blit(rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

        output_surface.blit(image, self.rect)
