import random

aleatorio = random.randint(1,10)

while True:
    num = int(input("ingrese numero entre 1 y 10"))
    if num == aleatorio:
        print("felicidades ganaste un cupon!")
        break
    elif num < aleatorio:
        print("el numero es mayor, intenta nuevamente")
    else:
        print("el numero es menor, intenta nuevamente")
        print("fin del juego")