'''
estructura de control if:
se utiliza para tomar decisiones
basadas en expresiones condicionales
'''
#ejeplo1:if simple
edad = int(input("ingresa tu edad:"))
documento = input("¿tienes documento(SI/NO):")
#condiocional: si la edad es mayor  igual a 18
if edad >= 18 and documento=='SI':
    #codigo para cuando es mayor a 18
    print("eres mayor de edad y tiene documento, puedes votar")
else:
    #codig para cuando es menor a 18
    print("eres menor de edad o no tienes documento, no puedes votar")
 #codigo que se ejecuta siempre
print("fin del programa")

