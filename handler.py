import json
import boto3
from transaccion import ProcesadorCSV, generar_resumen_texto, enviar_correo

def lambda_handler(event, context):
    # Crear una instancia del procesador
    archivo_csv = "transacciones.csv"
    procesador = ProcesadorCSV(archivo_csv)
    procesador.cargar_transacciones()

    # Generar el resumen
    resumen = procesador.generar_resumen()

    # Obtener la dirección de correo electrónico del destinatario desde el evento de Lambda
    email_receiver = event.get('email_receiver')

    # Verificar si la dirección de correo electrónico es proporcionada
    if not email_receiver:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: La dirección de correo electrónico del destinatario no está proporcionada.')
        }

    # Llamar a la función para enviar el correo
    enviar_correo(resumen, email_receiver)

    return {
        'statusCode': 200,
        'body': json.dumps('Correo electrónico enviado exitosamente.')
    }
