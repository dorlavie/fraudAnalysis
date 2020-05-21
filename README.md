# Dor Lavi - Fraud Challenge 

This is my solution to a fraud challenge

## Content of Project

In this project you will find:
* dorLavi-SupervisedChallenge.html - my notebook with all my research, and model build.
    * The raw json file (raw data) is required to run this notebook, however I don't include it in the project due to confidentiality.
* some pickle file - they are needed for the API to run, all of them are generated in the notbook
    * log_reg_model_v1.pickle - The trained model, logistic regression
    * features.pickle - all the features of the model
    * encodedVariables.pickle - one hot encoded featrues
    * thresholds.pickle - the threshold for for predicting class (based on the 1% rule in the instructions)
* api.py - this is the api file  
* README.md - this file

## How to Run api.py

open a command line in the folder that contain the file, than type `python api.py` to start the API server. send a post request to `http://127.0.0.1:5000/` with the following json structre:
```json
{
   "euro" : "8.51",
   "card_network" : "SchemeI",
   "card_type" : "CREDIT",
   "bank_country_id" : "6.0",
   "user_country_id" : "NaN",
   "merchant" : "Shop2"
 }
```

The response you should see is the following:
```
"The prediction is: 0
the input data is 
{'euro': '8.51', 'card_network': 'SchemeI', 'card_type': 'CREDIT', 'bank_country_id': '6.0', 'user_country_id': 'NaN', 'merchant': 'Shop2'}"
```
