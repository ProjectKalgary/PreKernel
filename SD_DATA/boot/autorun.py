import os
import kernel.console as console

def PRG_INIT(gd, dev):
    console.setgd(gd)
    console.writeline("Loading...")
    if not('prg' in os.listdir("/sd")):
        console.setrgb(0xFF, 0x00, 0x00)
        console.writeline("SYSTEMERROR: prg directory not found.")
    elif not('cmd.py' in os.listdir("/sd/prg")):
        console.setrgb(0xFF, 0x00, 0x00)
        console.writeline("SYSTEMERROR: cmd.py file not found.")
    else:
        import prg.cmd as cmd
        console.clear()
        cmd.PRG_INIT(gd, dev, ["cmd"])
