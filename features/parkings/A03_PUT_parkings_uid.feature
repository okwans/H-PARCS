@api
@parking
Feature: PUT_parkings_uid

  @A03_PUT_parkings_uid
  Scenario Outline: PUT parkings/{uid} 동작 확인
    Given A03.01 - API Test를 위한 서버가 준비되어 있고 ID, PW를 이용하여 access Token 데이터를 전달 받았다.
    When A03.01 - access Token과 "<parkingTypeName>"를 이용하여 PUT parkings/{"<uid>"} API 동작을 수행 후, response data를 정상적으로 전달 받아야 한다.
    Then A03.01 - 전달받은 response data 결과는 input으로 사용한 data의 "<parkingTypeName>" 정보는 동일 해야 한다.
    Examples: API_Data
    | uid        | parkingTypeName |
    | 14         | 사전등록차량        |
