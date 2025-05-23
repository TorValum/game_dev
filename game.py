import pygame

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

screen = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load('0qCNxSjX.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Perfect game")
clock = pygame.time.Clock()



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
        self.speed = 4

    def move(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


player = Player(1, 2, 'unseen_horror_new.png')


black = (0, 0, 0)
# Cоздание карты
s1 = pygame.image.load('catacombs_0.png')
s2 = pygame.image.load('cobble_blood_1.png')




running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Обновление экрана
    # Cоздание картыv
    for i in range(len(gamemap)):
        for j in range(len(gamemap[0])):
            if gamemap[i][j] == "*":
                rect = screen.blit(s1, (j * k, i * k))
            else:
                rect1 = screen.blit(s2, (j * k, i * k))

   # screen.blit()  # Заполняем экран черным цветом
    player.draw(screen)  # Рисуем персонажа
    pygame.display.flip()  # Обновляем экран

pygame.quit()
