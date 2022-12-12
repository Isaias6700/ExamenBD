import json
from crudmysql import MySQL
from env import variables
from mongodb import PyMongo

productos = [{"idProducto": 1850,
              "productoNombreCorto": "William Lawsons Std",
              "productoNombreLargo": "Whisky William Lawsons Std 750 ml",
              "productoDescripcion": "Es un whisky afrutado de cuerpo ligero, se caracteriza por su aroma a pastel de manzana y su sabor a cereal tostado y al tofee, con un final suave.",
              "productoTipo": 1,
              "productoPresentacion": "Botella",
              "productoCosto": 170.5,
              "productoGanancia":15,
              "productoDescuento": 0,
              "productoExistencia": 1000,
              "productoImagen": "Whisky-1850.webp"},
             {"idProducto": 1450,
              "productoNombreCorto": "Outer Space",
              "productoNombreLargo": "Vodka Outer Space 750 ml",
              "productoDescripcion": "Es un vodka hecho con maíz 100% americano, sin gluten, el diseño de su botella es único y llamativo. Tiene aromas y sabores a frutos secos.",
              "productoTipo": 1,
              "productoPresentacion": "Botella",
              "productoCosto": 700.5,
              "productoGanancia": 15,
              "productoDescuento": 0,
              "productoExistencia": 1000,
              "productoImagen": "Vodka-1450.webp"},
             {"idProducto": 850,
              "productoNombreCorto": "Ron Antillano Blanco",
              "productoNombreLargo": "Ron Antillano Blanco C/Vaso/Macerador 1L",
              "productoDescripcion": "",
              "productoTipo": 1,
              "productoPresentacion": "Botella",
              "productoCosto": 150.5,
              "productoGanancia": 15,
              "productoDescuento": 0,
              "productoExistencia": 1000,
              "productoImagen": "Ron-850.webp"}]

varmongo = {}
varmongo['host'] = 'localhost'
varmongo['db'] = 'Tienda'
varmongo['port'] = 27017
varmongo['timeout'] = 1000
varmongo['user'] = ''
varmongo['password'] = ''

def consult():
    objPymongo = PyMongo(varmongo)
    objPymongo.conectar_mongodb()

    for val in productos:
        print(val)
        objPymongo.insertar('categorias', val)
    objPymongo.desconectar_mongodb()
consult()

# for clave, valor in val.items():
#     for i in range(len(clave)):
#         dicc_prod[clave[i]] = valor[i]
#         print(dicc_prod)