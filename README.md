# Amazon Fine Food Reviews - Sentiment Analysis

# 📌 Project Overview

This project performs Sentiment Analysis on the Amazon Fine Food Reviews dataset. The goal is to classify customer reviews as Positive, Neutral, or Negative using Natural Language Processing (NLP) techniques and Machine Learning models.

## Key Features:

1. Text Preprocessing: Removing HTML tags, punctuation, stopwords, and applying stemming.

2. Feature Engineering: Using TF-IDF vectorization.

3. Model Training & Evaluation: Comparing multiple models like Naïve Bayes, Logistic Regression, and SVM.


# 🔄 Project Workflow

1. Data Collection: Loading the Amazon Fine Food Reviews dataset.

2. Data Cleaning & Preprocessing: Removing unwanted characters, stopwords, and applying stemming.

3. Exploratory Data Analysis (EDA): Understanding patterns in the dataset.

4. Feature Engineering: Converting text data into numerical form using TF-IDF.

5. Model Training & Evaluation: Training models and selecting the best one based on performance metrics.


# 📦 Results and Analysis
- **Best Model**: Logistic Regression.
- **Confusion Matrix**: **Logistic Regression** show high value in TP and TN.
  
 ![Alt text]("https://github.com/juna-99/Amazon-Fine-Food-Reviews/blob/9d63e74feef04c26e095ebbc8b7d22675617a79b/reports/figures/confusion_matrix.png") 
- **AUC-ROC Curve**: **Logistic Regression** has better discrimination between positive and negative instances.
  
![Alt text]("https://github.com/juna-99/Amazon-Fine-Food-Reviews/blob/9d63e74feef04c26e095ebbc8b7d22675617a79b/reports/figures/roc.png")

- **Performance Metrics**: Considering both Precision and Recall, **Logistic Regression** preferred as it has a high F1-Score.

| Model       | Logistic Regression | Multinomial Naive Bayes | Bernoulli Naive Bayes | 
|-------------|---------------------|-------------------------|-----------------------|
| Accuracy    | 0.92                | 0.85                    | 0.87                  | 
| Precision   | 0.93                | 0.87                    | 0.88                  |
| Recall      | 0.93                | 0.85                    | 0.88                  |
| F1 - Score  | 0.93                | 0.79                    | 0.88                  |   

# 🏗️ Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
