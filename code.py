import os
import bteve as eve
import time

gd = eve.Gameduino()
gd.init()

sleeptime = .5
boottxt = "Loading.."
global displaylogo
displaylogo = False

def BootScreenUpdate():
    gd.ClearColorRGB(0x20, 0x40, 0x20)
    gd.Clear()
    gd.cmd_text(gd.w//2, (gd.h//4)*3, 31, eve.OPT_CENTER, "Project Kalgary Pre Kernel")
    gd.cmd_text(gd.w // 2, (gd.h // 4)*3+50, 31, eve.OPT_CENTER, "v0.1")
    gd.cmd_text(gd.w // 2, (gd.h // 4)*3+100, 22, eve.OPT_CENTER, boottxt)
    print(boottxt)

    if displaylogo:
        gd.cmd_loadimage(0,0)
        gd.load(open("/sd/boot/logo.png", "rb"))
        gd.Begin(eve.BITMAPS)
        gd.Vertex2f(gd.w//2-75,gd.h//2-75)

    gd.swap()

def BootError(errmsg, exitcode):
    gd.ClearColorRGB(0xFF, 0x00, 0x00)
    gd.Clear()
    gd.cmd_text(gd.w//2, (gd.h//4), 31, eve.OPT_CENTER, "There was a problem booting.")
    gd.cmd_text(gd.w // 2, (gd.h // 2), 25, eve.OPT_CENTER, errmsg)
    gd.cmd_text(gd.w//2, (gd.h//4)*3+100, 22, eve.OPT_CENTER, "Exit Code: " + exitcode)
    gd.swap()

def Boot():
    global boottxt

    boottxt = "Detecting SD Storage..."
    BootScreenUpdate()
    time.sleep(sleeptime)

    dirinfo = os.listdir("/")
    if 'sd' in dirinfo:
        boottxt = "Detecting SD Storage...Complete"
        BootScreenUpdate()
    else:
        BootError("SD Storage could not be detected.", "-1")
        return -1

    time.sleep(sleeptime)
    boottxt = "Detecting /boot directory"
    BootScreenUpdate()
    time.sleep(sleeptime)

    dirinfo = os.listdir("/sd")
    if 'boot' in dirinfo:
        boottxt = "Detecting /boot directory...Complete"
        BootScreenUpdate()
    else:
        BootError("/boot doesn't exist.", "-1")
        return -1

    time.sleep(sleeptime)
    boottxt = "Loading /boot/logo.png file..."
    BootScreenUpdate()
    time.sleep(sleeptime)

    dirinfo = os.listdir("/sd/boot")
    if 'logo.png' in dirinfo:
        boottxt = "Loading /boot/logo.png file...Complete"
        global displaylogo
        displaylogo = True
        logo = open("/sd/boot/logo.png", "rb")
        global logobytes
        logobytes = logo.read()
        logo.close()
        BootScreenUpdate()

    else:
        boottxt = "Loading /boot/logo.png file...Failed"
        BootScreenUpdate()

    time.sleep(sleeptime)
    boottxt = "Done"
    BootScreenUpdate()
    time.sleep(sleeptime)

Boot()

# Stop from looping
while True:
    time.sleep(1)
