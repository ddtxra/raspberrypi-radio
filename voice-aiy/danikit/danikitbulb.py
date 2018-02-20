import sys
from danikitimg import get_image_color
from danikitlcd import lcd_message
from yeelight import Bulb

#Defines the light bulb
bulb = Bulb("192.168.178.164")

#see documentation https://yeelight.readthedocs.io/en/stable/
def light(color):
    #if(color == "blue"):
    #    bulb.set_rgb(0, 0, 255)
    if("of" in color or "down" in color):
        bulb.turn_off()
    elif(color == "on"):
        bulb.turn_on()
    else:
        lcd_message("searching ... ", color)
        array = get_image_color(color)
        lcd_message("found", str(array))
        bulb.set_rgb(array[0], array[1], array[2])
    lcd_message("Light", color)
#bulb.set_brightness(50)
#bulb.set_color_temp(4700)
#bulb.set_default()

if __name__ == "__main__":
    #bulb.set_brightness(100)
    #bulb.set_color_temp(4700)
    if len(sys.argv) >= 2:
        light(sys.argv[1])
    else:
        light("blue")
