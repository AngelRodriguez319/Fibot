import math as m

def operations_basic(*args):
    operation = args[0]
    num_1 = float(args[1])
    num_2 = float(args[2])

    if operation == "suma":
        return f"set_slot result '{num_1 + num_2}'"

    elif operation == "resta":
        return f"set_slot result '{num_1 - num_2}'"

    elif operation == "multiplicacion":
        return f"set_slot result '{num_1 * num_2}'"  

    elif operation == "division":
        return f"set_slot result '{num_1 / num_2}'"

    elif operation == "potenciacion":
        return f"set_slot result '{num_1 ** num_2}'"

    elif operation == "raiz":
         return f"set_slot result '{num_1 ** (1 / num_2)}'"

    

def operations_trigonometricas(*args):
    operation = args[0]
    angulo = float(args[1])
    angulo_rad = (m.pi * angulo) / 180

    if operation == "seno":
        return f"set_slot result {m.sin(angulo_rad)}"

    elif operation == "coseno":
        return f"set_slot result {m.cos(angulo_rad)}"

    elif operation == "tangente":
        if angulo == 45:
            return f"set_slot result {'Error'}" 
        return f"set_slot result {m.tan(angulo_rad)}"

    elif operation == "cotangente": 
        if angulo == 0:
            return f"set_slot result {'Error'}"
        return f"set_slot result {1 / (m.tan(angulo_rad))}"

    elif operation == "secante": 
        if angulo % 90 == 0 and angulo % 360 != 0:
            return f"set_slot result {'Error'}"
        return f"set_slot result {1 / (m.cos(angulo_rad))}"

    elif operation == "cosecante": 
        if angulo % 360 == 0 and angulo % 90 !=0:
            return f"set_slot result {'Error'}"
        return f"set_slot result {1 / (m.sin(angulo_rad))}"

    elif operation == "arcoseno":
        return f"set_slot result {(180 * m.asin(angulo)) / m.pi}"

    elif operation == "arcocoseno":
        return f"set_slot result {(180 * m.acos(angulo)) / m.pi}"

    elif operation == "arcotangente":
        return f"set_slot result {(180 * m.atan(angulo)) / m.pi}"

def lineal(a, b):
    a = float(a)
    b = float(b)
    if a == 0:
        return f"set_slot result {'no es ecuación lineal'}"
    return f"set_slot result { -b / a}"

def cuadratica(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0:
        return f"set_slot result {'No es ecuacion cuadratica'}"
    return f"set_slot result {(-b + m.sqrt(b*b - 4*a*c))/(2*a)}"