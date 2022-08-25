import pandas as pd
import numpy as np


# Read the excel file given
purchase_sales_listing = pd.read_excel("Purchase_sales_listing.xlsx",sheet_name="Purchases")

columnname_split = purchase_sales_listing.columns[0].split("-")
values = purchase_sales_listing.values

customernames = list()
vechiclenumber =list()

for i in values:
    print(i[0].split("-"))
    customernames.append(i[0].split("-")[0])
    vechiclenumber.append(i[0].split("-")[1])

purchase_sales_listing[columnname_split[0]] = customernames
purchase_sales_listing[columnname_split[1]] = vechiclenumber

new_sales_data = purchase_sales_listing.drop(columns=[purchase_sales_listing.columns[0]])

new_sales_data.to_excel("feature_engineered_purchases_listing.xlsx")