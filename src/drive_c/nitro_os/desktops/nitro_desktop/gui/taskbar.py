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

        # Handle Pinned Apps
        self.pinned_apps_list = ["Files"]
        self.pinned_apps_data = []
        for app in self.assets.get_asset("apps"):
            for pinned_app in self.pinned_apps_list:
                if app["name"] == pinned_app:
                    self.pinned_apps_data.append(app)
        # Icons
        self.pinned_apps_icons = []
        for app in self.pinned_apps_data:
            self.pinned_apps_icons.append(
                self.assets.get_asset("get_icon")(app["icon_name"])
            )
        # Rects
        self.pinned_apps_rects = []
        for i in range(len(self.pinned_apps_data)):
            self.pinned_apps_rects.append(
                pygame.Rect(
                    self.rect.x + (self.rect.height * i),
                    self.rect.y,
                    self.rect.height,
                    self.rect.height,
                )
            )

    def events(self, event) -> None:
        super().events(event)

        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(self.pinned_apps_rects)):
                if self.pinned_apps_rects[i].collidepoint(pygame.mouse.get_pos()):
                    self.assets.get_asset("launch_app")(self.pinned_apps_data[i]["class"])

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
        image.set_alpha(self.assets.get_asset("taskbar_transparency"))
        image.blit(rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

        output_surface.blit(image, self.rect)

        # Draw Icons
        for i in range(len(self.pinned_apps_data)):
            output_surface.blit(
                self.pinned_apps_icons[i],
                (
                    self.pinned_apps_rects[i].centerx
                    - (self.pinned_apps_icons[i].get_width() / 2),
                    self.pinned_apps_rects[i].centery
                    - (self.pinned_apps_icons[i].get_height() / 2),
                ),
            )
