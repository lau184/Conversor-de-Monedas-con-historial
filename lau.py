import datetime

tas_cambios= {
  "USD": {"EUR": 0.92, "ARS": 880.00, "BRL": 5.10},
    "EUR": {"USD": 1.09, "ARS": 950.00, "BRL": 5.50},
    "ARS": {"USD": 0.0011, "EUR": 0.00105, "BRL": 0.0058},
    "BRL": {"USD": 0.20, "EUR": 0.18, "ARS": 172.00}
}
money = ["USD", "EUR", "ARS", "BRL"]

def vali_money(moneda):
    return moneda.upper() in monedas
  
def vali_monto(monto):
    try:
        valor = float(monto)
        return valor > 0
    except ValueError:
        return False

def convrti(monto, origen, destino):
    if origen == destino:
        return monto
    tasa = tas_cambio[origen][destino]
    return monto * tasa
  
def se_guarda_historial(monto, origen, destino, resultado):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{fecha_hora} - {monto} {origen} → {resultado:.2f} {destino}\n"
    with open("historial.txt", "a") as archivo:
        archivo.write(linea)

def istorial():
    try:
        with open("historial.txt", "r") as archivo:
            print("\n--- Historial de conversiones ---")
            print(archivo.read())
    except FileNotFoundError:
        print("Todavía no hay historial guardado.")

def menu():
    while True:
        print("\nConversor de Monedas")
        print("1 Convertir monedas")
        print("2 Ver historial")
        print("3 Borrar historial")
        print("4 Salir")
        opcion = input("Elegí una opción (1-4): ")

        if opcion == "1":
    origen = input("Moneda de origen (USD, EUR, ARS, BRL): ").upper()
    destino = input("Moneda de destino (USD, EUR, ARS, BRL): ").upper()
    monto = input("Monto a convertir: ")

    if origen not in monedas or destino not in monedas:
        print("Tenés que elegir monedas válidas.")
    elif not monto.replace(".", "", 1).isdigit() or float(monto) <= 0:
        print("El monto debe ser un número positivo.")
    else:
        monto = float(monto)
        resultado = convertir(monto, origen, destino)
        print(f"Resultado: {resultado:.2f} {destino}")
        guardar_en_historial(monto, origen, destino, resultado)

  menu()
