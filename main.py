# geocoding.py

import pandas as pd
import googlemaps
import time
from tqdm import tqdm
try:
    from config import GOOGLE_MAPS_API_KEY, INPUT_FILE, OUTPUT_FILE
except ImportError:
    print("error: can't find config.py file! please ensure the config.py file exists and contains the necessary configuration information.")
    exit(1)

def geocode_addresses(input_file, output_file, api_key):
    """
    read addresses from Excel file and get their latitude and longitude, then save to a new Excel file
    
    Parameters:
    input_file (str): the path of the input Excel file
    output_file (str): the path of the output Excel file
    api_key (str): Google Maps API key
    """
    try:
        # initialize Google Maps client
        gmaps = googlemaps.Client(key=api_key)
        
        # read input file
        df = pd.read_excel(input_file)
        
        # ensure the 'addr' column exists
        if 'addr' not in df.columns:
            raise ValueError("the input file does not contain the 'addr' column")
        
        # create new latitude and longitude columns
        df['lat'] = None
        df['lgt'] = None
        
        # get the latitude and longitude for each address
        for index, row in tqdm(df.iterrows(), total=len(df), desc="processing addresses"):
            try:
                # get the latitude and longitude
                geocode_result = gmaps.geocode(row['addr'])
                
                if geocode_result and len(geocode_result) > 0:
                    location = geocode_result[0]['geometry']['location']
                    df.at[index, 'lat'] = location['lat']
                    df.at[index, 'lgt'] = location['lng']
                else:
                    print(f"warning: can't find the latitude and longitude for the address: {row['addr']}")
                
                # add delay to comply with API limits
                time.sleep(0.1)
                
            except Exception as e:
                print(f"error when processing the address: {row['addr']}: {str(e)}")
                continue
        
        # save the results to a new Excel file
        df.to_excel(output_file, index=False)
        print(f"processing completed! the results have been saved to {output_file}")
        
    except Exception as e:
        print(f"error when executing the program: {str(e)}")

if __name__ == "__main__":
    # run the program
    geocode_addresses(INPUT_FILE, OUTPUT_FILE, GOOGLE_MAPS_API_KEY)