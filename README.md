# Autotrader Estimator

## Project Overview
* A tool to estimate resale price **(MAE ~ £1k)** of second hand cars to help interested buyer/seller decide/negociate their deal.
* Scrapped over 1000 car sale advertisement from year 2017 to 2020 on autotrader.co.uk using python
* Engineered features from the text of each car sale description and carried out exploratory analysis on the extended features.
* Optimized Linear, Lasso and RandomForestRegressor using GridSearchCV to reach the best model.
* Build a client facing API using flask

## Code and Resources Used
* **Python Version**: 3.7
* **Packages**: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
* **For Web Framework Requirements**: `pip install -r requirements.txt`
* **Scraper Github**: https://github.com/suhailidrees/autotrader_scraper
* **Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scrapping
Tweaked the web scraper github repo (above) to scrape 1233 car sale postings from autotrader.co.uk at below settings:
* 10 miles range from my home address
* Year 2017 to 2020

Chosen car makes out of my own interest: Audi, BMW, Lexus, Mazda, Fiat, Hyundai, VW, Merceceds, Nissan
With each postings, following features are obtained:
* BHP (brake horse power)
* ULEZ (Ultra Low Emission Zone - exempt or not)
* Body type
* Fuel type
* Web link
* Mileage
* Name (description of the post)
* Owner (number of previous owners)
* Price
* Transimission
* Year (year registered)

## Data Cleaning and Feature Engineering
The raw data are preprocessed following the steps below:
* Engine size
  * For missing values, filled zero liter for electric cars
  * Parsed numeric data out of engine size
* Year
  * Parsed numeric data out of year 
  * Created a column for the age identifier
 * Name
   * Created a column for the length of the name (description)
   * created a column for the car make
   * created a column for the car model
 * BHP
   * For missing values, extract relevant information from name columns if available
   * For remaining missing values, use the median value of the same car make and model
 * Different unique features
   * Created columns for the most frequent words mentioned in the description (shown below in the word cloud), after removing relevant words of car makes, models and common stopwords.
 
![alt text](https://github.com/Hyang0219/Autotrader_estimator_project/blob/main/Images/feature_cloud.png "Word Cloud for Feature Engineering")
   * New columns created for the following features `"sport", "se", "amg", "tfsi", "nav", "tsi", "tdi", "premium", "dci", "m sport", "sportback", "edition", "tech", "crdi", "tronic", "cod", "s line", "bluetooth", "leather", "performance", "2dr", "3dr", "4dr", "5dr", "dsg", "speed", "gti", "gtd", "gte"`
 * Price
   * Parsed numeric data out of price
   
## EDA
Below are a few highlightes by assessing the distribution of the data and the value counts for the various categorical data:
* Correlation between price and variaous features

![alt text](https://github.com/Hyang0219/Autotrader_estimator_project/blob/main/Images/heatmap.png "headmap for price correlation")
* Bar charts of various features counts

![alt text](https://github.com/Hyang0219/Autotrader_estimator_project/blob/main/Images/body.png "bar chats")

* Year-on-year prices of different car makes

![alt text](https://github.com/Hyang0219/Autotrader_estimator_project/blob/main/Images/make-year.PNG "make-year prices")
* Price comparison between different types of fuel and transimission

![alt text](https://github.com/Hyang0219/Autotrader_estimator_project/blob/main/Images/fuel-transimission.PNG "fuel-transimission prices")
* Price comparision between different body types

![alt text](https://github.com/Hyang0219/Autotrader_estimator_project/blob/main/Images/body-price.PNG "body prices")

## Model Building
First, the categorical variables are tranformed into dummy variables. Also the data was splited into train and test set with a test size of 20%.   

Three different models are built and evaluated using Mean Absolute Error. MAE was chosen as the main evaluation metric because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

Three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, thus a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, this would be a good fit. 

## Model performance
The Random Forest model far outperformed the other approaches on the test set, marginally. 
*	**Random Forest** : MAE = 1042
*	**Lasso Regression**: MAE = 1148
*	**Linear Regression**: MAE = 1154

The feature importance of the Random Forest Regressor is printed below:
![alt text](https://github.com/Hyang0219/Autotrader_estimator_project/blob/main/Images/feature-importance.png "feature-importantce")

## Productionization 
In this step, a flask API endpoint was built which was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a car sale postings and returns an estimated resale price. 
