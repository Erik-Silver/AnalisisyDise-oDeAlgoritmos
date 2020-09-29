

def main():
    print("\n PROGRAMA NUMERO 5")
    print("\n QUE PERMITE VISUALIZAR LA TABAL DE MULTIPLICAR")
    print("\n DEL NUMERO QUE TU INDIQUES")

    a = int(input("\n\nUsuario introduce el numero de la tabla que deseas: "))

    for i in range(1,1000001):
        print(f" {a} x {i} = {a*i}")

    
main()
