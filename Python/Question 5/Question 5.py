import requests
import json
import pandas as pd
from bs4 import BeautifulSoup


# Define the API endpoint
api_url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Send a GET request to the API endpoint
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON data
    data = json.loads(response.text)

    # Extract the required attributes from the data
    show_id = data["id"]
    show_url = data["url"]
    show_name = data["name"]
    episodes = data["_embedded"]["episodes"]

    # Initialize lists to store the extracted data
    episode_data = []
    column_names = [
        "Episode ID",
        "Show ID",
        "Show URL",
        "Episode URL",
        "Show Name",
        "Episode Name",
        "Season",
        "Episode Number",
        "Type",
        "Airdate",
        "Airtime",
        "Runtime",
        "Average Rating",
        "Summary",
        "Medium Image Link",
        "Original Image Link",
    ]

    # Iterate over each episode and extract the attributes
    for episode in episodes:
        episode_id = episode["id"]
        episode_url = episode["url"]
        episode_name = episode["name"]
        episode_season = episode["season"]
        episode_number = episode["number"]
        episode_type = episode["type"]
        episode_airdate = episode["airdate"]
        episode_airtime = episode["airtime"]
        episode_runtime = episode["runtime"]
        episode_rating = episode["rating"]["average"]

        episode_summary = episode["summary"]
        # Remove HTML tags from the summary using BeautifulSoup
        soup = BeautifulSoup(episode_summary, "html.parser")
        episode_summary = soup.get_text()

        episode_image_medium = episode["image"]["medium"]
        episode_image_original = episode["image"]["original"]

        # Create a dictionary to store the episode data
        episode_dict = {
            "Episode ID": episode_id,
            "Show ID": show_id,
            "Show URL": show_url,
            "Episode URL":episode_url,
            "Show Name": show_name,
            "Episode Name": episode_name,
            "Season": episode_season,
            "Episode Number": episode_number,
            "Type": episode_type,
            "Airdate": episode_airdate,
            "Airtime": episode_airtime,
            "Runtime": episode_runtime,
            "Average Rating": episode_rating,
            "Summary": episode_summary,
            "Medium Image Link": episode_image_medium,
            "Original Image Link": episode_image_original,
        }

        # Append the episode data dictionary to the list
        episode_data.append(episode_dict)

    # Create a DataFrame from the episode data
    df = pd.DataFrame(episode_data, columns=column_names)

   
    
    # Save DataFrame as CSV
    output_file = "tvmaze1.csv"
    df.to_csv(output_file, index=False)
    
    # Print the formatted DataFrame
    #print(df)
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
