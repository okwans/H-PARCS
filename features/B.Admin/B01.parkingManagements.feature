@api_ing
@parking_managements
Feature: 관리자_주차장_운영정보_확인

  @B01.01.관리자_주차장_운영정보_확인
  Scenario Outline: 주차장 관리 - 입출차 내역 확인
    Given B01.01 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When B01.01 - API 동작을 통해 주차관리: 입출차 내역을 전달 받는다.
    Then B01.01 - 전달 받은 data에는 "<plateNumber>", "<parkingTypeName>", "<status>"등의 차량 정보가 포함되어야 한다.
    # 해당 차량이 어려번의 입출차 이력이 있을 경우 한번의 이력만 확인 후, Pass/Fail 여부 판단함.
    Examples: API_Data
    | plateNumber | parkingTypeName | status |
    | 67루0543    | 방문차량           | 미출차   |
    | 경기90자6743 | 방문차량           | 출차완료 |
    | 경기85사5793 | 등록차량           | 미출차   |
    | 경기92바3228 | 방문차량           | 출차완료 |
    | 60하6608    | 방문차량           | 출차완료 |
    | 154다1858   | 방문차량           | 출차완료  |
    | 46하0317    | 방문차량           | 출차완료 |
    | 42우7380    | 방문차량           | 출차완료 |
    | 36가2339    | 방문차량           | 미출차   |
    | 29다3366    | 방문차량           | 출차완료  |

  @B01.02.관리자_주차장_운영정보_확인
  Scenario Outline: 주차장 관리 - 주차정보 상세 확인
    Given B01.02 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When B01.02 - API 동작을 통해 특정 차량 "<uid>"를 이용하여 특정 차량의 주차 정보 상세 내역을 전달 받는다.
    Then B01.02 - 전달 받은 data에는 "<plateNumber>", "<parkingTimes>", "<inGateDate>", "<outGateDate>"등의 정보가 포함되어야 한다.
    Examples: API_Data
    | uid   | plateNumber | parkingTimes | inGateDate      | outGateDate      |
    | 3461  | 67나3566     | 6시간 13분    | 2020-08-15 12:27 | 2020-08-15 18:40 |
    | 11890 | 경기90자6743  | 0시간 24분    | 2020-11-19 14:32 | 2020-11-19 14:56 |
    | 11883 | 89노0993     | 0시간 11분    | 2020-11-19 13:47 | 2020-11-19 13:58 |
    | 11872 | 07가0202     | 39시간 5분    | 2020-11-17 20:14 | 2020-11-19 11:19 |
    | 11865 | 67호9155     | 0시간 10분    | 2020-11-19 10:11 | 2020-11-19 10:21 |


  @B01.03.관리자_주차장_운영정보_확인
  Scenario Outline: 주차장 관리 - 관리자 수동 입차 기능 동작 확인
    Given B01.03 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When B01.03 - API 동작을 통해 특정 차량를 참고하여 수동 입차 기능을 이용 "<plateNumber>", "<inGateDate>"정보를 수정한다.
    Then B01.03 - 해당 차량의 수정된 정보는 입력된 "<plateNumber>", "<inGateDate>"와 동일해야 한다.
    And B01.03 - Test 완료 후, 입차된 차량 정보는 삭제 진행한다.
    Examples: API_Data
    | plateNumber | inGateDate |
    | 10호1111    | yesterday   |
    #| 10호2222    | yesterday   |
    #| 10호3333    | yesterday   |
    #| 10호4444    | yesterday   |
    #| 10호5555    | yesterday   |
    #| 10호6666    | yesterday   |
    #| 10호7777    | yesterday   |
    #| 10호8888    | yesterday   |
    #| 10호9999    | yesterday   |
    #| 10호1818    | yesterday   |

  @B01.04.관리자_주차장_운영정보_확인
  Scenario Outline: 주차장 관리 - 관리자 수동 출차 기능 동작 확인
    Given B01.04 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    And B01.04 - Test를 위해 "<plateNumber>"와 "<plateNumber>"를 이용, API를 통해 차량을 입차 시킨다.
    When B01.04 - API 동작을 통해 특정 차량 "<uid>"를 이용하여 수동 출차 기능을 통해 "<plateNumber>", 다정보를 수정한다.
    Then B01.04 - 해당 차량의 수정된 정보는 입력된 "<plateNumber>", "<outGateDate>"와 동일해야 한다.
    And B01.04 - Test 완료 후, 입차된 차량 정보는 삭제 진행한다.
    Examples: API_Data
    # 수동 출차 기능은 오직 출차가 완료되지 않은 차량에서만 가능함.
    | plateNumber | inGateDate | outGateDate |
    | 10호1111    | yesterday   | today       |
    | 10호2222    | yesterday   | today       |
    | 10호3333    | yesterday   | today       |
    | 10호4444    | yesterday   | today       |
    | 10호5555    | yesterday   | today       |
    | 10호6666    | yesterday   | today       |
    | 10호7777    | yesterday   | today       |
    | 10호8888    | yesterday   | today       |
    | 10호9999    | yesterday   | today       |
    | 10호1818    | yesterday   | today       |


