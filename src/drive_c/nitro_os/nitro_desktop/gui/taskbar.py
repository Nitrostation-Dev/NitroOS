import pygame
from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.Window import WindowNoDecorRounded


class Taskbar(WindowNoDecorRounded):
    def __init__(self, id: int, assets: AssetManager, **kargs) -> None:
        super().__init__(
            id,
            assets,
            size=(
                assets.get_asset("monitor_size")[0]
                - (assets.get_asset("taskbar_margin")[0] * 2),
                assets.get_asset("taskbar_height")
                - (assets.get_asset("taskbar_margin")[1] * 2),
            ),
            pos=(
                assets.get_asset("taskbar_margin")[0],
                assets.get_asset("monitor_size")[1]
                - assets.get_asset("taskbar_height")
                + assets.get_asset("taskbar_margin")[1],
            ),
        )

    def draw(self, output_surface: pygame.Surface) -> None:
        # Rounded Corners & Transparent BG
        self.surface.fill(self.assets.get_asset("taskbar_bg_color"))

        rect_image = pygame.Surface(self.surface.get_size(), pygame.SRCALPHA)
        pygame.draw.rect(
            rect_image,
            (255, 255, 255),
            (0, 0, *self.surface.get_size()),
            border_radius=self.assets.get_asset("taskbar_border_radius"),
        )

        image = self.surface.copy().convert_alpha()
        image.set_alpha(128)
        image.blit(rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

        output_surface.blit(image, self.rect)
