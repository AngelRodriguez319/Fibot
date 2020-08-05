import math as m

def suma(a):
    op_sumas = ['suma', 'más', 'mas', 'sumame', 'sumar','sumado','sumados']
    if a  in op_sumas:
        return True
    return False

def resta(a):
    op_restas = ['resta','menos', 'diferencia', 'restar']
    if a  in op_restas:
        return True
    return False

def multiplicacion(a):
    op_mult = ['multiplicacion','producto', 'por', 'multiplicar', 'multiplicame']
    if a  in op_mult:
        return True
    return False

def division(a):
    op_div = [ 'division', 'cociente', 'entre', 'sobre', 'dividido', 'dividir', 'division']
    if a  in op_div:
        return True
    return False

def exponente(a):
    op_exp = ['potencia', 'elevado', 'a la']
    if a  in op_exp:
        return True
    return False

def raiz(a):
    op_raiz = ['raiz']
    if a  in op_raiz:
        return True
    return False

def seno(a):
    op_seno = ['seno']
    if a  in op_seno:
        return True
    return False

def coseno(a):
    return a == 'cos'

def tangente(a):
    return a == 'tangente'

def secante(a):
    return a == 'secante'

def cosecante(a):
    return a == 'cosecante'

def cotangente(a):
    return a == 'cotangente'

def secante(a):
    return a == 'secante'

def cosecante(a):
    return a == 'cosecante'

def cotangente(a):
    return a == 'cotangente'

def modelo(argumentos):
    res = 0
    if argumentos[0].isnumeric():
        if argumentos[1].isnumeric():
            if suma(argumentos[2]):
                return float(argumentos[0]) + float(argumentos[1])
            if resta(argumentos[2]):
                return float(argumentos[0]) - float(argumentos[1])
            if multplicacion(argumentos[2]):
                return float(argumentos[0]) * float(argumentos[1])
            if division(argumentos[2]):
                return float(argumentos[0]) / float(argumentos[1])
            if exponente(argumentos[2]):
                return float(argumentos[0]) ** float(argumentos[1])
        else:
            if suma(argumentos[1]):
                return float(argumentos[0]) + float(argumentos[2])
            if resta(argumentos[1]):
                return float(argumentos[0]) - float(argumentos[2])
            if multiplicacion(argumentos[1]):
                return float(argumentos[0]) * float(argumentos[2])
            if division(argumentos[1]):
                return float(argumentos[0]) / float(argumentos[2])
            if exponente(argumentos[1]):
                return float(argumentos[0]) ** float(argumentos[2])
    else:
        op = argumentos[0]
        if suma(op):
            return float(argumentos[1]) + float(argumentos[2])
        if resta(op):
            return float(argumentos[1]) - float(argumentos[2])
        if multiplicacion(op):
            return float(argumentos[1]) * float(argumentos[2])
        if division(op):
            return float(argumentos[1]) / float(argumentos[2])
        if exponente(op):
            return float(argumentos[1]) ** float(argumentos[2])
        if raiz(op):
            return m.sqrt(float(argumentos[1]))
        if seno(op):
            return m.sin(float(argumentos[1]) * (m.pi / 180))
        if coseno(op):
            return m.cos(float(argumentos[-1]) * (m.pi / 180))
        if tangente(op):
            return m.tan(float(argumentos[1]) * (m.pi / 180))
        if secante(op):
            return 1 / ( m.cos(float(argumentos[1]) * (m.pi / 180)))
        if cosecante(op):
            return 1 / ( m.sen(float(argumentos[1]) * (m.pi / 180)))
        if cotangente(op):
            return 1 / ( m.tan(float(argumentos[1]) * (m.pi / 180)))

def final(argumentos):
    try:
        a = modelo(argumentos)
        return f"set_slot result '{a}'"  
    except ValueError as err:
        print(err)
        return f"set_slot result 'No te entendi'"
      
