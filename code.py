#!/usr/bin/python3
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd
from hcsr04 import HCSR04
from time import sleep

# Using Robo HAT MM1 Servo Pins
lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d7 = digitalio.DigitalInOut(board.D12)
lcd_d6 = digitalio.DigitalInOut(board.D11)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d4 = digitalio.DigitalInOut(board.D9)
lcd_backlight = digitalio.DigitalInOut(board.D13)

lcd_columns = 16
lcd_rows = 2

# Using Robo HAT MM1 RCC Pins
trig = digitalio.DigitalInOut(board.D7)
echo = digitalio.DigitalInOut(board.D7)


# devices - distance sensor
sonar = HCSR04(trig, echo)
lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


# count push ups over a particular time.  Reset on restart.
push_count = 0

with HCSR04(trig, echo) as sonar:
    try:
        while True:
            print(sonar.dist_cm())
            sleep(2)
    except KeyboardInterrupt:
        pass

