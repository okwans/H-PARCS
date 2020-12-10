@api_ing
@parking_generalTickets
Feature: 차량_입출차_동작_확인-일반차량

  @A01.01.차량_입출차_동작_확인-일반차량
  Scenario Outline: 차량 입출차 동작 확인(일반 차량)
    Given A01.01 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When A01.01 - 차량 입고시간은 현재시간 기준 "<inGateDate>"분 전에 입차되는 형태로 "<plateNumber>" 차량을 API를 통해 설정한다.
    Then A01.01 - 해당 차량 출차시 주차시간이 회차시간 미만일 경우 요금 정산은 이뤄지지 않고 회차 시간 이상일 경우 over되는 시간 만큼 요금 "<bill>"원을 결재해야 한다.
    # Test 완료 후, 차량 입출차 확인시 사용한 내용들은 모두 삭제
    Examples: API_Data
    | plateNumber | inGateDate | bill  |
    | 10하9088    | 25        | 0     |
    | 20하9099    | 5         | 0     |
    | 30하1010    | 19        | 0     |
    | 40하8250    | 35        | 4000  |
    | 50하0102    | 55        | 6000  |
    | 60하7174    | 29        | 0     |
    | 70하1111    | 180       | 18000 |
    | 80하8888    | 1440      | 20000 |
    | 90하0001    | 100       | 10000 |
    | 10하9900    | 1800      | 40000 |

#  @A01.02.차량_입출차_동작_확인-일반차량
  Scenario Outline: 차량 입출차 동작 확인(일반 차량) - 사전정산 완료 후, 출차 동작 확인
    Given A01.02 - API Test를 위한 서버가 준비되어 있고 필요한 access Token 데이터를 전달 받았다.
    When A01.02 - 차량 입고시간은 현재시간 기준 "<inGateDate>"분 전에 입차되는 형태로 "<plateNumber>" 차량을 API를 통해 설정한다.
    And A01.02 - 출차 동작전 사전 정산을 통해 주차 요금을 납부완료 한다.
    Then A01.02 - 사전 정산 후, "<overTime>"분 후에, 차량 출차시 사전 정산 시간 내/외 여부에 따라 요금 "<bill>"원을 결재해야 한다.
    Examples: API_Data
    # entryTime은 30분 이상으로 설정해야 함.
    | plateNumber | inGateDate | overTime | bill |
    | 10하9088    | 35         | 5        | 0    |
    | 20하9099    | 60         | 30       | 1000 |
    | 30하1010    | 120        | 10       | 0    |
    | 40하8250    | 50         | 11       | 500  |
    | 50하0102    | 30         | 3        | 0    |
    | 60하7174    | 90         | 60       | 2500 |
    | 60하7174    | 180        | 9        | 0    |

