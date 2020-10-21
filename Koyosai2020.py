# mcp3208
# 1: "00000" & StartBit & SGL/DIFF & D2
# 2: D1 & D2 & "000000"
# 3: "00000000"
# CHx | D2 D1 D0
# ----+---------
# CH0 |  0  0  0
# CH1 |  0  0  1
# CH2 |  0  1  0
# CH3 |  0  1  1
# CH4 |  1  0  0
# CH5 |  1  0  1
# CH6 |  1  1  0
# CH7 |  1  1  1

class MCP3208:
    import time
    import spidev
    CH =   [[0x06, 0x00, 0x00],
            [0x06, 0x40, 0x00],
            [0x06, 0x80, 0x00],
            [0x06, 0xC0, 0x00],
            [0x07, 0x00, 0x00],
            [0x07, 0x40, 0x00],
            [0x07, 0x80, 0x00],
            [0x07, 0xC0, 0x00]]
    data = []
    spi = spidev.SpiDev()


    def __init__(self):
        #spidevインスタンス生成
        self.spi = spidev.SpiDev()

        # Setting
        self.spi.max_speed_hz = 1000000
        self.spi.mode = 0b00
        # 接続
        self.spi.open(0,0)

    def getValue(self):
        tmp = self.spi.xfer2(CH[0])
        self.data[0] = ((tmp[1] & 0x0f) << 8 | tmp[2])
        tmp = self.spi.xfer2(CH[1])
        self.data[1] = ((tmp[1] & 0x0f) << 8 | tmp[2])
        tmp = self.spi.xfer2(CH[2])
        self.data[2] = ((tmp[1] & 0x0f) << 8 | tmp[2])
        tmp = self.spi.xfer2(CH[3])
        self.data[3] = ((tmp[1] & 0x0f) << 8 | tmp[2])
        tmp = self.spi.xfer2(CH[4])
        self.data[4] = ((tmp[1] & 0x0f) << 8 | tmp[2])
        tmp = self.spi.xfer2(CH[5])
        self.data[5] = ((tmp[1] & 0x0f) << 8 | tmp[2])
        tmp = self.spi.xfer2(CH[6])
        self.data[6] = ((tmp[1] & 0x0f) << 8 | tmp[2])
        tmp = self.spi.xfer2(CH[7])
        self.data[7] = ((tmp[1] & 0x0f) << 8 | tmp[2])
        return data

    def __del__(self):
        self.spi.close()

class WS2815:
    from rpi_ws281x import ws, Color, Adafruit_NeoPixel
    LED_COUNT = 30        # Number of LED pixels.
    LED_0_PIN = 18        # GPIO pin connected to the pixels (must support PWM! GPIO 13 and 18 on RPi 3).
    LED_1_PIN = 13
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_0_DMA = 10        # DMA channel to use for generating signal (Between 1 and 14)
    LED_1_DMA = 11
    LED_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
    LED_0_CHANNEL = 0     # 0 or 1
    LED_1_CHANNEL = 1
    LED_STRIP = ws.WS2811_STRIP_GRB

    def __init__():
        strip0 = Adafruit_NeoPixel(self.LED_COUNT, self.LED_0_PIN, self.LED_FREQ_HZ,
                                   self.LED_0_DMA, self.LED_INVERT, self.LED_BRIGHTNESS,
                                   self.LED_0_CHANNEL, self.LED_STRIP)
        strip1 = Adafruit_NeoPixel(self.LED_COUNT, self.LED_1_PIN, self.LED_FREQ_HZ,
                                   self.LED_1_DMA, self.LED_INVERT, self.LED_BRIGHTNESS,
                                   self.LED_1_CHANNEL, self.LED_STRIP)
                                   


if __name__ = '__main__':
    mcp3208 = MCP3208()
    while 1:
        try:
            print = MCP3208.getValue()
            time.sleep(1)
        except KeyboardInterrupt:
            del mcp3208
            sys.exit(1)