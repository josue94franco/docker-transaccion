from transaccion import ProcesadorCSV


archivo_csv = "transacciones.csv"
procesador = ProcesadorCSV(archivo_csv)
procesador.cargar_transacciones()

resumen = procesador.generar_resumen()

# Mostrar el resumen
print(f"El saldo total es {resumen['Saldo total']:.2f}")

for mes, num_transacciones in resumen['Número de transacciones por mes'].items():
    print(f"Número de transacciones en {mes}: {num_transacciones}")

for mes, monto_promedio in resumen['Monto promedio del crédito por mes'].items():
    print(f"Monto promedio del crédito en {mes}: {monto_promedio:.2f}")

for mes, monto_promedio in resumen['Monto promedio del débito por mes'].items():
    print(f"Monto promedio del débito en {mes}: {monto_promedio:.2f}")

print(f"Importe medio del débito: {resumen['Importe medio del débito']:.2f}")






