#@api
#@parking
Feature: GET_parkings_uid

  @A02_GET_parkings_uid
  Scenario Outline: GET parkings/{uid} 동작 확인
    Given A02.01 - API Test를 위한 서버가 준비되어 있고 ID, PW를 이용하여 access Token 데이터를 전달 받았다.
    When A02.01 - access Token를 이용하여 GET parkings/{"<uid>"} API 동작을 수행 후, response data를 정상적으로 전달 받아야 한다.
    Then A02.01 - 전달받은 response data 결과와 "<plateNumber>"의 정보는 동일 해야 한다.
    Examples: API_Data
    | uid        | plateNumber |
    | 14         | 20하9088    |
