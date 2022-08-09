import requests
from keys import sheety_endpoint,BEARER_TOKEN


class DataManager:
    def __init__(self):
        self.prices = {}

    def getData(self):
        headers_sheety = {
            "Content-Type": "application/json"
        }
        # r = requests.post(sheety_endpoint, json =current_data, headers=headers_sheety, auth=(USERNAME, PASSWORD, ))
        # r.raise_for_status()
        bearer_headers = {
            "Authorization": "Bearer " + BEARER_TOKEN
        }
        r = requests.get(sheety_endpoint, headers=bearer_headers)
        r.raise_for_status()
        data = r.json()
        # pprint(r.json())
        self.prices = data["prices"]
        return self.prices

    def update_data(self):
        for line in self.prices:
            current_data = {
                "price": {
                    "iataCode" : line['iataCode'],
                    "lowestPrice": line["lowestPrice"]
                }
            }
            print(current_data)
            headers_sheety = {
                "Content-Type": "application/json"
            }
            bearer_headers = {
                "Authorization": "Bearer " + BEARER_TOKEN
            }
            ith_sheety_endpoint = sheety_endpoint +"/" + str(line['id'])
            #print(ith_sheety_endpoint)
            r = requests.put(ith_sheety_endpoint, json=current_data, headers=bearer_headers)
            r.raise_for_status()