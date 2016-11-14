import subprocess
import sys
import I2C_LCD_driver

proc = subprocess.Popen(['mpc'], stdout=subprocess.PIPE)

channel = ""
for line in iter(proc.stdout.readline,''):
    if channel == "":
        channel = line.rstrip()

mylcd = I2C_LCD_driver.lcd()

print channel
mylcd.lcd_display_string(channel, 1)

