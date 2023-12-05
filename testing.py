import pygame
pygame.init()
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Hello")

#Character attribute
x = 50
y = 50
width = 60
height = 60
vel = 20
isJump = False
jumpCount = 10
#Main loop
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > 0:
        x -= vel
    if keys[pygame.K_d] and x < 1000 - width:
        x += vel
    if not isJump:
        if keys[pygame.K_w] and y > 0:
            y -= vel
        if keys[pygame.K_s] and y < 1000 - height:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    win.fill((100, 100, 100))
pygame.quit()
