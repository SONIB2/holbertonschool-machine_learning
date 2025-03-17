#!/usr/bin/env python3
import requests
from collections import defaultdict

def get_launch_count_by_rocket():
    """
    Fetches SpaceX launches from the API and counts the number of launches per rocket.
    The result is ordered by the number of launches (descending) and by rocket name (alphabetically) if counts are the same.
    """
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    launches = response.json()

    # Create a dictionary to count launches per rocket
    rocket_count = defaultdict(int)

    for launch in launches:
        rocket_name = launch['rocket']
        rocket_count[rocket_name] += 1

    # Now sort the rockets by count (descending) and by rocket name (alphabetically if counts are equal)
    sorted_rockets = sorted(rocket_count.items(), key=lambda x: (-x[1], x[0]))

    # Print the results in the required format
    for rocket, count in sorted_rockets:
        print(f"{rocket}: {count}")

if __name__ == '__main__':
    get_launch_count_by_rocket()
