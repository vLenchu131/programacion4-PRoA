class autos:
    def _init_(self,nom,mod,pre):
        self.nom=nom
        self.mod=mod
        self.pre=pre
    def descripcion(self):
        print("nombre:{self.nom} modelo:{self.mod} precio:{self.pre}")
class Chevrolet(autos):
    def _init_(self,nom,mod,color,pre,marc):
        super(), __init__(self,nom,mod,pre)
        self.marc=marc
    def descripcion(self):
        super().descripcion()
        print(f"Marca: "(self.marc))
class Fiat: