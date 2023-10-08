import requests
import json

api = "ue9ZT35hp6gakjpLGV3BlgScm6L4JNaJMHePw8TN"
desired_date = "2023-09-29"

params = {
    "api_key": api,
    "date": desired_date
    # You can specify additional parameters here if needed, such as date, hd, etc.
}

apod_url = "https://api.nasa.gov/planetary/apod"


response = requests.get(apod_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    apod_data = response.json()

    response_text = response.text.lstrip('\ufeff')
    apod_data = json.loads(response_text)

    # Print the information
    print("Title:", apod_data["title"])
    print("Date:", apod_data["date"])
    print("Explanation:", apod_data["explanation"])
    print("URL:", apod_data["url"])

else:
    print("Failed to retrieve APOD data. Status code:", response.status_code)
