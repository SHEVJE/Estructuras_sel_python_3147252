estado_civil = input("ingresa tu estado civil:(soltero/casado/comprometido)")
edad = int(input("igresa tu edad:"))
temperamento = input("ingresa tu temperamento:(buena persona/mala pesona)")
fisico = input("ingresa el fisico:(lindo/a/feo/a)")
salario = int(input("ingresa el salario:"))

if estado_civil == "casado" or estado_civil == "comprometido":
    print("no puedes acecarte a esa persona, por que ya tiene compromiso")
elif edad < 18:
    print("no puedes acercarte a esa persona, por que no tiene la edad suficiente")
elif temperamento == "mala persona":
    print("no puedes acercarte a esa persona, por que te generaria estres")
elif fisico == "feo":
    print("no puedes acercarte a esa persona, por que no te atrae fisicamente")
elif salario  < 2000000:
    print("no puedes acercarte, no tiene buena establidad esconomica")
else:
    print("puedes hacercarte a esa persona")
print("fin del programa")
