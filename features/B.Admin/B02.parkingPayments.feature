@api_api
@parking_payments
Feature: 주차장_결재내역_확인

  @B02.01.관리자_주차장_운영정보_확인
  Scenario Outline: 주차장 관리 - 입출차 결재 내역 확인
    Given B02.01 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When B02.01 - API 동작 동작시 "<paymentTime>" "<plateNumber>"를 이용하여 입출차 결재 내역을 확인한다.
    Then B02.01 - 전달 받은 data에는 "<paymentTime>", "<plateNumber>"를 기준으로 관련 차량 정보가 출력 되어야 한다.
    Examples: API_Data
    | paymentTime | plateNumber |
    | 2020-11-18  | 10하9088    |
    | 2020-11-18  | 20하9099    |
    | 2020-11-18  | 30하1010    |
    | 2020-11-18  | 40하8250    |
    | 2020-11-18  | 50하0102    |
    | 2020-11-18  | 60하7174    |
    | 2020-11-18  | 70하1111    |
    | 2020-11-18  | 80하8888    |
    | 2020-11-18  | 90하0001    |
    | 2020-11-18  | 10하9900    |
