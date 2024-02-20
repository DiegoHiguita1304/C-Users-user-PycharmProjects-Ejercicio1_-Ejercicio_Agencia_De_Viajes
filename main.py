def Agencia_De_Viajes():
    total_Guajira = 0
    total_Chicamocha = 0
    total_Llanos = 0
    total_Adultos = 0
    total_Niños = 0
    total_Dinero = 0

    while True:
        print("------------------------------------------------------")
        nombre_cliente = input("Ingrese el nombre del cliente (o 'fin' para terminar): ")
        if nombre_cliente.lower() == 'fin':
            break

        Destino = input("Ingrese el destino del Cliente (Guajira, Chicamocha o Llanos Orientales): ").lower()
        total_Adultos = int(input("Ingrese el número de personas Adultas: "))
        total_Niños = int(input("Ingrese el número de Niños: "))

        Precios = {
            'guajira': {'adultos': 1450000, 'niños': 870000},
            'chicamocha': {'adultos': 1600000, 'niños': 960000},
            'llanos orientales': {'adultos': 1200000, 'niños': 720000}
        }

        Precios_Destino = Precios[Destino]

        subtotal = total_Adultos * Precios_Destino['adultos'] + total_Niños * Precios_Destino['niños']
        print("Subtotal:", subtotal)
        print("------------------------------------------------------")

        if Destino == 'guajira':
            total_Guajira += subtotal
        elif Destino == 'chicamocha':
            total_Chicamocha += subtotal
        elif Destino == 'Llanos Orientales':
            total_Llanos += subtotal
        else:
            print("Destino no válido.")

        # Cotización

        print("----------------------------------------")
        print(f"\nNombre del Cliente: {nombre_cliente}")
        print(f"Destino: {Destino}")
        print(f"Nro Personas Adultas:  {total_Adultos}")
        print(f"Nro Niños: {total_Niños}")
        print(f"Subtotal: {subtotal}")
        print("------------------------------------------------------")

        #Totales
        total_Adultos =+ total_Adultos
        total_Niños =+ total_Niños
        total_Dinero += subtotal

    # Impresión de totales al finalizar
    print("\nResumen:")
    print("--------------------------------------------------")
    print(f"Cantidad de personas que viajan para la Guajira:  {total_Adultos + total_Niños} ")
    print(f"Cantidad de personas que viajan para Cañón del Chicamocha: {total_Adultos + total_Niños}")
    print(f"Cantidad de personas que viajan para los Llanos Orientales: {total_Adultos + total_Niños}")
    print(f"Total, de dinero de los viajes para la Guajira: {total_Guajira}")
    print(f"Total, de dinero de los viajes para Cañón del Chicamocha: {total_Chicamocha}")
    print(f"Total, de dinero de los viajes para los Llanos Orientales: {total_Llanos}")
    print(f"Total, de personas Adultas: {total_Adultos}")
    print(f"Total, de Niños {total_Niños}")
    print(f"Total, de Dinero de todos los destinos {total_Dinero}")
    print("--------------------------------------------------")

if __name__ == '__main__':
    Agencia_De_Viajes()
