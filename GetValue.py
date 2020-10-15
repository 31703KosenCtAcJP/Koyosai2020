import time
import sys
import spidev

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

CH0 = [0x06, 0x00, 0x00]

#spidevインスタンス生成
spi = spidev.SpiDev()

# Setting
spi.max_speed_hz = 200000
spi.mode = 0b00

spi.open(0,0)

try:
    while True:
        tmp = spi.xfer2(CH0)
        data = ((tmp[1] & 0x0f) <<8 | tmp[2])
        print(data)
        time.sleep(1)

except KeyboadInterrupt:
    spi.close()
    sys.exit(0)
