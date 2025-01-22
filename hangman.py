import pygame
import random

# Initialize Pygame
pygame.init()

# Window dimensions
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

# Fonts
font = pygame.font.Font(None, 40)
input_font = pygame.font.Font(None, 30)

# Load hangman images
hangman_images = [
    pygame.image.load("images/hangman_1.png"),  # 0 attempts
    pygame.image.load("images/hangman_2.png"),  # 1 attempt
    pygame.image.load("images/hangman_3.png"),  # 2 attempts
    pygame.image.load("images/hangman_4.png"),  # 3 attempts
    pygame.image.load("images/hangman_5.png"),  # 4 attempts
    pygame.image.load("images/hangman_6.png"),  # 5 attempts
    pygame.image.load("images/hangman_7.png"),  # 6 attempts
]

# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Function to display the main menu
def show_menu():
    screen.fill(WHITE)
    draw_text("--- Hangman Game Menu ---", font, BLACK, screen, window_width // 2, window_height // 4)
    draw_text("1. Play", font, BLACK, screen, window_width // 2, window_height // 2 - 80)
    draw_text("2. Add a word", font, BLACK, screen, window_width // 2, window_height // 2 - 40)
    draw_text("3. View scores", font, BLACK, screen, window_width // 2, window_height // 2)
    draw_text("4. Delete all scores", font, BLACK, screen, window_width // 2, window_height // 2 + 40)
    draw_text("5. Quit", font, BLACK, screen, window_width // 2, window_height // 2 + 80)
    pygame.display.update()

# Function to display the difficulty selection screen
def show_difficulty_screen():
    screen.fill(WHITE)
    draw_text("Select Difficulty:", font, BLACK, screen, window_width // 2, window_height // 4)
    draw_text("1. Easy", font, BLACK, screen, window_width // 2, window_height // 2 - 30)
    draw_text("2. Medium", font, BLACK, screen, window_width // 2, window_height // 2)
    draw_text("3. Hard", font, BLACK, screen, window_width // 2, window_height // 2 + 30)
    pygame.display.update()

# Function to choose difficulty
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

# Function to get the player's name
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

# Function to load words from a file
def load_words(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return []

# Function to choose a word based on difficulty
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

# Function to view scores
def view_scores(score_file):
    try:
        with open(score_file, 'r', encoding='utf-8') as f:
            scores = f.readlines()
        if scores:
            screen.fill(WHITE)
            draw_text("Scores:", font, BLACK, screen, window_width // 2, window_height // 4)
            for i, score in enumerate(scores, start=1):
                draw_text(f"{i}. {score.strip()}", font, BLACK, screen, window_width // 2, window_height // 4 + i * 40)
            pygame.display.update()
            pygame.time.wait(3000)
        else:
            print("No scores available.")
    except FileNotFoundError:
        print("No scores file found.")

# Function to delete all scores
def delete_scores(score_file):
    try:
        open(score_file, 'w').close()  # Clear the file
        print("All scores deleted.")
    except FileNotFoundError:
        print("No scores file found.")

# Main game function
def play_game(word_file, score_file):
    words = load_words(word_file)
    if not words:
        print("No words available. Please add words to the file.")
        return

    difficulty = choose_difficulty()
    player_name = get_player_name()
    word_to_guess = choose_word(words, difficulty)
    guessed_letters = set()
    proposed_letters = set()
    remaining_attempts = 7 if difficulty == "easy" else 6 if difficulty == "medium" else 5
    score = 0

    # Game loop
    while remaining_attempts > 0:
        screen.fill(WHITE)
        draw_text(f"Word: {' '.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])}", font, BLACK, screen, window_width // 2, window_height // 3)
        draw_text(f"Attempts left: {remaining_attempts}", font, BLACK, screen, window_width // 2, window_height // 2)
        draw_text(f"Score: {score}", font, BLACK, screen, window_width // 2, window_height // 2 + 40)
        screen.blit(hangman_images[7 - remaining_attempts], (window_width // 2 - 100, window_height // 2 + 80))  # Display the hangman image

        pygame.display.update()

        # Listen for events
        letter = None
        while letter is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Return to menu

                    # Check if a valid letter was pressed
                    if pygame.K_a <= event.key <= pygame.K_z:
                        letter = chr(event.key).lower()

        if letter in proposed_letters:
            continue  # Skip if the letter was already proposed

        proposed_letters.add(letter)

        if letter in word_to_guess:
            guessed_letters.add(letter)
            score += 10  # Add points for a correct letter
        else:
            remaining_attempts -= 1
            score -= 5  # Deduct points for a wrong letter

        if all(letter in guessed_letters for letter in word_to_guess):
            draw_text(f"Congrats! You guessed the word: {word_to_guess}", font, GREEN, screen, window_width // 2, window_height // 2 + 100)
            pygame.display.update()
            pygame.time.delay(2000)
            break

    else:
        draw_text(f"You lost! The word was: {word_to_guess}", font, RED, screen, window_width // 2, window_height // 2 + 100)
        pygame.display.update()
        pygame.time.delay(2000)

    # Save the score
    with open(score_file, 'a', encoding='utf-8') as f:
        f.write(f"{player_name}: {score}\n")

# Main program loop
def main():
    word_file = "words.txt"
    score_file = "scores.txt"

    while True:
        show_menu()
        choice = None
        while choice is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        play_game(word_file, score_file)
                    elif event.key == pygame.K_2:
                        word = input("Enter a new word: ").strip()
                        if word:
                            with open(word_file, 'a', encoding='utf-8') as f:
                                f.write(f"{word}\n")
                            print("Word added successfully!")
                    elif event.key == pygame.K_3:
                        view_scores(score_file)
                    elif event.key == pygame.K_4:
                        delete_scores(score_file)
                    elif event.key == pygame.K_5:
                        pygame.quit()
                        exit()

if __name__ == "__main__":
    main()
