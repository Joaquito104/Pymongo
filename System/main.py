import pymongo
from System import Users
print('Bienvenido.')

print ("Iniciando Seccion")

while True:

    Privilegios= Users.usuario()
    if Privilegios == 1:


        continuar1 = print("Desea continuar?: [s/N]")
        if continuar1.lower() == 's':
            continue
        else:
            break
        
    elif Privilegios == 2:


        continuar2 = print("Desea continuar?: [s/N]")
        if continuar2.lower() == 's':
            continue
        else:
            break

        #print(coll.count_documents({}))
    

    else:
        print("Error. Ingrese los numeros correspondiente")