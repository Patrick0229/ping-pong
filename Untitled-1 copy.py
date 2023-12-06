import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

paddle_width, paddle_height = 10, 100
player_paddle = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_speed = 7

ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

bg_color = BLACK
paddle_color = WHITE
ball_color = WHITE

player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)
game_font = pygame.font.Font(None, 60)

title_font = pygame.font.Font(None, 100)
title_text = title_font.render("Ping Pong", True, WHITE)
text_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(bg_color)
    
    screen.blit(title_text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += paddle_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.left <= 0:
        opponent_score += 1
        if opponent_score == 10:
            running = False
        else:
            ball_speed_x *= -1
            ball.x = WIDTH // 2 - 15
            ball.y = HEIGHT // 2 - 15
    if ball.right >= WIDTH:
        player_score += 1
        if player_score == 10:
            running = False
        else:
            ball_speed_x *= -1
            ball.x = WIDTH // 2 - 15
            ball.y = HEIGHT // 2 - 15

    if opponent_paddle.top < ball.y:
        opponent_paddle.y += paddle_speed
    if opponent_paddle.bottom > ball.y:
        opponent_paddle.y -= paddle_speed

    pygame.draw.rect(screen, paddle_color, player_paddle)
    pygame.draw.rect(screen, paddle_color, opponent_paddle)
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    player_text = font.render(f"Player: {player_score}", True, WHITE)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
    screen.blit(player_text, (50, 20))
    screen.blit(opponent_text, (WIDTH - 200, 20))

    if running == False:
        if player_score == 10:
            text = game_font.render("You Won!", True, WHITE)
        else:
            text = game_font.render("Opponent Won!", True, WHITE)
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
