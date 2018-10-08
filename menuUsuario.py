from usuario import Usuario
import getpass
class MenuUsuario:
    def __init__(self, conexion, cursor):
        self.usuario = Usuario(conexion, cursor)
        while True:
            print("1) Agregar Usuario")
            print("2) Login")
            print("0) Salir")
            op = input()
            
            if op=="1":
                self.agregar()
            elif op=="2":
                self.login()
            elif op=="0":
                break
                
                
    def agregar(self):
        correo = input("Correo: ")
        contra = getpass.getpass("Contraseña: ")
        tipo = input("Tipo: ")
        self.usuario.crear(correo, contra, tipo)
    
    def login(self):
        usuario = input("Ingrese su correo: ")
        contra = getpass.getpass("Ingrese su contraseña: ")
        
        if self.usuario.login(usuario, contra):
            print("Bienvenido")
            
        else:
            print("Hubo un error")