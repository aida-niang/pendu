import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
window_width = 600
window_height = 800
screen = pygame.display.set_mode((window_width, window_height))
title = pygame.display.set_caption("Hangman Game")

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

# Display screen difficulty
def show_difficulty_screen():
    screen.fill(WHITE)
    draw_text("Select Difficulty:", font, BLACK, screen, window_width // 2, window_height // 4)
    draw_text("1. Easy", font, BLACK, screen, window_width // 2, window_height // 2 - 30)
    draw_text("2. Medium", font, BLACK, screen, window_width // 2, window_height // 2)
    draw_text("3. Hard", font, BLACK, screen, window_width // 2, window_height // 2 + 30)
    pygame.display.update()

# Choose difficulty
def choose_difficulty():
    show_difficulty_screen()
    difficulty = None
    while difficulty is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "easy"
                elif event.key == pygame.K_2:
                    difficulty = "medium"
                elif event.key == pygame.K_3:
                    difficulty = "hard"
    return difficulty

# Write First  name
def get_player_name():
    input_box = pygame.Rect(window_width // 2 - 100, window_height // 2, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 32)

    while True:
        screen.fill(WHITE)
        draw_text("Enter your name:", font, BLACK, screen, window_width // 2, window_height // 3)
        pygame.draw.rect(screen, color, input_box, 2)
        draw_text(text, font, BLACK, screen, window_width // 2, window_height // 2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                    color = color_active
                else:
                    active = False
                    color = color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

# Fonction pour charger les mots
def load_words(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return []

# Fonction pour choisir un mot selon la difficulté
def choose_word(words, difficulty):
    if difficulty == "easy":
        filtered_words = [word for word in words if len(word) <= 6]
    elif difficulty == "medium":
        filtered_words = [word for word in words if 7 <= len(word) <= 9]
    elif difficulty == "hard":
        filtered_words = [word for word in words if len(word) > 9]
    else:
        filtered_words = words

    return random.choice(filtered_words)

# Main loop
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
