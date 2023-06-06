
import requests
import pandas as pd

# Downloading the data from the provided link
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)

# Converting the data into a pandas dataframe
data = response.json()
df = pd.json_normalize(data["pokemon"])

# Saving the dataframe to an Excel file
df.to_excel("pokemon_data.xlsx", index=False)

print("Data saved to pokemon_data.xlsx")



'''
Explanation :-  This code downloads the data from the provided link using the requests library. 
It then converts the data into a pandas dataframe using the json_normalize() function. 
Finally, it saves the dataframe to an Excel file using the to_excel() function.
'''