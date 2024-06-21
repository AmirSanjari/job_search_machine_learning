# Machine Learning Binary Classification Project

## Overview
This project demonstrates a machine learning pipeline for binary classification using three different algorithms: Logistic Regression, Random Forest, and SGD Classifier. The project involves data preprocessing, feature engineering, model training, and evaluation.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)


## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/amir9895/job_search_machine_learning.git
    cd job_search_machine_learning
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Ensure the dataset is available and correctly referenced in `loadData.py`.
2. Run the preprocessing script:
    ```sh
    python preprocessing.py
    ```
3. Train and evaluate models:
    - Logistic Regression:
        ```sh
        python logistic_regression.py
        ```
    - Random Forest:
        ```sh
        python random_forest.py
        ```
    - SGD Classifier:
        ```sh
        python sgd_classifier.py
        ```

## Models and Results

### 1. Logistic Regression
- **Accuracy**: 73.28%
- **Description**: Logistic Regression is a simple and interpretable model, suitable for binary classification problems. It performed moderately well on our dataset.

### 2. Random Forest
- **Accuracy**: 81.30%
- **Description**: Random Forest is an ensemble learning method that is robust to overfitting and handles complex data structures well. It achieved the highest accuracy among the three models.

### 3. SGD Classifier
- **Accuracy**: 71.76%
- **Description**: Stochastic Gradient Descent (SGD) is a fast and efficient algorithm, especially for large datasets. It performed the least well, indicating a need for further tuning and optimization.

