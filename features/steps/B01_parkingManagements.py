import json
import requests
from behave import *
from Config import *
from web_handle import *
import datetime
import calendar
from selenium.webdriver.common.keys import Keys

api = urlconfig.Test_API_URL
ID = urlconfig.Test_ID
PW = urlconfig.Test_PW
WebBrowser = []

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
#   Scenario Outline: 주차장 관리 - 관리자 수동 입차/출차 기능 동작 확인
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


@when('B01.03 - API 동작을 통해 특정 차량를 등록하고 browser에서 수동 입차 기능을 이용 "{plateNumber}"와 어제 입차일로 정보를 수정한다.')
def step_impl(context, plateNumber):
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
                print(Test_Uid)
                break

        # 확인된 uid를 이용하여 해당 차량의 inGateDate 변경
        Test_URL2 = api + "/parkings/" + str(Test_Uid)

        # 해당 차량의 입차 시간을 Null 값을 이용하여 미인식차량으로 변경
        headers = {
            "Authorization": "Bearer " + access_Token,
            "Content-Type": "application/json"
        }

        data = {
            "inGateDate": None
        }

        response_data = requests.put(Test_URL2, headers=headers, data=json.dumps(data))
        print("### status-code : " + str(response_data.status_code))
        VehicleIn = json.loads(response_data.text)
        print(">>> 차량 입차 시간 수정 >>>>>>>>>>>>>>>>")
        oks = json.dumps(VehicleIn, indent=4, sort_keys=False, ensure_ascii=False)
        print(oks)

        # 미인식차량에 WebBrowser를 통해 입차 시간을 현재시간 기준 어제로 변경한다.
        web_url = "http://localhost:3000"
        handleweb.init_web_page(web_url, WebBrowser)

        # Browser에서 주차관리 버튼 click
        driver = WebBrowser[0]
        parkingManagement = driver.find_element_by_xpath('//*[@id="sc-header"]/nav/div[2]/div/a[2]/button/span')
        parkingManagement.click()
        time.sleep(2)

        # 차량 List에서 방금 입차 동작을 수행한 항목을 click
        targetCar = driver.find_element_by_xpath('//*[@id="sc-page-content"]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[2]/span/span')
        targetCar.click()
        time.sleep(2)

        # 수동 입차 버튼 click
        manual_in = driver.find_element_by_xpath('//*[@id="sc-page-content"]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/button[1]')
        manual_in.click()
        time.sleep(2)

        # 입차일시 선택
        inGatedateButton = driver.find_element_by_xpath('//*[@id="modal-manual-invehicle"]/div/div[2]/div[1]/div/input')
        inGatedateButton.click()
        time.sleep(2)

        # 표시되는 달력에서 어제 날짜를 찾아 선택한다.
        today = datetime.datetime.today()

        # 표시되는 달력에서 어제 날짜를 찾아 선택하고, 매월 첫번째 날일 경우 그전달 마지막일로 변경
        if int(today.day) == 1:
            if today.month == 1:
                targetDay = calendar.monthrange(int(today.year - 1), 12)[1]
                refDate = "12월 " + str(targetDay) + ", " + str(today.year - 1)
            else:
                targetDay = calendar.monthrange(today.year, int(today.month - 1))[1]
                refDate = str(today.month - 1) + "월 " + str(targetDay) + ", " + str(today.year)

            beforeMonth = driver.find_element_by_xpath('/html/body/div[4]/div[1]/span[1]')
            beforeMonth.click()
            time.sleep(3)
        else:
            targetDay = today.day - 1
            refDate = str(today.month) + "월 " + str(targetDay) + ", " + str(today.year)

        print("000 >>>>" + refDate)
        #aria - label = "12월 1, 2020"
        #findTargetDay = driver.find_elements_by_class_name('flatpickr-day').get_attribute('aria-label')
        #findTargetDay = driver.find_elements_by_tag_name('span')

        selectDay = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/span[contains(@aria-label, "' + refDate + '")]')
        selectDay.click()

        # 확인 버튼 click
        confirmButton = driver.find_element_by_xpath('/html/body/div[4]/div[4]')
        confirmButton.click()
        time.sleep(4)

        # 저장 버튼 click
        saveButton = driver.find_element_by_xpath('//*[@id="modal-manual-invehicle"]/div/div[2]/div[2]/button')
        saveButton.click()
        time.sleep(2)

        # browser 종료
        handleweb.webdriver_shutdown(WebBrowser)

        Test_Result = True

    except Exception as e:
        print(e)
        Test_Result = False

    assert Test_Result


@when('B01.03 - 입차 등록된 차량에 대해 browser에서 수동 출차 기능을 이용 오늘 출차일로 정보를 수정한다.')
def step_impl(context):
    try:
        # 미인식차량에 WebBrowser를 통해 입차 시간을 현재시간 기준으로 변경한다.
        web_url = "http://localhost:3000"
        handleweb.init_web_page(web_url, WebBrowser)

        # Browser에서 주차관리 버튼 click
        driver = WebBrowser[0]
        parkingManagement = driver.find_element_by_xpath('//*[@id="sc-header"]/nav/div[2]/div/a[2]/button/span')
        parkingManagement.click()
        time.sleep(2)

        # 차량 List에서 방금 수동 입차 동작을 수행한 항목을 click
        targetCar = driver.find_element_by_xpath(
            '//*[@id="sc-page-content"]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[2]/span/span')
        targetCar.click()
        time.sleep(2)

        # 수동 출차 버튼 click
        manual_in = driver.find_element_by_xpath(
            '//*[@id="sc-page-content"]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/button[2]/div')
        manual_in.click()
        time.sleep(2)

        # 확인 버튼 click
        confirmButton = driver.find_element_by_xpath('//*[@id="modal-manual-outvehicle"]/div/div/div[2]/button[2]')
        confirmButton.click()
        time.sleep(4)

        Test_Result = True

    except Exception as e:
        print(e)
        Test_Result = False

    assert Test_Result


@then('B01.03 - 해당 차량의 수정된 정보는 입력된 "{plateNumber}"와 동일해야 하며, 입출차 날짜는 어제/오늘로 설정되어야 한다.')
def step_impl(context, plateNumber):
    try:

        headers = {
            "Authorization": "Bearer " + access_Token
        }

        target_URL = "http://localhost:3000/api/parkings/" + str(Test_Uid)
        response_data = requests.get(target_URL, headers=headers)
        print(response_data.status_code)
        response_json = json.loads(response_data.text)
        #resp = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
        #print(resp)

        temp_ref_outGateDate = response_json['data']['outGateDate']
        temp_ref_inGateDate = response_json['data']['inGateDate']

        ref_plateNumber = response_json['data']['plateNumber']
        ref_inGateDate = temp_ref_inGateDate.split(' ') # 입차 시간은 날짜만 확인
        ref_outGateDate = temp_ref_outGateDate.split(' ') # 출차 시간은 날짜만 확인

        # 저장된 data의 확인을 위해 실제 어제 날짜와 오늘 날짜를 확인
        today = datetime.datetime.today()

        # 표시되는 달력에서 어제 날짜를 찾아 선택하고, 매월 첫번째 날일 경우 그전달 마지막일로 변경
        if int(today.day) == 1:
            if today.month == 1:
                targetDay = calendar.monthrange(int(today.year - 1), 12)[1]
                date_yesterday = str(today.year - 1) + "-" + "12" + "-" + '{0:0>2}'.format(str(targetDay))
            else:
                targetDay = calendar.monthrange(today.year, int(today.month - 1))[1]
                date_yesterday = str(today.year) + "-" + '{0:0>2}'.format(str(today.month - 1)) + "-" + '{0:0>2}'.format(str(targetDay))
        else:
            targetDay = today.day - 1
            date_yesterday = str(today.year) + "-" + '{0:0>2}'.format(str(today.month)) + "-" + '{0:0>2}'.format(str(targetDay))

        date_today = str(today.year) + "-" + '{0:0>2}'.format(str(today.month)) + "-" + '{0:0>2}'.format(str(today.day))

        print("Today >>> " + date_today)
        print("Yesterday >>> " + date_yesterday)
        print("Data_Yesterday >>> " + ref_inGateDate[0])
        print("Data_Today >>> " + ref_outGateDate[0])

        if plateNumber == ref_plateNumber and date_yesterday == ref_inGateDate[0] and date_today == ref_outGateDate[0]:
            print("### Test Pass ###")
            Test_Result = True
        else:
            print("### Test Fail ###")
            Test_Result = False
            resp = json.dumps(response_json, indent=4, sort_keys=False, ensure_ascii=False)
            print(resp)

        # browser 종료
        handleweb.webdriver_shutdown(WebBrowser)

    except Exception as e:
        print(e)
        Test_Result = False

    assert Test_Result


@then('B01.03 - Test 완료 후, 등록한 차량 정보는 삭제 진행한다.')
def step_impl(context):
    try:
        headers = {
            "Authorization": "Bearer " + access_Token
        }

        test_URL = "http://localhost:3000/api/parkings/" + str(Test_Uid)
        response_data = requests.delete(test_URL, headers=headers)
        print(response_data.status_code)
        print("### Delete >>> " + str(Test_Uid))

        Test_Result = True

    except Exception as e:
       print(e)
       Test_Result = False

    assert Test_Result
