from pygame import mixer
import pygame

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("MEGALOVANIA.mp3")

# Setting the volume
mixer.music.set_volume(0.5)

# Start playing the song
pygame.mixer.music.play(-1)

# Bullet Sound
bulletSound = pygame.mixer.Sound('Bullet.wav')
# hitSound = pygame.mixer.Sound('Wall.wav')
pygame.init()
win = pygame.display.set_mode((1024, 600))
pygame.display.set_caption("BORING GAMEE")

# images related to characters and background
'''walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
'''
bg = pygame.image.load('field5.jpg')
char = pygame.image.load('standing.png')
# facing = 1
left = False
right = False
# walkCount = 0

clock = pygame.time.Clock()


# Character attribute
class player(object):
    # Uploading Player1 images
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
                 pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
                 pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
                pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
                pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

    def __init__(self, x, y, width, height):
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
        # self.hitbox = (self.x + 20, self.y + 5, 28,60)
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.score = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        # self.hitbox = (self.x + 20, self.y + 5, 28, 60)

        # pygame.draw.rect(win, (255, 0, 0), self.hitbox,2)
        if self.visible:
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
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def Bullet(self):
        for bullet in bullets:
            if bullet.y - bullet.radius < man2.hitbox[1] + man2.hitbox[3] and bullet.y + bullet.radius > man2.hitbox[1]:
                if bullet.x + bullet.radius > man2.hitbox[0] and bullet.x - bullet.radius < man2.hitbox[0] + \
                        man2.hitbox[2]:
                    man2.hit()
                    # self.score += 1
                    bullets.pop(bullets.index(bullet))
            if bullet.x < 1024 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

    def BulletCal(self):
        if self.left:
            self.facing = -1
        if self.right:
            self.facing = 1
        if len(bullets) < 10:
            bullets.append(
                projectile(round(self.hitbox[0] + self.width // 2), round(self.hitbox[1] + self.height // 2), 6,
                           (255, 255, 255), self.facing))

    def hit(self):
        man2.score += 1
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


class player2(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.end = end
        # self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.standing = True
        self.facing = 1
        # self.hitbox = (self.x + 17, self.y + 5, 40, 60)
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.score = 0
        self.health = 10
        self.visible = True

    def draw(self, win):
        # self.hitbox = (self.x + 17, self.y + 5, 40, 60)

        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        if self.visible:
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

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def Bullet(self):
        for bullet in bullets:
            if bullet.y - bullet.radius < man.hitbox[1] + man.hitbox[3] and bullet.y + bullet.radius > man.hitbox[1]:
                if bullet.x + bullet.radius > man.hitbox[0] and bullet.x - bullet.radius < man.hitbox[0] + man.hitbox[2]:
                    man.hit()
                    # self.score += 1
                    bullets.pop(bullets.index(bullet))
            if bullet.x < 1024 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

    def BulletCal(self):
        if self.left:
            self.facing = -1
        if self.right:
            self.facing = 1
        if len(bullets) < 10:
            bullets.append(
                projectile(round(self.hitbox[0] + 30 + self.width // 2), round(self.hitbox[1] + self.height // 2), 6,
                           (255, 255, 255), self.facing))

    def hit(self):
        man.score += 1
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    text = font.render('Player 1:' + str(man.score), 1, (0, 0, 0))
    win.blit(text, (10, 10))
    text2 = font.render(str(man2.score) + ":Player 2", 1, (0, 0, 0))
    win.blit(text2, (900, 10))
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


# Main loop
font = pygame.font.SysFont('aerial', 30, True)  # pygame.font.sysfont(font,size,bold,italic)
man = player(0, 500, 64, 64)
man2 = player2(256, 500, 64, 64)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    man.Bullet()
    man2.Bullet()
    keys = pygame.key.get_pressed()

    # player1
    if keys[pygame.K_e] and shootLoop == 0:
        bulletSound.play()
        man.BulletCal()
        shootLoop = 1

    if keys[pygame.K_a] and man.x > 0:
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

    # player2
    if keys[pygame.K_END] and shootLoop == 0:
        bulletSound.play()
        man2.BulletCal()
        shootLoop = 1

    if keys[pygame.K_LEFT] and man2.x > 0:
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

    if man.health <= 0 or man2.health <= 0:
        pygame.quit()
    redrawGameWindow()
pygame.quit()
