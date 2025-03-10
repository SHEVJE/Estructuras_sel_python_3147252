'''
Operadores logicos 
Aquellos que operan unicamente 
con valores booleanos (V F) 
acorde a las tablas de la verdad 
'''

# Ejemplo 1:  operador not:
y= not True 
print ("El resultado de operar con not es", y)

# Ejemplo 2:  operador and:
y= False and True
print ("El resultado de operar and es", y)

#Ejemplo 3 operador or
y= False or False
print ("El resultado de operar con or es", y )

'''

Jerarquia de precedencia de operadores
(logicos inclusive)

1.      ()
2.      **
3.      *, /, %,
4.      +, -
5.     >, <, >=, <=, !=,
6.      not
7.      and
8.      or
9.      =
'''

#ejemplo 4: Jerarquia de operadores
y= False and not True or False
print ("El resultado de operar con jerarquia es", y)

#ejemplo 5: operadores relacionales y logicos 
y= not 3 > 4 and 4 == 4 or 3 < 2
