# Importing necessary libraries
import os
import json
import csv

# Function to read the apod data and returns a dictionaries contaning the APOD data
def read_apod_data():
    
    file_name = 'apod_data.json'
    
    #Using an try-except block to handle any exceptional errors
    try:
        # Opening the json file and loading its content
        with open(file_name, 'r') as file:
            data = json.load(file) # Loading json content in a python object
            
            # Checking if the file is empty
            if not data:
                print('File is empty')
                return []
            
            # Looping throught the data and printing date and title for each country
            for entry in data:
                print(f'Date: {entry.get('media_date')}, Title: {entry.get('media_title')}')
                
            return data #Returning the data
            
    except FileNotFoundError: #Handling errors where the file doesn't exists
        
        print(f'Error: {file_name} not found')
        return []
    
    except PermissionError: #Handling errors where the permission is denied
        
        print(f'Error: Permission denied for file {file_name}')
        return []
    
    except json.JSONDecodeError: #Handling errors where the file is not a valid json
        
        print(f'Error: {file_name} contains a invalid json')
        return []
    

# Function to Process and summarize the data
def analyze_apod_media(data):
    # Initializations of variables
    video_count = 0
    image_count = 0
    biggest_explanation = ''
    lattest_date = None

    # Looping throught the data to analyze
    for entry in data:
        # Counting medias based on its type
        if entry.get('media_type') == 'image':
            image_count += 1
        elif entry.get('media_type') == 'video':
            video_count += 1
    
        # Cheking the biggest expanation
        explanation = entry.get('media_explanation', '')
        if len (explanation) > len(biggest_explanation):
            biggest_explanation = explanation
            lattest_date = entry.get('media_date')
        
    # Printing the analyzis
    print(f'Total videos: {video_count}')
    print(f'Total image: {image_count}')     
    if lattest_date:
        print(f'The biggest explanation is from {lattest_date} with {len(biggest_explanation)} chacacters')
        
# Function that writes a summary APOD data to a csv file
def write_summary_to_csv(data):
    
    file_name = 'apod_summary.csv'
    
    # Defining the headers for the csv file
    headers = ['Date', 'Title', 'Media Type', 'URL']
    
    #Using an try-except block to handle any exceptional errors
    try:
        # Checking if the csv file already exixts
        file_exixts = os.path.exists(file_name)
        
        # Opening and appeding the file in case it exists, if not, creating it
        with open(file_name, 'a', newline='', encoding='utf-8') as file:
            write = csv.writer(file)
            
            # Writing headers if it is a new file
            if not file_exixts:
                write.writerow(headers)
                
            # Looping through the data and writing the entries
            for entry in data:
                write.writerow([
                    entry.get('media_date', None),
                    entry.get('media_title', None),
                    entry.get('media_type', None),
                    entry.get('media_url', None)
                ])  
        print(f'Data successfully written to {file_name}')
        
    except IOError as e:
        print(f'Error writing to {file_name}: {e}')
        
# Running the program
if __name__ == '__main__':
    # Readind and loading json data
    apod_data = read_apod_data()
    
    # Checking if the loading of the data was successull
    if apod_data:
        # Analazing and summarizing the data
        analyze_apod_media(apod_data)
        
        # Writing the summary data to a csv file
        write_summary_to_csv(apod_data)
            