# Use an API to get the current weather data

import requests

API_KEY = "eebf366bfeca8313740b6d9e180f36df"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter the name of a city: ")
request_url = (f"{BASE_URL}?appid={API_KEY}&q={city}")
response = requests.get(request_url)

if response.status_code == 200:
	print("####### data ###########")
	data = response.json()
	print(data)
	print("####### name ###########")
	name = data["name"]
	print(name)
	print("####### weather ###########")
	weather = data["weather"]
	print(weather)
	print("####### description ###########")
	description = data["weather"][0]["description"]
	print(f"The weather in {name} is {description}")
	print("####### temp k ###########")
	temperature_k = data["main"]["temp"]
	print(f"{temperature_k} degrees Kelvin")
	# convert temperature from Kelvin to Fahrenheit
	print("####### temp f ###########")
	temperature_f = temperature_k*(9/5)-459.67
	print(f"{round(temperature_f,0)} degrees Fahrenheit") 
else:
	print("An error occurred.")

