
def operations(*args):
    operation = args[0]
    num_1 = float(args[1])
    num_2 = float(args[2])
    resultado = 0
    if operation == "suma":
        return f"set_slot result {num_1 + num_2}"     
    elif operation == "resta":
        return f"set_slot result {num_1 - num_2}"
    elif operation == "multiplicacion":
        return f"set_slot result {num_1 * num_2}"     
    elif operation == "division":
        return f"set_slot result {num_1 / num_2}"    

