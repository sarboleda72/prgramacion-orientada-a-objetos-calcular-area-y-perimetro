class Figura:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def area(self):
        pass
    
    def perimetro(self):
        pass    

class Rectangulo(Figura):
    def __init__(self, base, altura, nombre):
        super().__init__(nombre)       
        self.base=base
        self.altura=altura
    
    def area(self):
        area=float(self.base)*float(self.altura)
        return area

    def perimetro(self):
        perimetro=(self.altura*2)+(self.base*2)
        return perimetro

    def __str__(self):
        return f'{self.nombre}[Base: {self.base} Altura: {self.altura}]'

class Circulo(Figura):
    def __init__(self, radio,nombre):
        super().__init__(nombre) 
        self.radio=radio
    
    def area(self):
        area=3.1416*(self.radio**2)
        return area
    
    def perimetro(self):
        perimetro=2*3.1416*self.radio
        return perimetro

    def __str__(self):
        return f'{self.nombre}[Radio: {self.radio}]'

def probar_figura(objeto):
    figura=objeto    
    print(figura)
    print('Area: ', figura.area())
    print('Perimetro: ',figura.perimetro())
    print('')
    





