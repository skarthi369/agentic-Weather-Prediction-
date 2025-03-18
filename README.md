# Tamil Nadu Weather Prediction 🌡️

A machine learning-powered weather prediction system for major cities in Tamil Nadu, India. This application uses historical weather data and current conditions to predict tomorrow's temperature.

## Features

- Real-time weather data from Open-Meteo API
- Machine learning-based temperature predictions
- Interactive web interface with Streamlit
- Support for major Tamil Nadu cities:
  - Chennai
  - Coimbatore
  - Madurai
  - Tiruchirappalli
  - Salem
- Historical temperature trends and visualization
- Prediction history tracking

## Setup Instructions

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Linux/Mac
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

The app will automatically open in your default web browser. If it doesn't, navigate to the URL shown in the terminal (usually http://localhost:8501).

## How it Works

The application:
1. Fetches current weather data for the selected city using the Open-Meteo API
2. Retrieves historical weather data for the past 7 days
3. Uses a Linear Regression model to predict tomorrow's temperature
4. Displays the prediction along with historical trends and previous predictions

## Project Structure

```
tnpredict/
├── app.py              # Streamlit web interface
├── weather_agent.py    # Weather prediction agent
├── requirements.txt    # Project dependencies
├── README.md          # Documentation
└── data/              # Directory for storing prediction history
    └── *_predictions.json
```

## Data Sources

- Real-time and historical weather data from Open-Meteo API
- No API key required
- Data includes:
  - Temperature
  - Wind speed
  - Historical trends

## Model Details

The prediction model uses:
- Linear Regression for temperature prediction
- Feature scaling for better accuracy
- Historical weather patterns
- Current weather conditions

## Requirements

- Python 3.7+
- Internet connection (for real-time weather data)
- Required packages listed in requirements.txt

## Future Enhancements

- Support for more Tamil Nadu cities
- Additional weather parameters (humidity, precipitation)
- More advanced prediction models
- Mobile-responsive design
- API endpoint for predictions

                                 +----------------+
                                 |  User Request  |
                                 +----------------+
                                        ↓
                    +------------------------------------+
                    |        City Selection Input         |
                    +------------------------------------+
                                        ↓
            +------------------------------------------------+
            |                 Weather Agent                    |
            |  +----------------+        +----------------+    |
            |  | Current Weather|        |Historical Data |    |
            |  | API Request    |        |API Request     |    |
            |  +----------------+        +----------------+    |
            +------------------------------------------------+
                           ↓                      ↓
            +----------------+            +----------------+
            |  Current Data  |            |Historical Data |
            +----------------+            +----------------+
                           ↓                      ↓
            +------------------------------------------------+
            |              Feature Engineering               |
            | - Data Preprocessing                          |
            | - Feature Scaling                             |
            | - Time Series Preparation                     |
            +------------------------------------------------+
                                        ↓
            +------------------------------------------------+
            |              Prediction Engine                  |
            | - Linear Regression Model                      |
            | - Model Training                               |
            | - Temperature Prediction                       |
            +------------------------------------------------+
                                        ↓
            +------------------------------------------------+
            |              Results Processing                 |
            | - Prediction Storage                           |
            | - Visualization Generation                     |
            | - Metrics Calculation                          |
            +------------------------------------------------+
                                        ↓
                    +------------------------------------+
                    |        User Interface Display       |
                    | - Current Weather                   |
                    | - Prediction Results                |
                    | - Historical Trends                 |
                    | - Previous Predictions              |
                    +------------------------------------+
