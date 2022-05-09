Feature: validate coinmarketcap API

  Scenario: Currency price conversion verification
    When User call the endpoint "cryptocurrency/map" for getting IDs of "BTC,USDT,ETH"
    Then User should convert them to "BOB" by calling the endpoint "tools/price-conversion"


  Scenario: Currency information verification
    When User call the endpoint "cryptocurrency/info" for getting info of "ETH"
    Then User should validate api response with the information from "currency_info.json"


  Scenario: Currencies having mineable tag associated
    When User call the endpoint "cryptocurrency/info" for getting information of "1,2,3,4,5,6,7,8,9,10" ids
    Then User should printed out currencies associated with "mineable" tag