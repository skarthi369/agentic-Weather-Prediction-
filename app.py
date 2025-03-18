import streamlit as st
import pandas as pd
from weather_agent import TNWeatherAgent
from datetime import datetime
import os
import json
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="TN Weather Prediction",
    page_icon="🌡️",
    layout="wide"
)

# Tamil Nadu major cities with their coordinates
TN_CITIES = {
    "Chennai": (13.0827, 80.2707),
    "Coimbatore": (11.0168, 76.9558),
    "Madurai": (9.9252, 78.1198),
    "Tiruchirappalli": (10.7905, 78.7047),
    "Salem": (11.6643, 78.1460)
}

def load_previous_predictions(city):
    """Load previous predictions for the selected city."""
    filename = f"data/{city.lower()}_predictions.json"
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def main():
    # Header
    st.title("🌡️ Tamil Nadu Weather Prediction")
    st.write("Predict tomorrow's temperature for major cities in Tamil Nadu")

    # Sidebar
    st.sidebar.title("Settings")
    selected_city = st.sidebar.selectbox(
        "Select City",
        list(TN_CITIES.keys())
    )

    # Create agent for selected city
    lat, lon = TN_CITIES[selected_city]
    agent = TNWeatherAgent(latitude=lat, longitude=lon, city=selected_city)

    # Main content
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Current Weather")
        current_weather = agent.get_current_weather()
        
        if current_weather:
            st.metric(
                "Temperature",
                f"{current_weather['temperature']}°C"
            )
            st.metric(
                "Wind Speed",
                f"{current_weather['windspeed']} km/h"
            )
        else:
            st.error("Unable to fetch current weather data")

    with col2:
        st.subheader("Temperature Prediction")
        if st.button("Predict Tomorrow's Temperature"):
            with st.spinner("Making prediction..."):
                prediction = agent.predict_tomorrow_temperature()
                
                if prediction:
                    st.metric(
                        "Predicted Temperature",
                        f"{prediction['predicted_temp']:.1f}°C",
                        delta=f"{prediction['predicted_temp'] - prediction['current_temp']:.1f}°C"
                    )
                    
                    # Save prediction
                    agent.save_prediction(prediction)
                else:
                    st.error("Unable to make prediction")

    # Historical Data and Trend
    st.subheader("Temperature Trend")
    historical_data = agent.get_historical_weather()
    
    if historical_data is not None:
        # Plot temperature trend
        fig = agent.plot_temperature_trend()
        if fig is not None:
            st.pyplot()
            plt.close(fig)  # Clean up the figure
        else:
            st.error("Unable to generate temperature trend plot")

    # Previous Predictions
    st.subheader("Previous Predictions")
    previous_predictions = load_previous_predictions(selected_city)
    
    if previous_predictions:
        df = pd.DataFrame(previous_predictions)
        df['prediction_time'] = pd.to_datetime(df['prediction_time'])
        df = df.sort_values('prediction_time', ascending=False)
        
        st.dataframe(
            df[['prediction_time', 'current_temp', 'predicted_temp']].rename(columns={
                'prediction_time': 'Time',
                'current_temp': 'Actual Temperature (°C)',
                'predicted_temp': 'Predicted Temperature (°C)'
            })
        )
    else:
        st.info("No previous predictions available")

if __name__ == "__main__":
    main() 