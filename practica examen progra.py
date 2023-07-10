import random as rd
from funciones import *


print("¡ Bienvenido !\n")

ops=""
while ops!="z":
    op=""
    while op != "1" and op != "2" and op != "3" and op != "4":
        op=input("Ingrese una opcion:\n \n1. Guardar datos \n2. Buscar persona \n3. Imprimir certificado \n4. Salir \n\nOpcion: ")
        print("") #salto
    else:
        if op=="1":
            grabar_datos()  
        elif op=="2":
            buscar_persona()
        elif op=="3": #
            imprimir_certificado()   
        elif op=="4":
            salir()
            break