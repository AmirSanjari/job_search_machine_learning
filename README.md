# Machine Learning Prediction Project

This repository contains a machine learning project that aims to predict specific outcomes based on a dataset. The project includes data analysis, preprocessing, and the implementation of various machine learning models.

## Table of Contents

- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Analysis](#analysis)
- [Models](#models)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Dataset

The dataset used in this project includes information about individuals' employment status, education level, job search duration, and other relevant factors. It is stored in the `Dataset` directory and consists of:

- `data-analysis.xlsx`
- `data.csv`

## Data Preprocessing

Data preprocessing is performed in the `preprocessing.py` script located in the `Models` directory. The preprocessing steps include:

1. Dropping unnecessary columns: 'id', 'pathrise_status', 'cohort_tag'.
2. Cleaning and handling missing values for various columns such as 'primary_track', 'program_duration_days', 'employment_status', etc.
3. Encoding categorical columns using `LabelEncoder`.

Detailed preprocessing steps can be found in the script and are essential for preparing the data for model training.

## Analysis

The `Analysis` directory contains several Jupyter notebooks that explore different aspects of the dataset, including:

- `analysis-biggetsChallenge.ipynb`
- `analysis-educationLevel.ipynb`
- `analysis-employmentStatus.ipynb`
- `analysis-genderStatus.ipynb`
- `analysis-lengthJobSearch.ipynb`
- `analysis-numberOfApplicationRequests.ipynb`
- `analysis-numberOfInterview.ipynb`
- `analysis-primaryTrack.ipynb`
- `analysis-professionalExperience.ipynb`
- `analysis-programDurationDays.ipynb`
- `analysis-race.ipynb`
- `analysis-workAuthorizationStatus.ipynb`

These notebooks provide insights into the data and help in understanding the factors affecting the predictions.

## Models

The `Models` directory contains Jupyter notebooks for different machine learning models:

- `LogisticRegressionClassification.ipynb`
- `RandomForestClassification.ipynb`
- `SGDClassification.ipynb`

Each notebook includes the implementation, training, and evaluation of the respective models.

Usage
Data Preprocessing:
Run the preprocessing.py script to clean and prepare the data.

bash
Copy code
python Models/preprocessing.py
Data Analysis:
Explore the data using the Jupyter notebooks in the Analysis directory.

Model Training:
Train the machine learning models by running the notebooks in the Models directory.
