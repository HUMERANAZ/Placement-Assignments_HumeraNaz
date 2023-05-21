#Ans 4.

import requests
import pandas as pd

def download_data(url):
    # Make a GET request to download the JSON data
    response = requests.get(url)
    data = response.json()
    
    return data

def convert_to_dataframe(data):
    # Convert JSON data to DataFrame
    df = pd.DataFrame(data)
    
    # Convert 'mass', 'reclate','reclong' columns to float
    df["mass"] = df["mass"].astype(float)
    df["reclat"] = df["reclat"].astype(float)
    df["reclong"] = df["reclong"].astype(float)
    
    #convert 'year' column to datetime format
    df['year'] = pd.to_datetime(df['year'], errors='coerce')
    
    #Renameing of columns
    df = df.rename(columns={'name': 'Name of Earth Meteorite',
                            'id':'ID of Earth Meteorite',
                            'year':'Year at which Earth Meteorite was hit'})
    
    #creating cordinate list 
    coordinates_list = []
    for coor in range(1000):  # Iterate 1000 times
        if coor < len(df):
            geolocation = df["geolocation"][coor]
            if isinstance(geolocation, dict):
                coordinates = geolocation.get('coordinates')
                if isinstance(coordinates, list):
                    a = [int(coordinates[0]), int(coordinates[1])]
                    coordinates_list.append(a)
            else:
                coordinates_list.append([0, 0])
        else:
            coordinates_list.append([0, 0])
    
    #Creating point coordinates columns in dataframe and assigning coordinate_list values to it
    df['point coordinates'] = coordinates_list
    
    #Drop extra columns from dataframe
    df = df.drop([':@computed_region_cbhk_fwbd','geolocation',':@computed_region_nnqa_25f4'], axis=1)
    
    return df


def save_as_csv(df, output_file):
    # Save the DataFrame as a CSV file
    df.to_csv(output_file, index=False)

# Define the URL of the JSON data and output file path
url = "https://data.nasa.gov/resource/y77d-th95.json"
output_file = "meteorite_data.csv"

# Download the data
data = download_data(url)

# Convert data to DataFrame
df = convert_to_dataframe(data)

# Save DataFrame as CSV
save_as_csv(df, output_file)

print("CSV file saved successfully.")