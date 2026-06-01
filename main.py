Web VPython 3.2

from vpython import *

# ======================
# 화면 설정
# ======================

scene.width = 1000
scene.height = 500
scene.background = color.black

# ======================
# 배경
# ======================

background = box(
    pos=vec(0,0,-1),
    size=vec(12,6,0.1),
    texture='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZ-vUt2g_4N_8j-pQZhzTXQxarxBJEQnWvsQ&s'
)

# ======================
# 판정선
# ======================

judge = ring(
    pos=vec(-2,0,0),
    axis=vec(0,0,1),
    radius=0.4,
    thickness=0.05,
    color=color.yellow
)

# 레인

line1 = box(
    pos=vec(0,1,0),
    size=vec(10,0.05,0.1),
    color=color.white
)

line2 = box(
    pos=vec(0,-1,0),
    size=vec(10,0.05,0.1),
    color=color.white
)

# ======================
# 게임 설정
# ======================

start_x = 6
judge_x = -2

speed = 2.5
beat = 0.5

balls = []

# ======================
# 노트 생성
# ======================

notes = []

for i in range(200):

    t = i * beat

    if i % 2 == 0:
        notes.append((t, "red"))
    else:
        notes.append((t, "blue"))

# ======================
# 안내 문구
# ======================

info = label(
    pos=vec(0,2,0),
    text="A = 빨간 공   |   L = 파란 공",
    box=False,
    height=20
)

# ======================
# 게임 루프
# ======================

time = 0
dt = 0.01

note_index = 0

last_a = False
last_l = False

while True:

    rate(100)

    time += dt

    keys = keysdown()

    # ------------------
    # 노트 생성
    # ------------------

    while note_index < len(notes) and time >= notes[note_index][0]:

        note_time, note_color = notes[note_index]

        if note_color == "red":

            b = sphere(
                pos=vec(start_x,0,0),
                size=vec(0.5,0.5,0.5),
                texture='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1b5CHDSqIj4zdUBToIQBdWy6h7z846xWeDZJfIHk1ug&s'
            )

            b.note_color = "red"

        else:

            b = sphere(
                pos=vec(start_x,0,0),
                size=vec(0.5,0.5,0.5),
                texture='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUg-dVgKP0FqnnHk5nZb6c4JlwiUuytsgrOUGdyiBb2g&s'
            )

            b.note_color = "blue"

        b.velocity = vec(-speed,0,0)

        balls.append(b)

        note_index += 1

    # ------------------
    # 공 이동
    # ------------------

    for b in balls[:]:

        b.pos += b.velocity * dt

        # 화면 밖으로 나가면 제거

        if b.pos.x < -5:

            b.visible = False

            if b in balls:
                balls.remove(b)

    # ------------------
    # A키
    # ------------------

    if 'a' in keys and not last_a:

        target = None

        for b in balls:

            if b.note_color == "red":

                if abs(b.pos.x - judge_x) < 0.6:

                    target = b

                    break

        if target:

            target.visible = False

            balls.remove(target)

    # ------------------
    # L키
    # ------------------

    if 'l' in keys and not last_l:

        target = None

        for b in balls:

            if b.note_color == "blue":

                if abs(b.pos.x - judge_x) < 0.6:

                    target = b

                    break

        if target:

            target.visible = False

            balls.remove(target)

    last_a = 'a' in keys
    last_l = 'l' in keys
