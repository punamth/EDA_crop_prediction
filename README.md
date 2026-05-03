# Exploratory Data Analysis for Weather-based-crop-farming.
1. Project Overview
EDA_crop_prediction is a data-driven analysis tool built in JupyterLab that examines weather, agriculture, and forestry datasets for Nepal to produce monthly crop-suitability recommendations. By combining a strict threshold model with a score-based ranking model, the tool helps farmers and agri-tech practitioners make informed planting decisions backed by real environmental data.

2. Objectives
•	Consolidate and clean multi-source datasets covering Nepal's weather, soil, and forestry indicators.
•	Perform exploratory analysis to uncover seasonal patterns in temperature, rainfall, and humidity.
•	Apply two complementary crop-suitability models (Strict and Score-Based) across 12 calendar months.
•	Identify the optimal crop(s) for each month of the agricultural calendar.
•	Present findings in a reproducible, notebook-based format accessible to agri-tech stakeholders.

3. Technology Stack
3.1 Environment
•	JupyterLab — interactive notebook development environment
•	Python 3.x — primary programming language

3.2 Core Libraries
Library	Version	Purpose
pandas	Latest	Data loading, cleaning, manipulation
numpy	Latest	Numerical computations & array operations
matplotlib.pyplot	Latest	Static data visualizations & plots
seaborn	Latest	Statistical visualizations & heatmaps
scikit-learn	Latest	Machine learning models & preprocessing
requests	Latest	HTTP requests for external data fetching

4. Data Sources
4.1 Weather Data
Nepal weather data was split into two CSV files covering the full calendar year and loaded as separate DataFrames before being merged for unified analysis:
•	nepal_weather_data_jan_to_jun.csv — Monthly weather records for January through June
•	nepal_weather_data_jul_to_dec.csv — Monthly weather records for July through December

Both files were loaded using:
df1 = pd.read_csv('../data/raw/nepal_weather_data_jan_to_jun.csv')
df2 = pd.read_csv('../data/raw/nepal_weather_data_jul_to_dec.csv')

4.2 Agriculture & Forestry Data
Additional datasets were sourced from public agriculture and forestry repositories covering Nepal's regional farming conditions. These datasets provided supplementary soil quality, crop history, and land-use indicators used alongside the weather data for crop scoring. Exact source URLs were not recorded at time of analysis.

4.3 Suggested Data Sources for Reference
•	Ministry of Agriculture and Livestock Development, Nepal — agri.gov.np
•	Department of Hydrology and Meteorology, Nepal — dhm.gov.np
•	FAO Nepal Country Data — fao.org/nepal
•	World Bank Open Data — data.worldbank.org

5. Analysis Methodology
5.1 Data Pipeline
The analysis followed a structured EDA pipeline:
•	Step 1 — Data Loading: Imported all CSV files into pandas DataFrames.
•	Step 2 — Data Cleaning: Handled missing values, removed duplicates, standardized column names, and aligned date formats.
•	Step 3 — Merging: Combined the two weather DataFrames into a single 12-month DataFrame.
•	Step 4 — Exploratory Analysis: Generated descriptive statistics, distribution plots (histograms, box plots), and correlation heatmaps using seaborn and matplotlib.
•	Step 5 — Feature Engineering: Derived monthly averages for temperature, rainfall, and humidity as input features for crop scoring.
•	Step 6 — Crop Suitability Modeling: Applied two models (Strict and Score-Based) for five major crops.
•	Step 7 — Output Generation: Produced the final monthly recommendation matrix.

5.2 Crops Analyzed
The following five major Nepalese crops were evaluated for suitability:
Crop	Primary Growing Season	Key Requirements
Rice	Kharif (May–Sep)	High rainfall, warm temperature, flooded fields
Wheat	Rabi (Nov–Mar)	Cool temperature, moderate moisture
Maize	Spring/Kharif (Mar–Sep)	Warm temp, moderate to high rainfall
Millet	Kharif (Apr–Oct)	Drought-tolerant, warm, well-drained soil
Potatoes	Winter/Spring (Oct–Apr)	Cool climate, well-drained fertile soil

5.3 Suitability Models
Strict Model
The Strict Model applies hard binary thresholds on weather and environmental parameters. A crop receives True only when ALL conditions are simultaneously satisfied — temperature range, minimum rainfall, humidity levels, and soil indicators. This model is conservative and eliminates borderline months to reduce farming risk.

Score-Based Model
The Score-Based Model assigns weighted scores to each environmental parameter per crop per month. A crop receives True if the total score exceeds a defined suitability threshold. This approach is more flexible — it accommodates months where some conditions are suboptimal but the overall environment remains favorable. It tends to recommend more months than the Strict model.

6. Results — Monthly Crop Suitability Matrix
The table below presents the final output of the EDA analysis. Each month is evaluated against all five crops under both models. ✅ indicates the crop is suitable for that month; ❌ indicates it is not recommended.

Month	#	Rice S	Wheat S	Maize S	Millet S	Potato S	Rice Sc	Wheat Sc	Maize Sc	Recommendation
January	1	✗	✓	✗	✗	✓	✗	✓	✗	Wheat, Potatoes
February	2	✗	✓	✗	✗	✓	✗	✓	✗	Wheat, Potatoes
March	3	✗	✗	✓	✗	✗	✗	✓	✓	Maize
April	4	✗	✓	✓	✓	✓	✗	✓	✓	Wheat, Maize, Millet, Potatoes
May	5	✓	✗	✓	✗	✗	✓	✓	✓	Rice, Maize
June	6	✓	✗	✗	✗	✗	✓	✓	✓	Rice
July	7	✓	✗	✗	✗	✗	✓	✗	✗	Rice
August	8	✗	✗	✗	✗	✗	✓	✗	✗	None (off-season)
September	9	✓	✗	✗	✗	✗	✓	✗	✓	Rice
October	10	✗	✗	✓	✓	✓	✗	✓	✓	Maize, Millet, Potatoes
November	11	✗	✗	✗	✗	✓	✗	✓	✓	Potatoes
December	12	✗	✓	✗	✗	✓	✗	✓	✗	Wheat, Potatoes

S = Strict Model   |   Sc = Score-Based Model   |   ✓ = Suitable   |   ✗ = Not Recommended

7. Key Findings
7.1 Rice
Rice is suitable primarily during the Kharif (monsoon) season from May through September under the Strict model. The Score-Based model extends suitability through August as well, reflecting marginal but workable growing conditions. This aligns with Nepal's traditional Kharif paddy cultivation window.

7.2 Wheat
Wheat shows strong suitability in the Rabi season (October–April), particularly January, February, April, and December under both models. The crop thrives in Nepal's cool winter months with moderate residual moisture, consistent with observed wheat cultivation patterns in the Terai and mid-hill zones.

7.3 Maize
Maize demonstrates the widest seasonal flexibility, appearing suitable across spring and early monsoon months (March–June) under the Strict model, and extending further under Score-Based analysis. This makes it a strong candidate for diversified seasonal farming strategies.

7.4 Millet
Millet suitability is concentrated in the transitional months of April, May, and October — periods of moderate warmth and variable moisture. Its drought tolerance makes it a reliable fallback when rainfall is inconsistent.

7.5 Potatoes
Potatoes have the most consistent year-round presence under the Score-Based model, appearing suitable in 8 out of 12 months. Under the Strict model they are concentrated in winter months (October–February). This highlights potatoes as a high-value, low-risk crop for Nepalese smallholder farmers.

8. Limitations & Future Work
8.1 Current Limitations
•	Dataset source URLs were not documented during development, reducing reproducibility for external researchers.
•	The analysis does not account for regional variation within Nepal (Terai plains vs. mid-hills vs. high mountain zones).
•	Soil quality parameters are generalized — site-specific soil testing data would improve precision.
•	The model does not incorporate market demand, price signals, or irrigation infrastructure data.
•	August shows no suitable crops under the Strict model — this may reflect data gaps rather than true unsuitability.

8.2 Recommended Future Enhancements
•	Integrate region-specific datasets (Terai, Hilly, Mountain zones) for disaggregated recommendations.
•	Add time-series forecasting (LSTM or Prophet) to predict future season suitability based on climate trends.
•	Incorporate more crops: soybeans, lentils, sugarcane, mustard, vegetables.
•	Build an interactive dashboard (Streamlit or Dash) for real-time farmer-facing recommendations.
•	Document all dataset URLs and version hashes for full reproducibility.

9. Project Directory Structure
EDA_crop_prediction/
├── data/
│   └── raw/
│       ├── nepal_weather_data_jan_to_jun.csv
│       ├── nepal_weather_data_jul_to_dec.csv
│       └── [agriculture & forestry datasets]
├── notebooks/
│   └── EDA_crop_prediction.ipynb
└── README.md

10. Glossary
Term	Definition
EDA	Exploratory Data Analysis — the process of investigating datasets to summarize main characteristics.
Strict Model	Binary threshold-based suitability model requiring ALL crop conditions to be simultaneously met.
Score-Based Model	Weighted scoring model that recommends a crop when the aggregate environmental score exceeds a threshold.
Kharif	Summer/monsoon crop season in South Asia, typically June–November.
Rabi	Winter crop season in South Asia, typically November–April.
Agri-tech	Agricultural technology — the application of digital tools and data science to improve farming outcomes.


