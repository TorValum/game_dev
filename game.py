import pygame

pygame.init()

WIDTH = 360  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
FPS = 60 # частота кадров в секунду

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perfect game")
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

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


player = Player(180, 240, 'unseen_horror_new.png')

black = (0, 0, 0)

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
    screen.fill(black)  # Заполняем экран черным цветом
    player.draw(screen)  # Рисуем персонажа
    pygame.display.flip()  # Обновляем экран

pygame.quit()
