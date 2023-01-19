from figuras import Rectangulo, Circulo, probar_figura

def main():
    while True:
        print('     AREA Y PERIMETRO DE FIGURAS GEOMETRICAS\n\n     1-Rectangulo\n     2-Circulo\n     3-Salir')
        ent=input('Ingrese una opción: ')
        print('')
        if ent=='1':
            base=float(input('Ingrese la base: '))
            altura=float(input('Ingrese la Altura: '))
            print('')
            rec1=Rectangulo(base,altura,'rectangulo')
            probar_figura(rec1)
        elif ent=='2':
            rad=float(input('Ingrese Radio: '))  
            print('')          
            cir1=Circulo(rad,'circulo')
            probar_figura(cir1)
        elif ent=='3':
            print('---Cerrando sistema---')
            break
        else:
            print('Ingrese un número de 1 al 3')

if __name__=='__main__':
    main()
    

