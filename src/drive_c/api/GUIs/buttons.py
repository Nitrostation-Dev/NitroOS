import pygame
from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.Events import Event
from src.drive_c.api.GUIs import FontStyle, GuiElement, PositionType


class GuiElementButton(GuiElement):
    def __init__(
        self,
        name: str,
        pos: (int, int),
        asset_manager: AssetManager,
        message: str,
        trigger_func,
        **kargs
    ) -> None:
        super().__init__(name, pos, asset_manager, **kargs)

        # Font Settings
        self.font_style = FontStyle.REGULAR
        self.font_size = self.asset_manager.get_asset("interface_font_size")
        self.fg_color = self.asset_manager.get_asset("interface_text_fg_color")
        self.message = message

        # Input Field Settings
        self.border_size = 2
        self.padding_h = 8
        self.padding_v = 3
        self.border_color = (75, 75, 75)
        self.background_color = (200, 200, 200)

        self.pos_type = PositionType.TOPLEFT
        self.trigger_func = trigger_func
        self.size_x = self.font_size * len(self.message)

        # Button Settings
        self.hover_border_color = (30, 30, 30)
        self.hover_bg_color = (175, 175, 175)
        self.click_border_color = (0, 0, 0)
        self.click_bg_color = (150, 150, 150)

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
            self.size_x + (2 * self.border_size) + (2 * self.padding_h),
            self.font_size + (2 * self.padding_v) + (2 * self.border_size),
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

        self.text_surface = self.font_family.render(self.message, True, self.fg_color)
        self.text_rect = self.text_surface.get_rect(center=self.background_rect.center)

        self.hover = False
        self.click = False

    def events(self, event: Event) -> None:
        mouse_pos = event.mouse_pos

        self.hover = self.border_rect.collidepoint(mouse_pos[0], mouse_pos[1])

        if self.hover:
            if not self.click and event.pg_event.type == pygame.MOUSEBUTTONDOWN:
                self.click = True
                self.trigger_func()
        else:
            self.click = False

        if event.pg_event.type == pygame.MOUSEBUTTONUP:
            self.click = False

    def draw(self, output_surface: pygame.Surface) -> None:
        if self.click:
            pygame.draw.rect(
                output_surface,
                self.click_border_color,
                self.border_rect,
                border_radius=8,
            )
            pygame.draw.rect(
                output_surface,
                self.click_bg_color,
                self.background_rect,
                border_radius=8,
            )

        elif self.hover:
            pygame.draw.rect(
                output_surface,
                self.hover_border_color,
                self.border_rect,
                border_radius=8,
            )
            pygame.draw.rect(
                output_surface,
                self.hover_bg_color,
                self.background_rect,
                border_radius=8,
            )

        else:
            pygame.draw.rect(
                output_surface, self.border_color, self.border_rect, border_radius=8
            )
            pygame.draw.rect(
                output_surface,
                self.background_color,
                self.background_rect,
                border_radius=8,
            )

        output_surface.blit(self.text_surface, self.text_rect)
