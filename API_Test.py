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
auth_key = urlconfig.Test_Auth
access_key = auth_key
WebBrowser = []

print(" /billing-service/v1/paymentMethodInfo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#print(access_key)
headers = {
	"Authorization": access_key
}
params = {
	"Authorization": access_key
}


#api_url = "https://api-staging.raidea.io" + "/billing-service/v1/paymentMethodInfo"
api_url = "https://api-staging.raidea.io" + "/booking-service/carPlat/v1/coDrivers"
print('GET url = ' + api_url)

response_data = requests.get(api_url, headers=headers)

print(response_data.status_code)
response_json = json.loads(response_data.text)
oks = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
#print(oks)
#print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

for temp in response_json['result']['data']:
    if(temp['groupId'] == "API_TEST1" or temp['groupId'] == "API_TEST2" or temp['groupId'] == "API_TEST3" or temp['groupId'] == "API_TEST4"):
        #oks = json.dumps(temp, indent=4, sort_keys=False, ensure_ascii=False)
        #print(oks)
        api_url = "https://api-staging.raidea.io" + "/booking-service/carPlat/v1/coDrivers/" + temp['coDriverId']
        response_data = requests.get(api_url, headers=headers)
        response_json = json.loads(response_data.text)
        oks = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
        print(oks)
        print("===========================================================================================")
        response_data = requests.delete(api_url, headers=headers)
        response_json = json.loads(response_data.text)
        oks = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
        print(oks)
        #print("delete >>> " + response_data.text)
    else:
        print("not found!")

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