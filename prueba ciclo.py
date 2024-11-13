print("Bienvenido a la página de ticketmaster \n Aqui puedes comprar los boletos de los eventos que quieras")
ejecutar = True
while ejecutar:
    print("Los artistas que tenemos son \n Mon Laferte \n Luis Miguel \n Twenty One Pilots")
    artista = input("Escribe aquí el artista que deseas ver ")
    if artista == "Mon Laferte":
        print("Selecciona tu región")
        print("presiona 1 para CDMX \n presiona 2 para Monterrey \n presiona 3 para Jalisco")
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
                    precio = 4279 * boletos
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
            else:
                print("La zona no está bien ecrita")
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
            else:
                print("La zona no está bien ecrita")
        else:
            print("El nivel está mal escrito")

        cotizacion = input("Deseas comprar los boletos? ")
        if cotizacion == "si":
            metododepago = input("Sería con débito o crédito? ")
            print("Ok! Serán " , boletos , " boletos para ir a ver a Mon Laferte en el palacio de los deportes el dia " , diasMon , " en la zona " , nivel,zona , " \n a un precio de $" ,precio , "en total")
        else:
            print("Gracias por recurrir a nosotros")
        aplicarciclo= input("Deseas buscar otro artista?")
        if aplicarciclo == "si":
            ejecutar = True
        else:
            print("Ok")
            ejecutar = False
    elif region == "2":
        print("Mon Laferte se presentará en el Auditorio Citibanamex")
        print("Escoge la fecha")
        print("4 de abril del 2025 \n 5 de abril del 2025 \n 6 de abril del 2025")
        diasMon = input("Escribe la fecha completa aquí ")
        print("Los niveles disponibles son: \n Beyond VIP \n Beyond \n Platinum \n B Platinum \n Perfiles \n Perfiles B \n Perfiles C" )
        nivel = input("escribe el nivel en el que deseas estar ")
        if nivel == "Beyond VIP":
            print("Las zonas disponibles son \n 1 \n 2 \n 3")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [1,2,3]:
                print("el precio por boleto sería de $4459")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 4459 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Beyond":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [1,2,3]:
                print("el precio por boleto sería de $4279")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 4279 * boletos
                print("Total: $", precio)
            elif zona in [4,5]:
                print("el precio por boleto sería de $3879")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3879 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Platinum":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(1,5):
                print("el precio por boleto sería de $3389")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3389 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "B Platinum":
            print("Las zonas disponibles son \n 6 \n 7")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [6,7]:
                print("el precio por boleto sería de $3159")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3159 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Perfiles":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(1,5):
                print("el precio por boleto sería de $2839")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 2839 * boletos
                print("Total: $", precio)
            elif zona in range(6,9):
                print("el precio por boleto sería de $2389")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 2389 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Perfiles B":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(1,3):
                print("el precio por boleto sería de $1599")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 1599 * boletos
                print("Total: $", precio)
            elif zona in range(4,7):
                print("el precio por boleto sería de $939")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 939 * boletos
                print("Total: $", precio)
            elif zona in [8,9]:
                print("el precio por boleto sería de $889")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 889 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Perfiles C":
            print("Las zonas disponibles son \n 10 \n 11")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [10,11]:
                print("el precio por boleto sería de $525")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 525 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        else:
            print("el nivel está mal escrito")

        cotizacion = input("Deseas comprar los boletos? ")
        if cotizacion == "si":
            metododepago = input("Sería con débito o crédito? ")
            print("Ok! Serán " , boletos , " boletos para ir a ver a Mon Laferte en el Auditorio Citibanamex el dia " , diasMon , " en la zona " , nivel,zona , " \n a un precio de $" ,precio , "en total")
        else:
            print("Gracias por recurrir a nosotros")
        aplicarciclo= input("Deseas buscar otro artista?")
        if aplicarciclo == "si":
            print("ciclo no se como")
        else:
            print("Ok")
    elif region == "3":
        print("Mon Laferte se presentará en el Auditorio Telmex")
        print("Escoge la fecha")
        print("11 de agosto del 2025 \n 12 de agosto del 2025 \n 13 de agosto del 2025")
        diasMon = input("Escribe la fecha completa aquí ")
        print("Los niveles disponibles son: \n Platea \n Zona Roja \n Zona Azul \n Zona Café \n Zona Blanca \n Zona Verde \n Zona Lila \n Zona Naranja \n Zona Amarilla" )
        nivel = input("escribe el nivel en el que deseas estar ")
        if nivel == "Platea":
            print("el precio por boleto sería de $4459")
            boletos = int(input("Cuántos boletos deseas comprar? "))
            precio = 4459 * boletos
            print("Total: $", precio)
        elif nivel == "Zona Roja":
            print("Las zonas disponibles son \n 102 \n 103 \n 104")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [102,103,104]:
                print("el precio por boleto sería de $4279")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 4279 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Azul":
            print("Las zonas disponibles son \n 201 \n 202 \n 203")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [201,202,203]:
                print("el precio por boleto sería de $3629")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3629 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Café":
            print("Las zonas disponibles son \n 204 \n 205")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [204,205]:
                print("el precio por boleto sería de $3489")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3489 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Blanca":
            print("Las zonas disponibles son \n 401 \n 402 \n 403 \n 404 \n 405 \n 406 \n 407")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(401,407):
                print("el precio por boleto sería de $3099")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3099 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Verde":
            print("Las zonas disponibles son \n 301 \n 302")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [301,302]:
                print("el precio por boleto sería de $2749")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 2749 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Lila":
            print("Las zonas disponibles son \n 501 \n 502 \n 503 \n 504 \n 505 \n 506 \n 507")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(501,507):
                print("el precio por boleto sería de $1669")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 1669 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Naranja":
            print("Las zonas disponibles son \n 601 602 \n 603 604 \n 605 606 \n 607 608 \n 609 610 \n 611 612 \n 613")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(601,605):
                print("el precio por boleto sería de $1019")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 1019 * boletos
                print("Total: $", precio)
            elif zona in range(606,609):
                print("el precio por boleto sería de $829")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 829 * boletos
                print("Total: $", precio)
            elif zona in range(610,613):
                print("el precio por boleto sería de $959")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 959 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Amarillo":
            print("Las zonas disponibles son \n 701 \n 702 \n 703 \n 704 \n 705 \n 706")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(701,706):
                print("el precio por boleto sería de $789")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 789 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        else:
            print("El nivel está mal escrito")
        cotizacion = input("Deseas comprar los boletos? ")
        if cotizacion == "si":
            metododepago = input("Sería con débito o crédito? ")
            print("Ok! Serán " , boletos , " boletos para ir a ver a Mon Laferte en el Auditorio Telmex el dia " , diasMon , " en la zona " , nivel,zona , " \n a un precio de $" ,precio , "en total")
        else:
            print("Gracias por recurrir a nosotros")
        aplicarciclo= input("Deseas buscar otro artista?")
        if aplicarciclo == "si":
            print("ciclo no se como")
        else:
            print("Ok")
            
elif artista == "Luis Miguel":
    print("Selecciona tu región")
    print("presiona 1 para CDMX \n presiona 2 para Monterrey \n presiona 3 para Jalisco")
    region = input("Escribe el # aquí ")
    if region == "1":
        print(" Luis Miguel se presentará en el Palacio de los Deportes")
        print("Escoge la fecha")
        print("20 de enero del 2025 \n 21 de enero del 2025 \n 22 de enero de 2025")
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
                precio = 4279 * boletos
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
            else:
                print("La zona no está bien ecrita")
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
            else:
                print("La zona no está bien ecrita")
        else:
            print("El nivel está mal escrito")

        cotizacion = input("Deseas comprar los boletos? ")
        if cotizacion == "si":
            metododepago = input("Sería con débito o crédito? ")
            print("Ok! Serán " , boletos , " boletos para ir a ver a Luis Miguel en el palacio de los deportes el dia " , diasMon , " en la zona " , nivel,zona , " \n a un precio de $" ,precio , "en total")
        else:
            print("Gracias por recurrir a nosotros")
        aplicarciclo= input("Deseas buscar otro artista?")
        if aplicarciclo == "si":
            print("ciclo no se como")
        else:
            print("Ok")
    elif region == "2":
        print("Luis Miguel se presentará en el Auditorio Citibanamex")
        print("Escoge la fecha")
        print("11 de junio del 2025 \n 12 de junio del 2025 \n 13 de junio del 2025")
        diasMon = input("Escribe la fecha completa aquí ")
        print("Los niveles disponibles son: \n Beyond VIP \n Beyond \n Platinum \n B Platinum \n Perfiles \n Perfiles B \n Perfiles C" )
        nivel = input("escribe el nivel en el que deseas estar ")
        if nivel == "Beyond VIP":
            print("Las zonas disponibles son \n 1 \n 2 \n 3")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [1,2,3]:
                print("el precio por boleto sería de $4459")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 4459 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Beyond":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [1,2,3]:
                print("el precio por boleto sería de $4279")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 4279 * boletos
                print("Total: $", precio)
            elif zona in [4,5]:
                print("el precio por boleto sería de $3879")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3879 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Platinum":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(1,5):
                print("el precio por boleto sería de $3389")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3389 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "B Platinum":
            print("Las zonas disponibles son \n 6 \n 7")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [6,7]:
                print("el precio por boleto sería de $3159")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3159 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Perfiles":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(1,5):
                print("el precio por boleto sería de $2839")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 2839 * boletos
                print("Total: $", precio)
            elif zona in range(6,9):
                print("el precio por boleto sería de $2389")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 2389 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Perfiles B":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(1,3):
                print("el precio por boleto sería de $1599")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 1599 * boletos
                print("Total: $", precio)
            elif zona in range(4,7):
                print("el precio por boleto sería de $939")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 939 * boletos
                print("Total: $", precio)
            elif zona in [8,9]:
                print("el precio por boleto sería de $889")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 889 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Perfiles C":
            print("Las zonas disponibles son \n 10 \n 11")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [10,11]:
                print("el precio por boleto sería de $525")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 525 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        else:
            print("el nivel está mal escrito")

        cotizacion = input("Deseas comprar los boletos? ")
        if cotizacion == "si":
            metododepago = input("Sería con débito o crédito? ")
            print("Ok! Serán " , boletos , " boletos para ir a ver a Luis Miguel en el Auditorio Citibanamex el dia " , diasMon , " en la zona " , nivel,zona , " \n a un precio de $" ,precio , "en total")
        else:
            print("Gracias por recurrir a nosotros")
        aplicarciclo= input("Deseas buscar otro artista?")
        if aplicarciclo == "si":
            print("ciclo no se como")
        else:
            print("Ok")
    elif region == "3":
        print("Luis Miguel se presentará en el Auditorio Telmex")
        print("Escoge la fecha")
        print("6 de noviembre del 2025 \n 7 de noviembre del 2025 \n 8 de noviembre del 2025")
        diasMon = input("Escribe la fecha completa aquí ")
        print("Los niveles disponibles son: \n Platea \n Zona Roja \n Zona Azul \n Zona Café \n Zona Blanca \n Zona Verde \n Zona Lila \n Zona Naranja \n Zona Amarilla" )
        nivel = input("escribe el nivel en el que deseas estar ")
        if nivel == "Platea":
            print("el precio por boleto sería de $4459")
            boletos = int(input("Cuántos boletos deseas comprar? "))
            precio = 4459 * boletos
            print("Total: $", precio)
        elif nivel == "Zona Roja":
            print("Las zonas disponibles son \n 102 \n 103 \n 104")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [102,103,104]:
                print("el precio por boleto sería de $4279")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 4279 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Azul":
            print("Las zonas disponibles son \n 201 \n 202 \n 203")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [201,202,203]:
                print("el precio por boleto sería de $3629")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3629 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Café":
            print("Las zonas disponibles son \n 204 \n 205")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [204,205]:
                print("el precio por boleto sería de $3489")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3489 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Blanca":
            print("Las zonas disponibles son \n 401 \n 402 \n 403 \n 404 \n 405 \n 406 \n 407")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(401,407):
                print("el precio por boleto sería de $3099")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3099 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Verde":
            print("Las zonas disponibles son \n 301 \n 302")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [301,302]:
                print("el precio por boleto sería de $2749")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 2749 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Lila":
            print("Las zonas disponibles son \n 501 \n 502 \n 503 \n 504 \n 505 \n 506 \n 507")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(501,507):
                print("el precio por boleto sería de $1669")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 1669 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Naranja":
            print("Las zonas disponibles son \n 601 602 \n 603 604 \n 605 606 \n 607 608 \n 609 610 \n 611 612 \n 613")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(601,605):
                print("el precio por boleto sería de $1019")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 1019 * boletos
                print("Total: $", precio)
            elif zona in range(606,609):
                print("el precio por boleto sería de $829")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 829 * boletos
                print("Total: $", precio)
            elif zona in range(610,613):
                print("el precio por boleto sería de $959")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 959 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Amarillo":
            print("Las zonas disponibles son \n 701 \n 702 \n 703 \n 704 \n 705 \n 706")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(701,706):
                print("el precio por boleto sería de $789")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 789 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        else:
            print("El nivel está mal escrito")
        cotizacion = input("Deseas comprar los boletos? ")
        if cotizacion == "si":
            metododepago = input("Sería con débito o crédito? ")
            print("Ok! Serán " , boletos , " boletos para ir a ver a Luis Miguel en el Auditorio Telmex el dia " , diasMon , " en la zona " , nivel,zona , " \n a un precio de $" ,precio , "en total")
        else:
            print("Gracias por recurrir a nosotros")
        aplicarciclo= input("Deseas buscar otro artista?")
        if aplicarciclo == "si":
            print("ciclo no se como")
        else:
            print("Ok")

elif artista == "Twenty One Pilots":
    print("Selecciona tu región")
    print("presiona 1 para CDMX \n presiona 2 para Monterrey \n presiona 3 para Jalisco")
    region = input("Escribe el # aquí ")
    if region == "1":
        print("Twenty One Pilots se presentarán en el Palacio de los Deporte")
        print("Escoge la fecha")
        print("13 de septiembre del 2025 \n 14 de septiembre del 2025 \n 15 de septiembre de 2025")
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
                precio = 4279 * boletos
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
            else:
                print("La zona no está bien ecrita")
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
            else:
                print("La zona no está bien ecrita")
        else:
            print("El nivel está mal escrito")

        cotizacion = input("Deseas comprar los boletos? ")
        if cotizacion == "si":
            metododepago = input("Sería con débito o crédito? ")
            print("Ok! Serán " , boletos , " boletos para ir a ver a Twenty One Pilots en el palacio de los deportes el dia " , diasMon , " en la zona " , nivel,zona , " \n a un precio de $" ,precio , "en total")
        else:
            print("Gracias por recurrir a nosotros")
        aplicarciclo= input("Deseas buscar otro artista?")
        if aplicarciclo == "si":
            print("ciclo no se como")
        else:
            print("Ok")
    elif region == "2":
        print("Twenty One Pilots se presentarán en el Auditorio Citibanamex")
        print("Escoge la fecha")
        print("18 de julio del 2025 \n 19 de julio del 2025 \n 203 de julio del 2025")
        diasMon = input("Escribe la fecha completa aquí ")
        print("Los niveles disponibles son: \n Beyond VIP \n Beyond \n Platinum \n B Platinum \n Perfiles \n Perfiles B \n Perfiles C" )
        nivel = input("escribe el nivel en el que deseas estar ")
        if nivel == "Beyond VIP":
            print("Las zonas disponibles son \n 1 \n 2 \n 3")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [1,2,3]:
                print("el precio por boleto sería de $4459")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 4459 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Beyond":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [1,2,3]:
                print("el precio por boleto sería de $4279")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 4279 * boletos
                print("Total: $", precio)
            elif zona in [4,5]:
                print("el precio por boleto sería de $3879")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3879 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Platinum":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(1,5):
                print("el precio por boleto sería de $3389")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3389 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "B Platinum":
            print("Las zonas disponibles son \n 6 \n 7")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [6,7]:
                print("el precio por boleto sería de $3159")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3159 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Perfiles":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(1,5):
                print("el precio por boleto sería de $2839")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 2839 * boletos
                print("Total: $", precio)
            elif zona in range(6,9):
                print("el precio por boleto sería de $2389")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 2389 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Perfiles B":
            print("Las zonas disponibles son \n 1 \n 2 \n 3 \n 4 \n 5 \n 6 \n 7 \n 8 \n 9")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(1,3):
                print("el precio por boleto sería de $1599")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 1599 * boletos
                print("Total: $", precio)
            elif zona in range(4,7):
                print("el precio por boleto sería de $939")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 939 * boletos
                print("Total: $", precio)
            elif zona in [8,9]:
                print("el precio por boleto sería de $889")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 889 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Perfiles C":
            print("Las zonas disponibles son \n 10 \n 11")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [10,11]:
                print("el precio por boleto sería de $525")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 525 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        else:
            print("el nivel está mal escrito")

        cotizacion = input("Deseas comprar los boletos? ")
        if cotizacion == "si":
            metododepago = input("Sería con débito o crédito? ")
            print("Ok! Serán " , boletos , " boletos para ir a ver a Twenty One Pilots en el Auditorio Citibanamex el dia " , diasMon , " en la zona " , nivel,zona , " \n a un precio de $" ,precio , "en total")
        else:
            print("Gracias por recurrir a nosotros")
        aplicarciclo= input("Deseas buscar otro artista?")
        if aplicarciclo == "si":
            print("ciclo no se como")
        else:
            print("Ok")
    elif region == "3":
        print("Twenty One Pilots se presentarán en el Auditorio Telmex")
        print("Escoge la fecha")
        print("23 de septiembre del 2025 \n 24 de septiembre del 2025 \n 25 de septiembre del 2025")
        diasMon = input("Escribe la fecha completa aquí ")
        print("Los niveles disponibles son: \n Platea \n Zona Roja \n Zona Azul \n Zona Café \n Zona Blanca \n Zona Verde \n Zona Lila \n Zona Naranja \n Zona Amarilla" )
        nivel = input("escribe el nivel en el que deseas estar ")
        if nivel == "Platea":
            print("el precio por boleto sería de $4459")
            boletos = int(input("Cuántos boletos deseas comprar? "))
            precio = 4459 * boletos
            print("Total: $", precio)
        elif nivel == "Zona Roja":
            print("Las zonas disponibles son \n 102 \n 103 \n 104")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [102,103,104]:
                print("el precio por boleto sería de $4279")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 4279 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Azul":
            print("Las zonas disponibles son \n 201 \n 202 \n 203")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [201,202,203]:
                print("el precio por boleto sería de $3629")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3629 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Café":
            print("Las zonas disponibles son \n 204 \n 205")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [204,205]:
                print("el precio por boleto sería de $3489")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3489 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Blanca":
            print("Las zonas disponibles son \n 401 \n 402 \n 403 \n 404 \n 405 \n 406 \n 407")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(401,407):
                print("el precio por boleto sería de $3099")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 3099 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Verde":
            print("Las zonas disponibles son \n 301 \n 302")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in [301,302]:
                print("el precio por boleto sería de $2749")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 2749 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Lila":
            print("Las zonas disponibles son \n 501 \n 502 \n 503 \n 504 \n 505 \n 506 \n 507")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(501,507):
                print("el precio por boleto sería de $1669")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 1669 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Naranja":
            print("Las zonas disponibles son \n 601 602 \n 603 604 \n 605 606 \n 607 608 \n 609 610 \n 611 612 \n 613")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(601,605):
                print("el precio por boleto sería de $1019")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 1019 * boletos
                print("Total: $", precio)
            elif zona in range(606,609):
                print("el precio por boleto sería de $829")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 829 * boletos
                print("Total: $", precio)
            elif zona in range(610,613):
                print("el precio por boleto sería de $959")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 959 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        elif nivel == "Zona Amarillo":
            print("Las zonas disponibles son \n 701 \n 702 \n 703 \n 704 \n 705 \n 706")
            zona = int(input("Escribe el número de zona en la que deseas estar "))
            if zona in range(701,706):
                print("el precio por boleto sería de $789")
                boletos = int(input("Cuántos boletos deseas comprar? "))
                precio = 789 * boletos
                print("Total: $", precio)
            else:
                print("La zona no está bien escrita")
        else:
            print("El nivel está mal escrito")
        cotizacion = input("Deseas comprar los boletos? ")
        if cotizacion == "si":
            metododepago = input("Sería con débito o crédito? ")
            print("Ok! Serán " , boletos , " boletos para ir a ver a Twenty One Pilots en el Auditorio Telmex el dia " , diasMon , " en la zona " , nivel,zona , " \n a un precio de $" ,precio , "en total")
        else:
            print("Gracias por recurrir a nosotros")
        aplicarciclo= input("Deseas buscar otro artista?")
        if aplicarciclo == "si":
            print("ciclo no se como")
        else:
            print("Ok")

else:
    print("lo siento, no conozco ese artista")

