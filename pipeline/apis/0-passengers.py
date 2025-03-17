#!/usr/bin/env python3
"""
Module to fetch available ships from SWAPI.
"""

import requests


def availableShips(passengerCount):
    """
    Returns a list of ships that can hold at least passengerCount passengers.

    Args:
        passengerCount (int): The number of passengers the ship must accommodate.

    Returns:
        list: A list of ship names meeting the criteria.
    """
    url = "https://swapi.dev/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data["results"]:
            passengers = ship["passengers"].replace(",", "").strip()
            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship["name"])

        url = data["next"]

    return ships
