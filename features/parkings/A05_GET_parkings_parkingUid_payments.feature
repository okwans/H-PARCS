@api
@parking
Feature: GET_parkings_parkingUid_payments

  @A05_GET_parkings_parkingUid_payments
  Scenario Outline: GET parkings/{parkingUid}/payments 동작 확인
    Given A05.01 - API Test를 위한 서버가 준비되어 있고 ID, PW를 이용하여 access Token 데이터를 전달 받았다.
    When A05.01 - access Token를 이용하여 GET parkings/{"<parkingUid>"}/payments API 동작을 수행 후, response data를 정상적으로 전달 받아야 한다.
    Then A05.01 - 전달받은 response data 결과와 "<payMethodName>", "<uid>", "<payMethod>", "<fare>"의 정보는 동일 해야 한다.
    Examples: API_Data
    | parkingUid | payMethodName | uid | payMethod | fare |
    | 1926       | 카드           | 996 | 1         | 400  |
