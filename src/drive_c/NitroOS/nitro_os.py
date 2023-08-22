import sys
import pygame

from src.drive_c.api.Monitor import Monitor
from src.drive_c.api.Desktop import DesktopHandler
from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.NitroOS.login_screen import LoginDesktop


class NitroOS:
    def __init__(self) -> None:
        # Monitor
        self.output_res = (1600, 900)
        self.output_fps = 60

        self.clock = pygame.time.Clock()

        self.monitor = Monitor(self.output_res, 60)
        # Assets
        self.assets = AssetManager()

        self.assets.add_asset("monitor_size", self.output_res)

        interface_font_size = 20
        self.assets.add_asset("interface_font_size", interface_font_size)

        # Interface Fonts
        self.assets.add_asset(
            "interface_font_family_regular",
            pygame.font.Font(
                "src/drive_c/assets/fonts/Ubuntu-Regular.ttf", interface_font_size
            ),
        )
        self.assets.add_asset(
            "interface_font_family_bold",
            pygame.font.Font(
                "src/drive_c/assets/fonts/Ubuntu-Bold.ttf", interface_font_size
            ),
        )
        self.assets.add_asset(
            "interface_font_family_italic",
            pygame.font.Font(
                "src/drive_c/assets/fonts/Ubuntu-Italic.ttf", interface_font_size
            ),
        )

        self.assets.add_asset("interface_text_fg_color", (0, 0, 0))

        # Desktop
        self.desktop_handler = DesktopHandler(self.assets)
        # self.desktop_handler.add_desktop(LoginDesktop(0, self.output_res))
        self.desktop_handler.create_desktop(LoginDesktop)

        self.running = True

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.desktop_handler.draw(self.monitor.output_surface)

        pygame.display.update()
        self.clock.tick(self.output_fps)

    def loop(self) -> None:
        while self.running:
            self.events()
            self.update()
            self.draw()
