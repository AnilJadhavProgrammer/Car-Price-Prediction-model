Overview
This project aims to predict car prices using various machine learning techniques. The dataset is sourced from the quikr_car.csv file, and the script preprocesses the data to make it suitable for building predictive models. The project is implemented in Python and makes use of popular data science libraries such as pandas, numpy, matplotlib, and seaborn.

Dataset
The dataset used in this project is quikr_car.csv, which contains information about various cars including their year, price, kilometers driven, fuel type, and more.

Project Structure
quikr_car.csv: The dataset used for the analysis.
Car_Price_Prediction.py: Python script containing the data cleaning and prediction steps.
README.md: This file, providing an overview and instructions.
Installation
To run the analysis, you need to have Python installed along with the following libraries:

pandas
numpy
matplotlib
seaborn
You can install the required libraries using pip:

sh
Copy code
pip install pandas numpy matplotlib seaborn
Usage
Prepare the Dataset: Ensure that the quikr_car.csv file is in the same directory as the script.
Run the Script: Execute the following command to preprocess the data and start the prediction process.
sh
Copy code
python Car_Price_Prediction.py
Example
Here is an example of what the script does:

Data Loading: Loads the car price dataset.
Data Cleaning:
Removes non-numeric years and converts the 'year' column to integers.
Filters out rows where the price is not specified.
Cleans and converts the 'Price' and 'kms_driven' columns to integers.
Drops rows with missing fuel type.
Data Transformation:
Extracts the first three words from the 'name' column for better aggregation.
Resets the index of the cleaned DataFrame.
