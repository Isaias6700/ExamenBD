
import json
from crudmysql import MySQL
from env import variables
ar=[]
tp=[]

kardex=[]
alum=[]

def solicitar_control():
    control = input("Ingresa un numero de control: ")
    return control

def consultar(ctrl):
    k_alum = {}
    obj_MySQL = MySQL(variables)
    print(" == JSON GENERADO ==")
    ctrl = ctrl

    sql = "SELECT E.nombre, K.materia, K.calif  FROM estudiantes E, kardex K "
    sql = sql + f" WHERE E.control = K.control and E.control={ctrl};"
    resp = obj_MySQL.consulta_sql(sql)
    if resp:

        for mat in resp:
            k_alum['Nombre'] = mat[0]
            materia = {}
            materia["Nombre: "] = mat[1]
            materia["calificacion: "] = str(mat[2])
            kardex.append(materia)
        k_alum['Materias: '] = kardex
    else:
        print(f"El estudiante no existe")
    alum.append(k_alum)
    with open('Json' + '.json', 'w') as file:
        json.dump(alum, file, indent=4)




consultar(solicitar_control())
