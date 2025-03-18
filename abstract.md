   # Tamil Nadu Weather Prediction - Abstract Overview

   ## Quick System Overview
   ```
                     [User Interface]
                           ↓
   [City Selection] → [Weather Agent] → [Prediction Engine]
                           ↓                  ↓
                     [Data Collection]    [ML Processing]
                           ↓                  ↓
                     [Results Display] ← [Predictions]
   ```

   ## Core Components
   ```
   +------------------+      +------------------+
   |   Data Sources   | →    |  Processing      |
   | - Current        |      | - Cleaning       |
   | - Historical     |      | - Training       |
   | - Local Storage  |      | - Prediction     |
   +------------------+      +------------------+
            ↓                       ↓
   +------------------+      +------------------+
   |   Visualization  | ←    |  User Interface  |
   | - Trends         |      | - City Selection |
   | - Predictions    |      | - Display        |
   +------------------+      +------------------+
   ```

   ## Data Flow Abstract
   ```
   [Input]
      ↓
   [Processing] → [Storage]
      ↓             ↓
   [Analysis] ← [Retrieval]
      ↓
   [Output]
   ```

   ## Key Features Overview
   1. **Data Collection**
      - Real-time weather data
      - Historical patterns
      - Local storage

   2. **Processing**
      - Machine learning model
      - Feature engineering
      - Prediction generation

   3. **Presentation**
      - Interactive UI
      - Visual analytics
      - Historical tracking

   ## System Interaction Flow
   ```
   User → Select City → Get Data → Process → Display
   ↑                                         ↓
   └─────────── Store Results ←─────────────┘
   ```

   ## Technology Stack Summary
   ```
   Frontend: [Streamlit] → Backend: [Python + ML] → Data: [APIs + Storage]
   ``` 