@api_ing
@parking_terminals
Feature: 주차장_단말기_확인

  @C01.01.주차장_단말기
  Scenario Outline: 주차장 단말기 상태 check 동작 확인
    Given C01.01 - API Test를 위한 서버가 준비되어 있고 ID, PW를 이용하여 access Token 데이터를 전달 받았다.
    When C01.01 - access Token를 이용하여 개별 단말기 "<terminalId>"의 상태 check 동작을 수행한다.
    Then C01.01 - 전달받은 response data를 이용하여 개별 단말기의 정상 동작 유무를 확인한다.
     Examples: API_Data
    | terminalId |
    | 1          |
    | 2          |
    | 3          |
    | 1          |
    | 2          |
    | 3          |

  @C01.02.주차장_단말기
  Scenario Outline: 주차장 차단기 Open/Close 동작 확인
    Given C01.02 - API Test를 위한 서버가 준비되어 있고 ID, PW를 이용하여 access Token 데이터를 전달 받았다.
    When C01.02 - access Token를 이용하여 개별 차단기 "<terminalId>"의 "<gate>" 동작을 수행한다.
    Then C01.02 - 전달받은 response data를 이용하여 개별 차단기 "<terminalId>"의 "<gate>"의 정상 동작 유무를 확인한다.
    Examples: API_Data
    | terminalId | gate  |
    | 1          | open  |
    | 2          | close |
    | 3          | open  |
    | 1          | close |
    | 2          | open  |
    | 3          | close |