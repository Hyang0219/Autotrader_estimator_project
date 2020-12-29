"""
Created on Tuesday 15 Dec 2020

@ author: Hanlin
"""

# Import all tools

from autotrader_scraper import get_cars, save_csv, save_json
import pandas as pd

# Define the targeted make and model in a tuple list

target_model = [("Audi","A1"),
                ("Audi","A3"),
                ("BMW","2 SERIES"),
                ("BMW","3 SERIES"),
                ("Lexus","CT 200h"),
                ("Lexus","NX 300h"),
                ("Mazda","Mazda3"),
                ("Mazda","Mazda6"),
                ("Fiat","500"),
                ("Hyundai","Kona"),
                ("Hyundai","Tucson"),
                ("Volkswagen","Golf"),
                ("Mercedes-Benz","A Class"),
                ("Mercedes-Benz","C Class"),
                ("Nissan","Qashqai")]

# Function to generate all raw data from a list of tuples of the targeted make and model

def generate_car_price(target=target_model):
    results = []
    for make, model in target:
        results_price = get_cars(make = make,
                                 model = model,
                                 postcode = "CF23 8PG",
                                 radius = 10,
                                 min_year = 2017,
                                 max_year = 2020,
                                 include_writeoff = "include",
                                 max_attempts_per_page = 5,
                                 verbose = False)
        results += results_price
    return results

# Scrape the data

results = generate_car_price(target_model)

# Save scrapped data as csv
pd.DataFrame(results).to_csv("autotrader_prices_raw1.csv", index = False)