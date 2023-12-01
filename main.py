import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FALLING_SPEED_INCREMENT = 0.1  # Gravity effect
FALLING_ITEM_SIZE = 50
BASKET_SIZE = 60  # Smaller basket size

# Colors
WHITE = (255, 255, 255)

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Mr. Cornish")

# Load images
basket_img = pygame.image.load('images/basket.png')
basket_img = pygame.transform.scale(basket_img, (BASKET_SIZE, BASKET_SIZE))

cornish_img = pygame.image.load('images/Cornish.png')
cornish_img = pygame.transform.scale(cornish_img, (FALLING_ITEM_SIZE, FALLING_ITEM_SIZE))

# Variables
basket_x = SCREEN_WIDTH // 2
falling_item_x = random.randint(0, SCREEN_WIDTH - FALLING_ITEM_SIZE)
falling_item_y = -FALLING_ITEM_SIZE
falling_speed = 5
score = 0

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and basket_x > 0:
        basket_x -= 5
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and basket_x < SCREEN_WIDTH - BASKET_SIZE:
        basket_x += 5

    # Update falling item with gravity effect
    falling_item_y += falling_speed
    falling_speed += FALLING_SPEED_INCREMENT
    if falling_item_y > SCREEN_HEIGHT:
        falling_item_y = -FALLING_ITEM_SIZE
        falling_speed = 5
        falling_item_x = random.randint(0, SCREEN_WIDTH - FALLING_ITEM_SIZE)

    # Check collision
    if (falling_item_y + FALLING_ITEM_SIZE > SCREEN_HEIGHT - BASKET_SIZE and
        basket_x < falling_item_x + FALLING_ITEM_SIZE / 2 < basket_x + BASKET_SIZE):
        score += 1
        falling_item_y = -FALLING_ITEM_SIZE
        falling_speed = 5
        falling_item_x = random.randint(0, SCREEN_WIDTH - FALLING_ITEM_SIZE)

    # Draw
    screen.blit(basket_img, (basket_x, SCREEN_HEIGHT - BASKET_SIZE))
    screen.blit(cornish_img, (falling_item_x, falling_item_y))
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()