print("Bienvenido a la página de ticketmaster \n Aqui puedes comprar los boletos de los eventos que quieras")
artista = input("Escribe el artista que deseas ver")
if artista == "Mon Laferte":
    print("selecciona tu región")
    print("presiona 1 para CDMX \n presiona 2 para Monterrey \n presiona 3 para Jalisco \n presiona 4 para Guanajuato \n presiona 5 para Cancún")
    región = input("Ingresa aquí tu número ")
    if región == "1":
        print("Mon Laferte se presentará en el Palacio de los Deporte")
        print("los días 18 de octubre del 2025 \n 19 de octubre del 2025 \n y el 20 de octubre de 2025 ")
        print("presiona 1 para el 18 \n presiona 2 para el 19 \n presiona 3 para el 20")
        diasMon = input("Ingresa aquí tu número")
        print("Los niveles disponibles son: A \n B \n C \n D \n E")
        nivel = input("Escribe el nivel en la que deseas estar")
        if nivel == "A":
            print("Las zonas disponibles son A1 \n A2 \n A3 \n A4 \n A5 \n A6 \n A7 \n A8 ")
            zona=input("escribe la zona en la que deseas estar")
else:
    print("lo siento, no tengo conozco a ese artista")
    regresar = input("Deseas buscar de nuevo?")
    if regresar == "si":
            ejecutar = False
    else:
         print("Gracias")