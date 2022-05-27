##diccionarios
y = set() #conjunto
x = dict() #diccionario
z = tuple()


Empleados = {
    "Docentes":[]
}

profesor_1 = {
"Nombre": 'carlos' ,
"Apellido": 'daniel',
"Edad": '5'

}
Empleados["Docentes"] .append( profesor_1)

profesor_2 = {
"Nombre": 'angel' ,
"Apellido": 'suarez',
"Edad": '767'

}

Empleados["Docentes"] .append( profesor_2)




#print(profesor_2)

def verDocentes(Empleados:dict):
    i = Empleados["Docentes"]
    for k in i:
        print(k["Nombre"])
        


verDocentes(Empleados)