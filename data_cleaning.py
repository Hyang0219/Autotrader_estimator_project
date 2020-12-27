"""
Created on Tuesday 27 Dec 2020

@ author: Hanlin
"""

# Import all tools

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read scrapped data
df = pd.read_csv("autotrader_prices.csv", parse_dates=["year"])

# raw data exploratation
df.info()
df.describe()

# check missing data
df.isna().sum()

# Data Cleaning
## filling missing BHP, Tried to first replace with median value,
## however, need to use a more sensible way of filling up this
## feature
df_clean = df.copy()
df_clean["BHP"].fillna(df.BHP.median(), inplace=True)

## filling ULEZ compliance
df_clean["ULEZ"].fillna("Non-ULEZ", inplace=True)

## engine size parsing - get rid of the Liter "L" and convert to float
df_clean["engine"] = df_clean["engine"].apply(lambda x: float(x[:-1]))

# Remove link
df_clean.drop(["link"], axis=1, inplace=True)

## parsing name into multiple extra features
df_clean["make"] = df_clean["name"].apply(lambda x:x.split()[0])
df_clean["model"] = df_clean["name"].apply(lambda x:x.split()[1])

## diffentiate from "ECO", SE", "Sport", "M Sport", "Lux", Nav/Satellite", "Bluetooth",
## "Leather", "3-door"
df_clean["se"] = df_clean["name"].apply(lambda x: 1 if "se" in x.lower() else 0)
df_clean["se"].value_counts()

# maybe too small/biased to be relevant
df_clean["eco"] = df_clean["name"].apply(lambda x: 1 if "eco" in x.lower() else 0)
df_clean["eco"].value_counts()

df_clean["sport"] = df_clean["name"].apply(lambda x: 1 if "sport" in x.lower() else 0)
df_clean["sport"].value_counts()

df_clean["m_sport"] = df_clean["name"].apply(lambda x: 1 if "m sport" in x.lower() else 0)
df_clean["m_sport"].value_counts()

# maybe too small/biased to be relevant
df_clean["lux"] = df_clean["name"].apply(lambda x: 1 if "lux" in x.lower() else 0)
df_clean["lux"].value_counts()

df_clean["sat_nav"] = df_clean["name"].apply(lambda x: 1 if "sat" in x.lower() or "nav" in x.lower() else 0)
df_clean["sat_nav"].value_counts()

df_clean["bluetooth"] = df_clean["name"].apply(lambda x: 1 if "bluetooth" in x.lower() else 0)
df_clean["bluetooth"].value_counts()

df_clean["leather"] = df_clean["name"].apply(lambda x: 1 if "leather" in x.lower() else 0)
df_clean["leather"].value_counts()

df_clean["three_door"] = df_clean["name"].apply(lambda x: 1 if "3-door" in x.lower() else 0)
df_clean["three_door"].value_counts()

## filling missing owners with median value
df_clean["owners"].fillna(df.owners.median(), inplace=True)

## parsing years
df_clean["year_reg"] = df_clean["year"].apply(lambda x: x.split("(")[1].replace(")",""))
df_clean["year"] = df_clean["year"].apply(lambda x: int(x.split("(")[0]))

## parsing price
df_clean["price"] = df_clean["price"].apply(lambda x: int(x.replace("£","").replace(",","")))

## parsing fuel
df_fuel = df_clean[df_clean.fuel.isna()]
df_fuel.make

df_fuel = df_clean[df_clean.make == "Fiat"]
df_fuel.fuel.value_counts()

df_clean["fuel"].fillna("Petrol", inplace=True)

# Check and save
df_clean.drop(["name"], axis=1, inplace=True)
df_clean.to_csv("autotrader_prices_cleaned.csv", index=False)