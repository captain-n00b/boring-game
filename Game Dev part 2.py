from pygame import mixer
import pygame
# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("MEGALOVANIA.mp3")

# Setting the volume
mixer.music.set_volume(2.0)

# Start playing the song
mixer.music.play()


pygame.init()
win = pygame.display.set_mode((1024, 600))
pygame.display.set_caption("Hello")

#images related to characters and background
'''walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
'''
bg = pygame.image.load('field5.jpg')
char = pygame.image.load('standing.png')
#facing = 1
left = False
right = False
#walkCount = 0

clock = pygame.time.Clock()
#Character attribute
class player(object):
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.height = width
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.facing = 1
        self.hitbox = (self.x + 20, self.y + 5, 28, 60)
    def draw(self, win):
        self.hitbox = (self.x + 20, self.y + 5, 28, 60)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox,2)
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))

    def hit(self):
        print("HIT!!!! Player2")


class player2(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]

    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.end = end
        #self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.standing = True
        self.facing = 1
        self.hitbox = (self.x + 17, self.y + 5, 40, 60)

    def draw(self, win):
        self.hitbox = (self.x + 17, self.y + 5, 40, 60)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))
    def hit(self):
        print("HIT!!!!! Player 1")





def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    man.draw(win)
    man2.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 50 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


#Main loop
man = player(0, 500, 64, 64)
man2 = player2(256, 500, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < man.hitbox[1] + man.hitbox[3] and bullet.y + bullet.radius > man.hitbox[1]:
            if bullet.x + bullet.radius > man.hitbox[0] and bullet.x - bullet.radius < man.hitbox[0] + man.hitbox[2]:
                man.hit()
                bullets.pop(bullets.index(bullet))
        if bullet.y - bullet.radius < man2.hitbox[1] + man2.hitbox[3] and bullet.y + bullet.radius > man2.hitbox[1]:
            if bullet.x + bullet.radius > man2.hitbox[0] and bullet.x - bullet.radius < man2.hitbox[0] + man2.hitbox[2]:
                man2.hit()
                bullets.pop(bullets.index(bullet))
        if bullet.x < 1024 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()
    #player1
    if keys[pygame.K_e]:
        if man.left:
            man.facing = -1
        if man.right:
            man.facing = 1
        if len(bullets) < 10:
            bullets.append(projectile(round(man.hitbox[0] + 5 + man.width// 2), round(man.hitbox[1] + 5 + man.height// 2), 6, (255, 255, 255), man.facing))

    if keys[pygame.K_a] and man. x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_d] and man.x < 1024 - man.width:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not man.isJump:
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
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

    #player2
    if keys[pygame.K_END]:
        if man2.left:
            man2.facing = -1
        if man2.right:
            man2.facing = 1
        if len(bullets) < 10:
            bullets.append(projectile(round(man2.hitbox[0] + 50 + man2.width // 2), round(man2.hitbox[1] + man2.height// 2), 6, (255, 255, 255), man2.facing))

    if keys[pygame.K_LEFT] and man2. x > 0:
        man2.x -= man2.vel
        man2.left = True
        man2.right = False
        man2.standing = False

    elif keys[pygame.K_RIGHT] and man2.x < 1024 - man2.width:
        man2.x += man2.vel
        man2.left = False
        man2.right = True
        man2.standing = False
    else:
        man2.standing = True
        man2.walkCount = 0
    if not man2.isJump:
        if keys[pygame.K_UP]:
            man2.isJump = True
            man2.right = False
            man2.left = False
            man2.walkCount = 0
    else:
        if man2.jumpCount >= -10:
            neg = 1
            if man2.jumpCount < 0:
                neg = -1
            man2.y -= (man2.jumpCount ** 2) * 0.5 * neg
            man2.jumpCount -= 1
        else:
            man2.isJump = False
            man2.jumpCount = 10


    redrawGameWindow()
pygame.quit()
