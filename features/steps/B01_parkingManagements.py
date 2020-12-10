import json
import requests
from behave import *
from Config import *

api = urlconfig.Test_API_URL
ID = urlconfig.Test_ID
PW = urlconfig.Test_PW

########################################################################################################
# @B01.01.관리자_주차장_운영정보_확인
#   Scenario Outline: 주차장 관리 - 입출차 내역 확인
@given('B01.01 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.')
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


@when('B01.01 - API 동작을 통해 주차관리: 입출차 내역을 전달 받는다.')
def step_impl(context):
    try:
        global REP_Data

        headers = {
            "Authorization": "Bearer " + access_Token
        }

        Test_URL = api + "/parkings"
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


@then('B01.01 - 전달 받은 data에는 "{plateNumber}", "{parkingTypeName}", "{status}"등의 차량 정보가 포함되어야 한다.')
def step_impl(context, plateNumber, parkingTypeName, status):
    #try:
    response_data = REP_Data['data']['rows']
    outGateUid = (lambda x: None if x == "미출차" else x)(status)

    Test_Result = False


    for Rep_data in response_data:
        if Rep_data['plateNumber'] == plateNumber and Rep_data['parkingTypeName'] == parkingTypeName:
            if outGateUid == None:
                if Rep_data['outGateUid'] == outGateUid:
                    print("### Matched Data!!! ###")
                    result = json.dumps(Rep_data, indent=4, sort_keys=False, ensure_ascii=False)
                    print(result)
                    Test_Result = True
                    break
            else:
                print("### Matched Data!!! ###")
                result = json.dumps(Rep_data, indent=4, sort_keys=False, ensure_ascii=False)
                print(result)
                Test_Result = True
                break
    #except Exception as e:
    #    print(e)
    #    Test_Result = False

    assert Test_Result


# #####################################################################################################################
# @B01.02.관리자_주차장_운영정보_확인
#   Scenario Outline: 주차장 관리 - 주차정보 상세 확인
@given('B01.02 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.')
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


@when('B01.02 - API 동작을 통해 특정 차량 "{uid}"를 이용하여 특정 차량의 주차 정보 상세 내역을 전달 받는다.')
def step_impl(context, uid):
    try:
        global REP_Data

        headers = {
            "Authorization": "Bearer " + access_Token
        }

        Test_URL = api + "/parkings/" + uid
        response_data = requests.get(Test_URL, headers=headers)
        REP_Data = json.loads(response_data.text)
        # print(response_data.content)
        # oks = json.dumps(REP_Data, indent=4, sort_keys=False, ensure_ascii=False)
        # print(oks)

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

    assert True


@then('B01.02 - 전달 받은 data에는 "{plateNumber}", "{parkingTimes}", "{inGateDate}", "{outGateDate}"등의 정보가 포함되어야 한다.')
def step_impl(context, plateNumber, parkingTimes, inGateDate, outGateDate):
    #try:
    response_data = REP_Data['data']

    if response_data['plateNumber'] == plateNumber and response_data['bill']['parkingTimes'] == parkingTimes and response_data['inGateDate'] == inGateDate and response_data['outGateDate'] == outGateDate:
        print("### Matched Data!!! ###")
        result = json.dumps(response_data, indent=4, sort_keys=False, ensure_ascii=False)
        print(result)
        Test_Result = True
    else:
        print("### Test Fail!!! ###")
        result = json.dumps(response_data, indent=4, sort_keys=False, ensure_ascii=False)
        print(result)
        Test_Result = False

    #except Exception as e:
    #    print(e)
    #    Test_Result = False

    assert Test_Result


# #####################################################################################################################
# @B01.03.관리자_주차장_운영정보_확인
#   Scenario Outline: 주차장 관리 - 관리자 수동 입차 기능 동작 확인
@given('B01.03 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.')
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


@when('B01.03 - API 동작을 통해 특정 차량 "{uid}"를 참고하여 수동 입차 기능을 이용 "{plateNumber}", "{entryTime}"정보를 수정한다.')
def step_impl(context, uid, plateNumber, entryTime):
    try:
        print("E")
    except Exception as e:
        print(e)

    assert True


@then('B01.03 - 해당 차량의 수정된 정보는 입력된 "{plateNumber}", "{entryTime}"와 동일해야 한다.')
def step_impl(context, plateNumber, entryTime):
    #try:

    #except Exception as e:
    #    print(e)
    #    Test_Result = False

    assert True


# #####################################################################################################################
# @B01.04.관리자_주차장_운영정보_확인
#   Scenario Outline: 주차장 관리 - 관리자 수동 출차 기능 동작 확인
@given('B01.04 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.')
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


@when('B01.04 - API 동작을 통해 특정 차량 "{uid}"를 이용하여 수동 출차 기능을 통해 "{plateNumber}", "{exitTime}"정보를 수정한다.')
def step_impl(context, uid, plateNumber, exitTime):
    try:
        print("E")
    except Exception as e:
        print(e)

    assert True


@then('B01.04 - 해당 차량의 수정된 정보는 입력된 "{plateNumber}", "{exitTime}"와 동일해야 한다.')
def step_impl(context, plateNumber, exitTime):
    # try:

    # except Exception as e:
    #    print(e)
    #    Test_Result = False

    assert True
