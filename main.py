import requests
from datetime import datetime

GENDER = "YOUR_GENDER"
WEIGHT_IN_KG = YOUR_WEIGHT
HEIGHT_IN_CM =  YOUR_HEIGHT
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
#-------------Step2------
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheety_endpoint = "https://api.sheety.co/331582b0270ee0406a0838223a682e5f/myWorkouts/workouts"
print(result['exercises'])
for i in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)
    print(sheet_response.text)
