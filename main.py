import pygame
import random
import sys
import nltk
from nltk.corpus import wordnet

pygame.init()

WIDTH, HEIGHT = 600, 400
FONT_SIZE = 36
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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


def main():
    score = 0
    current_word, current_definition = get_random_word_definition()
    user_input = ""

    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)

    
        definition_text = font.render(f"Definition: {current_definition}", True, BLACK)
        screen.blit(definition_text, (10, 50))

     
        input_text = font.render(f"Your Answer: {user_input}", True, BLACK)
        screen.blit(input_text, (10, 100))

  
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 150))

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
