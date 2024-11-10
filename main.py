class Asiento:
    def __init__(self,color,precio,registro) :
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,Piel):
        if Piel=="rojo"or Piel=="verde"or Piel=="amarillo"or Piel=="negro"or Piel=="blanco":
            self.piel=Piel


class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro (self,a):
        self.registro=a
    def asignarTipo(self,newtipo):
        if newtipo in ["gasolina","electrico"]:
            self.tipo=newtipo




class Auto:
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados) :
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        self.cantidadCreados=cantidadCreados
    
    def cantidadAsientos(self):
        c=0
        for h in self.asientos:
            if type(h)==Asiento:
                c+=1
        return c
    def VerificarIntegridad(self):
        for h in self.asientos:
            if isinstance(h,Asiento)==True and (self.registro!=h.registro or h.registro !=self.motor.registro) :
                return"Las piezas no son originales"
        return "Auto original"
    








        




