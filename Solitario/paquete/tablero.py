def crear_tablero():

    filas = 10
    columnas = 7
    
    tablero = []

    for i in range(filas):
        elem = {}
        fila = [elem] * columnas
        tablero.append(fila)

    return tablero

#def mostrar_tablero():
    