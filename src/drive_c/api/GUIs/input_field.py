import pygame
from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.Events import Event
from src.drive_c.api.GUIs import FontStyle, GuiElement, PositionType


class GuiElementInputField(GuiElement):
    def __init__(
        self,
        name: str,
        pos: (int, int),
        asset_manager: AssetManager,
        message: str,
        **kargs
    ) -> None:
        super().__init__(name, pos, asset_manager, **kargs)

        # Font Settings
        self.font_size = self.asset_manager.get_asset("interface_font_size")
        self.font_style = FontStyle.REGULAR
        self.message = message
        self.fg_color = self.asset_manager.get_asset("interface_text_fg_color")
        self.placehold_text_color = (175, 175, 175)

        # Input Field Settings
        self.border_size = 2
        self.padding = 3
        self.border_color = (75, 75, 75)
        self.background_color = (200, 200, 200)

        self.size_x = 300

        self.is_pass = False

        super().__init__(name, pos, asset_manager, **kargs)

        if self.font_style == FontStyle.REGULAR:
            self.font_family = self.asset_manager.get_asset(
                "interface_font_family_regular"
            )

        elif self.font_style == FontStyle.ITALIC:
            self.font_family = self.asset_manager.get_asset(
                "interface_font_family_italic"
            )

        elif self.font_style == FontStyle.BOLD:
            self.font_family = self.asset_manager.get_asset(
                "interface_font_family_bold"
            )

        size = (
            self.size_x + (2 * self.border_size) + (2 * self.padding),
            self.font_size + (2 * self.padding) + (2 * self.border_size),
        )
        self.surface = pygame.Surface(size)
        if self.pos_type == PositionType.TOPLEFT:
            self.border_rect = pygame.Rect(self.pos[0], self.pos[1], size[0], size[1])
            self.background_rect = pygame.Rect(
                self.pos[0] + self.border_size,
                self.pos[1] + self.border_size,
                size[0] - (2 * self.border_size),
                size[1] - (2 * self.border_size),
            )

        elif self.pos_type == PositionType.MIDLEFT:
            self.border_rect = pygame.Rect(
                self.pos[0], self.pos[1] - int(size[1] / 2), size[0], size[1]
            )
            self.background_rect = pygame.Rect(
                self.pos[0] + self.border_size,
                self.pos[1] + self.border_size - int(size[1] / 2),
                size[0] - (2 * self.border_size),
                size[1] - (2 * self.border_size),
            )

        elif self.pos_type == PositionType.CENTER:
            self.border_rect = pygame.Rect(
                self.pos[0] - int(size[0] / 2),
                self.pos[1] - int(size[1] / 2),
                size[0],
                size[1],
            )
            self.background_rect = pygame.Rect(
                self.pos[0] + self.border_size - int(size[0] / 2),
                self.pos[1] + self.border_size - int(size[1] / 2),
                size[0] - (2 * self.border_size),
                size[1] - (2 * self.border_size),
            )

        self.placehold_text_surface = self.font_family.render(
            self.message, True, self.placehold_text_color
        )
        self.placehold_text_rect = self.placehold_text_surface.get_rect(
            midleft=(
                self.background_rect.x + self.padding,
                self.border_rect.y + size[1] / 2,
            )
        )

        self.is_active = False
        self.input_text = ""
        self.input_text_surface = self.font_family.render(
            self.input_text, True, self.fg_color
        )
        self.input_rect = self.input_text_surface.get_rect(
            midleft=(
                self.background_rect.left + self.padding,
                self.background_rect.centery,
            )
        )
        self.input_rect.width = self.background_rect.width - (2 * self.padding)

    def events(self, event: Event) -> None:
        if event.pg_event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.mouse_pos
            if self.border_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                self.is_active = True
            else:
                self.is_active = False

        if event.pg_event.type == pygame.KEYDOWN:
            if self.is_active and event.pg_event.key == pygame.K_ESCAPE:
                self.is_active = False

            if self.is_active:
                if event.pg_event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]

                else:
                    self.input_text += event.pg_event.unicode

    def draw(self, output_surface: pygame.Surface) -> None:
        pygame.draw.rect(
            output_surface, self.border_color, self.border_rect, border_radius=8
        )
        pygame.draw.rect(
            output_surface, self.background_color, self.background_rect, border_radius=8
        )

        text = self.input_text if not self.is_pass else "*" * len(self.input_text)
        if self.is_active:
            self.input_text_surface = self.font_family.render(
                text + "|", True, self.fg_color
            )
        else:
            self.input_text_surface = self.font_family.render(
                text, True, self.fg_color
            )

        input_surface = pygame.Surface(
            (
                self.background_rect.width - (2 * self.padding),
                self.input_text_surface.get_size()[1],
            ),
            pygame.SRCALPHA,
            32,
        )

        if not self.is_active and self.input_text == "":
            output_surface.blit(self.placehold_text_surface, self.placehold_text_rect)
        else:
            input_surface.blit(self.input_text_surface, (0, 0))
            output_surface.blit(input_surface.convert_alpha(), self.input_rect)
