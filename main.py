import requests
from datetime import datetime

GENDER = "_YOUR_GENDER_"
WEIGHT_IN_KG = YOUR_WEIGHT
HEIGHT_IN_CM = YOUR_HEIGHT
AGE = YOUR_AGE

APP_ID = "YOUR_APPID"
API_KEY  = "YOUR_API_KEY"

exercise_input = input("Tell me what exercise you did today: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_IN_KG,
    "height_cm": HEIGHT_IN_CM,
    "age": AGE
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
