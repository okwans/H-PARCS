#@api
#@parking
#Feature: GET_parkings_parkingUid_bill
#
#  @A04_GET_parkings_parkingUid_bill
#  Scenario Outline: GET parkings/{parkingUid}/bill 동작 확인
#    Given A04.01 - API Test를 위한 서버가 준비되어 있고 ID, PW를 이용하여 access Token 데이터를 전달 받았다.
#    When A04.01 - access Token를 이용하여 GET parkings/{"<parkingUid>"}/bill API 동작을 수행 후, response data를 정상적으로 전달 받아야 한다.
#    Then A04.01 - 전달받은 response data 결과와 "<plateNumber>", "<price>", "<totalPaidPrice>", "<parkingDate>"의 정보는 동일 해야 한다.
#    Examples: API_Data
#    | parkingUid | plateNumber | price | totalPaidPrice | parkingDate      |
#    | 1926       | 경기90자6743  | 400   | 400            | 2020-07-22 17:46 |
