import pygame
pygame.init()
win = pygame.display.set_mode((500, 470))
pygame.display.set_caption("Hello")

#images related to characters and background
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

left = False
right = False
walkCount = 0

clock = pygame.time.Clock()
#Character attribute
class player(object):
    def __init__(self,x,y,width,heigh):
        self.x = x
        self.y = y
        self.width = width
        self.height = width
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))


man = player(0, 390, 64, 64)

run = True


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    man.draw(win)
    pygame.display.update()

#Main loop


while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and man. x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_d] and man.x < 500 - man.width:
        man.x += man.vel
        man.left = False
        man.right = True
    else:
        man.right = False
        man.left = False
        walkCount = 0
    if not man.isJump:
        '''if keys[pygame.K_w] and y > 0:
            y -= vel
        if keys[pygame.K_s] and y < 1000 - height:
            y += vel'''
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()
pygame.quit()
