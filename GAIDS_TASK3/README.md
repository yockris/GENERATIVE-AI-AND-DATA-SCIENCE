Matplotlib Data Visualization Notebook
📌 Overview
This Jupyter Notebook demonstrates how to use Matplotlib, Pandas, and Seaborn to visualize data from a CSV file. 
The dataset used is cars_data.csv, which contains information about various car models, including manufacturer, 
engine size, fuel type, year of manufacture, mileage, and price.

📂 Dataset
File: cars_data.csv 

Columns:
Manufacturer, Model, Engine size, Fuel type, Year of manufacture, Mileagem, Price

Imported Libraries 
pandas – for data manipulation
matplotlib.pyplot – for plotting
seaborn – for styled visualizations

📊 Visualizations
1. Line Plot
Purpose: Visualize trends across the first 30 rows of the dataset.
X-axis: DataFrame index (0–29)
Y-axis: Each numeric columns of the dataset

2. Scatter Plot
Purpose: Examine relationships between two continuous variables.
Example: Model vs Mileage
X-axis: Model
Y-axis: Mileage

4. Histogram
Purpose: Show distribution of a single variable.
Example: Distribution of car prices

4. Box Plot
Purpose: Visualize spread and detect outliers.
Example: Mileage grouped by Fuel Type

🚀 How to Run
Ensure cars_data.csv is in the same directory as the notebook.
Install required libraries:

bash
pip install pandas matplotlib seaborn

📌 Notes
You can modify the plots to explore other relationships.
Seaborn themes like whitegrid are used for cleaner visuals.
