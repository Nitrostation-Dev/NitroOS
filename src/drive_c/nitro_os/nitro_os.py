import sys
import os
import pygame

from src.drive_c.api.Monitor import Monitor
from src.drive_c.api.Desktop import DesktopHandler
from src.drive_c.api.AssestManager import AssetManager

from src.drive_c.nitro_os.read_json import get_json_data
from src.drive_c.nitro_os.login_screen import LoginDesktop
from src.drive_c.nitro_os.desktop import NitroDesktop


class NitroOS:
    def __init__(self) -> None:
        # Monitor
        self.output_res = (1600, 900)
        self.output_fps = 60
        self.monitor = Monitor(self.output_res)
        self.clock = pygame.time.Clock()

        # Get All User Logins Data
        login_details = []

        user_folders = os.listdir("src/drive_c/users/")
        for folder in user_folders:
            user_data = get_json_data(
                "src/drive_c/users/" + folder + "/data/login_details.json"
            )
            login_details.append(user_data)

        # Assets
        self.assets = AssetManager()

        interface_font_size = 20
        self.assets.update_asset(
            {
                "monitor_size": self.output_res,
                "fps": self.output_fps,
                "login_details": login_details,
                "interface_font_size": 20,
                "interface_font_family_regular": pygame.font.Font(
                    "src/drive_c/assets/fonts/Ubuntu-Regular.ttf", interface_font_size
                ),
                "interface_font_family_italic": pygame.font.Font(
                    "src/drive_c/assets/fonts/Ubuntu-Italic.ttf", interface_font_size
                ),
                "interface_font_family_bold": pygame.font.Font(
                    "src/drive_c/assets/fonts/Ubuntu-Bold.ttf", interface_font_size
                ),
                "interface_text_fg_color": (0, 0, 0),
                "login_wallpaper": pygame.transform.scale(
                    pygame.image.load(
                        "src/drive_c/assets/wallpapers/unsplash-login.jpg"
                    ),
                    self.output_res,
                ),
                "desktop_wallpaper": pygame.transform.scale(
                    pygame.image.load(
                        "src/drive_c/assets/wallpapers/unsplash-desktop.jpg"
                    ),
                    self.output_res,
                ),
            }
        )

        # Desktops
        self.desktop_handler = DesktopHandler(self.assets)
        self.desktop_handler.add_desktop(
            LoginDesktop(0, self.output_res, self.assets, self.desktop_handler)
        )
        self.desktop_handler.create_desktop(NitroDesktop)

        self.running = True

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            self.desktop_handler.events(event)

    def update(self) -> None:
        self.desktop_handler.update()

    def draw(self) -> None:
        self.desktop_handler.draw(self.monitor.output_surface)

        pygame.display.update()
        self.clock.tick(self.output_fps)

    def loop(self) -> None:
        while self.running:
            self.events()
            self.update()
            self.draw()
