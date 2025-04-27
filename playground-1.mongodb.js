use('Acme')
/*db.createCollection('ventas')
db.createCollection('Ganancias')
db.createCollection('Stock')*/

// Stock de testeo
db.Stock.insertMany([
    {Salmon: 'Atlantico', Stock : 10},
    {Salmon: 'Nordico', Stock : 10},
    {Salmon: 'Pacifico', Stock : 10}])