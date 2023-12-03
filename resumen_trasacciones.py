from transaccion import ProcesadorCSV


archivo_csv = "transacciones.csv"
procesador = ProcesadorCSV(archivo_csv)
procesador.cargar_transacciones()

resumen = procesador.generar_resumen()

# Mostrar el resumen
"""print(f"El saldo total es {resumen['Saldo total']:.2f}")

for mes, num_transacciones in resumen['Número de transacciones por mes'].items():
    print(f"Número de transacciones en {mes}: {num_transacciones}")

for mes, monto_promedio in resumen['Monto promedio del crédito por mes'].items():
    print(f"Monto promedio del crédito en {mes}: {monto_promedio:.2f}")

for mes, monto_promedio in resumen['Monto promedio del débito por mes'].items():
    print(f"Monto promedio del débito en {mes}: {monto_promedio:.2f}")

print(f"Importe medio del débito: {resumen['Importe medio del débito']:.2f}")"""


def generar_resumen_texto(resumen):
    texto_resumen = f"El saldo total es {resumen['Saldo total']:.2f}\n\n"

    for mes, num_transacciones in resumen['Número de transacciones por mes'].items():
        texto_resumen += f"Número de transacciones en {mes}: {num_transacciones}\n"

    for mes, monto_promedio in resumen['Monto promedio del crédito por mes'].items():
        texto_resumen += f"Monto promedio del crédito en {mes}: {monto_promedio:.2f}\n"

    for mes, monto_promedio in resumen['Monto promedio del débito por mes'].items():
        texto_resumen += f"Monto promedio del débito en {mes}: {monto_promedio:.2f}\n"

    texto_resumen += f"Importe medio del débito: {resumen['Importe medio del débito']:.2f}\n"

    return texto_resumen

# Define email sender and receiver
email_sender = "http.joshua@gmail.com"
email_password = "outesihfvwdblmdc"
print(email_password)
email_receiver = input("Escribe el correo electronico del destinatario")


subject = 'Resumen general se su cuenta'

# Crear una instancia del procesador
archivo_csv = "transacciones.csv"
procesador = ProcesadorCSV(archivo_csv)
procesador.cargar_transacciones()

# Generar el resumen
resumen = procesador.generar_resumen()
# Crear el cuerpo del correo con el resumen
body = generar_resumen_texto(resumen)

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

