Feature: Testing webpage

Scenario: Search
  Given url 'https://www.onkelper.com'
  When method get
  Then status 200
