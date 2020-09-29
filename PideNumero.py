

def main():
    '''
    Equipo 2
    Alumnos:
    Galindo Rosales Erik Eduardo
    Loaeza Nava José Alfredo
    Ramos Vallinas Héctor Ulises
    '''
    
    print("\n PROGRAMA NUMERO ")
    print("\n QUE PERMITE VISUALIZAR LA TABLA DE MULTIPLICAR")
    print("\n DEL NUMERO QUE TU INDIQUES")

    a = int(input("\n\nUsuario introduce el numero de la tabla que deseas (1- 10): "))

    for i in range(1,1000001):
        print(f" {a} x {i} = {a*i}")

    
main()
