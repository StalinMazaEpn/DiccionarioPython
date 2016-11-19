print('\t ESCUELA POLITECNCA NACIONAL')
print('INTEGRANTES:\n')
print('\t\t Edison Osorio')
print('\t\t Micha Cardenas')
def triangulo():
    print('\tTRIANGULO\n')
    lado=int(input('Ingrese la longitud del lado (base):\n'))
    altura=int(input('Ingrese la altura:\n'))
    area=(lado*altura)/2
    perimetro=lado*3
    print('El area del triangulo es: ',area)
    print('El perímetro del triángulo es: ',perimetro)


def cuadrado():
    print('\tCUADRADO\n')
    lado=int(input('Ingrese la longitud del lado: \n'))
    area=lado*lado
    perimetro=lado*4
    print('El area del cuadrado es: ',area)
    print('El perímetro del cuadrado es: ',perimetro)

def main():
    while True:
        NumLados=input('INGRESE EL # DE LADOS\n')
        if NumLados=='3':
            triangulo()
        elif NumLados=='4':
            cuadrado()
        else:
            input('¡¡ERROR!!.. EL NUMERO DE LADOS DEBE ESTAR EN EL RANGO DE 3 A 10... VUELVA A INGRESAR EL # DE LADOS')

main()
