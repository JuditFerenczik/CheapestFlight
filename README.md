# CheapestFlight
Look for cheap flights using API-s

The script reads the data stored on sheety, which contains the previous cheapest fligths data including destination city name we liked to visit and
the lowest flight price to that city. After giving the name of the city where we want to travel from the script looks for the cheapest price in the next 6 months.
If the new search price is less than the one saved on sheety then it updates the lowest price to the new one on sheety and send a message with the flight details
using twilio.
