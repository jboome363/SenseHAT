from sense_hat import SenseHat
import time
sense = SenseHat()
print("Starting Pong...")
white = (255, 255, 255)
bat_y = 4
#write more for draw_bat later
def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y - 1, white)
    sense.set_pixel(0, bat_y + 1, white)
#______Main program_______
draw_bat()
time.sleep(1)
sense.clear()