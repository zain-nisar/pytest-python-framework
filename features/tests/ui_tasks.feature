Feature: validate coinmarketcap UI

  Scenario: coinmarketcap dropdown verification
    When user navigates to "https://coinmarketcap.com" page
    And  user select "Show rows" dropdown value to "100"
    Then the user should see "100" rows displayed on the page


  Scenario: coinmarketcap filter verification
    When user navigates to "https://coinmarketcap.com" page
    And user clicks on "Filters" button
    And user clicks on "More Filters" button
    And user select "Market Cap" value "$1B - $10B"
    And user select "Price" value "$101 - $1,000"
    And user clicks on "Show results" button
    Then the user should see correct record on the page