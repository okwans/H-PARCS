@api
@parking_discountTicketsControl
Feature: 주차장_할인권_적용_확인

  @C02.01.주차장_할인권_적용
  Scenario Outline: 주차장 관리 - 관리자 할인권 부여시 즉시 적용 여부 확인
    Given C02.01 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When C02.01 - API 동작을 통해 특정 차량 "<uid>", "<plateNumber>", "<userName>", "<company>", "<startDay>", "<endDay>"를 이용하여 사전할인 차량 등록을 수행한다.
    Then C02.01 - 해당 차량의 정보는 입력된 "<plateNumber>", "<userName>", "<company>", "<startDay>", "<endDay>"와 동일해야 한다.
    And C02.01 - 할인권이 부여 동작 후, 30초 이후 차량 출차시 주차 요금은 청구되지 않아야 한다.
    Examples: API_Data
    # 수동 출차 기능은 오직 출차가 완료되지 않은 차량에서만 가능
    | uid | plateNumber | userName | company | startDay         | endDay            |
    | 1   | 10호1111    | 홍길동     | 카플랫     | 2020-11-18 12:00 | 2020-11-18 12:00  |
    | 2   | 10호2222    | 서태웅     | 휴맥스     | 2020-11-18 12:00 | 2020-11-18 12:00  |
    | 3   | 10호3333    | 강백호     | 하이파킹   | 2020-11-18 12:00  | 2020-11-18 12:00  |
    | 4   | 10호4444    | 팽수      | HPARCS   | 2020-11-18 12:00  | 2020-11-18 12:00  |