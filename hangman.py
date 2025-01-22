import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
window_width = 600
window_height = 800
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Hangman Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Font
font = pygame.font.Font(None, 40)
input_font = pygame.font.Font(None, 30)


# Display a text in the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Display Menu
def show_menu():
    screen.fill(WHITE)
    draw_text("--- Hangman Game Menu ---", font, BLACK, screen, window_width // 2, window_height // 4)
    draw_text("1. Play", font, BLACK, screen, window_width // 2, window_height // 2 - 80)
    draw_text("2. Add a word", font, BLACK, screen, window_width // 2, window_height // 2 - 40)
    draw_text("3. View scores", font, BLACK, screen, window_width // 2, window_height // 2)
    draw_text("4. Delete all scores", font, BLACK, screen, window_width // 2, window_height // 2 + 40)
    draw_text("5. Quit", font, BLACK, screen, window_width // 2, window_height // 2 + 80)
    pygame.display.update()

# Fonction principale
def main():
    running = True
    while running:
        show_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("Play selected.")
                elif event.key == pygame.K_2:
                    print("Add a word selected.")
                elif event.key == pygame.K_3:
                    print("View scores selected.")
                elif event.key == pygame.K_4:
                    print("Delete all scores selected.")
                elif event.key == pygame.K_5:
                    print("Quit selected.")
                    running = False

    pygame.quit()

# Lancer le programme
if __name__ == "__main__":
    main()
