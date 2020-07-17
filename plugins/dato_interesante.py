import random

def get_dato_interesante(*args):
    dato = random.choice(args)
    respuesta = f"Dato Interesante: Alusivo a {dato[0] }, {dato[1]}. Esto fue {dato[2]}"
    return f"set_slot dato_interesante '{respuesta}'"
