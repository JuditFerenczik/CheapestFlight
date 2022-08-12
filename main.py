from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt
from twilio.rest import Client
from keys import auth_token, account_sid, FROM_NUMBER, TO_NUMBER

dataset = DataManager()
sheet_data = dataset.getData()
# print(len(sheet_data))
pprint(sheet_data)
# print(sheet_data[1]['iataCode'] =='')
today_date = dt.datetime.now()
flight_search = FlightSearch()
#flight_data = FlightData()
departure_city = input("Where would you like to travel from?")
from_city = flight_search.getDestination(departure_city)
for i in range(0, len(sheet_data)):
    if sheet_data[i]['iataCode'] =='':
        sheet_data[i]['iataCode'] = flight_search.getDestination(sheet_data[i]['city'])
    search_data = {
        "fly_from" : from_city,
        "fly_to": sheet_data[i]['iataCode'],
        "date_from ":str(today_date.date().strftime('%d/%m/%Y')),
        "date_to": str((today_date.date() + dt.timedelta(days=180)).strftime('%d/%m/%Y')),
        "nights_in_dst_from":7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "curr": "EUR"
    }
    # print(search_data)
    result_of_search = flight_search.getFlights(search_data)

    if (not isinstance(result_of_search, int)) and (result_of_search < sheet_data[i]['lowestPrice']):

        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Low price alert! Only {result_of_search}USD to travel from {departure_city} to {sheet_data[i]['city']} \n from to \n From Judy's script",
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )
        print(message.status)
        print(result_of_search)
        sheet_data[i]['lowestPrice'] = result_of_search.price
        print(sheet_data[i]['city'], ": ", result_of_search.price)
    else:
        print(f"No flight to {sheet_data[i]['city']}")
dataset.update_data()
pprint(sheet_data[3])

## TODO: put the twilio API to the notification class after testing