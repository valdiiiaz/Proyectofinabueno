print("¡Bienvenido a la Charrera!")
print("Lugar donde puedes comer toda la arrachera que quieras por $300")
promocionilimitada= input("¿Deseas usar estar promo?")
if promocionilimitada == "si":
        entradas= input("Deseas ordenar alguna entrada? ")
        if entradas == "si":
            print("Tenemos:\n Queso fundido con chorizo \n Guacamole \n Ceviche de camarón \n Tostadas de tinga")
            entrada= input("¿Que te gustaría? ")
        elif entradas == "no":
            print("ok")
elif promocionilimitada == "no":
     ejecutar = True
#Ciclo
ejecutar = True
while ejecutar:
    print("Que platillo de arrachera le gistaría? ")
    print("Tenemos tacos de arrachera \n arrachera a la parrila \n aracherra a la mexicana \n arrachera en fajitas \n arrachera con papas al gusto \n burritos de arrachera \n arrachera en salsa roja \n ensaada de arrachera \n molletes de arrachera \n tostadas de arrachera")
    arrachera = input("Escribe aquí lo que desea ordenar ")
    if arrachera == "arrachera con papas al gusto":
         papas = input("Te gustarían fritas o al horno? ")
         print("ok")
    else:
         termino = input("A que termino le gustaría su arrachera?" )
    print("Y de tomar?")
    bebida = input ("Le gustaría tomar algo con alcohol? ")
    if bebida == "si":
         print("Contamos con vino \n cerveza \n mezcal \n tequila \n whisky")
         bebidaalcoholica = input("que se desea tomar? ")
    elif bebida == "no":
         print("Tenemos agua de jamaica \n horchata \n limon con chia \n té de menta \n sangría sin alcohol")
         bebidasana = input("Que desea le gustaría tomar?")
         if entradas == "si":
              print("Entonces será ", entrada)
         else:
              print ("una", arrachera)
              print(" con termino de", termino)
              print ("y un ", bebidaalcoholica / bebidasana )
              ejecutar = False
