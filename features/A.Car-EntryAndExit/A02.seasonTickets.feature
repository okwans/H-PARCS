@api
@parking_seasonTickets
Feature: 차량_입출차_동작_확인-정기권차량

  @A02.01.차량_입출차_동작_확인-정기권차량
  Scenario Outline: 차량 입출차 동작 확인(정기권 차량)
    Given A02.01 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When A02.01 - 차량 입고시간은 현재시간 기준 "<entryTime>"분 전에 입차되는 형태로 "<plateNumber>" 차량을 API를 통해 설정한다.
    And A02.01 - 해당 차량 모두 기 등록된 정기권 권한을 부여한다.
    Then A02.01 - 해당 차량 출차시 회차시간 여부와 상관없이 주차 요금은 모두 "<bill>"원으로 설정되어야 한다.
    Examples: API_Data
    | plateNumber | entryTime | bill  |
    | 10호1111    | 5         | 0     |
    | 10호2222    | 29        | 0     |
    | 10호3333    | 30        | 0     |
    | 10호4444    | 31        | 0     |
    | 10호5555    | 90        | 0     |
    | 10호6666    | 80        | 0     |
    | 10호7777    | 1440      | 0     |
    | 10호8888    | 2000      | 0     |
    | 10호9999    | 720       | 0     |
    | 10호1234    | 120       | 0     |
