# Crop Yield Prediction – End-to-End ML Pipeline

This project demonstrates an end-to-end machine learning pipeline for predicting crop yield using agricultural and environmental data.

## Objective

To build a complete machine learning workflow that preprocesses the data, trains a regression model, makes predictions, and evaluates the model performance.

## Dataset

The project uses the `yield_df.csv` dataset.

### Input Features

* `Area`
* `Item`
* `Year`
* `average_rain_fall_mm_per_year`
* `pesticides_tonnes`
* `avg_temp`

### Target

* `hg/ha_yield` — crop yield

## ML Pipeline

The project follows these steps:

1. Load and inspect the dataset
2. Check and preprocess the data
3. Encode categorical features using One-Hot Encoding
4. Split the data into training and testing sets
5. Build a preprocessing and model pipeline
6. Train a Random Forest Regression model
7. Generate crop yield predictions
8. Evaluate the model using MAE, RMSE, and R²
9. Analyze feature importance
10. Visualize actual vs predicted values and feature importance

## Model

**Random Forest Regressor**

The model is integrated with the preprocessing steps using Scikit-learn's `Pipeline` and `ColumnTransformer`.

## Evaluation

The model is evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook

## Files

* `Crop_Yield_ML_Pipeline.ipynb` — Complete ML pipeline implementation
* `yield_df.csv` — Dataset used for the project
* `README.md` — Project documentation
