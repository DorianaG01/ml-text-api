# ML Text Preprocessing API

REST microservice developed with **FastAPI** for text normalization and analysis.
The project simulates a component of a Machine Learning pipeline, separating the TextProcessor logic from the web interface.

## Project Structure

```text
ml-text-api/
├── app/
│   ├── main.py          # API Entry point and route handling
│   └── processor.py     # Business Logic (Text Cleaning)
├── Dockerfile           # Container configuration
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
```

## Features

* **Text Cleaning:** Removal of special characters, whitespace normalization, lowercase.
* **Analysis:** Word and character count.
* **Security:** Authentication via API Key header.
* **Fault Tolerance:** Input validation via Pydantic.
* **Containerization:** Docker ready.

## Requirements

* Python 3.10+
* Docker (Optional)

## Installation and Execution

### Method 1: Docker

```bash
# 1. Build the image
docker build -t ml-api-image .

# 2. Run the container on port 8000
docker run -d -p 8000:8000 --name ml-container ml-api-image
```

### Method 2: Local Development

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
uvicorn app.main:app --reload
```

## Usage and Security

The API is protected via Header authentication.
Every request must include the `access_token` header.

* **Demo Key:** `super-segreto-123`
* **Base URL:** `http://127.0.0.1:8000`

### Example Request (cURL)
You can test the `/process` endpoint from the terminal:

```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/process](http://127.0.0.1:8000/process)' \
  -H 'accept: application/json' \
  -H 'access_token: super-segreto-123' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Hello!!! I won 1000 euros.",
  "remove_digits": true
}'
```

## Interactive Documentation

Once the server is running, you can explore and test the API directly from the browser:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
