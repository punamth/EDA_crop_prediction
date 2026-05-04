# 🌾 EDA Crop Prediction

## Exploratory Data Analysis for Weather-Based Crop Farming in Nepal

This project performs **Exploratory Data Analysis (EDA)** on Nepal’s weather, agriculture, and forestry datasets to identify the most suitable crops for different months of the year.

The analysis combines environmental indicators such as:

- Temperature
- Rainfall
- Humidity
- Seasonal patterns
- Soil-related agricultural indicators

to generate monthly crop recommendations using both:

- **Strict Threshold Model**
- **Score-Based Suitability Model**

---

## 📌 Project Objectives

- Clean and preprocess multi-source agricultural datasets
- Analyze seasonal weather patterns in Nepal
- Visualize rainfall, humidity, and temperature trends
- Build crop suitability logic using environmental thresholds
- Recommend suitable crops for each month
- Create reproducible EDA workflows using Jupyter Notebook

---

## 🌱 Crops Analyzed

| Crop | Growing Season | Key Requirements |
|---|---|---|
| Rice | Kharif (May–Sep) | High rainfall, warm climate |
| Wheat | Rabi (Nov–Mar) | Cool temperature, moderate moisture |
| Maize | Spring/Kharif | Warm climate, moderate rainfall |
| Millet | Kharif | Drought tolerant, warm weather |
| Potatoes | Winter/Spring | Cool climate, fertile soil |

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| JupyterLab | Interactive notebook development |
| Pandas | Data analysis and manipulation |
| NumPy | Numerical computation |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Data preprocessing and ML utilities |

---

## 📁 Project Structure

```bash
EDA_crop_prediction/
│
├── data/
│   ├── raw/
│   │   ├── nepal_weather_data_jan_to_jun.csv
│   │   ├── nepal_weather_data_jul_to_dec.csv
│   │   └── agriculture_forestry_data.csv
│   │
│   └── processed/
│       └── cleaned_weather_data.csv
│
├── notebooks/
│   └── EDA_crop_prediction.ipynb
│
├── outputs/
│   ├── charts/
│   ├── heatmaps/
│   └── recommendation_matrix.csv
│
├── docs/
│   └── project_documentation.docx
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📊 Analysis Workflow

1. Data Collection
2. Data Cleaning
3. Data Merging
4. Exploratory Data Analysis
5. Feature Engineering
6. Crop Suitability Modeling
7. Result Visualization

---

## 📈 Visualizations Included

- Correlation Heatmaps
- Temperature Distribution Plots
- Rainfall Analysis
- Seasonal Trend Charts
- Crop Suitability Matrix
- Monthly Recommendation Graphs

---

## ✅ Crop Suitability Models

### Strict Model
A crop is recommended only when **all environmental conditions** are satisfied.

### Score-Based Model
A weighted scoring approach where crops are recommended if the total suitability score exceeds a threshold.

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/EDA_crop_prediction.git
```

### 2. Navigate to Project Directory

```bash
cd EDA_crop_prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook

```bash
jupyter lab
```

---

## 📌 Key Findings

- Rice performs best during Nepal’s monsoon season
- Wheat thrives in winter months
- Maize shows the highest seasonal flexibility
- Potatoes remain suitable across multiple months
- Seasonal weather strongly impacts crop suitability

---

## 🔮 Future Improvements

- Add region-specific analysis (Terai, Hilly, Mountain)
- Integrate machine learning forecasting models
- Include more crop varieties
- Build interactive dashboard using Streamlit
- Add real-time weather integration

---

## 📚 Data Sources
- FAOSTAT Nepal Data(https://www.fao.org/faostat/en/#home)
- Visual Crossing Weather API(https://www.visualcrossing.com/weather-api/)

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed as part of a Data Science and Agricultural Analytics project using Python and JupyterLab.
