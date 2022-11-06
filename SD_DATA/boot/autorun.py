import bteve as eve
import time
import digitalio
import adafruit_hid
import kernel.console as console

def PRG_INIT(gd):
    gd.init()
    console.setgd(gd)
    console.writeline("Hello, World!")
    console.writeline("This is the kernel's built in console!")
    time.sleep(2)
    console.writeline("Changing background in 3...")
    time.sleep(1)
    console.write(" 2...")
    time.sleep(1)
    console.write(" 1...")
    time.sleep(1)
    console.setrgb(0xFF, 0x00, 0x00)
    console.writeline("TA-DA!")
