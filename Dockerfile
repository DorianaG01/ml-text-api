# 1. BASE IMAGE: Partiamo da una versione leggera di Linux con Python 3.10
FROM python:3.10-slim

# 2. WORKDIR: Creiamo una cartella di lavoro dentro il container
WORKDIR /code

# 3. CACHING: Copiamo PRIMA solo i requirements
# Trucco da Senior: Se cambi il codice ma non le librerie, 
# Docker salta questo passaggio e la build è istantanea.
COPY ./requirements.txt /code/requirements.txt

# 4. INSTALL: Installiamo le dipendenze
# --no-cache-dir serve a mantenere l'immagine leggera
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. COPY CODE: Copiamo tutto il resto del codice dentro il container
COPY ./app /code/app

# 6. CMD: Il comando di avvio
# Attenzione a "0.0.0.0": serve per dire "accetta connessioni anche da fuori dal container"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]