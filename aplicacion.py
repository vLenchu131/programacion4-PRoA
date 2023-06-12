class prov:
    def __init__(self,idproveedor,nombre,direccion):
        self.idproveedor = idproveedor
        self.nombre = nombre
        self.direccion = direccion
    def mostrar(self):
        print("proveedor: ",self.idproveedor,"nombre:",self.nombre, "direccion:",self.direccion)


prove = input("que proveedor es? ")
nom = input("cual es su nombre? ")
dir =  input("cual es su direccion? ")


a1 = prov(prove,nom,dir)
a1.mostrar()