import pygame, random, json
from style import *

def get_font(size):
    return pygame.font.Font("assets/GLS.ttf", size)

def write_text(text, size, x, y, screen):
    text_font = get_font(size)
    title_surface = text_font.render(text, True, BLACK, PURPLE)
    score_rect = title_surface.get_rect(center = (x, y))
    screen.blit(title_surface, score_rect)

def update_score(username):
    with open('score.json', 'r') as file:
        user_list = json.load(file)
    
        if not username in user_list:
            user_list[username] = 1

        if username in user_list:

            user_list[username] += 1

    with open("score.json", "w") as file:
        json.dump(user_list, file, indent=4)

def main(username):
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Hangman Game")

    # Define fonts
    title_font = get_font(72)
    word_font = get_font(48)
    letter_font = get_font(36)

    # Load images
    hangman_images = []
    for i in range(7):
        hangman_images.append(pygame.image.load(f"assets/images/hangman_{i}.png"))

    # Load words
    with open("words.txt", "r") as f:
        words = f.read().splitlines()
    words = [word.strip() for word in words]

    # Choose a random word
    word = random.choice(words)

    # Create a list of underscores for the word
    word_display = ["_" for i in range(len(word))]

    # Set up game variables
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    guessed_letters = []

    # Game loop
    running = True
    while running:
        # print(word)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    letter = event.unicode.upper()
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if not letter in word.upper():
                            incorrect_guesses += 1
                        else:
                            for i in range(len(word)):
                                if word[i].upper() == letter:
                                    word_display[i] = letter

                

        # Draw the screen
        screen.fill(WHITE)

        # Draw the title
        write_text("Hangman Game", 60, 400, 50, screen)
    
        # Draw the hangman image
        screen.blit(hangman_images[incorrect_guesses], (20, 150))

        # Draw the word
        word_text = word_font.render(" ".join(word_display), True, BLACK)
        screen.blit(word_text, (400, 430))

        # Draw the guessed letters
        guessed_letters_text = letter_font.render(", ".join(guessed_letters), True, BLACK)
        screen.blit(guessed_letters_text, (screen_width // 2 - guessed_letters_text.get_width() // 2, 500))

        # Check if the game is over
        if "_" not in word_display or incorrect_guesses == max_incorrect_guesses:
            running = False

        # Update the screen
        pygame.display.update()

    # Game over
    if "_" not in word_display:
        update_score(username)
        game_over_text = title_font.render("You Win!", True, BLACK)
    else:
        game_over_text = title_font.render("You Lose!", True, BLACK)
    screen.blit(game_over_text, (400, 200))

    pygame.display.update()

    # Wait for a few seconds before closing the window
    pygame.time.wait(2000)

    # Quit Pygame
    pygame.quit()