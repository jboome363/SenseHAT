from sense_hat import SenseHat
import time
sense = SenseHat()
print("Starting Pong...")
white = (255, 255, 255)
blue = (0, 0, 255)
bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]
#_____Functions_____
def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1], blue)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 7 or ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity [0]
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity [1]
    ball_position[1] += ball_velocity[1]
    if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y +1):
        ball_velocity[0] = -ball_velocity[0]
def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y - 1, white)
    sense.set_pixel(0, bat_y + 1, white)
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
    draw_bat()
    time.sleep(0.25)
    sense.clear()


