import pandas as pd
import numpy as np


def feature_engineer(filename, sheetname):
    # Read the excel file given
    print("We are reading the file....")
    purchase_sales_listing = pd.read_excel("Purchase_sales_listing.xlsx",sheet_name="Sales")

    #retrieve the splitted column name for the dataframe
    columnname_split = purchase_sales_listing.columns[0].split("-")
    
    #retrieve the column values for the dataframe
    values = purchase_sales_listing.values

    #create a list to save customer names and vehicle numbers
    customernames = list()
    vechiclenumber =list()

    #loop through values to split the data and store it in the lists respectively
    for i in values:
        customernames.append(i[0].split("-")[0])
        vechiclenumber.append(i[0].split("-")[1])

    #copy values from list to the new columns
    purchase_sales_listing[columnname_split[0]] = customernames
    purchase_sales_listing[columnname_split[1]] = vechiclenumber

    #drop the original column from the dataframe
    new_sales_data = purchase_sales_listing.drop(columns=[purchase_sales_listing.columns[0]])


    #export the new dataframe to an excel file
    new_sales_data.to_excel("feature_engineered_sales_listing.xlsx")
    print("Cheers!! Hip Hip HUrray! Your file is converted, kindly check the file and report if any errors!")



print("Hey Raghava, hope you will be get the most out of our work!")

user_filename = input("Enter file location and name with uppercase and lowercase carefully! Consider typing the file format as well")
user_sheetname = input("Enter sheetname to be accessed kindly, with lowercase and uppercase letters.")
feature_engineer(user_filename, user_sheetname)