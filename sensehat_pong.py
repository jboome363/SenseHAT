from sense_hat import SenseHat
import time
import random
sense = SenseHat()
sense.clear() 
bat_y = 4
speed = 0.25
speed2 = 0.25
score = 0
ball_position = [random.randint(1,5), 2]
ball2_position = [1, 2]
print(ball_position)
print(ball2_position)
ball_velocity = [1, 1]
ball2_velocity = [1, 1]
def setup_game():
    global bat_y
    global speed
    global score
    global ball_position
    global ball_velocity
    bat_y = 4
    speed = 0.25
    score = 0
    ball_position = [random.randint(1,5), random.randint(1,5)]
    ball_velocity = [1, random.choice([-1, 1])]
    print("Starting Pong...")
setup_game()
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
#speed closer to 0 is faster
#_____Functions_____
def reset_game():
    print("Resetting...")
    time.sleep(1)
    setup_game()
def draw_ball():
    global score
    global speed
    sense.set_pixel(ball_position[0], ball_position[1], blue)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 7 or ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity [0]
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity [1]
    ball_position[1] += ball_velocity[1]
    if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y +1):
        ball_velocity[0] = -ball_velocity[0]
        score += 1
        speed -= 0.001
    if ball_position[0] == 0:
        print("SCORE = " + str(score))
        sense.show_message("You Lose")
        sense.show_message("SCORE = " + str(score))
        sense.clear()
        time.sleep(2)
        setup_game()
def draw_ball2():
    global score
    global speed
    sense.set_pixel(ball2_position[0], ball2_position[1], green)
    ball2_position[0] += ball2_velocity[0]
    if ball2_position[0] == 7 or ball2_position[0] == 0:
        ball2_velocity[0] = -ball2_velocity [0]
    if ball2_position[1] == 7 or ball2_position[1] == 0:
        ball2_velocity[1] = -ball2_velocity [1]
    ball2_position[1] += ball2_velocity[1]
    if ball2_position[0] == 1 and (bat_y - 1) <= ball2_position[1] <= (bat_y +1):
        ball2_velocity[0] = -ball2_velocity[0]
    if ball2_position[0] == 0:
        print("SCORE = " + str(score))
        sense.show_message("You Lose")
        sense.show_message("SCORE = " + str(score))
        sense.clear()
        time.sleep(2)
        setup_game()
def draw_bat():
    global speed
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y - 1, white)
    sense.set_pixel(0, bat_y + 1, white)
    time.sleep(speed)
def move_up(event):
    global bat_y
    if bat_y >= 2:
        if event.action == 'pressed':
            bat_y -= 1
def move_down(event):
    global bat_y
    if bat_y <= 5:
        if event.action == 'pressed':
            bat_y += 1
#______Main program________
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

if ball_position[0] == 0:
    ball_velocity[0] = -ball_velocity[0]
while True:
    draw_ball()
    if score >= 30:
        draw_ball2()
    draw_bat()
    sense.clear()
