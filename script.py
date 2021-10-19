#import certain modules/ packages
import requests
import pandas as pd
import os
import json
import csv 
from dotenv import load_dotenv

load_dotenv()


def request_url(name, key):
    """
        This function is used to compile an accessible DeFi Pulse link using the project name and API key as inputs.
        @param: two parameters are passed to this function. The first is the name
                and is a string. The second is the API key which is a string.
    """
    link = f"https://public.defipulse.com/api/GetHistory?period=1y&project={name}&api-key={key}"
    return link 


#One simple main program

if __name__ == "__main__":
    
    #get key
    API = os.environ.get("API_KEY")
        
    #define column names
    column_names= ["Time", "TVL_USD", "TVL_ETH", "BTC", "ETH", "DAI"]
    
    #Welcome message
    print("Welcome to the DeFi Pulse Data Reader")
    print("")
    print("Currently, this script only pulls TVL")

    project_name = str(input("What project do you want to get TVL history for? "))

    url = str(request_url(project_name, API))

    #Grab data
    response = requests.request("GET", url)
   
    #write to file
    #define file name
    file_name = f"TVLdata_{project_name}.csv" 
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", file_name)


    #parse from the response text into dictionary
    parsed_response = response.json()


    # #write in the items to the file
    with open(csv_filepath, "w") as file:
        writer = csv.DictWriter(file, column_names)
        #write in the headers
        writer.writeheader()

        for data in parsed_response:
            #loop each different timestamp row using this established row format 
                writer.writerow({
                    "Time": data['timestamp'],
                    "TVL_USD": data['tvlUSD'],
                    "TVL_ETH": data['tvlETH'],
                    "BTC": data['BTC'],
                    "ETH": data['ETH'],
                    "DAI": data['DAI'],
                })

    #close file
    file.close()
    