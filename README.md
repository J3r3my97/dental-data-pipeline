# fast-app-template
A template for spinning up a FastAPI app with Docker support

## Quick Start

### Using Docker (Recommended)
```bash
# Build and run with Docker Compose
docker-compose up --build

# Or run with plain Docker
docker build -t fast-app .
docker run -p 8000:8000 fast-app
```

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run the app
python run.py
```

## API Endpoints
- `GET /` - Hello World
- `GET /health` - Health check

The app will be available at http://localhost:8000
