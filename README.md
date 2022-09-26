# enviroplusd

This is a daemon designed to poll Pimironi's Enviroplus (aka Enviro+) for environmental data, and to power the LCD located on the Enviroplus.

## Installation

1. Enable I2C: `raspi-config nonint do_i2c 0`

2. Enable SPI: `raspi-config nonint do_spi 0`
