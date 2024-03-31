import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake setup
snake_block = 10
snake_speed = 3
snake_list = []
length_of_snake = 1

# Food setup
foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

# Score setup
score = 0
level = 1

# Font setup
font_style = pygame.font.SysFont("bahnschrift", 25)

# Clock
clock = pygame.time.Clock()

# Functions
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

def draw_score(score):
    value = font_style.render("Your Score: " + str(score), True, red)
    screen.blit(value, [0, 0])

def draw_level(level):
    value = font_style.render("Level: " + str(level), True, blue)
    screen.blit(value, [0, 20])

def gameLoop():  # main game loop
    global foodx, foody, score, level,snake_speed
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            draw_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        draw_score(score)
        draw_level(level)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 1
            if score % 3 == 0:  # Increase level every 3 points
                level += 1
                snake_speed += 5  # Increase snake speed

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

gameLoop()
