print('\t\t ESCUELA POLITECNCA NACIONAL')
print('INTEGRANTES:')
print('\t\t Edison Osorio')
print('\t\t Micha Cardenas')
print("\t\t Stalin Maza")
import sys
def triangulo():
    print('\tTRIANGULO')
    lado=int(input('Ingrese la longitud del lado (base):\n'))
    altura=int(input('Ingrese la altura:\n'))
    area=(lado*altura)/2
    perimetro=lado*3
    print('El area del triangulo es: ',area)
    print('El perímetro del triángulo es: ',perimetro)

def cuadrado():
    print('\tCUADRADO')
    lado=int(input('Ingrese la longitud del lado: \n'))
    area=lado*lado
    perimetro=lado*4
    print('El area del cuadrado es: ',area)
    print('El perímetro del cuadrado es: ',perimetro)

def pentagonoR():
    print("\tPENTAGONO REGULAR")
    lado = int(input('Ingrese la longitud del lado: \n'))
    apotema = int(input('Ingrese el valor del apotema : \n')) #recibe los datos necesarios
    perimetro = 5 * lado #calcula el perimetro 
    area = (perimetro*apotema)/2 #calcula el area
    print('El area del pentagonoo es: ',area)
    print('El perímetro del pentagono es: ',perimetro)

def hexagonoR():
    print("\tHEXAGONO REGULAR")
    lado = int(input('Ingrese la longitud del lado: \n'))
    apotema = int(input('Ingrese el valor del apotema : \n'))#recibe los datos necesarios
    perimetro = 6 * lado  #calcula el perimetro
    area = 3 * lado * apotema  #calcula el area
    print('El area del pentagonoo es: ',area)
    print('El perímetro del pentagono es: ',perimetro)

def heptagonoR():
    print("\tHEPTAGONO REGULAR")
    lado = int(input('Ingrese la longitud del lado: \n'))
    apotema = int(input('Ingrese el valor del apotema : \n'))#recibe los datos necesarios
    perimetro = 7 * lado  #calcula el perimetro
    area = (perimetro*apotema)/2  #calcula el area
    print('El area del pentagono es: ',area)
    print('El perímetro del pentagono es: ',perimetro)

def switch(NumLados):    
    if NumLados=='3':
        triangulo()
        repetir()
    elif NumLados=='4':
        cuadrado()
        repetir()
    elif NumLados == '5':   #aqui realizamos las opciones del switch de acuerdo a lo que escoga
        pentagonoR()        #a lo que escoga el usuario.
        repetir()
    elif NumLados == '6':
        hexagonoR()
        repetir()
    elif NumLados == '7':
        heptagonoR()
        repetir()
    else:
        print("¡¡ERROR!!..NUMERO DE LADOS DEBE ESTAR EN RANGO DE 3 A 10")
        menu()
        
def menu():
    NumLados =input('INGRESE EL # DE LADOS\n')   
    switch(NumLados) #Este es el que recibe el numero de lados    
            
def repetir():
    escoger = input("Ingrese S si desea continuar o N si desea salir\n")
    while escoger == "S" or escoger == "s":
        menu()   #aqui damos la opcion al usuario de si desea continuar en el programa
    print ("Programa Terminado")
    sys.exit()
    
def main():
    menu()    #llamamos a la funcion del menu

main()
