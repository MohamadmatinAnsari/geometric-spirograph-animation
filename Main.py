import math
import sys
import pygame

WIDTH, HEIGHT = 900, 700
FPS = 60

BG_COLOR = (15, 15, 25)
PRIMARY_COLOR = (0, 229, 255)
SECONDARY_COLOR = (255, 0, 128)
ACCENT_COLOR = (124, 77, 255)
TEXT_COLOR = (200, 200, 220)


class GeometricPatternAnimator:

    def __init__(self, width: int, height: int):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Geometric Wave & Spirograph Animation - Pygame")
        self.clock = pygame.time.Clock()
        self.time_counter = 0.0

        try:
            self.font = pygame.font.SysFont("Arial", 18)
        except Exception:
            self.font = pygame.font.Font(None, 24)

    def draw_background_grid(self):
        grid_size = 50
        for x in range(0, self.width, grid_size):
            pygame.draw.line(self.screen, (25, 25, 40), (x, 0), (x, self.height), 1)
        for y in range(0, self.height, grid_size):
            pygame.draw.line(self.screen, (25, 25, 40), (0, y), (self.width, y), 1)

    def draw_wave_pattern(self):
        center_x, center_y = self.width // 2, self.height // 2
        num_circles = 18
        max_radius = 280

        for i in range(num_circles):
            offset_angle = self.time_counter * 1.5 + (i * 0.3)
            radius = int(max_radius * abs(math.sin(offset_angle * 0.5)) + 40)
            
            orbit_radius = 60 * math.sin(self.time_counter * 0.8 + i * 0.2)
            x = center_x + int(orbit_radius * math.cos(offset_angle))
            y = center_y + int(orbit_radius * math.sin(offset_angle))

            color_factor = (math.sin(self.time_counter + i * 0.2) + 1) / 2
            color = (
                int(PRIMARY_COLOR[0] * (1 - color_factor) + SECONDARY_COLOR[0] * color_factor),
                int(PRIMARY_COLOR[1] * (1 - color_factor) + SECONDARY_COLOR[1] * color_factor),
                int(PRIMARY_COLOR[2] * (1 - color_factor) + SECONDARY_COLOR[2] * color_factor),
            )

            pygame.draw.circle(self.screen, color, (x, y), radius, 1)

            if i > 0:
                prev_x = center_x + int(orbit_radius * math.cos(self.time_counter * 1.5 + ((i - 1) * 0.3)))
                prev_y = center_y + int(orbit_radius * math.sin(self.time_counter * 1.5 + ((i - 1) * 0.3)))
                pygame.draw.line(self.screen, ACCENT_COLOR, (prev_x, prev_y), (x, y), 1)

    def render_hud(self):
        fps_text = f"FPS: {int(self.clock.get_fps())}"
        text_surface = self.font.render(fps_text, True, TEXT_COLOR)
        self.screen.blit(text_surface, (20, 20))

        guide_surface = self.font.render("Press ESC to Exit", True, (100, 100, 120))
        self.screen.blit(guide_surface, (20, self.height - 40))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.time_counter += 0.02
            self.screen.fill(BG_COLOR)

            self.draw_background_grid()
            self.draw_wave_pattern()
            self.render_hud()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    animator = GeometricPatternAnimator(WIDTH, HEIGHT)
    animator.run()
