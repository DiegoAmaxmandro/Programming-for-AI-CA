# Importing necessary libraries for API requests, data handling and time manipulation
import requests # type: ignore
import os
import json
import time
from datetime import datetime, timedelta


# Creating a functions to retrieve data from Nasa APOD API
# This function will return a dictionary with the relevant data information retrieved from the APOD API
# It extracts relevant data as date, title, url, description and type
def get_apod_data(api_key, date):
    
    base_url = 'https://api.nasa.gov/planetary/apod' # API endpoint
    parameters = {
        'api_key' : api_key, # API key for authentication
        'date': date, # Date for which APOD data requested
    }
    
    #Using an try-except block to handle any exceptional errors
    try:
        response = requests.get(base_url, params= parameters) # Sending the GET request
        response.raise_for_status() # Raise an exception status error 
        data = response.json() # Parse the json response
        
        # Retrieving the relevant data informations from the API
        apod_informations = {
            'media_date' : data.get('date'),
            'media_title' : data.get('title'),
            'media_url' : data.get('url'),
            'media_explanation': data.get('explanation'),
            'media_type' : data.get('media_type'),
            
        }
        return apod_informations # Returning the data retrieved
    
    # Cathing exceptions and printing a error message
    except requests.exceptions.RequestException as e: 
        print (f'Error fetching Apod data for {date} : {e}')
        return None
    
# Creatng function to retrieve APOD data for all dates within a large enough date range    
def fetch_multiple_apod_data(api_key, start_date, end_date):
    
    # Converting string to object data
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    #Define the name of teh jason file to store the APOD data
    file_name = 'apod_data.json'
    
    #Iterating through the range of dates, it loops through each day in the date range
    for n in range((end_date - start).days + 1):
        date = (start + timedelta(days=n)).strftime('%Y-%m-%d') # Calculate the current date in the range and format it as a string
        apod_data = get_apod_data(api_key, date) # Fetching APOD data for the current date using the get_apod_data function
        
        # Proceed only if the data was retrieved
        if apod_data:
            try:
                if not os.path.exists(file_name): # Checking if the file already exists
                    # If the file doesn't exists, it is created and it write as the first entrt as a list
                    with open(file_name, 'w') as file:
                        json.dump([apod_data], file, indent= 4)
                else:
                    # If the file exists, it reads the existing data and append a new data and then write it back
                    with open(file_name, 'r+') as file:
                        existing_data = json.load(file) #Load the existing json from the file 
                        existing_data.append(apod_data) # Append the new data to the list
                        file.seek(0) # It moves the file pointer to the beginning of the file 
                        json.dump(existing_data, file, indent= 4) # It writes the updated list back to the file
            # Handling any error that may occour            
            except IOError as e: 
                print(f'Error writing to file {file_name} : {e}')
                
        # Adding a 1 second delay between requests
        time.sleep(1)
        
# Main program entry point
if __name__ == '__main__':
    # Retrieving the API key from the environment variable
    api_key = os.getenv('API_KEY')
    
    # Checking if the API key is present
    if not api_key:
        print('API key not found.')
    else:
        # Feching data
        fetch_multiple_apod_data(api_key, '2020-01-01', '2020-12-31')
        print('Data retrieval completed.')