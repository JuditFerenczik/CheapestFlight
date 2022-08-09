import requests
from keys import TE_ENDPOINT, API_KEY


class FlightSearch:

    def getDestination(self, city):
        location_endpoint = f"{TE_ENDPOINT}/locations/query"
        headers = {"apikey": API_KEY}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        iAta = results[0]["code"]
        #print(iAta)
        return iAta