Feature: Testing Base-bibliotek

  Background:
    * def BasePath = 'https://nb.no/basebibliotek/rest/bibnr/'

  Scenario: Lookup by bibnr
    * def bibNr = '1023001'
    * def savedResponse = read('bb_response.xml')
    # Merk at timestamp er satt til ignore og inst_eng har fått en &#x20; i bb_response.xml
    Given url BasePath + bibNr
    When method get
    Then status 200
    And match response/BaseBibliotek == $savedResponse/BaseBibliotek

  Scenario: Requesting non-existing resource
    * def bibNrNonExisting = '884284289023489432'
    Given url BasePath + bibNrNonExisting
    When method get
    Then status 200
    And match response/error/message == `Not found: bibnr/${bibNrNonExisting}`





