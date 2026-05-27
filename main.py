Web VPython 3.2

import random
from vpython import *
#scene.camera.pos = vector(0, 0, 3)
#scene.userzoom = False
#scene.userspin = False
#scene.userpan = False


point1=ring(pos=vec(-2, 0, 0), axis=vec(1, 0, -7), radius = 0.4, thickness = 0.05, color=color.yellow)
red_ball=sphere(pos=vec(2,0,0),size=vec(0.5,0.5,0.5),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1b5CHDSqIj4zdUBToIQBdWy6h7z846xWeDZJfIHk1ug&s')
blue_ball=sphere(pos=vec(2,0,0),size=vec(0.5,0.5,0.5),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUg-dVgKP0FqnnHk5nZb6c4JlwiUuytsgrOUGdyiBb2g&s')
red_ball_2=sphere(pos=vec(6,0,0),size=vec(0.5,0.5,0.5),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1b5CHDSqIj4zdUBToIQBdWy6h7z846xWeDZJfIHk1ug&s')
blue_ball_2=sphere(pos=vec(7,0,0),size=vec(0.5,0.5,0.5),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUg-dVgKP0FqnnHk5nZb6c4JlwiUuytsgrOUGdyiBb2g&s')
red_ball_3=sphere(pos=vec(8,0,0),size=vec(0.5,0.5,0.5),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1b5CHDSqIj4zdUBToIQBdWy6h7z846xWeDZJfIHk1ug&s')
blue_ball_3=sphere(pos=vec(9,0,0),size=vec(0.5,0.5,0.5),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUg-dVgKP0FqnnHk5nZb6c4JlwiUuytsgrOUGdyiBb2g&s')
red_ball_4=sphere(pos=vec(10,0,0),size=vec(0.5,0.5,0.5),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1b5CHDSqIj4zdUBToIQBdWy6h7z846xWeDZJfIHk1ug&s')
blue_ball_4=sphere(pos=vec(11,0,0),size=vec(0.5,0.5,0.5),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUg-dVgKP0FqnnHk5nZb6c4JlwiUuytsgrOUGdyiBb2g&s')

#다 같은 위치에서 있어야함

ball_list = [red_ball,blue_ball,red_ball_2,blue_ball_2,red_ball_3,blue_ball_3,red_ball_4,blue_ball_4]




blue_ball.velocity=vec(-1,0,0)
blue_ball_2.velocity=vec(-1,0,0)
blue_ball_3.velocity=vec(-1,0,0)
blue_ball_4.velocity=vec(-1,0,0)

red_ball.velocity=vec(-1,0,0)
red_ball_2.velocity=vec(-1,0,0)
red_ball_3.velocity=vec(-1,0,0)
red_ball_4.velocity=vec(-1,0,0)
line2=box(pos=vec(0,-1,0),size=vec(6,0.05,0.1))
line1=box(pos=vec(0,1,0),size=vec(6,0.05,0.1))

background=box(pos=vec(0,0,-1),size=vec(8,5,1),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZ-vUt2g_4N_8j-pQZhzTXQxarxBJEQnWvsQ&s')

k=keysdown()
if k=' 'and blue_ball.pos=vec(-2,0,0):
    dt_b = 0.01
    while True:
        rate(100)
        blue_ball.pos = blue_ball.pos + blue_ball.velocity * dt_b
    
    dt_b2 = 0.01
    while True:
        rate(100)
        blue_ball_2.pos = blue_ball_2.pos + blue_ball_2.velocity * dt    
    
    
    
    
#if k=' ' and blue_ball.pos=vec(-2,0,0):
#스페이스 누르고 위치 맞으면 공 삭제,그와 동시에 화면 밖에 공을 생성하고 속도를 0으로 설정한다.
#개념 구조화해서 가져오자...
