import json
import time
import datetime
import requests
import os
from Config import *
import urllib.request
#from bs4 import BeautifulSoup
#from web_handle import *

api = urlconfig.Test_API_URL
ID = urlconfig.Test_ID
PW = urlconfig.Test_PW

Token_URL = api + "/auth/login"

print('User Token url = ' + Token_URL)

headers = {
    'Content-Type': 'application/json'
}

data = {
    "id": ID,
    "password": PW
}

response_data = requests.post(Token_URL, headers=headers, data=json.dumps(data))
print(response_data.status_code)

response_json = json.loads(response_data.text)
access_Token = response_json['data']['token']
print(ID + " - accessToken >>> " + access_Token)
resp = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
print(resp)
#print(oks)
#print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


headers = {
            "Authorization": "Bearer " + access_Token
        }

test_URL = "http://localhost:3000/api/parkings"
response_data = requests.get(test_URL, headers=headers)
print(response_data.status_code)
All_vehivle = json.loads(response_data.text)

uid_array = []
count = 0
plate = ["10하9088", "20하9099", "30하1010", "40하8250", "50하0102", "60하7174", "70하7174", "80하8888", "90하0001", "10하9900"]


for temp in All_vehivle['data']['rows']:
    if temp['plateNumber'] == plate[count]:
        uid_array.append(temp['uid'])
        count += 1

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
for oks in uid_array:
    test_URL = "http://localhost:3000/api/parkings/" + str(oks)
    response_data = requests.delete(test_URL, headers=headers)
    print(response_data.status_code)
    print("### Delete >>> " + str(oks))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
print(" /mobile/orders ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
headers = {
	"x-access-token": access_token
}

api_url = "https://biz-mobile-api.dev.platdev.net" + "/mobile/orders"
response_data = requests.get(api_url, headers=headers)
response_json = json.loads(response_data.text)
oks = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
print(oks)

print(" /mobile/orderHistories ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
headers = {
	"x-access-token": access_token
}

api_url = "https://biz-mobile-api.dev.platdev.net" + "/mobile/orderHistories"
response_data = requests.get(api_url, headers=headers)
response_json = json.loads(response_data.text)
oks = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
print(oks)

print(" /mobile/business/orderDetail ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
headers = {
	"x-access-token": access_token,
    "orderId": "OCT00000037"
}

api_url = "https://biz-mobile-api.dev.platdev.net" + "/mobile/business/orderDetail"
response_data = requests.get(api_url, headers=headers)
response_json = json.loads(response_data.text)
oks = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
print(oks)

print(" /mobile/business/orderDetail ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
headers = {
	"x-access-token": access_token,
    "orderId": "OCM00000014"
}

api_url = "https://biz-mobile-api.dev.platdev.net" + "/mobile/business/drivingDetail"
response_data = requests.get(api_url, headers=headers)
response_json = json.loads(response_data.text)
oks = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
print(oks)

print(" /mobile/business/carList  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
headers = {
	"x-access-token": access_token
}

api_url = "https://biz-mobile-api.dev.platdev.net" + "/mobile/business/carList"
response_data = requests.get(api_url, headers=headers)
response_json = json.loads(response_data.text)
oks = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
print(oks)

print(" /mobile/personal/personalCar  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
headers = {
	"x-access-token": access_token
}

api_url = "https://biz-mobile-api.dev.platdev.net" + "/mobile/personal/personalCar"
response_data = requests.get(api_url, headers=headers)
response_json = json.loads(response_data.text)
oks = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
print(oks)

print(" /mobile/personal/subscriptionProductList  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
headers = {
	"x-access-token": access_token
}

api_url = "https://biz-mobile-api.dev.platdev.net" + "/mobile/personal/subscriptionProductList"
response_data = requests.get(api_url, headers=headers)
response_json = json.loads(response_data.text)
oks = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
print(oks)
"""