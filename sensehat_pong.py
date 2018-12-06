from sense_hat import SenseHat
import time
sense = SenseHat()
print("Starting Pong...")
white = (255, 255, 255)
bat_y = 4
#_____Functions_____
#write more for draw_bat later
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
#______Main program________
sense.stick.direction_up = move_up
while True:
    draw_bat()