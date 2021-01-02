# Autotrader Estimator

## Project Overview
* A tool to estimate resale price of the second hand cars to help interested buyer/seller decide/negociate their deal.
* Scrapped over 1000 car sale advertisement from year 2017 to 2020 on autotrader.co.uk using python
* Engineered features from the text of each car sale description and carried out exploratory analysis on the extended features.
* Optimized Linear, Lasso and RandomForestRegressor using GridSearchCV to reach the best model.
* Build a client facing API using flask

## Code and Resources Used
**Python Version**: 3.7
**Packages**: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
**For Web Framework Requirements**: `pip install -r requirements.txt`
**Scraper Github**:https://github.com/suhailidrees/autotrader_scraper
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scrapping
Tweaked the web scraper github repo (above) to scrape 1233 car sale postings from autotrader.co.uk at below settings:
* 10 miles range from my home address
* Year 2017 to 2020
* Chosen car makes out of my own interest: Audi, BMW, Lexus, Mazda, Fiat, Hyundai, VW, Merceceds, Nissan
With each postings, following features are obtained:
* BHP (brake horse power)
* ULEZ (Ultra Low Emission Zone - exempt or not)
* Body type
* Fuel type
* Web link
* Mileage
* Name (posting description)
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
   * Created columns for the most frequent words mentioned in the description, after removing relevant words of car makes, models and stopwords, `"sport","se", "amg", "tfsi", "nav", "tsi", "tdi", "premium", "dci", "m sport", "sportback", "edition", "tech", "crdi", "tronic", "cod", "s line", "bluetooth", "leather", "performance", "2dr", "3dr", "4dr", "5dr", "dsg", "speed", "gti", "gtd", "gte"`
 * Price
   * Parsed numeric data out of price
   
