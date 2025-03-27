# Usamos Python como base
FROM python:3.12.4

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir --upgrade pip \
    && pip install -r requirements.txt

# Exponer el puerto en el que correrá Django
EXPOSE 8000

# Comando para ejecutar Django con runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
