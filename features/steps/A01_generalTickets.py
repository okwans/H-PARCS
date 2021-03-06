import json
import requests
from behave import *
from Config import *
import datetime

api = urlconfig.Test_API_URL
ID = urlconfig.Test_ID
PW = urlconfig.Test_PW

########################################################################################################
# @A01.01.차량_입출차_동작_확인-일반차량
#   Scenario Outline: 차량 입출차 동작 확인(일반 차량)
@given('A01.01 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.')
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
        #print(response_data.status_code)

        response_json = json.loads(response_data.text)
        access_Token = response_json['data']['token']
        #print(ID + " - accessToken >>> " + access_Token)
        resp = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
        #print(resp)

    except Exception as e:
        print(e)

    assert (response_data.status_code == 200)


@when('A01.01 - 차량 입고시간은 현재시간 기준 "{entryTime}"분 전에 입차되는 형태로 "{plateNumber}" 차량을 API를 통해 설정한다.')
def step_impl(context, entryTime, plateNumber):
    try:
        global Test_Uid

        headers = {
            "Authorization": "Bearer " + access_Token
        }

        data = {
            "machineCode": "PM0001",
            "plateNumber": plateNumber,
            "cameraType": "1",
            "eventId": "0",
            "plateImg": "test" # 별도 이미지는 첨부하지 않음
        }

        # 먼저 /gate/vehicle/in을 이용하여 차량 입차 동작을 수행
        Test_URL = api + "/gate/vehicle/in"
        response_data = requests.post(Test_URL, headers=headers, data=data)
        VehicleIn = json.loads(response_data.text)
        # print(response_data.content)
        oks = json.dumps(VehicleIn, indent=4, sort_keys=False, ensure_ascii=False)
        print(oks)

        if (response_data.status_code == 200):
            print("### status-code : " + str(response_data.status_code))
            print("### response data OK!")
            Test_Result = True
        else:
            print("### status-code : " + str(response_data.status_code))
            print("### response data Not OK!")
            raise Exception("### response data Not OK!")

        # 입차 동작을 수행한 차량의 plateNumber를 이용하여 uid를 확인
        Test_URL = api + "/parkings"
        response_data = requests.get(Test_URL, headers=headers)
        All_vehivle = json.loads(response_data.text)

        # match되는 plateNumber가 있을 경우 해당 uid를 확인
        for temp in All_vehivle['data']['rows']:
            if temp['plateNumber'] == plateNumber:
                Test_Uid = temp['uid']
                break

        # 확인된 uid를 이용하여 입차 시간을 entryTime 만큼 변경
        Test_URL = api + "/parkings/" + str(Test_Uid)

        # 현재 시간을 기준으로 만큼 entryTime 만큼 이전으로 수정
        current = datetime.datetime.now()
        temp_CarInTime = current - datetime.timedelta(minutes=int(entryTime))
        CarInTime = temp_CarInTime.strftime('%Y-%m-%d %H:%M:%S')
        print("### Change inGateDate >>> " + CarInTime)

        data = {
            "inGateDate": CarInTime
        }

        response_data = requests.put(Test_URL, headers=headers, data=data)
        VehicleIn = json.loads(response_data.text)
        oks = json.dumps(VehicleIn, indent=4, sort_keys=False, ensure_ascii=False)
        print(oks)


    except Exception as e:
        print(e)
        Test_Result = False

    assert Test_Result


@then('A01.01 - 해당 차량 출차시 주차시간이 회차시간 미만일 경우 요금 정산은 이뤄지지 않고 회차 시간 이상일 경우 over되는 시간 만큼 요금 "{bill}"원을 결재해야 한다.')
def step_impl(context, bill):
    #try:
    headers = {
        "Authorization": "Bearer " + access_Token
    }

    # 먼저 /parkings/{uid}/bill API를 이용하여 차량 주차 요금이 정의된 사향과 맞는지 확인
    Test_URL = api + "/parkings/" + str(Test_Uid) + "/bill"
    response_data = requests.get(Test_URL, headers=headers)
    Car_Bill = json.loads(response_data.text)
    # print(response_data.content)
    oks = json.dumps(Car_Bill, indent=4, sort_keys=False, ensure_ascii=False)
    print(oks)

    if int(Car_Bill['data']['finalPrice']) == int(bill):
        print("### Actual Price >>> " + str(Car_Bill['data']['finalPrice']) + " ::: Expected Price >>> " + str(bill))
        print("### Pass - matched data OK!")
        Test_Result = True
    else:
        print("### Actual Price >>> " + str(Car_Bill['data']['finalPrice']) + " ::: Expected Price >>> " + str(bill))
        print("### Fail - Not matched data!")
        Test_Result = False

    # Test 종료 후, 생성한 Data는 삭제
    Test_URL = api + "/parkings/" + str(Test_Uid)
    response_data = requests.delete(Test_URL, headers=headers)

    #except Exception as e:
    #    print(e)
    #    Test_Result = False

    assert Test_Result


# #####################################################################################################################
# @A01.02.차량_입출차_동작_확인-일반차량
#   Scenario Outline: 차량 입출차 동작 확인(일반 차량) - 사전정산 완료 후, 출차 동작 확인
@given('A01.02 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.')
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
        #print(response_data.status_code)

        response_json = json.loads(response_data.text)
        access_Token = response_json['data']['token']
        print(ID + " - accessToken >>> " + access_Token)
        resp = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
        #print(resp)

    except Exception as e:
        print(e)

    assert (response_data.status_code == 200)


@when('A01.02 - 차량 입고시간은 현재시간 기준 "{inGateDate}"과 "{overTime}"분 전에 입차되는 형태로 "{plateNumber}" 차량을 API를 통해 설정한다.')
def step_impl(context, inGateDate, overTime, plateNumber):
    try:
        global Test_Uid, CarOverTime, CarEntryTime

        headers = {
            "Authorization": "Bearer " + access_Token
        }

        data = {
            "machineCode": "PM0001",
            "plateNumber": plateNumber,
            "cameraType": "1",
            "eventId": "0",
            "plateImg": "test" # 별도 이미지는 첨부하지 않음
        }

        # 먼저 /gate/vehicle/in을 이용하여 차량 입차 동작을 수행
        Test_URL = api + "/gate/vehicle/in"
        response_data = requests.post(Test_URL, headers=headers, data=data)
        VehicleIn = json.loads(response_data.text)
        # print(response_data.content)

        print(">>> 차량 입차 >>>>>>>>>>>>>>>>")
        oks = json.dumps(VehicleIn, indent=4, sort_keys=False, ensure_ascii=False)
        print(oks)

        if (response_data.status_code == 200):
            print("### status-code : " + str(response_data.status_code))
            print("### response data OK!")
            Test_Result = True
        else:
            print("### status-code : " + str(response_data.status_code))
            print("### response data Not OK!")
            raise Exception("### response data Not OK!")

        # 입차 동작을 수행한 차량의 plateNumber를 이용하여 uid를 확인
        Test_URL = api + "/parkings"
        response_data = requests.get(Test_URL, headers=headers)
        All_vehivle = json.loads(response_data.text)

        # match되는 plateNumber가 있을 경우 해당 uid를 확인
        for temp in All_vehivle['data']['rows']:
            if temp['plateNumber'] == plateNumber:
                Test_Uid = temp['uid']
                break

        # 확인된 uid를 이용하여 입차 시간을 inGateDate + overTime 만큼 변경
        Test_URL = api + "/parkings/" + str(Test_Uid)

        # 현재 시간을 기준으로 만큼 entryTime 만큼 이전으로 수정
        current = datetime.datetime.now()
        temp_CarInTime = current - datetime.timedelta(minutes=(int(inGateDate) + int(overTime)))
        CarInTime = temp_CarInTime.strftime('%Y-%m-%d %H:%M:%S')
        print("### Change inGateDate >>> " + CarInTime)

        # overTime 만큼에 대한 시간도 설정
        temp_CarInTime = current - datetime.timedelta(minutes=int(overTime))
        CarOverTime = temp_CarInTime.strftime('%Y-%m-%d %H:%M:%S')
        print("### overTime >>> " + CarOverTime)

        data = {
            "inGateDate": CarInTime
        }

        response_data = requests.put(Test_URL, headers=headers, data=data)
        VehicleIn = json.loads(response_data.text)
        print(">>> 차량 입차 시간 수정 >>>>>>>>>>>>>>>>")
        oks = json.dumps(VehicleIn, indent=4, sort_keys=False, ensure_ascii=False)
        print(oks)

        CarEntryTime = inGateDate

    except Exception as e:
        print(e)
        Test_Result = False

    assert Test_Result


@when('A01.02 - 출차 동작 전 사전 정산을 통해 주차 요금을 납부완료 한다.')
def step_impl(context):
    try:
        Car_Payment = 0
        CarRemainderTime = int(CarEntryTime)

        # 먼저 inGateDate의 시간을 통해 사전 정산시 지불해야 하는 비용을 확인
        if (CarRemainderTime // 1440) > 0:
            temp_pay = divmod(CarRemainderTime, 1440)
            Car_Payment += temp_pay[0] * 20000
            CarRemainderTime = temp_pay[1]
            print("# overday! #")

        if (CarRemainderTime // 200) > 0:
            temp_pay = divmod(CarRemainderTime, 200)
            Car_Payment += 20000
            CarRemainderTime = temp_pay[1]
            print("# overfree! #")

        if Car_Payment == 0 and CarRemainderTime < 30:
            Car_Payment = 0
        else:
            temp_pay = divmod(CarRemainderTime, 10)
            Car_Payment += temp_pay[0] * 1000
            if temp_pay[1] != 0:
                Car_Payment += 1000

        print("### 차량 주차요금 (사전 정산전) >>> " + str(Car_Payment))

        # 확인된 주차요금을 이용하여 사전 정산 동작을 수행
        headers = {
            "Authorization": "Bearer " + access_Token
        }

        data = {
            "parkingUid": 1926,
            "payMethod": 0,
            "fare": Car_Payment,
            "payDate": CarOverTime,
            "fareDeviceUid": 5,
            "fareDeviceCode": "PM0004",
            "fareDeviceName": "출구정산기",
            "createdAt": CarOverTime,
            "updatedAt": CarOverTime
        }

        Test_URL = api + "/parkings/" + str(Test_Uid) + "/payments"
        response_data = requests.post(Test_URL, headers=headers, data=data)
        Bill = json.loads(response_data.text)
        print(">>> 차량 사전정산 지불 완료>>>>>>>>>>>>>>>>")
        oks = json.dumps(Bill, indent=4, sort_keys=False, ensure_ascii=False)
        print(oks)

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


@then('A01.02 - 사전 정산 후, "{overTime}"분 후에, 차량 출차시 사전 정산 시간 내/외 여부에 따라 요금 "{bill}"원을 결재해야 한다.')
def step_impl(context, overTime, bill):
    #try:
    # /parkings/{uid}/bill API를 이용하여 최종 차량 주차 요금 확인
    headers = {
        "Authorization": "Bearer " + access_Token
    }

    # /parkings/{uid}/bill API를 이용하여 차량 주차 요금 확인
    Test_URL = api + "/parkings/" + str(Test_Uid) + "/bill"
    response_data = requests.get(Test_URL, headers=headers)
    Final_Bill = json.loads(response_data.text)

    print(">>> 차량 최종 주차 요금 확인 >>>>>>>>>>>>>>>>")
    oks = json.dumps(Final_Bill, indent=4, sort_keys=False, ensure_ascii=False)
    print(oks)

    print("+++ price >>> " + str(Final_Bill['data']['price']))
    print("+++ totalPaidPrice >>> " + str(Final_Bill['data']['totalPaidPrice']))
    print("+++ finalPrice >>> " + str(Final_Bill['data']['finalPrice']))

    if Final_Bill['data']['finalPrice'] == int(bill):
        print("### status-code : " + str(response_data.status_code))
        print("### response data OK!")
        Test_Result = True
    else:
        print("### status-code : " + str(response_data.status_code))
        print("### response data Not OK!")
        Test_Result = False

    # Test 종료 후, 생성한 Data는 삭제
    Test_URL = api + "/parkings/" + str(Test_Uid)
    response_data = requests.delete(Test_URL, headers=headers)

    #except Exception as e:
    #    print(e)
    #    Test_Result = False

    assert Test_Result
