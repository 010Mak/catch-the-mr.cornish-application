# code built by 010mak
# if you use it pls give credit

import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FALLING_SPEED_INCREMENT = 0.05
FALLING_ITEM_SIZE = 50
BASKET_SIZE = 60
BASKET_MOVE_SPEED = 10
SIZE_DECREMENT = 0.5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Mr. Cornish")

basket_img = pygame.image.load('images/basket.png')
basket_img = pygame.transform.scale(basket_img, (BASKET_SIZE, BASKET_SIZE))

cornish_img = pygame.image.load('images/Cornish.png')
cornish_img = pygame.transform.scale(cornish_img, (FALLING_ITEM_SIZE, FALLING_ITEM_SIZE))

font = pygame.font.SysFont(None, 36)
button_font = pygame.font.SysFont(None, 28)

score = 0
high_score = 0
current_basket_size = BASKET_SIZE
basket_x = SCREEN_WIDTH // 2
falling_item_x = random.randint(0, SCREEN_WIDTH - FALLING_ITEM_SIZE)
falling_item_y = -FALLING_ITEM_SIZE
falling_speed = 5

def reset_game():
    global score, current_basket_size, falling_speed, falling_item_y, falling_item_x, basket_x
    score = 0
    current_basket_size = BASKET_SIZE
    falling_speed = 5
    falling_item_y = -FALLING_ITEM_SIZE
    falling_item_x = random.randint(0, SCREEN_WIDTH - FALLING_ITEM_SIZE)
    basket_x = SCREEN_WIDTH // 2

def game_over_screen():
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if 350 < mouse_pos[0] < 450 and 350 < mouse_pos[1] < 390:
                    reset_game()
                    game_over = False

        screen.fill(GRAY)
        game_over_text = font.render("You didn't catch the Mr. Cornishes in time", True, BLACK)
        screen.blit(game_over_text, (150, 200))

        pygame.draw.rect(screen, WHITE, [350, 350, 100, 40])
        try_again_text = button_font.render("Try Again", True, BLACK)
        screen.blit(try_again_text, (360, 355))

        pygame.display.update()

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and basket_x > 0:
        basket_x -= BASKET_MOVE_SPEED
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and basket_x < SCREEN_WIDTH - current_basket_size:
        basket_x += BASKET_MOVE_SPEED

    falling_item_y += falling_speed
    falling_speed += FALLING_SPEED_INCREMENT
    if falling_item_y > SCREEN_HEIGHT:
        game_over_screen()

    if (falling_item_y + FALLING_ITEM_SIZE > SCREEN_HEIGHT - current_basket_size and
        basket_x < falling_item_x + FALLING_ITEM_SIZE / 2 < basket_x + current_basket_size):
        score += 1
        if score > high_score:
            high_score = score
        falling_item_y = -FALLING_ITEM_SIZE
        falling_speed = 5
        falling_item_x = random.randint(0, SCREEN_WIDTH - FALLING_ITEM_SIZE)
        current_basket_size = max(30, current_basket_size - SIZE_DECREMENT)
        basket_img = pygame.transform.scale(basket_img, (int(current_basket_size), int(current_basket_size)))

    screen.blit(basket_img, (basket_x, SCREEN_HEIGHT - current_basket_size))
    screen.blit(cornish_img, (falling_item_x, falling_item_y))

    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    high_score_text = font.render(f'High Score: {high_score}', True, BLACK)
    screen.blit(high_score_text, (SCREEN_WIDTH - 200, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
