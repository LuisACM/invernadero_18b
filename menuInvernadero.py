from invernaderos import Invernadero
class MenuInvernadero:
    def __init__(self, conexion, cursor):
        self.invernaderos = Invernadero(conexion, cursor)
        while True:
            print("1) Agregar Invernadero")
            print("2) Mostrar Invernadero")
            print("0) Salir")
            op = input()
            
            if op=="1":
                self.agregar()
            elif op=="2":
                self.mostrar()
            elif op=="0":
                break
                
                
    def agregar(self):
        nombre = input("Nombre: ")
        ubicacion = input("Ubicacion: ")
        id_dueno = input("ID Dueño: ")
        self.invernaderos.crear(nombre, ubicacion, id_dueno)
        
    def mostrar(self):
        resultados = self.invernaderos.recuperar()
        for r in resultados:
            print("{0:3} {1:10} {2:8} {3:3}".format(r[0], r[1], r[2], r[3]))