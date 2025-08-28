# Crypto Alert System

Real-time cryptocurrency price monitoring and alert system built with FastAPI.

**Live API**: https://crypto-alerts-dfwo.onrender.com

## Features

- 🔐 User registration and management
- 📊 Real-time price monitoring via Binance API
- 🔔 Price alerts (above/below targets)
- 🚀 RESTful API with automatic documentation
- 💾 SQLite database with SQLAlchemy ORM
- 🔄 Background tasks with Celery + Redis
- 🐳 Docker Compose orchestration
- ✅ CI/CD with GitHub Actions

## Tech Stack

- **Backend**: FastAPI (Python 3.10)
- **Database**: SQLAlchemy + SQLite
- **Queue**: Celery + Redis
- **Container**: Docker
- **Deploy**: Render
- **CI/CD**: GitHub Actions
## Quick Start

### Local Development

```bash
# Clone repository
git clone https://github.com/DemirSacirovic/crypto-alerts.git
cd crypto-alerts

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run with Docker Compose
docker-compose up -d

# Or run directly
uvicorn app.main:app --reload

API Endpoints

- GET / - API status
- GET /health - Health check
- GET /docs - Swagger documentation
- POST /api/users/ - Create user
- GET /api/users/ - List users
- POST /api/alerts/ - Create price alert
- GET /api/alerts/ - List alerts

# Create alert
curl -X POST https://crypto-alerts-dfwo.onrender.com/api/alerts/ \
  -H "Content-Type: application/json" \
  -d '{"symbol":"btcusdt","target_price":150000,"alert_type":"above"}'

Project Structure
app/
├── api/          # API endpoints
├── models/       # Database models
├── schemas/      # Pydantic schemas
├── services/     # Business logic
├── tasks.py      # Celery tasks
└── main.py       # Application entry

Author

Demir Sacirovic - https://github.com/DemirSacirovic
