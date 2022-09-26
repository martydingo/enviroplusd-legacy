import bme280
import ST7735
from PIL import Image, ImageDraw, ImageFont


class envplusd:
    def __init__(self) -> None:
        pass

    def __initUserConfiguration__(self) -> None:
        from fonts.ttf import RobotoMedium

        importFont = RobotoMedium
        fontSize = "20"
        self.font = ImageFont.truetype(importFont, fontSize)

    def __initTemperatureSensor__(self) -> None:

        self.TEMPERATURE_SENSOR = bme280.BME280()

    def __initDisplay__(self) -> None:

        self.DISPLAY = ST7735.ST7735(
            port=0, cs=1, dc=9, backlight=12, rotation=270, spi_speed_hz=10000000
        )
        self.DISPLAY.begin()
        self.DISPLAY_HEIGHT = self.DISPLAY.HEIGHT
        self.DISPLAY_WIDTH = self.DISPLAY.WIDTH

        displayImage = Image.new(
            mode="RGB",
            size=(self.DISPLAY_HEIGHT, self.DISPLAY_WIDTH),
            color=(33, 33, 33),
        )
        self.displayDraw = ImageDraw.Draw(displayImage)

        initMsg = "initialising.."
        self.displayDraw.text(
            xy=(self.DISPLAY_HEIGHT / 2, self.DISPLAY_WIDTH / 2),
            message=initMsg,
            font=self.font,
            fill=(255, 255, 255),
        )
