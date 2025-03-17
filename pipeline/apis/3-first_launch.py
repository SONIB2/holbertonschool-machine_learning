#!/usr/bin/env python3
import requests
from datetime import datetime

def get_first_launch():
    # SpaceX API URL for launches
    url = "https://api.spacexdata.com/v4/launches"
    
    # Make an HTTP GET request to the SpaceX API to fetch launch data
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data from SpaceX API")
        return

    # Get the list of launches from the response
    launches = response.json()

    # Sort the launches by the 'date_unix' field (ascending)
    launches.sort(key=lambda launch: launch['date_unix'])

    # Get the first launch
    first_launch = launches[0]

    # Debugging: print the first launch to inspect its structure
    print("First Launch Data:", first_launch)

    try:
        launch_name = first_launch['name']
        launch_date = datetime.utcfromtimestamp(first_launch['date_unix']).strftime('%Y-%m-%dT%H:%M:%S%z')
        
        # Fetch rocket information using the rocket ID
        rocket_id = first_launch['rocket']
        rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
        rocket_response = requests.get(rocket_url)
        rocket_name = rocket_response.json().get('name', 'Unknown Rocket')

        # Fetch launchpad information using the launchpad ID
        launchpad_id = first_launch['launchpad']
        launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
        launchpad_response = requests.get(launchpad_url)
        launchpad_data = launchpad_response.json()
        launchpad_name = launchpad_data.get('name', 'Unknown Launchpad')
        launchpad_locality = launchpad_data.get('locality', 'Unknown Locality')

        # Print the result in the required format
        print(f"{launch_name} ({launch_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})")
    
    except KeyError as e:
        print(f"Error: Missing key {e} in launch data.")
    except TypeError as e:
        print(f"Error: Type error - {e}")

if __name__ == '__main__':
    get_first_launch()
