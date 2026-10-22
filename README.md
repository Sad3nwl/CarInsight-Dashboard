<div align="center">
# 🚗 CarInsight Dashboard
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
 
*An interactive web dashboard for exploring the Auto MPG dataset with live filtering, statistical insights, and visual analytics.*

</div>

---

### 📌 Overview

This project takes a raw automobile dataset, cleans it, performs exploratory data analysis (EDA), and presents the results in an interactive web dashboard with real-time filters and dynamic charts.

---

### 📊 Dataset

[![Dataset](https://img.shields.io/badge/Dataset-Auto_MPG-green?style=for-the-badge&logo=commonworkflowlanguage)](https://archive.ics.uci.edu/ml/datasets/auto+mpg)
[![Records](https://img.shields.io/badge/Records-398_Cars-blue?style=for-the-badge)](#)
[![Columns](https://img.shields.io/badge/Original_Columns-9-orange?style=for-the-badge)](#)

#### Data Schema
| Column | Description |
|---|---|
| `name` | Full original car name |
| `mpg` | Miles per gallon (fuel efficiency) |
| `cylinders` | Number of engine cylinders |
| `displacement` | Engine displacement (cubic inches) |
| `horsepower` | Engine horsepower |
| `weight` | Car weight (lbs) |
| `acceleration` | 0–60 mph time (seconds) |
| `model_year` | Model year (2-digit) |
| `origin` | Country of origin (USA / Europe / Japan) |

> 💡 **Engineered Features Added**: `manufacturer`, `model`, `model_year_full`

---

### 🧹 Data Cleaning Pipeline

![Data Cleaning Script](https://img.shields.io/badge/Pipeline-clean__automobile.py-yellow?style=for-the-badge&logo=python)

- 🩹 **Missing Values**: Imputed missing `horsepower` values using median grouped by `cylinders`.
- ✏️ **Typo Fixes**: Corrected brand typos (e.g., `chevroelt` → `chevrolet`, `maxda` → `mazda`, `vw` → `volkswagen`).
- ✂️ **Feature Extraction**: Split `name` into `manufacturer` and `model`.
- 📅 **Date Standardisation**: Converted 2-digit `model_year` into a 4-digit `model_year_full`.
- 🔍 **Quality Check**: Verified duplicates and audited outliers (retained legitimate vehicle records).

---

### 📈 Key Insights & Analysis

- 📉 **Strongest Correlation**: Vehicle `weight` has the strongest negative correlation with MPG (**-0.83**).
- ⛽ **Historical Shift**: Notable jump in MPG efficiency around **1980**, coinciding with the late-1970s energy crisis response.
- 🌍 **Regional Trends**: Distinct distribution patterns in fuel efficiency across USA, Europe, and Japan.

---

### 🖥️ Dashboard Features

Implemented with **Streamlit** and **Plotly**:

- 🎛️ **Sidebar Filters**: Origin, manufacturer, cylinder range, and model year range.
- 📊 **KPI Summary Cards**: Total car count, average MPG, average horsepower, and average weight.
- 📉 **Distribution Tab**: MPG histogram and cylinder count distribution.
- 🔗 **Relationships Tab**: Weight vs. MPG scatter plot, correlation heatmap, and timeline trends.
- 🌐 **By Origin Tab**: MPG boxplots by region and top 10 manufacturers analysis.
- 📑 **Data Table Tab**: Interactive filtered view with a 💾 **CSV Download** feature.

---

### 📁 Project Structure

```text
├── app.py                 # Streamlit dashboard entrypoint
├── clean_automobile.py    # Data cleaning & preprocessing pipeline
├── analyze_automobile.py  # Statistical & descriptive analysis
├── eda_automobile.py      # Exploratory visualization scripts
├── Automobile.csv         # Raw source dataset
├── Automobile_clean.csv   # Processed dataset
├── requirements.txt       # Project dependencies
└── assets/
    └── car.jpg            # Dashboard UI asset
