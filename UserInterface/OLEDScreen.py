from .IUInterface import IUInterface

import time

import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

class ScreenConfig:
    width = 128
    height = 32
    do_not_show = ["timestamp"]
    sleep = 2

class OLEDScreen(IUInterface):
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.oled = adafruit_ssd1306.SSD1306_I2C(ScreenConfig.width,
                                                 ScreenConfig.height,
                                                 self.i2c)
        
        super(OLEDScreen, self).__init__()
        
    def provide(self, data_dict):
        for key, item in data_dict.items():
            if key in ScreenConfig.do_not_show:
                continue
            image = Image.new("1", (self.oled.width, self.oled.height))
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()
            text = "{}: {}".format(key, item)
            left, top, right, bottom = font.getbbox(text)
            font_width = right - left
            font_height = bottom - top
            draw.text(
                (self.oled.width // 2 - font_width // 2,
                 self.oled.height // 2 - font_height // 2),
                text,
                font=font,
                fill=255)
            self.oled.image(image)
            self.oled.show()
            
            time.sleep(ScreenConfig.sleep)
            self.__clear()

    def start(self):
        self.__clear()

    def stop(self):
        self.__clear()

    def __clear(self):
        self.oled.fill(0)
        self.oled.show()
