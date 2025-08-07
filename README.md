  # Crypto Alert System

  Real-time cryptocurrency price monitoring and alert system built with FastAPI.

  ## Features

  - 🔐 User registration and management
  - 📊 Real-time price monitoring via Binance WebSocket
  - 🔔 Price alerts (above/below targets)
  - 🚀 RESTful API with automatic documentation
  - 💾 SQLite database with SQLAlchemy ORM

  ## Tech Stack

  - **Backend**: FastAPI (Python 3.13)
  - **Database**: SQLAlchemy + SQLite
  - **WebSocket**: Binance streaming API
  - **Validation**: Pydantic

  ## Installation

  1. Clone the repository:
  ```bash
  git clone https://github.com/DemirSacirovic/crypto-alerts.git
  cd crypto-alerts

  2. Create virtual environment:
  python -m venv venv
  source venv/bin/activate  # Linux/Mac

  3. Install dependencies:
  pip install -r requirements.txt

  4. Run the application:
  uvicorn app.main:app --reload

  5. Open browser: http://localhost:8000/docs

  API Endpoints

  - POST /api/users/ - Create user
  - GET /api/users/ - List users
  - POST /api/alerts/ - Create price alert
  - GET /api/alerts/ - List alerts
  - GET /api/prices/current/{symbol} - Get current price

  Example Usage

  Create a price alert:
  POST /api/alerts/
  {
    "symbol": "BTCUSDT",
    "target_price": 50000,
    "alert_type": "above"
  }

  Project Structure

  app/
  ├── api/          # API endpoints
  ├── models/       # Database models
  ├── schemas/      # Pydantic schemas
  ├── services/     # Business logic
  └── main.py       # Application entry

  Future Improvements

  - Email notifications
  - Multiple cryptocurrency pairs
  - Historical price charts
  - User authentication with JWT

  Author

  Demir Sacirovic - https://github.com/DemirSacirovic
