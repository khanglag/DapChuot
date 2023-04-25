import pygame
import random

# Thiết lập màn hình
pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game đập chuột")

# Thiết lập các đối tượng
mouse1 = pygame.image.load(r'C:\Users\nhond\Cuong\Python\Test\img\mouse1.jpg')
mouse2 = pygame.image.load(r'C:\Users\nhond\Cuong\Python\Test\img\mouse2.jpg')
mouse3 = pygame.image.load(r'C:\Users\nhond\Cuong\Python\Test\img\mouse3.jpg')
mice = [mouse1, mouse2, mouse3]
score = 0
font = pygame.font.Font(None, 36)

# Thiết lập vị trí các con chuột
pos_possible = [(275,230) ,(430,230),(585,230),(275,360),(430,360),(585,360),(275,490),(430,490),(585,490)]
mouse_positions = random.sample(pos_possible, 3)

# Vòng lặp chính của game
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    # Xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Kiểm tra xem người chơi có đập chuột không
            for i in range(3):
                if mice[i].get_rect().move(mouse_positions[i]).collidepoint(event.pos):
                    score += 1
                    mouse_positions[i] = random.choice(pos_possible)

    # Cập nhật màn hình
    screen.fill((255, 255, 255))
    for i in range(3):
        screen.blit(mice[i], mouse_positions[i])
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

# Đóng cửa sổ Pygame
pygame.quit()
