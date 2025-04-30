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
