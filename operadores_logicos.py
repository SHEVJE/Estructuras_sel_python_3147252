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
5.     >, <, >=, <=, !=, ==
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

#ejemplo 6: operadores aritmeticos
#relacionales y logicos 

y= 3+5 * 2 > 3 and 4== 4 or 3 < 2

# ejemplo 7: con parentesis 
y= 3+5 != 2*3 and 4== 4 or not 3<2

# ejemplo 8: todo junto
y= 4**2* 3 < 6 / (7-5) and 7*2 +1==14 or not 3+5 <2

