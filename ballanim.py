import sys, pygame
pygame.init()

size = width, height = 1024, 800
speed = [2, -2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("Penguin.png")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_l]:
                speed[0] = -speed[0]
            if keys[pygame.K_r]:
                speed[1] = -speed[1]

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()