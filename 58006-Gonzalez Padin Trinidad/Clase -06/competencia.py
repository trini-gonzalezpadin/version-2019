from generador import generador,generador_mejor
buscado=generador(1,100000)
nadie_adivino=True
listanumero=[]
while nadie_adivino:
    print("Ingrese un numero")
    numero=int(input())
    if numero == buscado:
            print("Ganaste ,fin del juego")
            nadie_adivino=False
    if numero < buscado :
            print("El numero es mayor")
    if numero > buscado:
            print("El numero es menor")
    if nadie_adivino==True:
        numero2=generador_mejor(1,100000,listanumero)
        print("El numero que penso la compu en su turno fue:" + str(numero2))
        listanumero.append(numero2)
        if numero2==buscado:
            print("Gano la compu")
            nadie_adivino=False
    

