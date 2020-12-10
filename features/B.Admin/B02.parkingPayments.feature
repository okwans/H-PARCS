@api
@parking_payments
Feature: 주차장_결재내역_확인

  @B02.01.관리자_주차장_운영정보_확인
  Scenario Outline: 주차장 관리 - 입출차 결재 내역 확인
    Given B02.01 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When B02.01 - API 동작 동작시 "<uid>"를 이용하여 특정 차량의 입출차 결재 내역을 확인한다.
    Then B02.01 - 전달 받은 data에는 "<uid>", "<payDate>", "<fare>", "<cardCompany>" 등 관련 정보가 출력 되어야 한다.
    Examples: API_Data
    # 추후 실제 결재관련 내용을 테스트용으로 업데이트한 후, 해당 정보의 일치 여부를 확인하는 형태로 구현 진행 필
    | uid   | payDate                  | fare  | cardCompany |
    | 11597 | 2020-11-17T03:06:17.000Z | 20000 | -           |
    | 9391  | 2020-10-14T07:19:14.000Z | 10    | 삼성비자법인    |
    | 11637 | 2020-11-17T02:14:17.000Z | 100   | 하나카드       |