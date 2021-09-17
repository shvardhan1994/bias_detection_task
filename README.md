# Bias detection task

The goal of this task is to train a classifier to detect political bias in news articles.

# Data

The data folder contains three files

- bias_articles_train.json: Json containing array of dicts with 
  - `id`: unique integer id for each article
  - `title`: Title of the article
  - `body`: Body of the article
  - `bias`: Class label it can be "Left", "Center" and "Right"
- bias_articles_dev.json: Same as bias_articles_train, but used for validation of the models.
- bias_articles_test.json: Same as bias_articles_train, but does not contain bias labels (to be predicted.)

# Code
bias_classifier.py: Contains classifier class.
