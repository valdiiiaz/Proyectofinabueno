nombre = input ("Escribe tu nombre: ")
print ("Hola " + nombre + ", aquí te ayudaremos a escoger el platillo que comerás hoy ")
print("Primero quiero saber que prefieres: salado o dulce?")
print("presiona 1 si te gusta la comida salada")
print("presiona 2 si te gusta la comida dulce")
opcion = int(input (" Escribe la opción que deseas usar "))

#Opción 1 Salado 
if opcion == 1:
#Opción picante
    opcionpicante = input("Te gustaría comer algo picante? ")
    if opcionpicante == "si":
        escalapicante = input("De la escala del 1 al 10 que tan picante te gustaría? ")
        if escalapicante == "1":
            platillopicante1x1 = input("Te gustaría un guacamole con totopos? ")
            if platillopicante1x1 == "si":
                print("disfruta tu comida")
            else:
                platillopicante1x2 = input("O tal vez pico de gallo con totopos ")
                if platillopicante1x2 == "si":
                    print("Disfruta tu platillo")
                else:
                    platillopicante1x3 = input("Entoces tal vez te gustaria una sopa de tortilla ")
                    if platillopicante1x3 == "si":
                        print("Disfruta tu platillo")
                    else:
                        print("Lo siento, no se que recomendarte")
        elif escalapicante == "2":
            platillopicante2x1 = input("Te gustaría comer ceviche de camarón? ")
            if platillopicante2x1 == "si":
                print("disfruta tu platillo")
            else: 
                platillopicante2x2 = input("Te gustaría comer unas enchiladas? ")
                if platillopicante2x2 == "si":
                    enchiladas = input("verdes, rojas, suizas o de mole? ")
                    if enchiladas == "mole":
                        mole = input("mole poblano, rojo, verde, amarillo, pipián o negro ")
                        if mole in("poblano","rojo","verde","amarillo","pipian","negro"):
                            print("Disfruta tu platillo")
                        else:
                            print("Lo siento no te entendí")
                    elif enchiladas in("verdes","rojas","suizas"):
                        print("Disfruta tu platillo")
                    else:
                        print("Lo siento no te etendí")
                        
                else:
                    platillopicante2x3 = input("Entonces tal vez prefieras tacos al pastor ")
                    if platillopicante2x3 == "si":
                        print("Disfruta tu platillo")
                    else: 
                        print("Lo siento, no se que recomendarte :(")
    
    
    #Opcion mariscos
        elif escalapicante == "3":
            platillopicante3x1 = input("Te gustaría comer un sope con chorizo? ")
            if platillopicante3x1 == "si":
                print("Disfruta tu platillo")
            else:
                platillopicante3x2 = input("Entonces tal vez te gustaría comer pozole rojo ")
                if platillopicante3x2 == "si":
                        print("Disfruta tu platillo ")
                else: 
                    platillopicante3x3 = input("Entonces se me ocurre que tal vez tengas antojo de tamales ")
                    if platillopicante3x3 == "si":
                        print("disfruta tu platillo")
                    else: 
                        print("Lo siento, no se que recomendarte :(")
                        
#otras opciones
        elif escalapicante == "4":
            platillopicante4x1 = input("Te gustaría comer chile relleno? ")
            if platillopicante4x1 == "si":
                print("disfruta tu platillo")
            else:
                platillopicante4x2 = input("Y que te parecen unas fajitas de pollo adobadas?")
                if platillopicante4x2 == "si":
                    print("Disfruta tu platillo")
                else: 
                    platillopicante4x3 = input("Entonces unas tortas ahogadas? ")
                    if platillopicante4x3 == "si":
                        print("Disfruta tu platillo")
                    else:
                        print("Lo siento, no se que recomendarte")
    else:
        print("De estás opciones cual se te antoja más? mariscos, carnes o pasta?")
        opcion1 = input("Escribe la opción que se te antoje más")
        if opcion1 == "mariscos":
            platillo1 = input("te gustaría un coctel de camarón? ")
            if platillo1 == "si":
                print("Disfruta tu platillo")
            else:
                platillo2 = input("Te gustaría un filete de salmón? ")
                if platillo2 == "si":
                    print("disfruta tu platillo")
                else: 
                    platillo3 = input("Te gustaría un filete de pescado empanizado? ")
                    if platillo3 == "si":
                        print("Disfruta tu platillo")
                    else: 
                        print("Lo siento, no se que recomendarte")
                    
    #Opcion 1 carnes
                        
                    
    #opcion 1 pastas
        elif opcion1 == "carnes":
            platillo4 = input("Te gustaría comer arrachera?")
            if platillo4 == "si":
                print("Disfruta tu platillo")
            else:
                platillo5 = input("Te gustaría una hamburguesa? ")
                if platillo5 == "si":
                    print("Disfruta tu platillo")
                else: 
                    platillo6 = input("Te gustaría comer tacos?")
                    if platillo6 == "si":
                        print("Disfruta tu platillo")
                    else:
                        print("Lo siento, no se que recomendarte")
                        
        elif opcion1 == "pasta":
            platillo7 = input("Te gustaría comer spaghetti a la bolognesa ")
            if platillo7 == "si":
                print("Disfruta tu platillo")
            else:
                platillo8 = input("Te gustaría un fetuchini?")
                if platillo8 == "si":
                    print("disfruta tu platillo")
                else:
                    platillo9 = input("Te gustaría comer rabioles?")      
                    if platillo9 == "si":
                        print("Disfruta tu platillo")
                    else:
                        print("Lo siento, no se que recomendarte")
        else:
            print("Lo siento, no te entendí")

        
#Opcion 2 dulces
elif opcion == 2:
    print("Te gustaría algo frio o al tiempo? ")
    opcion2 = input("Escribe aqui lo que más se te antoje ")
    #Opcion frio
    if opcion2 == "frio":
        platillo10 = input("Te gustaría un helado? ")
        if platillo10 == "si":
            print("Disfruta tu platillo ")
        else:
            platillo11 = input("Te gustaría un pudín? ")
            if platillo11 == "si":
                print("Disfruta tu platillo")
            else:
                platillo12 = input("Entonces tal vez prefieras un flan ")
                if platillo12 == "si":
                    print("Disfruta tu platillo")
                else:
                    print("Lo siento, no se que recomendarte")
                    
    #Opcion al tiempo
    elif opcion2 == "al tiempo":
        platillo13 = "Te gustaría algún pan dulce? "
        if platillo13 == "si":
            print("Disfruta tu platillo")
        else:
            platillo14 = input("Te gustaría comer crepas? ")
            if platillo14 == "si":
                print("Disfruta tu platillo")
            else:
                platillo15 = input("Te gustaría comer pastel?")
                if platillo15 == "si":
                    print("Disfruta tu platillo")
                else:
                    print("Lo siento, no se que recomendarte :c")

                    
#Opcion else
else:
    print("Lo siento, no te entendí")





