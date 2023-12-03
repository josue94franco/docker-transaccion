# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias del proyecto
#RUN pip install --no-cache-dir -r requirements.txt  # Si tienes un archivo requirements.txt

# Define el comando predeterminado para ejecutar tu aplicación
CMD ["python", "main.py"]

#para ejecutar el docker: 
# Se crea el contenerdor --> build -t transaccion1 .
#Se ejecuta el contenedor --> docker run -it transaccion1