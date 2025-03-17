'''
if en cascada:
estructura de control que permite
evalua varias condiciones en
cascada, es decir, si la primera
condicion no se cumple,
se evalua la siguiente
y asi sucesivamente
'''
#ejemplo 1:
#modificar el programa de votacion 
#para que considre la edad de 17 
#años

edad = int(input("ingresa tu edad:"))
if edad > 18:
    print("puedes votar")
elif edad == 17:
    print("puedes votar el proximo año")
elif edad > 10:
    print("eres muy peque, tienes registro civil")
elif edad < 17:
    print("no puedes votar aun")
elif edad == 18:
    print("Bienvenido ciudadano, puedes votar con contraseña")

print("fin del programa")