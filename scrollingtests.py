import RPi.GPIO as GPIO
#importingRPi.GPIO library

from RPLCD.gpio import CharLCD
#importing CharLCDfrom  RPLCD.gpio

import time
#importing the time library

GPIO.setwarnings(False)
#setting warnings to false

framebuffer = ['Hello!','',]
#a data structure "frame buffer" has defined with two elements

def write_to_lcd(lcd, framebuffer, num_cols):
#defined a function of "write_to_lcd" with three parameters
lcd.home()
    #used to place the cursor of lcd at (0,0) position of LCD
    for row in framebuffer:
    #initiated a for loop
lcd.write_string(row.ljust(num_cols)[:num_cols])
        #displayed the values of "frame buffer"
lcd.write_string('\r\n')
        #placed the pointer in new line and new row

lcd = CharLCD(pin_rs=15,pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
numbering_mode=GPIO.BOARD,
              cols=16, rows=2, dotsize=8,
auto_linebreaks=True, compat_mode=True)
#defined the lcd pins with GPIO pins of Raspberry Pi

write_to_lcd(lcd, framebuffer, 16)
#calling the function and passed the parameters especially num_cols

long_string = 'Welcome to the LinuxHint'
#store a string in variable "long_string"

def loop_string(string, lcd, framebuffer, row, num_cols, delay=0.5):
#defined another function loop_string

    padding = ' ' * num_cols
    #spaces with num_cols and storing in "padding"
    s = padding + string + padding
    #declaring a new variable and store values in it

    for i in range(len(s) - num_cols + 1):
    #declared a new infinite for loop

        framebuffer[row] = s[i:i+num_cols]
        #store values in framebuffer array data structure
write_to_lcd(lcd, framebuffer, num_cols)
        #displayed the output on LCD
time.sleep(0.5)
        #generated a delay of 0.5 seconds

while True:
#initialize the infinite while loop

loop_string(long_string, lcd, framebuffer, 1, 16)
    #call the function loop_string