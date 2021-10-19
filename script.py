#import certain modules/ packages
import requests
import json 
import os
import csv 


def request_url(ticker, API_key):
    """
        This function is used to compile an accessible DeFi Pulse link using the ticker and API key as inputs.
        @param: two parameters are passed to this function. The first is the ticker 
                and is a string. The second is the API key which is a string.
    """
    link = f"https://public.defipulse.com/api/GetHistory?period=1y&{ticker}=all&format=csv&api-key={API_key}"
    return link 


#One simple main program

if __name__ == "__main__":
    
    #get key
    API_KEY = os.environ.get("API_KEY")
    
    #Welcome message
    print("Welcome to the DeFi Pulse Data Reader")
    print("")
    print("Currently, this script only pulls TVL")

    project_ticker = str(input("What project do you want to get TVL history for? (Input ticker) "))

    url = request_url(project_ticker, API_KEY)

    #Grab data
    response = requests.get(url)



