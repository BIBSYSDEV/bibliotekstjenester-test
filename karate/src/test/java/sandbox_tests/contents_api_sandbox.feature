Feature: Testing contents api Sandbox

  Background:
    * def basePath = 'https://api.sandbox.bibs.aws.unit.no/contents'

  Scenario: Look-up contents with isbn
    * def isbn = '9788205377547'
    Given url basePath + '?isbn=' + isbn
    When method get
    Then status 200
    And match response.isbn == isbn
    And match response.title contains 'Pelsjegerliv blandt Nord-Canadas indianere'
    And match response.source == 'BOKBASE'
    And match response.created == '#string'
    And match response.dateOfPublication == '1931'
    And match response.descriptionShort contains 'Etter å ha brutt opp fra sin sakførerpraksis i Norge'
    And match response.descriptionLong contains 'Pelsjegerliv er beretningen om hans opplevelser i denne tiden'
    And match response.tableOfContents == 'The openingSecond breakfastCinco de mayo'
    And match response.imageSmall == 'files/images/small/7/4/9788205377547.jpg'

  Scenario: Requesting non-existing resource returns empty
    * def isbnNonExisting = '000000000'
    Given url basePath + '?isbn=' + isbnNonExisting
    When method get
    Then status 404
    And match response.title == 'Not Found'
    And match response.detail == 'Document with id=000000000 was not found.'

  Scenario: Requesting with no parameters returns error
    Given url basePath
    When method get
    Then status 400
    And match response.title == 'Bad Request'
    And match response.detail == 'Missing from query parameters: isbn'
