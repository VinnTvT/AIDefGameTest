import pygame
import random
import sys
import nltk
from nltk.corpus import wordnet

pygame.init()

WIDTH, HEIGHT = 800, 600
FONT_SIZE = 36
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

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Definition Game")

font = pygame.font.Font(None, FONT_SIZE)

def render_text_centered(text, y_position, color=BLACK):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, y_position))
    screen.blit(text_surface, text_rect)

def main():
    score = 0
    current_word, current_definition = get_random_word_definition()
    user_input = ""

    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)

        render_text_centered(f"Definition: {current_definition}", HEIGHT // 3)
        render_text_centered(f"Your Answer: {user_input}", HEIGHT // 2)
        render_text_centered(f"Score: {score}", HEIGHT * 2 // 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input.lower() == current_word:
                        score += 1
                        user_input = ""
                        current_word, current_definition = get_random_word_definition()
                    else:
                        print(f"Wrong! The correct word was: {current_word}")
                        user_input = ""
                        current_word, current_definition = get_random_word_definition()
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    if event.unicode.isalpha() and len(event.unicode) == 1:
                        user_input += event.unicode

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
