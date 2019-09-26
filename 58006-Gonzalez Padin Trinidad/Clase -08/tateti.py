from tablero import draw_tablero,full,validate,win
tablero=[]
for i in range(0,9):
    tablero.append(" ")
draw_tablero(tablero)
while not win(tablero) and not full(tablero):
    print("Es el turno de la x")
    valido=False
    while not valido:
        print("Ingrese una posicion valida de 1 a 9 (x)")
        posicion=int(input())
        valido=validate (tablero,posicion)
        if not valido:
            print("Error de poscion")
    tablero[posicion-1]="x"
    draw_tablero(tablero)
    gano=win(tablero)
    if gano:
        print("Gano la x")
    else: 
        print("Es el turno de la o")
        valido=False
        while not valido:
            print("Ingrese una posicion valida de 1 a 9 (o)")
            posicion=int(input())
            valido=validate (tablero,posicion)
            if not valido:
                print("Error de poscion")
        tablero[posicion-1]="o"
        draw_tablero(tablero)
        gano=win(tablero)
        if gano:
            print("Gano la o")
if full(tablero) and not win(tablero):
    print("Nadie gano")


