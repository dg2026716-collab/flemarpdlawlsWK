Web VPython 3.2

from vpython import *

# 화면
scene.camera.pos = vector(0, 0, 3)
scene.userzoom = False
scene.userspin = False
scene.userpan = False

scene.width = 1100
scene.height = 500
scene.background = color.black

# 배경
box(
    pos=vec(0,0,-1),
    size=vec(12,6,0.1),
    texture='https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2288630/4b4ea308e7fdbbfaa59ab3597e2a15f856961b5b/capsule_616x353_koreana.jpg?t=1777500241'
)

# 판정선
judge_x = -3.3

ring(
    pos=vec(-2.7,0,0),
    axis=vec(0,0,1),
    radius=0.2,
    thickness=0.05,
    color=color.yellow
)


# 선
box(pos=vec(0,1,0), size=vec(10,0.05,0.1))
box(pos=vec(0,-1,0), size=vec(10,0.05,0.1))

# 설정
speed = 3.5
beat = 0.1
start_x = 6

balls = []
#빈 리스트 생성

# 노트 목록
notes = []

for i in range(100):

    if i % 2 == 0:
        notes.append((i*beat, "red"))
    else:
        notes.append((i*beat, "blue"))

# 안내문
label(
    pos=vec(0,2,0),
    text="A = 빨강   L = 파랑",
    box=False
)

# 게임 변수
time = 0
dt = 0.01
note_index = 0

while True:


    rate(50)
    time += dt

    # 노트 생성
    if note_index < len(notes):

        note_time, note_color = notes[note_index]

        if time >= note_time:

            img = ""

            if note_color == "red":
                img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1b5CHDSqIj4zdUBToIQBdWy6h7z846xWeDZJfIHk1ug&s"
            else:
                img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUg-dVgKP0FqnnHk5nZb6c4JlwiUuytsgrOUGdyiBb2g&s"

            ball = sphere(
                pos=vec(start_x,0,0),
                radius=0.25,
                texture=img
            )

            ball.note_color = note_color
            balls.append(ball)

            note_index += 1

    # 공 이동
    for ball in balls[:]:

        ball.pos.x -= speed * dt

        if ball.pos.x < -5:

            ball.visible = False
            balls.remove(ball)

    keys = keysdown()

    # A키
    if 'a' in keys:

        for ball in balls[:]:

            if ball.note_color == "red":

                if abs(ball.pos.x - judge_x) < 0.6:

                    ball.visible = False
                    balls.remove(ball)
                    break

    # L키
    if 'l' in keys:

        for ball in balls[:]:

            if ball.note_color == "blue":

                if abs(ball.pos.x - judge_x) < 0.6:

                    ball.visible = False
                    balls.remove(ball)
                    break
                
                
                
    score=0 
    score2=0
    if 'a' in keys:

        for ball in balls[:]:

            if ball.note_color == "red":
                
                if abs(ball.pos.x - judge_x) < 0.6:
                    
                    score=score+1
                    
                    
    if 'l' in keys:

        for ball in balls[:]:

            if ball.note_color == "blue":

                if abs(ball.pos.x - judge_x) < 0.6:
                    
                    score2=score2+1

#text(text='score\n:', align='center', color=color.white,pos=vec())      
#        label2(
#    pos=vec(0,1,3),
#    text="점수",
#)


