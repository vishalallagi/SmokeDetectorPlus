from sense_hat import SenseHat
import time

sense = SenseHat()

R = [255, 0, 0]
G = [0, 255, 0]
B = [0, 0, 255]
W = [255, 255, 255]
GR = [50, 50, 50]

pixel1 = [
    GR, GR, GR, GR, GR, GR, GR, GR,
    GR, GR, GR, GR, GR, GR, GR, GR,
    GR, GR, GR, GR, GR, GR, R, GR,
    GR, GR, GR, GR, R, R, R, R,
    GR, GR, GR, G, GR, GR, R, GR,
    GR, GR, GR, G, GR, GR, GR, GR,
    GR, GR, G, G, G, GR, GR, GR,
    GR, GR, GR, G, GR, GR, GR, GR,
    ]

pixel2 = [
    GR, GR, GR, GR, GR, GR, GR, GR,
    GR, GR, GR, GR, GR, GR, GR, GR,
    GR, GR, GR, GR, GR, GR, R, GR,
    GR, GR, GR, GR, R, R, R, R,
    GR, GR, GR, G, GR, GR, R, GR,
    GR, GR, GR, G, GR, GR, GR, GR,
    GR, GR, G, G, G, GR, GR, GR,
    GR, GR, GR, G, GR, GR, GR, GR,
    ]

sense.set_pixels(pixel1)
time.sleep(10)
sense.clear()
