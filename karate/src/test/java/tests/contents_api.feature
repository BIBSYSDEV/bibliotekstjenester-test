Feature: Testing contents api

  Background:
    * def basePath = 'https://api.test.bibs.aws.unit.no/contents'

  Scenario: Search contents with isbn
    * def isbn = '9780199601714'
    Given url basePath + '?isbn=' + isbn
    When method get
    Then status 200
    And match response.isbn == isbn
    And match response.title == '#string'
    And match response.source == '#string'
    And match response.created == '#string'
    And match response.dateOfPublication == '#string'
    And match response.descriptionLong == '#string' || '#null'
    And match response.imageSmall == '#string' || '#null'

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



