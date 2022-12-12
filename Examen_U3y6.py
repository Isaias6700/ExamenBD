from mongodb import PyMongo

varmongo = {}
varmongo['host'] = 'localhost'
varmongo['db'] = 'Estados'
varmongo['port'] = 27017
varmongo['timeout'] = 1000
varmongo['user'] = ''
varmongo['password'] = ''


archivo = open("CPdescarga.txt")
lineas = archivo.readlines()
lista ={}
asentamiento = {}
arr_asen = []


def estados():
    id = 1
    objPymongo = PyMongo(varmongo)
    objPymongo.conectar_mongodb()
    for lin in lineas[2:]:
        cod = lin.split("|")
        estado = {}
        estado["IdEstado"] = id
        estado["Estado"] = cod[4]
        asentamiento["Codigo_Postal"] = cod[6]
        asentamiento["Nombre_Asentamiento"] = cod[1]
        arr_asen.append(asentamiento)
        estado["Asentamiento"] = arr_asen
        lista[cod[0]] = estado

        id=id+1
    print(lista)
    objPymongo.insertar('Estados', lista)
    objPymongo.desconectar_mongodb()
estados()