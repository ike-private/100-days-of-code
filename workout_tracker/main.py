import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
BEAVER_TOKEN = os.getenv("BEAVER_TOKEN")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    "x-remote-user-id" : "Ikeoluwa"
}
workout_endpoint = os.getenv("NUTRITIONIX_ENDPOINT")
sheety_endpoint = os.getenv("SHEETY_WORKOUT_ENDPOINT")

exercise_input = input("Tell which exercise you did today?: ")
GENDER = "FEMALE"
WEIGHT_KG = "80"
HEIGHT = "170" #entered random height in cm
AGE = "24"
parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}
now = dt.datetime.now()
date = now.strftime("%x")
time = now.strftime("%X")

response = requests.post(url=workout_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(result)

beaver_header = {"Authorization": f"Bearer {BEAVER_TOKEN}"}
output = {
    "workout":{
        "date": date,
        "time": time,
        "exercise": result['exercises'][0]['name'],
        "duration": result['exercises'][0]['duration_min'] ,
        "calories": result['exercises'][0]['nf_calories']
    }
}

sheety_response = requests.post(url=sheety_endpoint, json=output, headers=beaver_header)
print(sheety_response.text)
