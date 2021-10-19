#import certain modules/ packages
import requests
import json 
import os
import csv 

#One simple main program

if __name__ == "__main__":
    
    #get key
    API_KEY = os.environ.get("API_KEY")

    #TVL URL
    url = "https://public.defipulse.com/api/GetHistory?period=1y&project="
    
    #End CSV component
    end_url = "&format=csv&api-key="
    #Welcome message
    print("Welcome to the DeFi Pulse Data Reader")
    print("")
    print("Currently, this script only pulls TVL")

    project_name = input("What project do you want to get TVL history for?")

    #url shaping
    url_project = str(url, project_name)
    url_with_csv = str(url_project, end_url)

    url_to_go = str(url_with_csv, API_KEY)


    #Grab data
    response = requests.get(url_to_go)



