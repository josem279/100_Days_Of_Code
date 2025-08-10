import os
import requests
from datetime import datetime

# Nutritionix
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

GENDER = "male"
WEIGHT_KG = "66"
HEIGHT_CM = "166"
AGE = 29

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Please describe the exercise you performed and for how long you performed the exercise:")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(
  exercise_endpoint, 
  json=parameters, 
  auth=(
      USERNAME, 
      PASSWORD,
  )
)
result = response.json()

################### Start of Step 4 Solution ######################
username = "a5e4303ef798beb154012cb04e6837b6"
projectName = "myWorkoutsTracker"
sheetName = "workouts"

sheet_endpoint = f"https://api.sheety.co/{username}/{projectName}/{sheetName}"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)