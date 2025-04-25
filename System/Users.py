""" Datos  sistema

Usuarios: vendedor (seller), administrador (admin)

vendedor: 1 a 3 tipos,  en caso de querer el mismo tipo y quilo => venta separada 

"""
import pymongo

server = pymongo.MongoClient('localhost', 27017)

#Datos server db = acme, collection = Ventas
db = server['acme']    
coll = db['Ventas']

def peticion ():
    
