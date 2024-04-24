import pygame, random

def obs1():
    obstacle1.x -= obstacleSpeed
    if obstacle1.x < 0:
        obstacle1.x = SCREEN_WIDTH+10
        random_number = random.randint(0, SCREEN_HEIGHT)
        obstacle1.y = random_number

def obs2():
    obstacle2.x -= obstacleSpeed
    if obstacle2.x < 0:
        obstacle2.x = SCREEN_WIDTH+10
        random_number = random.randint(0, SCREEN_HEIGHT)
        obstacle2.y = random_number

def obs3():
    obstacle3.x -= obstacleSpeed
    if obstacle3.x < 0:
        obstacle3.x = SCREEN_WIDTH+10
        random_number = random.randint(0, SCREEN_HEIGHT)
        obstacle3.y = random_number

pygame.init()
clockobject = pygame.time.Clock()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player = pygame.Rect((50,SCREEN_HEIGHT/2,50,50))
playerSpeed = 1
obstacle1 = pygame.Rect((SCREEN_WIDTH+10,SCREEN_HEIGHT/2,50,50))
obstacle2 = pygame.Rect((SCREEN_WIDTH+10,SCREEN_HEIGHT/2,100,50))
obstacle3 = pygame.Rect((SCREEN_WIDTH+10,SCREEN_HEIGHT/2,50,100))
obstacleSpeed = 1
font = pygame.font.Font(None, 36)


run = True
while run == True:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,255,0),player)
    pygame.draw.rect(screen,(0,0,255),obstacle1)
    pygame.draw.rect(screen,(0,0,255),obstacle2)
    pygame.draw.rect(screen,(0,0,255),obstacle3)

    # Player controls
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and player.top > 0:
        player.move_ip(0,-playerSpeed)
    if key[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
        player.move_ip(0,playerSpeed)

    # Obstacle movement. Every game tick its moves by the obstacleSpeed
    obs1()
    obs2()
    obs3()

    # GAME OVER BOOIIIIIIIIIIIIIIIIIIIIIIIIIIIII
    if player.colliderect(obstacle1) or player.colliderect(obstacle2) or player.colliderect(obstacle3):
        font = pygame.font.Font(None, 36)
        playerSpeed = 0
        obstacleSpeed = 0
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    clockobject.tick(1000)
    pygame.display.update()
    

pygame.quit()