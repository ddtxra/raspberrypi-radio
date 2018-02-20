import subprocess
import sys

def lcd_message(l1, l2):
    subprocess.call('sudo python /home/pi/bin/lcd.py \"' + str(l1) + '\" \"' + str(l2) + '\"', shell=True)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        lcd_message(sys.argv[1], sys.argv[2])
    else:
        lcd_message("Hello", "World")
