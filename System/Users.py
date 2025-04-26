""" Datos  sistema

Usuarios: vendedor (seller), administrador (admin)

vendedor: 1 a 3 tipos,  en caso de querer el mismo tipo y quilo => venta separada 

"""
import pymongo

server = pymongo.MongoClient('localhost', 27017)

#Datos server db = acme, collection = Ventas
db = server['Acme']    
coll = db['Ventas']

#Opcion Ordenes
def OrdenSalmon ():

    print('Las opciones de salmones estan enumeradas correspondientemente desde el 1 al 3:\n1.- Atlantico\t2.- Nordico\t3.- Pacifico\n ')
    salmon = int(input('Eliga el numero correspondiente del salmon: '))

    if salmon == 1:
        print('El precio del Salmon atlantico por kilo es: $5000 con un costo de $3000')
        kilo1= int(input('Cuantos kilos necesita?: '))

        costoXtotal1= 5000*kilo1 + 3000
        coll.insert_one({'Salmon':'Atlantico', 'Costo':costoXtotal1}).inserted_id
        
    if salmon == 2:

        print('El precio del Salmon Nordico por kilo es: $7000 con un costo de $4500')
        kilo2= int(input('Cuantos kilos necesita?: '))

        costoXtotal2= 7000*kilo2 + 4500
        coll.insert_one({'Salmon':'Nordico', 'Costo':costoXtotal2}).inserted_id
        
    if salmon == 3:
        
        print('El precio del Salmon Pacifico por kilo es: $3000 con un costo de $1500') 
        kilo3= int(input('Cuantos kilos necesita?: '))

        costoXtotal3= 3000*kilo3 + 1500
        coll.insert_one({'Salmon':'Pacifico', 'Costo':costoXtotal3}).inserted_id

    else:
        print('ERROR. Numero ingresado invalido. Orden cancelada')


#Usuarios

input

def usuario():
    pass

