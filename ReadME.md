# ML Text Preprocessing API

Microservizio REST sviluppato con **FastAPI** per la normalizzazione e l'analisi di testi.
Il progetto simula un componente di una pipeline ML, separando la logica di business (TextProcessor) dall'interfaccia web.

## Struttura del Progetto

```text
ml-text-api/
├── app/
│   ├── main.py          # Entry point API e gestione rotte
│   └── processor.py     # Logica di Business (Text Cleaning)
├── Dockerfile           # Configurazione container
├── requirements.txt     # Dipendenze Python
└── README.md            # Documentazione
```

##  Funzionalità

* **Pulizia Testo:** Rimozione caratteri speciali, normalizzazione spazi, lowercase.
* **Analisi:** Conteggio parole e caratteri.
* **Sicurezza:** Autenticazione tramite API Key header.
* **Fault Tolerance:** Validazione input rigorosa tramite Pydantic.
* **Containerizzazione:** Docker ready.

##  Requisiti

* Python 3.10+
* Docker (Opzionale)

##  Installazione ed Esecuzione

### Metodo 1: Docker (Consigliato)
Il modo più veloce per avviare il servizio senza configurare l'ambiente locale.

```bash
# 1. Costruisci l'immagine
docker build -t ml-api-image .

# 2. Avvia il container sulla porta 8000
docker run -d -p 8000:8000 --name ml-container ml-api-image
```
### Metodo 2: Sviluppo Locale
Se vuoi modificare il codice o eseguire il progetto senza container:

```bash
# 1. Crea e attiva l'ambiente virtuale
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate

# 2. Installa le dipendenze
pip install -r requirements.txt

# 3. Avvia il server
uvicorn app.main:app --reload

```

```markdown
## Utilizzo e Sicurezza

L'API è protetta tramite autenticazione Header.
Ogni richiesta deve includere l'header `access_token`.

* **Chiave Demo:** `super-segreto-123`
* **URL Base:** `http://127.0.0.1:8000`

### Esempio di chiamata (cURL)
Puoi testare l'endpoint `/process` dal terminale:

```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/process](http://127.0.0.1:8000/process)' \
  -H 'accept: application/json' \
  -H 'access_token: super-segreto-123' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Ciao!!! Ho vinto 1000 euro.",
  "remove_digits": true
}'

```

```markdown
## Documentazione Interattiva

Una volta avviato il server, puoò esplorare e testare le API direttamente dal browser:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)