import json
import requests
from behave import *
from Config import *
import urllib.request

api = urlconfig.Test_API_URL
ID = urlconfig.Test_ID
PW = urlconfig.Test_PW

########################################################################################################
# @A01_GET_parkings
#   Scenario Outline: GET parkings 동작 확인
@given('A01.01 - API Test를 위한 서버가 준비되어 있고 ID, PW를 이용하여 access Token 데이터를 전달 받았다.')
def step_impl(context):
    try:
        # API 동작에 필요한 Token 설정 진행 #################################################
        global access_Token

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
        access_Token = response_json['data']['tooken']
        print(ID + " - accessToken >>> " + access_Token)
        resp = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
        print(resp)

    except Exception as e:
        print(e)

    assert (response_data.status_code == 200)


@when('A01.01 - access Token를 이용하여 GET parkings API 동작을 수행 후, response data를 정상적으로 전달 받아야 한다.')
def step_impl(context, groupId, category, paymentTime, paymentMethod, rightType, billingStartDay, billingEndDay):
    #try:

    #except Exception as e:
    #    print(e)
    #    Test_Result = False

    assert True


@then('A01.01 - 전달받은 response data 결과중 "<uid>", "<platenumber>"의 정보가 포함된 내용이 있어야 한다.')
def step_impl(context):
    #try:

    #except Exception as e:
    #    print(e)
    #    Test_Result = False

    assert True

