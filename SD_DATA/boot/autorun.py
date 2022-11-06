import bteve as eve
import time

def PRG_INIT(gd):
    gd.init()
    while True:
        gd.ClearColorRGB(0x00, 0x00, 0xFF)
        gd.Clear()
        gd.cmd_text(gd.w//2, (gd.h//2), 31, eve.OPT_CENTER, "Booted from MicroSD!")
        gd.swap()
        time.sleep(1)
        gd.ClearColorRGB(0x00, 0x00, 0xFF)
        gd.Clear()
        gd.swap()
        time.sleep(1)
