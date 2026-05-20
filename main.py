Web VPython 3.2

from vpython import *

scene.camera.pos = vector(0, 0, 3)
scene.userzoom = False
scene.userspin = False
scene.userpan = False

point1=ring(pos=vec(-2, 0, 0), axis=vec(1, 0, -7), radius = 0.4, thickness = 0.05, color=color.yellow)
blue_ball=sphere(pos=vec(2,0,0),size=vec(0.5,0.5,0.5),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUg-dVgKP0FqnnHk5nZb6c4JlwiUuytsgrOUGdyiBb2g&s')
red_ball=sphere(pos=vec(2,0,0),size=vec(0.5,0.5,0.5),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1b5CHDSqIj4zdUBToIQBdWy6h7z846xWeDZJfIHk1ug&s')
blue_ball.velocity=vec(-1,0,0)
line2=box(pos=vec(0,-1,0),size=vec(6,0.1,0))
line1=box(pos=vec(0,1,0),size=vec(6,0.1,0))
k=keysdown()
background=box(pos=vec(0,0,-1),size=vec(8,5,0),texture=' https://media.triple.guide/triple-cms/c_limit,f_auto,h_1024,w_1024/839938e7-9518-4d99-960e-1bcbf1b3b7ee.jpeg')
#bright_background = cv2.add(image, 50)
dt = 0.01
while True:
    rate(100)
    blue_ball.pos = blue_ball.pos + blue_ball.velocity * dt
    
#if k=' ' and blue_ball.pos=vec(-2,0,0):
#스페이스 누르고 위치 맞으면 공 삭제,그와 동시에 화면 밖에 공을 생성하고 속도를 0으로 설정한다.

