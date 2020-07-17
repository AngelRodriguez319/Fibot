import random

def get_welcome(*args):
    var = args[0]
    opts = args[1]
    msg = random.choice(['Bienvenido','Hola','Que tal!']+opts)
    return 'set_slot {0} "{1}"'.format(var,msg)