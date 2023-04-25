import pgzrun, pygame , math , random

from pykka import Actor
WIDTH= 2560
HEIGHT= 1937

time_left=60
score=0
start_game=False
game_over=False

Pos_possible=[
    (140,30),
    (455,30),
    (775,30),
    (140,185),
    (455,185),
    (775,185),
    (140,345),
    (455,345),
    (775,345)

]

background=Actor("background")
enemy=Actor('mole_1')
enemy.pos=(455,185)
player=Actor('hammer0')
background_begin=Actor('begin2')
play_box=Rect(0,0,160,50)
play_box.move_ip(415,370)
background_finish=Actor('finish')
play_again=Actor('playagain1')

music.play('bgm')


def eneny_reset():   # set up ve con chuot tro choi
    global enemy
    enemy=Actor('mole_1')
    enemy.pos=Pos_possible[random.randint(0,8)]
clock.schedule_interval(eneny_reset,1.5)

def hang_up():  # set up ve cai bua
    player.image='hammer0'
def on_mouse_move(pos):  # set up ve di chuyen cai bua
    player.pos=(pos[0],pos[1])
    if play_box.collidepoint(pos):
        background_begin.image='begin4'
    else:
        background_begin.image='begin2'

    if play_again.collidepoint(pos):
        play_again.image='playagain2'
    else:
        play_again.image='playagain1'

def on_mouse_down(pos): # set up hanh dong khi click chuot
    global score , game_over , time_left , start_game
    player.image='hammer1'
    clock.schedule_unique(hang_up,0.1)
    if enemy.collidepoint(pos):
        enemy.image='mole_laugh2'
        score= score+10
        sounds.hammering.play()
        clock.schedule(eneny_reset,0.3)

    if play_box.collidepoint(pos):
        start_game=True
        time_left=60
        

    if play_again.collidepoint(pos):
        start_game=True
        game_over=False
        score=0
        time_left=60
        
        
    

def time_up():  # set up ve thoi gian tro choi
    global time_left , game_over
    if time_left:
        time_left=time_left-1
        if time_left==10:
            sounds.count_down.play()
    else:
        game_over=True
clock.schedule_interval(time_up,1.0)

def update():
    global select_x , select_y
    mouse_x , mouse_y= pygame.mouse.get_pos()
    select_x=math.floor(mouse_x)
    select_y=math.floor(mouse_y)
    if game_over:
        play_again.pos=(498,388)
    else:
        play_again.pos=(-100,388)
    
    if start_game:  
            
        play_box.move_ip(-100,-100)

def draw():
    if not start_game and not game_over:
        background_begin.draw()
        
    else:
        background.draw()
        enemy.draw()
        player.draw()        
        screen.draw.text('Time : '+ str(time_left),(850,30), fontsize=30)
        screen.draw.text('Score : '+ str(score),(850,400), fontsize=30, color='brown')
    if game_over:
        background_finish.draw()
        play_again.draw()
        screen.draw.text('Your score : '+ str(score),(336,207), fontsize=60)
    
pgzrun.go()