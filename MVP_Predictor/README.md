# Predicting the MVP Award Winner for the Current NBA Season

This project is a predictive analysis project that uses Python and scikit-learn to predict who will win the MVP award for the current NBA season. The project collects data from reference-basketball.com, cleans and preprocesses the data, selects the most relevant features for predicting the MVP award winner, trains a linear regression model on the selected features, and evaluates the performance of the model using `accuracy_score` and other relevant metrics.

## How it works

To use this project, follow these steps:

1. Clone or download the repository to your local machine.
2. Install the required libraries by running the following command in your terminal: `pip install -r requirements.txt`.
3. Run the `main.py` file to train the model on the available data and output the predicted MVP award winner. You can modify the file to include additional data or modify the features used for prediction.
4. To deploy the model on new data, create a CSV file with the same columns as the `data.csv` file provided and run the `main.py` file with the name of the new data file as an argument, like this: `python main.py new_data.csv`.

## Requirements

- Python 3.6 or higher
- pandas
- scikit-learn
- seaborn
- matplotlib
- requests
- BeautifulSoup

## Authors

- [Micah Thornton](https://github.com/micahtml)
 
