import smtplib
import ssl
from email.message import EmailMessage
#mport os
from transaccion import ProcesadorCSV
from resumen_trasacciones import generar_resumen_texto

texto_resumen = generar_resumen_texto()


# Define email sender and receiver
email_sender = "http.joshua@gmail.com"
email_password = "outesihfvwdblmdc"
print(email_password)
email_receiver = input("Escribe el correo electronico del destinatario")


# Set the subject and body of the email
subject = 'Resumen general se su cuenta'
#body = """procesador.generar_resumen_texto(resumen)"""
# Crear el cuerpo del correo con el resumen
body = generar_resumen_texto(texto_resumen)

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