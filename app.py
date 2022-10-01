import requests 
import json

print("Section Two")

data = requests.get('https://data.cms.gov/data-api/v1/dataset/b35c77ac-26e2-4320-91e1-ba71c4d7ff2c/data')

apiDataset = data.json() 

print(apiDataset)

print("\n\n\n")

