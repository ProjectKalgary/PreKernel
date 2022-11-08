import os
import kernel.console as console

cancmd = True

def PRG_INIT(gdl, devi, args):
    global cancmd
    cancmd = True
    if len(args) != 1:
        console.write("ERROR: Invalid number of arguments.")
        return
    console.setgd(gdl)
    os.chdir("/sd")
    console.writeline(devi[0] + " " + devi[1])
    console.writeline("Use 'help' for a list of commands.")
    while True:
        if cancmd:
            cancmd = False
            e = docmd(cmd(), gdl, devi)
            if e == -1:
                return


def cmd():
    console.writeline(os.getcwd() + ">")
    cmd = input(os.getcwd() + ">")
    console.write(cmd)
    args = cmd.split(" ")
    return args


def docmd(a, gd, dev):
    global cancmd
    CMD = a[0].lower()
    if CMD == "exit":
        if len(a) != 1:
            console.writeline("ERROR: Invalid number of arguments.")
        else:
            return -1
    elif CMD == "":
        console.writeline("")
    elif CMD + ".py" in os.listdir("/sd/prg") or CMD + ".mpy" in os.listdir("/sd/prg"):
        file = "prg." + CMD
        try:
            load = my_import(file)
            load.PRG_INIT(gd, dev, a)
        except Exception as e:
            console.writeline("PROGRAMERROR: " + str(e) + ".")
    else:
        console.writeline("ERROR: " + CMD + " doesn't exist.")
    cancmd = True

def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod
