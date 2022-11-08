import kernel.console as console

def PRG_INIT(gdl, devi, args):
    if(len(args) != 1):
        console.writeline("ERROR: Invalid number of arguments")
        return
    console.writeline(devi[0] + " " + devi[1])
