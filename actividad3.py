'''
actividad3:
escribir un prgrama
que calcule el salario neto 
de un trabajador
despues de descuentos
y bonificaciones
=> INICIALMENTE, el programa
debe solicitar un tipo de 
tabajador entre los siguientes:
a - contrato a temino indefinido
b - contrato por prestacion de 
servicios
c - contrato de aprendizaje
d - jornal
=> jornal:
se debe solicitar:
- el tiempo de unidad a pagar
- el valor de a unidad
- el valor de la unidad
 el salari se calcula como
 el valor_undad * numero_unidades
 si el numero de unidades es mayor a 100
 se le da una bonificacion del 10%
 =>cntrato de aprendizaje:
 se debe solicitar el salario minm
 el salario neto es 
 el 75% del salario minimo
 => contrato por prestacion de sevicios
 se debe solicitar:
 - el valor del contrato
 - el numero de meses trabajados
 - antiguedad de la empresa
 se calcula dividiendo e valor del contrato 
 entre el numero de meses trabajados
 - si la antiguedad es menor a 2 años
 se le aumenta el 2% al salario mensual
 - si la antiguedad esta entre 2 y 5 años 
 se le aumnta el 5% al salario mensual
 - si la antiguedad es mayor a 5 años
 se le aumenta el 10% a salario mensual 
 descuentos de ley
 - 8% de salud
 - 10% de pension
 - 1% de caja
 => contrato a termino indefinido
 el salario mensual se calcula 
 con base en la siguente tabla
 de escalafnes o grados:
- 1: 1.5 veces el SMLV
- 2: 1.7 veces el SMLV
- 3: 2 veces el SMLV
- 4: 2.5 veces el SMLV
- 5: 3 veces el SMLV
el programa debe solicitar 
el escalafon o grado 
del empleado
- las bonificaciones y descuentos de ley son las mismas 
que en el caso b
'''
#varable global:
#variable que puede ser reconocida
#y asignada en cualquier parte del
#programa
#NOTA:se recomienda inicializar
#definir y dar valor inicial a las
#las vaiables globales al principio
#del programa
#ejemplo de esto son las variabls
#para almacenar resultados finales
tipo_empleado = input("Ingrese tipo de empleado (a/b/c/d): ")
salario_neto =0
if tipo_empleado == "a":
    print("Ha ingresado término indefinido")
    SMLV = int(input("ingrese SMLV:"))
    escalafon = int(input("ingrese el escalafon:"))
    antiguedad = int(input("Ingrese la antiguedad en años: "))
    if escalafon == 1:
        salario_mensual = 1.5 * SMLV
    elif escalafon == 2:
        salario_mensual = 1.7 * SMLV
    elif escalafon == 3:
        salario_mensual = 2 * SMLV
    elif escalafon == 4:
        salario_mensual = 2.5 * SMLV
    elif escalafon == 5:
        salario_mensual = 3 * SMLV
    salario_neto = salario_mensual
    #bonificaciones
    if antiguedad < 2:
        bonificacion = salario_mensual * 0.02
    elif 2 <= antiguedad <= 5:
        bonificacion = salario_mensual * 0.05
    else:
        bonificacion = salario_mensual * 0.10
    
    salario_mensual += bonificacion

     #descuentos
    descuento_salud = salario_mensual * 0.08
    descuento_pension = salario_mensual * 0.10
    descuento_caja = salario_mensual * 0.01
    
    salario_neto = salario_mensual - (descuento_salud + descuento_pension + descuento_caja)
    


elif tipo_empleado == "b":
    print("Ha ingresado prestación de servicio")
    valor_contrato = int(input("ingrese el valor del contrato:"))
    numero_meses = int(input("ingrese el numero de meses trabajados:"))
    antiguedad = int(input("ingrese la antiguedad en la empresa:"))
    salario_mensual = valor_contrato / numero_meses
    #bonificacions: elif anidados
    if antiguedad < 2:
        bonificacion = salario_mensual * 0.02
    elif antiguedad >= 2 and antiguedad <= 5:
        bonificacion = salario_mensual * 0.05
    elif antiguedad > 5:
        bonificacion = salario_mensual * 0.10
        #refactorizacion
    salario_mensual = salario_mensual + bonificacion
        #descuentos
    descuento_salud = salario_mensual * 0.08
    descuento_pension = salario_mensual * 0.10
    descuento_caja = salario_mensual * 0.01
    salario_neto = salario_mensual - descuento_salud - descuento_pension - descuento_caja + bonificacion

elif tipo_empleado == "c":
    print("Ha ingresado contrato de aprendizaje")
    salario_minimo = int(input("ingrese el salario minimo: "))
    descuento = salario_minimo * 0.25
    salario_neto = salario_minimo - descuento
elif tipo_empleado == "d":
    print("Ha ingresado jornal")
    #variables locales
    #variables que solo pueden ser
    #reconocidas asignadas en un bloque
    #de codigo especifico
    tipo_unidad = input("ingrese el tipo de unidad:")
    numero_unidades = int(input("ingrese el numero de " + tipo_unidad + " hechas:"))
    valor_unidad = float(input("ingrese valor de " + tipo_unidad))
    salario_neto = numero_unidades * valor_unidad
else:
    print("Tipo de empleado no reconocido")
#mostrar salario neto
print("el salario neto es:", salario_neto)
print("Fin del programa")

