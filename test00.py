import requests

url = "https://priaid-symptom-checker-v1.p.rapidapi.com/symptoms"

querystring = {"format": "json", "language": "en-gb"}

headers = {
    'x-rapidapi-host': "priaid-symptom-checker-v1.p.rapidapi.com",
    'x-rapidapi-key': "8384a30b45mshd82923e01e66c7fp1d4035jsn9cc1bd51e260"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())
