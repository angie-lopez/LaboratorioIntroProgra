class circulo (): 
    def __init__(self, radio): 
        radio : float ()
        self.radio = radio
    def obtener_Perimetro(self):
        return 2 * math.pi * self.radio
    def obtener_Area(self):
        return math.pi * self.radio ** 2 
    def obtener_volumen(self): 
         return 4 * math.pi * self.radio ** 3 / 3
import math

math.pi

circulo = circulo(10)

print(circulo.obtener_Perimetro()) 
print(circulo.obtener_Area())  
print(circulo.obtener_volumen())  