from math import log10
from random import randint
from unicodedata import digit

DEBUG = True
COUNT = 4

def generate_secret(max_digits = 4) -> str:
    num = randint(0, 10**max_digits)
    return str(num).zfill(max_digits)

def loopinput(message, tfn=None, emsg='Vuelva a Intentarlo'):
    transform_fn = str if tfn is None else tfn
    while True:
        inp = input(message)
        try:
            trns = transform_fn(inp)
            return trns
        except KeyboardInterrupt as e:
            raise e
        except ValueError as ve:
            print(emsg, end='\r')
            input()
def printd(*args, **kwargs):
    if not DEBUG:
        return
    print('[debug]', *args, **kwargs)

def launch_game(secret: str):
    printd(f'the secret: {secret}')
    ldigitos = list(secret)
    printd('Lista de valores:', ldigitos)
    ha_ganado = False
    intentos = 1
    while not ha_ganado: 
        numero_ins = loopinput('🎲 Ingrese el número: ', int, emsg='⚠️ Debe ingresar un número')
        si = str(numero_ins).zfill(COUNT)
        if numero_ins < 0:
            print('💥 No se aceptan números negativos')
            continue
        if len(si) != COUNT:
            print(f'Se esperaba una cadena de {COUNT} dígitos')
            continue
        print(f"Ingresaste 👉 '{si}'")
        ldigitoing = list(si)
        ok = 0
        okPos = 0
        for i in range(COUNT):
            digito = ldigitoing[i] # El i-esimo caracter ingresado

            for j in range(COUNT):
                num = ldigitos[j] # El j-caracter secreto
                isOk = num == digito
                ok += isOk
                okPos += isOk and i == j
        if okPos == COUNT:
            break 
        
        print(
            f'👀 Hay {okPos} dígito(s) en la posición correcta',
            f'✨ Hay {ok} Dígito(s) coorectos en total, trata de reordenalos para adivinar 👀',
            sep='\n'
        )
        intentos += 1
    
    print('🎉 Felicidades has ganado!!')
    print(f'⏰ Te ha tomado {intentos} intentos')

    

if __name__ == '__main__':
    launch_game(generate_secret())