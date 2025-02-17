import pygame
import random
import sys
import nltk
from nltk.corpus import wordnet

pygame.init()

# Default settings
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 24
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

nltk.download('wordnet')

def get_random_word_definition():
    all_words = list(wordnet.all_lemma_names())
    random_word = random.choice(all_words)
    synsets = wordnet.synsets(random_word)
    if synsets:
        definition = synsets[0].definition()
    else:
        definition = "No definition found."
    return random_word, definition

def get_user_settings():
    global WIDTH, HEIGHT, FONT_SIZE, FPS
    while True:
        try:
            WIDTH = int(input("Enter screen width (default 800): ") or 800)
            HEIGHT = int(input("Enter screen height (default 600): ") or 600)
            FONT_SIZE = int(input("Enter font size (default 24): ") or 24)
            FPS = int(input("Enter frames per second (default 30): ") or 30)

            # Validate the inputs
            if WIDTH <= 0 or HEIGHT <= 0 or FONT_SIZE <= 0 or FPS <= 0:
                print("Please enter positive values for width, height, font size, and FPS.")
                continue
            
            # Check for reasonable screen size
            if WIDTH > 3000 or HEIGHT > 3000:
                print("Please enter reasonable values for width and height (max 3000).")
                continue
            
            break  # Exit the loop if all inputs are valid
        except ValueError:
            print("Invalid input, please enter numeric values.")

def render_text_centered(screen, text, y_position, font, color=BLACK):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, y_position))
    screen.blit(text_surface, text_rect)

def main():
    get_user_settings()  # Get user settings at the start

    # Initialize the Pygame screen with user-defined dimensions
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Word Definition Game")

    # Update font size based on user input
    font = pygame.font.Font(None, FONT_SIZE)

    score = 0
    current_word, current_definition = get_random_word_definition()
    user_input = ""

    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)

        # Render text with improved spacing
        line_spacing = FONT_SIZE + 10  # Adjust line spacing as needed
        render_text_centered(screen, "Word Definition Game", HEIGHT // 10, font)
        render_text_centered(screen, f"Definition: {current_definition}", HEIGHT // 3, font)
        render_text_centered(screen, f"Your Answer: {user_input}", HEIGHT // 2 + line_spacing, font)
        render_text_centered(screen, f"Score: {score}", HEIGHT * 2 // 3 + 2 * line_spacing, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input.strip() == "":
                        print("Please enter a word.")
                    elif user_input.lower() == current_word:
                        score += 1
                        user_input = ""
                        current_word, current_definition = get_random_word_definition()
                    else:
                        print(f"Wrong! The correct word was: {current_word}")
                        user_input = ""
                        current_word, current_definition = get_random_word_definition()
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_SPACE:  # Allow space input
                    user_input += " "
                else:
                    if event.unicode.isalpha() and len(event.unicode) == 1:
                        user_input += event.unicode

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
