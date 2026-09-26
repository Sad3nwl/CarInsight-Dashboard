# 🚗 CarInsight Dashboard
An interactive dashboard for exploring the Auto MPG dataset — built with Python, Pandas, and Streamlit.
## Overview
This project takes a raw automobile dataset, cleans it, runs exploratory data analysis, and presents the results in an interactive web dashboard with live filters and charts.
## Dataset
**Source**: Auto MPG Dataset (398 cars, 9 original columns)
| Column | Description |
|---|---|
| name | Full original car name |
| mpg | Miles per gallon (fuel efficiency) |
| cylinders | Number of engine cylinders |
| displacement | Engine displacement (cubic inches) |
| horsepower | Engine horsepower |
| weight | Car weight (lbs) |
| acceleration | 0–60 mph time (seconds) |
| model_year | Model year (2-digit) |
| origin | Country of origin (USA / Europe / Japan) |
**Added during cleaning**: `manufacturer`, `model`, `model_year_full`
## Data Cleaning
- Filled missing `horsepower` values using the median grouped by `cylinders`
- Fixed manufacturer name typos (e.g. `chevroelt` → `chevrolet`, `maxda` → `mazda`, `vw` → `volkswagen`)
- Split `name` into separate `manufacturer` and `model` columns
- Converted 2-digit `model_year` into a full 4-digit `model_year_full`
- Checked for duplicate rows and statistical outliers (kept, since they were legitimate cars, not errors)
Full pipeline: `clean_automobile.py`
## Analysis
- Descriptive statistics and group comparisons by origin, manufacturer, and year
- Correlation analysis (weight has the strongest negative correlation with MPG: -0.83)
- A clear MPG efficiency jump around 1980, likely tied to the late-1970s energy crisis
 ## Dashboard
Built with Streamlit and Plotly. Features:
- **Sidebar filters**: origin, manufacturer, cylinder range, model year range
- **KPI cards**: car count, average MPG, average horsepower, average weight
- **Distribution tab**: MPG histogram, cylinder count
- **Relationships tab**: weight vs. MPG scatter, correlation heatmap, MPG trend over time
- **By Origin tab**: MPG boxplot by origin, top 10 manufacturers
- **Data Table tab**: filtered data view with CSV download
## Project Structure
```
├── app.py                    # Streamlit dashboard
├── clean_automobile.py       # Data cleaning script
├── analyze_automobile.py     # Descriptive analysis script
├── eda_automobile.py         # Matplotlib/Seaborn EDA plots
├── Automobile.csv            # Raw dataset
├── Automobile_clean.csv      # Cleaned dataset
├── requirements.txt          # Python dependencies
└── assets/
    └── car.jpg               # Dashboard corner image
```
## Setup
```bash
pip install -r requirements.txt
```
## Run
```bash
streamlit run app.py
```
Made by Sadeen Abdelalrahman
