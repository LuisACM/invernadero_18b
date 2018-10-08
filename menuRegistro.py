from registro import Registro
from datetime import date
class MenuRegistro:
    def __init__(self, conexion, cursor):
        self.registro = Registro(conexion, cursor)
        while True:
            print("1) Agregar Registro")
            print("2) Buscar Registros")
            print("0) Salir")
            op = input()
            
            if op=="1":
                self.agregar()
            elif op=="2":
                self.buscar()
            elif op=="0":
                break
                
                
    def agregar(self):
        dia = input("Dia: ")
        mes = input("Mes: ")
        year = input("Año: ")
        fecha = date(int(year), int(mes), int(dia))
        ph = input("pH: ")
        luz = input("Luz: ")
        humedad = input("Humedad: ")
        c02 = input("co2: ")
        id_planta = input("ID Planta: ")
        self.registro.crear(fecha, ph, luz, humedad, c02, id_planta)
        
    def buscar(self):
        id_planta = input("ID Planta: ")
        resultados=self.registro.recuperar(id_planta)
        
        for p in resultados:
            print("{0:2} {1:5} {2:5} {3:5} {4:5} {5:5} {6:5}".format(p[0], str(p[1]), p[2], p[3], p[4], p[5], p[6]))