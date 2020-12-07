import json
import requests
from behave import *
from Config import *
import urllib.request

api = urlconfig.Test_API_URL
ID = urlconfig.Test_ID
PW = urlconfig.Test_PW

########################################################################################################
# @A05_GET_parkings_parkingUid_payments
#   Scenario Outline: GET parkings/{parkingUid}/payments 동작 확인
@given('A05.01 - API Test를 위한 서버가 준비되어 있고 ID, PW를 이용하여 access Token 데이터를 전달 받았다.')
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


@when('A05.01 - access Token를 이용하여 GET parkings/{"{parkingUid}"}/payments API 동작을 수행 후, response data를 정상적으로 전달 받아야 한다.')
def step_impl(context, parkingUid):
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


@then('A05.01 - 전달받은 response data 결과와 "{payMethodName}", "{uid}", "{payMethod}", "{fare}"의 정보는 동일 해야 한다.')
def step_impl(context, payMethodName, uid, payMethod, fare):
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

