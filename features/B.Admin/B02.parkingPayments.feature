@api
@parking_payments
Feature: 주차장_결재내역_확인

  @B02.01.관리자_주차장_운영정보_확인
  Scenario Outline: 주차장 관리 - 입출차 결재 내역 확인
    Given B02.01 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When B02.01 - API 동작을 통해 특정 차량 "<uid>", "<plateNumber>", "<userName>", "<company>", "<startDay>", "<endDay>"를 이용하여 사전할인 차량 등록을 수행한다.
    Then B02.01 - 전달 받은 data에는 "<plateNumber>", "<payment>", "<entryTime>", "<exitTime>"등의 차량 정보가 포함되어야 한다.
    Examples: API_Data
    | plateNumber | payment | entryTime        | exitTime         |
    | 10하9088    | 3000    | 2020-11-18 12:00 | 2020-11-18 12:00 |
    | 20하9099    | 15000   | 2020-11-18 12:00 | 2020-11-18 12:00 |
    | 30하1010    | 3000    | 2020-11-18 12:00 | 2020-11-18 12:00 |
    | 40하8250    | 3000    | 2020-11-18 12:00 | 2020-11-18 12:00 |
    | 50하0102    | 3000    | 2020-11-18 12:00 | 2020-11-18 12:00 |
    | 60하7174    | 3000    | 2020-11-18 12:00 | 2020-11-18 12:00 |
    | 70하1111    | 3000    | 2020-11-18 12:00 | 2020-11-18 12:00 |
    | 80하8888    | 3000    | 2020-11-18 12:00 | 2020-11-18 12:00 |
    | 90하0001    | 3000    | 2020-11-18 12:00 | 2020-11-18 12:00 |
    | 10하9900    | 3000    | 2020-11-18 12:00 | 2020-11-18 12:00 |
