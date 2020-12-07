import json
import requests
from behave import *
from Config import *
import urllib.request

api = urlconfig.Test_API_URL
ID = urlconfig.Test_ID
PW = urlconfig.Test_PW

########################################################################################################
# @B02.01.관리자_주차장_운영정보_확인
#   Scenario Outline: 주차장 관리 - 입출차 결재 내역 확인
@given('B02.01 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.')
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
        access_Token = response_json['data']['token']
        print(ID + " - accessToken >>> " + access_Token)
        resp = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
        print(resp)

    except Exception as e:
        print(e)

    assert (response_data.status_code == 200)


@when('B02.01 - API 동작 동작시 "{paymentTime}" "{plateNumber}"를 이용하여 입출차 결재 내역을 확인한다.')
def step_impl(context, paymentTime, plateNumber):
    try:
        global REP_Data

        headers = {
            "Authorization": "Bearer " + access_Token
        }

        Test_URL = api + "/parkings/" + parkingUid + "/payments"
        response_data = requests.get(Test_URL, headers=headers)
        REP_Data = json.loads(response_data.text)
        # print(response_data.content)
        #oks = json.dumps(REP_Data, indent=4, sort_keys=False, ensure_ascii=False)
        #print(oks)

        if (response_data.status_code == 200):
            print("### status-code : " + str(response_data.status_code))
            print("### response data OK!")
            Test_Result = True
        else:
            print("### status-code : " + str(response_data.status_code))
            print("### response data Not OK!")
            Test_Result = False

    except Exception as e:
        print(e)
        Test_Result = False

    assert Test_Result


@then('B02.01 - 전달 받은 data에는 "{paymentTime}", "{plateNumber}"를 기준으로 관련 차량 정보가 출력 되어야 한다.')
def step_impl(context, paymentTime, plateNumber):
    #try:
    response_data = REP_Data['data'][0]

    if response_data['payMethodName'] == payMethodName and response_data['uid'] == int(uid) and response_data['payMethod'] == int(payMethod) and response_data['fare'] == int(fare):
        print("### Matched Data! ###")
        print("### Test Pass ###")
        Test_Result = True
    else:
        print("### Test Fail ###")
        Test_Result = False
    result = json.dumps(REP_Data['data'][0], indent=4, sort_keys=False, ensure_ascii=False)
    print(result)
    #except Exception as e:
    #    print(e)
    #    Test_Result = False

    assert Test_Result

