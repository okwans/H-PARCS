@api
@parking_payments
Feature: 주차장_결재내역_확인

  @B04_주차장_결재내역
  Scenario Outline: GET parkings 동작 확인
    Given A01.01 - API Test를 위한 서버가 준비되어 있고 ID, PW를 이용하여 access Token 데이터를 전달 받았다.
    When A01.01 - access Token를 이용하여 GET parkings API 동작을 수행 후, response data를 정상적으로 전달 받아야 한다.
    Then A01.01 - 전달받은 response data 결과중 "<uid>", "<plateNumber>"의 정보가 포함된 내용이 있어야 한다.
    Examples: API_Data
    | uid        | plateNumber |
    | 14         | 20하9088    |
