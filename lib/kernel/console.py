import bteve as eve
import time

updaterate = .0
gd = ""
r = 0x00
g = 0x00
b = 0xFF
autoupdate = True

mem = []

def setautoupdate(b):
    global autoupdate
    autoupdate = b

def setgd(g):
    global gd
    gd = g

def setrgb(nr, ng, nb):
    global r, g, b
    r = nr
    g = ng
    b = nb
    aupdate()

def aupdate():
    global autoupdate
    if autoupdate:
        update()

def update():
    global mem, updaterate
    gd.ClearColorRGB(r, g, b)
    gd.Clear()
    y = 15
    for i in mem:
        gd.cmd_text(35, y, 25, 0, i)
        y += 35
        time.sleep(updaterate)
    gd.swap()


def writeline(str):
    global mem
    mem.append(str)
    aupdate()

def write(str):
    global mem
    mem[len(mem)-1] += str
    aupdate()


