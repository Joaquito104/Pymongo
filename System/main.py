import pymongo

print('Bienvenido.')
user = int(input("Ingrese 1 para iniciar como administrador o Ingrese 2 para iniciar como vendedor"))
print ("Iniciando Seccion")

while True:

    if user == 1:



        continuar1 = print("Desea continuar?: [s/N]")
        if continuar1.lower() == 's':
            continue
        else:
            break
        
    elif user == 2:


        continuar2 = print("Desea continuar?: [s/N]")
        if continuar2.lower() == 's':
            continue
        else:
            break
        

    else:
        print("Error. Ingrese los numeros correspondiente")