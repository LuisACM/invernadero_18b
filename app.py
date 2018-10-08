import mysql.connector
from duenos import Dueno
from menuDueno import MenuDueno
from menuInvernadero import MenuInvernadero
from menuUsuario import MenuUsuario
from menuPlanta import MenuPlanta
from menuRegistro import MenuRegistro
conexion = mysql.connector.connect(user='jorge', password='nano199699', database='invernadero')
cursor = conexion.cursor()

while True:
    print("1) Menu Dueño")
    print("2) Menu Invernadero")
    print("3) Menu Usuario")
    print("4) Menu Planta")
    print("5) Menu Registro")
    print("0) Salir")
    op = input()
    
    if op=="1":
        menuD=MenuDueno(conexion, cursor)
    elif op=="2":
        menuI=MenuInvernadero(conexion, cursor)
    elif op=="3":
        menuU=MenuUsuario(conexion,cursor)
    elif op=="4":
        menuP=MenuPlanta(conexion,cursor)
    elif op=="5":
        menuP=MenuRegistro(conexion,cursor)
    elif op=="0":
        break
#d = Dueno(conexion, cursor)
#d.crear('Ronald', 'Tep')
#print(d.recuperar())