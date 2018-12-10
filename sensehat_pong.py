from sense_hat import SenseHat
import time
sense = SenseHat()
print("Starting Pong...")
white = (255, 255, 255)
turquoise = (0, 255, 200)
bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]
#_____Functions_____
def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1], turquoise)
    ball_position[0] += ball_velocity[0]
def draw_bat():
    sense.clear()
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y - 1, white)
    sense.set_pixel(0, bat_y + 1, white)
    time.sleep(0.25)
def move_up(event):
    global bat_y
    if event.action == 'pressed':
        bat_y -= 1
def move_down(event):
    global bat_y
    if event.action == 'pressed':
        bat_y += 1
#______Main program________
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
while True:
    draw_ball()
    draw_bat()


