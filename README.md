# Flask Hello World App

This is a simple Flask web application for DevOps practice.

## Features
- `/` : Returns a welcome message.
- `/time` : Returns the current server time.

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation
1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

2. Run the app:
   ```powershell
   python app.py
   ```

3. Open your browser and visit:
   - http://localhost:5000
   - http://localhost:5000/time

### Docker
To run the app in Docker:
```powershell
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

## Deployment
You can deploy this app to free cloud platforms like Render, Railway, or Fly.io.

## License
This project is for learning and demonstration purposes.
