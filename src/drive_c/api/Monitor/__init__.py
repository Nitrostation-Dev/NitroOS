import pygame

class Monitor:
    def __init__(self, resolution, fps) -> None:
        self.name = "Monitor"
        self.resolution = resolution
        self.fps = fps

        pygame.display.set_caption(self.name)
        self.output_surface = pygame.display.set_mode(resolution)

    def update_output(self, surface: pygame.Surface) -> None:
        self.output_surface.fill((0, 0, 0))

        self.output_surface.blit(surface, (0, 0))
