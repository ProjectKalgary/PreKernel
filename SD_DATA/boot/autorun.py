import bteve as eve
import time
import digitalio
import adafruit_hid
import os
import kernel.console as console

cancmd = True
devinfo = []

def PRG_INIT(gd, dev):
    global devinfo
    devinfo = dev
    console.setgd(gd)
    os.chdir("/sd")
    console.writeline(devinfo[0] + " " + devinfo[1])
    console.writeline("Use 'help' for a list of commands.")
    while True:
        global cancmd
        if cancmd:
            cancmd = False
            docmd(cmd())


def cmd():
    console.writeline(os.getcwd() + ">")
    cmd = input(os.getcwd() + ">")
    console.write(cmd)
    args = cmd.split(" ")
    return args

def docmd(args):
    global devinfo, cancmd
    CMD = args[0].lower()
    if CMD == "help" and len(args) == 1:
        console.writeline(devinfo[0] + " " + devinfo[1] + " Help Menu:")
        console.writeline("help ......................... brings you here....duh")
        console.writeline("uname ...................... lists system information")
        console.writeline("cls ................................... clears screen")
        console.writeline("dir ............. lists contents of current directory")
        console.writeline("cd [dir] ................. changes directory to [dir]")
        console.writeline("say [message] ............ types [message] to console")
        console.writeline("py [python code] ............. executes [python code]")
    elif CMD == "uname" and len(args) == 1:
        console.writeline(devinfo[0] + " " + devinfo[1])
    elif CMD == "cls" and len(args) == 1:
        console.clear()
    elif CMD == "dir" and len(args) == 1:
        console.writeline(', '.join([str(a) for a in os.listdir()]))
    elif CMD == "cd" and len(args) == 2:
        os.chdir(args[1])
    elif CMD == "say" and len(args) > 1:
        say = args
        del say[0]
        console.writeline(' '.join([str(a) for a in say]))
    elif CMD == "py" and len(args) > 1:
        py = args
        del py[0]
        try:
            exec(' '.join([str(a) for a in py]))
        except Exception as e:
            console.writeline("PYERROR: " + str(e))
    elif CMD == "":
        console.writeline("")
    else:
        console.writeline("INVALID")
    cancmd = True
