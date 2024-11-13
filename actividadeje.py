print("Bienvenido a la página de ticketmaster \n Aqui puedes comprar los boletos de los eventos que quieras")
artista = input("Escribe aquí el artista que deseas ver ")
if artista == "Mon Laferte":
      print("Selecciona tu región")
      print("presiona 1 para CDMX \n presiona 2 para Monterrey \n presiona 3 para Jalisco \n presiona 4 para Guanajuato \n presiona 5 para Cancún")
      region = input("Escribe el # aquí ")
      if region == "1":
        print("Mon Laferte se presentará en el Palacio de los Deporte")
        print("Escoge la fecha")
        print("18 de octubre del 2025 \n 19 de octubre del 2025 \n 20 de octubre de 2025")
        diasMon = input("Escribe la fecha completa aquí ")
        print("Los niveles disponibles son: \n A \n B \n C \n D \n E")
        nivel = input("escribe el nivel en el que deseas estar ")
        if nivel == "A":
            print("Las zonas disponibles son \n A1 \n A2 \n A3 \n A4 \n A5 \n A6 \n A7 \n A8")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(1,4):
                print("el precio por boleto sería de $4459")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 4459 * boletos
                print("Total: $", precio)
            elif zona in range(5,8):
                print("el precio por boleto sería de $4279")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 4229 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "B":
            print("Las zonas disponibles son \n B1 \n B2 \n B3 \n B4 \n B5 \n B6 \n B7 \n B8")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(3,6):
                print("el precio por boleto sería de $3389")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3389 * boletos
                print("Total: $", precio)
            elif zona in [1,2,7,8]:
                print("el precio por boleto sería de $2749")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 2749 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "C":
            print("Las zonas disponibles son \n C3 \n C4 \n C5 \n C6 \n C7 \n C8 \n C9 \n C10 \n C11 \n C12 \n C13 \n C14 \n C14 \n C15 \n C16 \n C17 \n C18")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(7,14):
                print("el precio por boleto sería de $2049")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 2049 * boletos
                print("Total: $", precio)
            elif zona in range(3,6)or(15,18):
                print("el precio por boleto sería de $1669")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 1669 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "D":
            print("Las zonas disponibles son \n D6 D7 D8 D9 \n D10 D11 D12 D13 \n D14 D15 D16 D17 \n D18 D19 D20 D21 \n D22 D23 D24 D25 \n D26 D27 D28 D29 \n D30 D31")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(12,25):
                print("el precio por boleto sería de $1019")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 1019 * boletos
                print("Total: $", precio)
            elif zona in range(6,11)or(26,31):
                print("el precio por boleto sería de $959")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 959 * boletos
        elif nivel == "E":
            print("Las zonas disponibles son \n E7 E8 E9 E10 \n E11 E12 E13 E14 \n E15 E16 E17 E18 \n E19 E20 E21 E22 \n E23 E24 E25 E26 \n E27 E28 E29 E30 \n E31")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(13,26):
                print("el precio por boleto sería de $789")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 789 * boletos
                print("Total: $", precio)
            elif zona in range(7,12)or(27,31):
                print("el precio por boleto sería de $649")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 649 * boletos
        cotizacion = input("Deseas comprar los boletos? ")
        if cotizacion == "si":
            metododepago = input("Sería con débito o crédito? ")
            print("Ok! Serán " , boletos , " boletos para ir a ver a Mon Laferte en el palacio de los deportes el dia " , diasMon , " en la zona " , nivel,zona , " \n a un precio de $" ,precio , "en total")
        else:
            aplicarciclo= input("Deseas buscar otro artista?")
            if aplicarciclo == "si":
                print("ciclo no se como")
            else:
                print("Gracias por recurrir a nosotros")
else:
    print("lo siento, no conozco ese artista")
