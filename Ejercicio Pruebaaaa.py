def promedio(lista_funcion):
    acum=0
    for x in lista_funcion:
        acum=acum+x[2]
    cant=len(lista_funcion)
    promedio=acum/cant
    return promedio

def buscar(lista_jugadores, numero_a_buscar):
    encontrado = False
    for jugador in lista_jugadores:
        if numero_a_buscar==jugador[0]:
            encontrado = True
            print("Numero de camiseta: ",jugador[0],"Nombre: ",jugador[1],"Goles: ",jugador[2],"Categoria: ",jugador[3])
            break
    return encontrado
def eliminar_jugador(lista_jugadores, numero_a_eliminar):
    encontrado=False
    for jugador in lista_jugadores:
        if numero_a_eliminar==jugador[0]:
            print("Numero de camiseta: ",jugador[0],"Nombre: ",jugador[1],"Goles: ",jugador[2],"Categoria: ",jugador[3])
            lista_jugadores.remove(jugador)
            break
    return encontrado
        
lista=[]
while True:
    print("")
    print("-.-.-.- M E N U -.-.-.-")
    print("1.- Agregar Jugador")
    print("2.- Listar Jugadores")
    print("3.- Imprimir datos de jugador")
    print("4.- Eliminar Jugador")
    print("5.- Estadisticas")
    print("6.- Generar bbdd")
    print("7.- Cargar datos desde Archivo")
    print("0.- Salir")
    print("")
    op=int(input("Ingrese una opción: "))
    if op==1:
        print("")
        n_camiseta=int(input("Ingrese su numero de camiseta"))
        nombre=input("Ingrese su nombre")
        goles=int(input("Ingrese su numero de goles"))
        if goles>0 and goles<=5:
            categoria = "Amateur"
        elif goles>5 and goles<=15:
            categoria = "Semi"
        elif goles>15:
            categoria = "PRO"
        jugador_nuevo=[n_camiseta,nombre,goles,categoria]
        lista.append(jugador_nuevo)                
                       
    elif op==2:
        for jugador in lista:
            print("Numero de camiseta: ",jugador[0],"Nombre: ",jugador[1],"Goles: ",jugador[2],"Categoria: ",jugador[3])
            print("")
    elif op==3:
        encontrado = False
        print("")
        print("-.-.-.- D a t o s   d e l   J u g a d o r -.-.-.-")
        n_buscar=int(input("Ingrese su numero de camiseta a buscar"))
        bus=buscar(lista,n_buscar)
        if bus:
            print("Jugador Encontrado")
        else:
            print("Jugador no encontrado")
        '''
        for jugador in lista:
            if n_camiseta==jugador[0]:
                print("Numero de camiseta: ",jugador[0],"Nombre: ",jugador[1],"Goles: ",jugador[2],"Categoria: ",jugador[3])
                print("")
                encontrado = True
                break
        '''        
    elif op==4:
        encontrado = False
        print("")
        print("-.-.-.- J u g a d o r   a   E l i m i n a r -.-.-.-")
        n_eliminar=int(input("Ingrese su numero de camiseta a eliminar"))
        eli=eliminar_jugador(lista,n_eliminar)
        if eli:
            print("Jugador eliminado correctamente")
        else:
            print("Jugador no eliminado")
        
    elif op==5:
        print("")
        print("-.-.-.- E S T A D I S T I C A S -.-.-.-")
        print("")
        print("-.-.- P r o m e d i o   d e   g o l e s -.-.-")
        prom=promedio(lista)
        print("Promedio de goles: ",int(prom))
    elif op==6:
        print("")
    elif op==7:
        print("")
    elif op==8:
        print("")
    else:
        print("")
        print("Error.... volviendo al menu principal")
        print("")
