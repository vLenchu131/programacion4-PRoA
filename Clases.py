class producto:
        def __init__(self, nombre, precio, canstock, idproveedor):
         self.nombre=nombre
         self.precio=precio
         self.canstock=canstock
         self.idproveedor=idproveedor
        def mostrar (self):
              print("producto", self.nombre)
              print("precio:", self.precio)

              P1=producto("CocaCola", "180", "10", "Distribuidoras Sierras") 
              P1=mostrar ()