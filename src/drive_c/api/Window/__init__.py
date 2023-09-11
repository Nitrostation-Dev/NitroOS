import pygame
from enum import Enum

from src.drive_c.api.AssestManager import AssetManager


class WindowAnimation(Enum):
    OPENING = 1
    CLOSING = 2


class WindowNoDecorations:
    def __init__(self, id: int, assets: AssetManager, **kargs) -> None:
        self.name = "Undefined Title"
        self.id = id
        self.assets = assets

        self.size = (600, 350)
        self.pos = (30, 30)

        self.__dict__.update(kargs)

        self.surface = pygame.Surface(self.size)
        self.rect = self.surface.get_rect(topleft=self.pos)

        # Animation Variables
        self.animation = WindowAnimation.OPENING
        self.should_animate = False
        self.is_animating = False

    def final_init(self) -> None:
        # del self.size
        # del self.pos
        pass

    def animate_opening(self, delta: float, init_v: float = 7500) -> None:
        if self.should_animate:
            self.is_animating = True
            self.should_animate = False

            # Animate 'Ease Out' From Bottom to Top
            self.final_pos_y = self.rect.y
            self.rect.y = self.assets.get_asset("monitor_size")[1]
            self.init_distance = -(self.final_pos_y - self.rect.y)
            self.initial_velocity = init_v
            self.animation_velocity = self.initial_velocity

        if self.is_animating:
            if self.rect.y > self.final_pos_y:
                self.animation_velocity = (
                    self.initial_velocity
                    * (-(self.final_pos_y - self.rect.y) / self.init_distance)
                    * delta
                )
                self.animation_velocity = (
                    1.0 if self.animation_velocity < 1.0 else self.animation_velocity
                )

                self.rect.y -= self.animation_velocity
                self.rect.y = (
                    self.final_pos_y if self.rect.y <= self.final_pos_y else self.rect.y
                )

            else:
                self.should_animate = False
                self.is_animating = False

    def handle_animations(self, delta: float) -> None:
        if not self.should_animate and not self.is_animating:
            return

        if self.animation == WindowAnimation.OPENING:
            self.animate_opening(
                delta, self.assets.get_asset("window_opening_initial_velocity")
            )

    def events(self, event) -> None:
        pass

    def update(self, delta: float) -> None:
        pass

    def draw(self, output_surface: pygame.Surface) -> None:
        output_surface.blit(self.surface, self.rect)


class WindowNoDecorRounded(WindowNoDecorations):
    def __init__(self, id: int, assets: AssetManager, **kargs) -> None:
        self.border_radius = 8

        super().__init__(id, assets, **kargs)

    def draw(self, output_surface: pygame.Surface) -> None:
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


class Window(WindowNoDecorRounded):
    def final_init(self) -> None:
        super().final_init()

        self.animation = WindowAnimation.OPENING
        self.should_animate = True

    def update(self, delta: float) -> None:
        self.handle_animations(delta)
        return super().update(delta)
