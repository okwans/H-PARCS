@api
@parking_discountCoupons
Feature: 차량_입출차_동작_확인-할인권차량

  @A03_01_차량_입출차_동작_확인-할인권차량
  Scenario Outline: 차량 입출차 동작 확인(할인권 차량)
    Given A03.01 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When A03.01 - 차량 입고시간은 현재시간 기준 "<entryTime>"분 전에 입차되는 형태로 "<plateNumber>" 차량을 API를 통해 설정한다.
    And A03.01 - 해당 차량 모두 할인권 "<coupon_cash>"과 "<coupon_time>"을 부여한다.
    Then A03.01 - 해당 차량이 출차시 주차시간이 회차시간 미만일 경우 요금 정산은 이뤄지지 않고 회차시간 이상일 경우 over되는 시간 만큼 요금 "<bill>"원을 결재해야 한다.
    Examples: API_Data
    | plateNumber | entryTime | coupon_cash | coupon_time | bill  |
    | 10하9088    | 25        | 0           | 120         | 0     |
    | 20하9099    | 5         | 1000        | 30          | 0     |
    | 30하1010    | 19        | 0           | 30          | 0     |
    | 40하8250    | 35        | 2000        | 30          | 0     |
    | 50하0102    | 55        | 3000        | 30          | 0     |
    | 60하7174    | 29        | 0           | 0           | 0     |
    | 70하1111    | 180       | 10000       | 30          | 0     |
    | 80하8888    | 1440      | 0           | 30          | 20000 |
    | 90하0001    | 100       | 3000        | 30          | 0     |
    | 10하9900    | 1800      | 5000        | 30          | 38000 |

  @A03_02_차량_입출차_동작_확인-할인권차량
  Scenario Outline: 차량 입출차 동작 확인(할인권 차량)
    Given A03.02 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When A03.02 - 차량 입고시간은 현재시간 기준 "<entryTime>"분 전에 입차되는 형태로 "<plateNumber>" 차량을 API를 통해 설정한다.
    And A03.02 - 해당 차량 모두 할인권 "<coupon_cash>"과 "<coupon_time>"을 부여한다.
    And A03.02 - 출차 동작전 사전 정산을 통해 주어진 coupon으로 주차 요금을 납부완료 한다.
    Then A03.02 - 사전 정산 후, "<overTime>"분 후에, 차량 출차시 사전 정산 시간 내/외 여부에 따라 요금 "<bill>"원을 결재해야 한다.
    Examples: API_Data
    | plateNumber | entryTime | coupon_cash | coupon_time | overTime | bill  |
    | 10하9088    | 25        | 0           | 120         | 10        | 0     |
    | 20하9099    | 5         | 1000        | 30          | 9         | 0     |
    | 30하1010    | 19        | 0           | 30          | 20        | 0     |
    | 40하8250    | 35        | 2000        | 30          | 30        | 0     |
    | 50하0102    | 55        | 3000        | 30          | 60        | 0     |
    | 60하7174    | 29        | 0           | 0           | 18        | 0     |
    | 70하1111    | 180       | 10000       | 30          | 5         | 0     |
    | 80하8888    | 1440      | 0           | 30          | 120       | 20000 |
    | 90하0001    | 100       | 3000        | 30          | 25        | 0     |
    | 10하9900    | 1800      | 5000        | 30          | 66        | 38000 |