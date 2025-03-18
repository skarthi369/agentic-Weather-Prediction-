import requests
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import json
import os
import matplotlib.dates as mdates

class TNWeatherAgent:
    def __init__(self, latitude=13.0827, longitude=80.2707, city="Chennai"):
        """Initialize the weather prediction agent for Tamil Nadu cities."""
        self.latitude = latitude
        self.longitude = longitude
        self.city = city
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        self.data_dir = "data"
        
        # Create data directory if it doesn't exist
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def get_current_weather(self):
        """Fetch current weather data from Open-Meteo API."""
        url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&current_weather=true"
        try:
            response = requests.get(url)
            data = response.json()
            return {
                'temperature': data['current_weather']['temperature'],
                'windspeed': data['current_weather']['windspeed'],
                'time': data['current_weather']['time']
            }
        except Exception as e:
            print(f"Error fetching current weather: {str(e)}")
            return None

    def get_historical_weather(self, days=7):
        """Fetch historical weather data for the past specified days."""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&hourly=temperature_2m,windspeed_10m&start_date={start_date.strftime('%Y-%m-%d')}&end_date={end_date.strftime('%Y-%m-%d')}"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            # Convert to DataFrame
            df = pd.DataFrame({
                'time': pd.to_datetime(data['hourly']['time']),
                'temperature': data['hourly']['temperature_2m'],
                'windspeed': data['hourly']['windspeed_10m']
            })
            
            # Resample to daily values
            daily_data = df.set_index('time').resample('D').agg({
                'temperature': 'mean',
                'windspeed': 'mean'
            }).reset_index()
            
            return daily_data
        except Exception as e:
            print(f"Error fetching historical weather: {str(e)}")
            return None

    def prepare_features(self, data):
        """Prepare features for the prediction model."""
        if data is None or len(data) < 2:
            return None, None
        
        # Create features (previous day's weather)
        X = data[['temperature', 'windspeed']].values[:-1]
        y = data['temperature'].values[1:]  # Next day's temperature
        
        return X, y

    def train_model(self, X, y):
        """Train the prediction model."""
        if X is None or y is None:
            return False
        
        try:
            # Scale features
            X_scaled = self.scaler.fit_transform(X)
            
            # Train model
            self.model.fit(X_scaled, y)
            return True
        except Exception as e:
            print(f"Error training model: {str(e)}")
            return False

    def predict_tomorrow_temperature(self):
        """Predict tomorrow's temperature."""
        try:
            # Get historical data
            historical_data = self.get_historical_weather()
            if historical_data is None:
                return None
            
            # Prepare features and train model
            X, y = self.prepare_features(historical_data)
            if not self.train_model(X, y):
                return None
            
            # Get current weather for prediction
            current_weather = self.get_current_weather()
            if current_weather is None:
                return None
            
            # Prepare current weather features
            current_features = np.array([[
                current_weather['temperature'],
                current_weather['windspeed']
            ]])
            
            # Scale and predict
            current_features_scaled = self.scaler.transform(current_features)
            prediction = self.model.predict(current_features_scaled)[0]
            
            return {
                'current_temp': current_weather['temperature'],
                'predicted_temp': prediction,
                'city': self.city,
                'prediction_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:
            print(f"Error making prediction: {str(e)}")
            return None

    def plot_temperature_trend(self, save_path=None):
        """Plot temperature trend and prediction."""
        try:
            historical_data = self.get_historical_weather()
            if historical_data is None:
                return None
            
            prediction_result = self.predict_tomorrow_temperature()
            if prediction_result is None:
                return None
            
            # Create plot
            fig, ax = plt.subplots(figsize=(12, 6))
            
            # Plot historical data
            dates = mdates.date2num(historical_data['time'].dt.to_pydatetime())
            ax.plot_date(dates, historical_data['temperature'], 
                        fmt='o-', label='Historical Temperature')
            
            # Add prediction point
            tomorrow = mdates.date2num(datetime.now() + timedelta(days=1))
            ax.plot_date([tomorrow], [prediction_result['predicted_temp']], 
                        fmt='ro', markersize=10, label='Predicted Temperature')
            
            # Format x-axis
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            ax.set_title(f'Temperature Trend and Prediction for {self.city}')
            ax.set_xlabel('Date')
            ax.set_ylabel('Temperature (°C)')
            ax.legend()
            ax.grid(True)
            
            # Rotate x-axis labels for better readability
            ax.tick_params(axis='x', rotation=45)
            
            # Adjust layout
            fig.tight_layout()
            
            if save_path:
                fig.savefig(save_path)
                plt.close(fig)
                return None
                
            return fig
        except Exception as e:
            print(f"Error plotting temperature trend: {str(e)}")
            return None

    def save_prediction(self, prediction):
        """Save prediction results to a JSON file."""
        if prediction is None:
            return False
        
        try:
            filename = os.path.join(self.data_dir, f"{self.city.lower()}_predictions.json")
            
            # Load existing predictions if file exists
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    predictions = json.load(f)
            else:
                predictions = []
            
            # Add new prediction
            predictions.append({
                **prediction,
                'prediction_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
            # Save to file
            with open(filename, 'w') as f:
                json.dump(predictions, f, indent=4)
            
            return True
        except Exception as e:
            print(f"Error saving prediction: {str(e)}")
            return False

if __name__ == "__main__":
    # Example usage
    agent = TNWeatherAgent()
    prediction = agent.predict_tomorrow_temperature()
    
    if prediction:
        print("\nPrediction Results:")
        print(f"City: {prediction['city']}")
        print(f"Current Temperature: {prediction['current_temp']}°C")
        print(f"Predicted Temperature for Tomorrow: {prediction['predicted_temp']:.1f}°C")
        
        # Save prediction
        agent.save_prediction(prediction)
        
        # Plot and save temperature trend
        agent.plot_temperature_trend(save_path="temperature_trend.png") 