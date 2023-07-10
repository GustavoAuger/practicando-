import random as rd

Certficado_Nac=rd.randrange(1500,3500)
Certficado_Con=rd.randrange(1500,3500)
Certficado_Union=rd.randrange(1500,3500)

lista_personas=[]
persona={'Nombre':"Rodrigo","Edad":"33","NIF":"43143143-RRR"} #creamos el diccionario persona
lista_personas.append(persona.copy()) #insertamos la persona en una lista

def grabar_datos(): 
    print(lista_personas)
    repite="r"
    edad=0
    verificacion=""
    while(True): 
        try:
            nombre= input("Ingrese su nombre: ")
            while edad<=0:
                edad= int(input("Ingrese su edad: "))
            if edad>15:
                while repite=="r":
                    nif= input("ingrese su numero NIF: ").upper()
                    largo=0
                    guion=0
                    for i in nif:
                        largo=largo+1
                        if "-"== i:
                            verificacion=int(verificacion)
                            verificacion=str(verificacion)
                            largoAnt=largo
                            guion=guion+1
                        else:
                            verificacion=verificacion+i
                    if largo-largoAnt==3 and guion==1 and largoAnt>7:
                        persona={"Nombre":nombre,"Edad":edad,"NIF":nif}
                        lista_personas.append(persona.copy())
                        print("datos ingresados correctamente")
                        repite=""
                    else:
                        print("Número NIF ingresado no es válido")
                        repite="r"
            else:
                break
            break
        except:
             verificacion=""
             print("Error. Favor vuelva a intentar")       

def buscar_persona():   
    global lista_personas
    print(lista_personas)
    index=0
    existe=0
    persona_busqueda=""
    while(True): 
        try:
            persona_busqueda= input("Ingrese NIF de la persona: ").upper()
            print("")
            break
        except:
            print("Error de ingreso, favor vuelva a intentar")  
    for busqueda in lista_personas:
        index=index+1
        if persona_busqueda==busqueda["NIF"]: 
            existe=1 #existe
            persona_busqueda=(lista_personas[index-1])
            for datos in persona_busqueda:
                print(datos,":",persona_busqueda[datos])  
            break     
    if existe==0: #no existe
        print(persona_busqueda, "no existe en registros\n")     
            

def imprimir_certificado(): 
    opc=0
    while(opc != "1" and opc != "2" and opc != "3" and opc != "4"):
        opc= input(f"Ingrese una opcion:\n \n1. Imprimir certificados de Emisión de contaminantes, Valor: ${Certficado_Nac} \n2. Imprimir certificados de anotaciones vigentes Valor: ${Certficado_Con}\n3. Imprimir certificados de multas Valor: ${Certficado_Union} \n\nOpcion: ")
        print("") #salto
    else:
        if opc=="1":
            print("Certificados de nacimiento:")
        elif opc=="2":
            print("Certificados estado conyugal:")
        elif opc=="3": 
            print("Certificados perteneciente a la Unión Europea:")

    persona_busqueda=""
    index=0

    while(True): 
        try:
            persona_busqueda= input("Ingrese NIF de la persona: ").upper()
            print("")
            break
        except:
            print("Error de ingreso, favor vuelva a intentar")  
    for busqueda in lista_personas:
        index=index+1
        if persona_busqueda==busqueda["NIF"]: 
            existe=1 #existe
            persona_busqueda=(lista_personas[index-1])
            for datos in persona_busqueda:
                print(datos,":",persona_busqueda[datos])  
            break     
    if existe==0: #no existe
        print(persona_busqueda, "no existe en registros\n")  


def salir():
    global ops
    print("\n¡ Hasta pronto !\nRealizado por: Gustavo Auger\n Versión: 2.0")
    ops="z"

    