import time
import pygame ,  random
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
countdown = 60
#Lấy vị trí của chuột khi di chuyển
def get_mouse_pos():
    global x , y
    x , y = pygame.mouse.get_pos()
    return x, y
pos_possible = [(275,230) ,(430,230),(585,230),(275,360),(430,360),(585,360),(275,490),(430,490),(585,490)]
def mouse_reset():
    mouse1 = pygame.image.load(r'D:\OneDrive - IT software\vscode\python\Test\img\mouse1.jpg')
    mouse2 = pygame.image.load(r'D:\OneDrive - IT software\vscode\python\Test\img\mouse2.jpg')
    mouse3 = pygame.image.load(r'D:\OneDrive - IT software\vscode\python\Test\img\mouse3.jpg')
    mouse1 = pygame.transform.scale(mouse1, (106,73))
    mouse2 = pygame.transform.scale(mouse2, (106,73))
    mouse3 = pygame.transform.scale(mouse3, (106,73))
    mice = [mouse1, mouse2, mouse3]
    #Cho các đối tượng xuất hiện ngẫu nhiên
    global mouse
    mouse = random.choice(mice)
    #Cho các đối tượng xuất hiện ngẫu nhiên tại các lỗ
    global obj_x , obj_y
    obj_x ,obj_y = random.choice(pos_possible)   
    time.sleep(0.8)
def hammer_up() : #lỗi
    player = pygame.image.load(r'D:\OneDrive - IT software\vscode\python\Test\img\hammer0.png')
    player = pygame.transform.scale(player, (106,73))

#Thiết lập vị trí khi di chuyển búa :
def on_mouse_move() :
    global player
    player = pygame.image.load(r'D:\OneDrive - IT software\vscode\python\Test\img\hammer0.png')
    player = pygame.transform.scale(player, (106,73))
    global player_x , player_y
    player_x = x - 10
    player_y = y - 30
    
#set up khi click chuột
def click_mouse() :
    global cplayer
    player = pygame.image.load(r'D:\OneDrive - IT software\vscode\python\Test\img\hammer1.png')
    cplayer = pygame.transform.scale(player, (106,73))
    time.sleep(0.2)
#set up thời gian chơi
def time_up():
    global countdown
    countdown -=1
    time.sleep(1.0)
    if countdown == 0 :
        pygame.quit()
        exit()
def draw() :
    #Thiết lập kich thước màn hình
    WIDTH= 1000
    HEIGHT= 750
    #Thiết lập tiêu đề và icon của game
    pygame.display.set_caption("Game đập chuột")
    icon = pygame.image.load(r'D:\OneDrive - IT software\vscode\python\Test\img\icon.jpg')
    pygame.display.set_icon(icon)
    #Thiết lập background bắt đầu
    # background_begin = pygame.image.load(r'C:\Users\nhond\Cuong\Python\Test\img\begin1.jpg')
    # background_begin = pygame.transform.scale(background_begin, (WIDTH,HEIGHT))
    #Thiết lập background 
    background = pygame.image.load(r'D:\OneDrive - IT software\vscode\python\Test\img\background.jpg')
    background = pygame.transform.scale(background, (WIDTH,HEIGHT))
    #Thiết lập các đối tượng 
    #Cửa sổ game
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    font = pygame.font.SysFont(None,30)
    font_time = pygame.font.SysFont("Ravie", 20)
    running = True
    
    while running :
        # clock.tick(60)
        x,y = get_mouse_pos()
        text = font.render(f"Mouse position: x={x}, y={y}", True, (255, 255, 255))
        screen.fill((0,0,0,))
        # screen.blit(background_begin,(0,0))
        screen.blit(background,(0,0))
        screen.blit(text,(10,10))
        # play_box =Rect(0,0,120,100)
        # pygame.surface.Surface(120,100)
        # #Thiết lập thời gian chơi game , tối đa 60 giây
        time_up()
        text_time = font_time.render(f"00:{countdown}",True,pygame.Color("brown"))
        screen.blit(text_time,(350,190))
        # Tạo ra ngẫu nhiên đối tượng xuất hiện
        num = random.randint(1,3) 
        for i in range(num) :
            mouse_reset() 
            screen.blit(mouse,(obj_x,obj_y))
        # mouse_reset()
        # screen.blit(mouse,(obj_x,obj_y))
        # Thiết lập đối tượng hammer lên màn hình theo tọa độ của chuột
        on_mouse_move()
        screen.blit(player,(player_x,player_y))
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN :
                click_mouse()
                screen.blit(player,(player_x,player_y))
            else :
                hammer_up()
                screen.blit(player,(player_x,player_y))
        for event in pygame.event.get() :
            if event.type == QUIT :
                running = False
            # Khi nháy chuột
            elif event.type == pygame.MOUSEBUTTONDOWN :
                click_mouse()
                screen.blit(cplayer,(player_x,player_y))
                # if event.type ==pygame.MOUSEBUTTONUP :
                #     hammer_up()
                #     screen.blit(player,(player_x,player_y))
        pygame.display.flip()
        # pygame.quit()
def main () :
    draw()
if __name__ =="__main__" :
    main()





