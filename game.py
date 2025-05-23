import pygame
import os
import random
game_path = os.path.split(os.path.abspath(__file__))[0]
print(type(game_path))

pygame.init()
gamemap = [
    "***************",
    "*             *",
    "*             *",
    "*             *",
    "*             *",
    "*****      ****",
    "*   *         *",
    "*             *",
    "*             *",
    "***************"]

k = 32

WIDTH = len(gamemap[0])*k  # ширина игрового окна
HEIGHT = len(gamemap)*k # высота игрового окна
FPS = 60 # частота кадров в секунду

def ap(rp):
    """ принимает относительный путь, возвращает абсолютный
    >>> ap('0qCNxSjX.png')
    \'c:\\\\Users\\\\student\\\\Documents\\\\safronov\\\\game_dev-SafronooFF-patch-1\\\\0qCNxSjX.png\'
    """
    return os.path.join(game_path, rp)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

icon = pygame.image.load(ap('0qCNxSjX.png'))

pygame.display.set_icon(icon)
pygame.display.set_caption("Perfect game")
clock = pygame.time.Clock()

def igor(x, y):
    return x//k, y//k

def rauf(rect, dx, dy):
    dx, dy = int(dx),int(dy)
    result = True
    for i in [rect.topleft, rect.topright, rect.bottomleft, rect.bottomright]:
        if gamemap[(i[1] + dy)//k][(i[0] + dx)//k]=="*": result = False
    return result
           

##class GameObj():
  #  def __init__(self, img, x, y):
   #     self.python_image = pygame.image.load(img)
    #    self.point = self.python_image.get_rect(center=(x, y))

    #def draw(self, screen):
     #   screen.blit(self.python_image, self.point)



##class GameObj():
  #  def __init__(self, img, x, y):
   #     self.python_image = pygame.image.load(img)
    #    self.point = self.python_image.get_rect(center=(x, y))

    #def draw(self, screen):
     #   screen.blit(self.python_image, self.point)


class Player:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x*k, y*k))

        self.speed = 5



    def move(self, keys):
        if keys[pygame.K_a] and rauf(self.rect, -self.speed, 0):
            self.rect.x -= self.speed
        if keys[pygame.K_d] and rauf(self.rect, self.speed, 0):
            self.rect.x += self.speed
        if keys[pygame.K_w] and rauf(self.rect, 0 , -self.speed):
            self.rect.y -= self.speed
        if keys[pygame.K_s] and rauf(self.rect, 0 , self.speed):
            self.rect.y += self.speed
            
    def move_joystick(self, dx, dy):
        dx, dy = dx * self.speed, dy * self.speed
        if rauf(self.rect, dx, dy):
            self.rect.x += dx
        if rauf(self.rect, dx , dy):
            self.rect.y += dy
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class BotPlayer:
    def __init__(self, x, y, image_path):
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(original_image, (k, k))  # уменьшаем до 32x32
        self.rect = self.image.get_rect(topleft=(x * k, y * k))
        self.last_move_time = pygame.time.get_ticks()
        self.move_delay = 1000  # 1 секунда
        self.speed = k


    def random_move(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time >= self.move_delay:
            dx, dy = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
            dx *= self.speed
            dy *= self.speed
            if rauf(self.rect, dx, dy):
                self.rect.x += dx
                self.rect.y += dy
            self.last_move_time = current_time

    def draw(self, screen):
        screen.blit(self.image, self.rect)

player = Player(2, 2, ap('unseen_horror_new.png'))
bot = BotPlayer(3, 3, ap('ghost1.png'))

black = (0, 0, 0)
# Cоздание карты
s1 = pygame.image.load(ap('catacombs_0.png'))
s2 = pygame.image.load(ap('cobble_blood_1.png'))

pygame.joystick.init()
joysticks = {}


running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    pygame.event.pump()
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYDEVICEADDED:
            # This event will be generated when the program starts for every
            # joystick, filling up the list without needing to create them manually.
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks[joy.get_instance_id()] = joy
            print(f"Joystick {joy.get_instance_id()} connencted")

        if event.type == pygame.JOYDEVICEREMOVED:
            del joysticks[event.instance_id]
            print(f"Joystick {event.instance_id} disconnected")

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    player.move(keys)
    bot.random_move()

    for joystick in joysticks.values():
        player.move_joystick(joystick.get_axis(0),joystick.get_axis(1))
        for i in range(joystick.get_numaxes()):
            axis = joystick.get_axis(i)

##        for i in range(joystick.get_numbuttons()):
##            button = joystick.get_button(i)
##            print(screen, f"Button {i:>2} value: {button}")
##
##        hats = joystick.get_numhats()
##        print(f"Number of hats: {hats}")
##
##        # Hat position. All or nothing for direction, not a float like
##        # get_axis(). Position is a tuple of int values (x, y).
##        for i in range(hats):
##            hat = joystick.get_hat(i)
##            print(f"Hat {i} value: {str(hat)}")

    # Обновление экрана

    # Cоздание карты

    for i in range(len(gamemap)):
        for j in range(len(gamemap[0])):
            if gamemap[i][j] == "*":
                rect = screen.blit(s1, (j * k, i * k))
            else:
                rect1 = screen.blit(s2, (j * k, i * k))

   # screen.blit()  # Заполняем экран черным цветом

    player.draw(screen) # Рисуем персонажаpygame.event.pump()
    bot.draw(screen)

    pygame.display.flip()  # Обновляем экран
    

pygame.quit()
