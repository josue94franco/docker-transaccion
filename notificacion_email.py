import smtplib
import ssl
import base64
from email.message import EmailMessage
from transaccion import ProcesadorCSV

# Crear una instancia del procesador
archivo_csv = "transacciones.csv"
procesador = ProcesadorCSV(archivo_csv)
procesador.cargar_transacciones()

# Generar el resumen
resumen = procesador.generar_resumen()

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

def enviar_correo(resumen, email_receiver):
    # Define email sender and receiver
    email_sender = "http.joshua@gmail.com"
    email_password = "outesihfvwdblmdc"
    
    # Extraer el nombre antes del símbolo '@'
    email_receiver_name = email_receiver.split('@')[0]
    # Set the subject and body of the email
    subject = 'Resumen general de su cuenta y logotipo'
    
    # Ruta del archivo del logotipo
    logotipo = 'Bank.png'
    # Leer el contenido del logotipo como bytes y codificarlo en base64
    with open(logotipo, 'rb') as imagen:
        contenido_base64 = base64.b64encode(imagen.read()).decode('utf-8')
        
    # Crear el cuerpo del correo con el resumen y el logotipo
    #body = generar_resumen_texto(resumen)
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Estilo para la imagen */
            img {{
                width: 100px; /* Ajusta este valor según sea necesario */
                height: auto; /* Esto asegura que la altura se ajuste automáticamente para mantener la proporción original */
            
            /* Estilo para el encabezado h1 */
            h1 {{
                font-size: 15px; /* Ajusta este valor según sea necesario */
            }}
            }}
        </style>
    </head>
    <body>
        <h1>Hola {email_receiver_name} - Resumen de cuenta y logotipo</h1>
        <p>{generar_resumen_texto(resumen)}</p>
        <img src="data:image/png;base64, {contenido_base64}" alt="Logo">
    </body>
    </html>
    """
    # Create EmailMessage instance
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body, subtype='html') # Establecer el cuerpo del mensaje como HTML

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
# Llamar a la función para enviar el correo
email_receiver = input("Escribe el correo electronico del destinatario: ")
enviar_correo(resumen, email_receiver)
    