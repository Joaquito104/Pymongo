""" Datos  sistema

Usuarios: vendedor (seller), administrador (admin)

vendedor: 1 a 3 tipos,  en caso de querer el mismo tipo y quilo => venta separada 

Costos: Atlantico: $3000, Nordico: $4500', Pacifico: $1500
Ganacias: Atlancico: $5000, Nordico: $7000, Pacifico: $3000

"""
import pymongo

server = pymongo.MongoClient('localhost', 27017)

#Datos server db = acme, colecciones = Ventas , Disponibilidad, Ganancias
db = server['Acme']    
ventas = db['ventas']
ganancias = db['ganancias']
stock = db['Stock']
#Opcion Ordenes
def ordenSalmon ():

    print('Las opciones de salmones estan enumeradas correspondientemente desde el 1 al 3:\n1.- Atlantico\t2.- Nordico\t3.- Pacifico\n ')
    salmon = input('Eliga el numero correspondiente del salmon: ')

    if salmon == '1':
        print('El precio del Salmon Atlantico por kilo es: $5000')
        kilo1= int(input('Cuantos kilos necesita?: '))

        totalKilo1= 5000*kilo1     
        costo1 = 3000

        ventas.insert_one({'Salmon':'Atlantico', 'Cantidad Kilos': kilo1 ,'Monto':totalKilo1}).inserted_id
        ganancias.insert_one({'Salmon':'Atlantico','Cantidad Kilos vendidos': kilo1 ,'Costo':costo1, 'Ganancia': totalKilo1 - costo1}).inserted_id
       

    elif salmon == '2':

        print('El precio del Salmon Nordico por kilo es: $7000 ')
        kilo2= int(input('Cuantos kilos necesita?: '))

        totalKilo2= 7000*kilo2 
        costo2 = 4500
        ventas.insert_one({'Salmon':'Nordico','Cantidad Kilos': kilo2 ,'Monto':totalKilo2}).inserted_id
        ganancias.insert_one({'Salmon':'Nordico','Cantidad Kilos vendidos': kilo2 ,'Costo':costo2, 'Ganancia': totalKilo2 - costo2}).inserted_id
        
    elif salmon == '3':
        
        print('El precio del Salmon Pacifico por kilo es: $3000') 
        kilo3= int(input('Cuantos kilos necesita?: '))

        totalKilo3= 3000*kilo3 
        costo3 = 1500

        ventas.insert_one({'Salmon':'Pacifico','Cantidad Kilos': kilo3 ,'Monto':totalKilo3}).inserted_id
        ganancias.insert_one({'Salmon':'Pacifico','Cantidad Kilos vendidos': kilo3 ,'Costo':costo3, 'Ganancia': totalKilo3 - costo3}).inserted_id

    else:
        print('Error . Numero ingresado invalido. Orden cancelada')


#Usuarios
def usuario():
    ingreso = input('Para iniciar como administrador ingrese 1. Para iniciar como vendedor ingrese 2. ')
    if ingreso == '1':
        print('Bienvenido estimado administrador.')
        print('Eliga la opcion correspondiente\nPara añadir una compra de salmon ingrese 1')
        print('Para reporte de pedidos ingrese 2\nPara editar el stock y disponibilidad ingrese 3')

        crud = input('Porfavor ingrese numero correspondinte a las opciones: ')

        if crud == '1':
            ordenSalmon()

        elif crud == '2':
            print('Estimado administrador, que reporte necesita? : Opcion 1: Pedidos. Opcion 2: Ganancias')
            reporte = input('Porfavor ingrese numero correspondinte a las opciones: ')

            if reporte == '1':
                reporteVentas = ventas.find({}) 
                for x in reporteVentas:       #Recorre en todos los documentos 1 en 1 
                    print(x)     

            elif reporte == '2':
                reporteGanancias = ganancias.find({})
                for x in reporteGanancias:
                    print(x)
            
            else: 
                print('Error. Cancelando accion')
                   
        elif crud == '3':
            print('Estimado administrador, de que salmon necesitar editar el stock y disponibilidad')
            print('Opcion 1: Atlantico. Opcion 2: Nordico. Opcion 3: Pacifico')

            editar = input('Porfavor ingrese numero correspondinte a las opciones: ')
            
            if editar == '1':
                nuevoStock1 = int(input('Ingrese el numero con el cual se modificara el stock: '))       #Crud : Update
                resultados1 = stock.update_one({"Salmon":"Atlantico"},{"$set":{"Stock":nuevoStock1}})

                if resultados1.matched_count > 0:
                    print("Stock actualizado correctamente.")
                else:
                    print("No se encontró el salmón para actualizar.")
                
            elif editar == '2':
                nuevoStock2 = int(input('Ingrese el numero con el cual se modificara el stock: '))
                resultados2 = stock.update_one({"Salmon":"Nordico"},{"$set":{"Stock":nuevoStock2}})

                if resultados2.matched_count > 0:
                    print("Stock actualizado correctamente.")
                else:
                    print("No se encontró el salmón para actualizar.")

            elif editar == '3':
                nuevoStock3 = int(input('Ingrese el numero con el cual se modificara el stock: '))
                resultados3 = stock.update_one({"Salmon":"Pacifico"},{"$set":{"Stock":nuevoStock3}})

                if resultados3.matched_count > 0:
                    print("Stock actualizado correctamente.")
                else:
                    print("No se encontró el salmón para actualizar.")                

            else: 
                print('Error. Cancelando accion')          

        
    elif ingreso == '2':
        print('Bienvenido estimado vendedor.')
        ordenSalmon()
    
    else:
        print('Error. Cancelando inicio de seccion')


#usuario()

