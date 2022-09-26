import bme280
import ST7735
from PIL import Image, ImageDraw, ImageFont


class envplusd:
    def __init__(self) -> None:
        pass

    def __initTemperatureSensor__(self) -> None:

        self.TEMPERATURE_SENSOR = bme280.BME280()

    def __initDisplay__(self) -> None:

        self.DISPLAY = ST7735.ST7735(
            port=0, cs=1, dc=9, backlight=12, rotation=270, spi_speed_hz=10000000
        )
        self.DISPLAY.begin()
        self.DISPLAY_HEIGHT = self.DISPLAY.HEIGHT
        self.DISPLAY_WIDTH = self.DISPLAY.WIDTH

        initImg = Image.new(
            mode="RGB",
            size=(self.DISPLAY_HEIGHT, self.DISPLAY_WIDTH),
            color=(33, 33, 33),
        )
        plac1 = Image
        plac2 = ImageDraw
        plac3 = ImageFont
