# System Architecture and Flow Diagrams

## 1. High-Level System Architecture
```
+----------------------------------------------------------------------------------------+
|                                  User Interface Layer                                    |
|  +------------------+     +----------------------+     +-------------------------+       |
|  |  City Selection  |     | Weather Display      |     | Temperature Prediction |       |
|  |  (Streamlit UI) |     | (Current & Historic) |     | (Visualization & Data) |       |
|  +------------------+     +----------------------+     +-------------------------+       |
+----------------------------------------------------------------------------------------+
                                         ↕
+----------------------------------------------------------------------------------------+
|                                  Application Layer                                       |
|  +------------------+     +----------------------+     +-------------------------+       |
|  | Weather Agent    |     | Prediction Engine    |     | Data Management        |       |
|  | - API Client     |     | - ML Model          |     | - Storage Handler      |       |
|  | - Data Fetcher   |     | - Feature Engineer  |     | - History Tracker      |       |
|  +------------------+     +----------------------+     +-------------------------+       |
+----------------------------------------------------------------------------------------+
                                         ↕
+----------------------------------------------------------------------------------------+
|                                   Data Layer                                            |
|  +------------------+     +----------------------+     +-------------------------+       |
|  | External API     |     | Model Storage        |     | Prediction History     |       |
|  | (Open-Meteo)     |     | (Scikit-learn)      |     | (JSON Files)          |       |
|  +------------------+     +----------------------+     +-------------------------+       |
+----------------------------------------------------------------------------------------+
```

## 2. Data Flow Diagram
```
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
```

## 3. Component Interactions

### A. Data Collection Flow
1. User selects a city from the UI
2. Weather Agent activates:
   - Fetches current weather from Open-Meteo API
   - Retrieves historical data for the past 7 days
   - Stores data in memory for processing

### B. Prediction Flow
1. Feature Engineering:
   - Data preprocessing and cleaning
   - Feature scaling using StandardScaler
   - Time series data preparation

2. Model Training:
   - Linear Regression model initialization
   - Training on historical data
   - Feature importance analysis

3. Prediction Generation:
   - Current weather data transformation
   - Model prediction for tomorrow's temperature
   - Confidence calculation

### C. Display Flow
1. Results Processing:
   - Prediction formatting
   - Historical data visualization
   - Trend analysis

2. UI Updates:
   - Current weather metrics
   - Prediction display with delta
   - Temperature trend graph
   - Previous predictions table

### D. Storage Flow
1. Prediction Storage:
   - JSON file creation/update
   - Historical prediction tracking
   - City-wise data segregation

## 4. Key Components Description

### A. User Interface Layer
- **City Selection**: Dropdown menu for Tamil Nadu cities
- **Weather Display**: Current conditions and historical data
- **Prediction Display**: Tomorrow's temperature and trends

### B. Application Layer
- **Weather Agent**: Handles API communication and data fetching
- **Prediction Engine**: ML model training and prediction
- **Data Manager**: Storage and retrieval operations

### C. Data Layer
- **External API**: Open-Meteo weather data source
- **Model Storage**: Trained model parameters
- **History Storage**: JSON-based prediction archives

## 5. Technical Stack

### A. Frontend
- Streamlit: Web interface framework
- Matplotlib: Data visualization
- Pandas: Data manipulation

### B. Backend
- Python: Core programming language
- Scikit-learn: Machine learning operations
- NumPy: Numerical computations

### C. Data
- Open-Meteo API: Weather data source
- JSON: Local storage format
- DataFrame: In-memory data structure 