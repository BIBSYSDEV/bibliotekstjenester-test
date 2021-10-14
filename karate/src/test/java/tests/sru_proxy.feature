Feature: Testing SRU-PROXY

  Background:
    * def libCode = '1060501'
    * def SRUBasePath = 'https://api.sandbox.bibs.aws.unit.no/alma'

  Scenario: Search
    * def mmsId = '999919774625402210'
    Given url SRUBasePath + '?mms_id=' + mmsId + '&institution=HIT&libraryCode=' + libCode + '&recordSchema=isohold'
    When method get
    Then status 200
    And match response.mmsId == mmsId
    And match response.institution == 'HIT'
    And match response.libraryCode == libCode
    And match response.totalNumberOfItems == '#number'
    And match response.numberAvailForInterLibraryLoan == '#number'
    And match response.availableDate == '#notnull'

  Scenario: Requesting non-existing resource returns empty
    * def mmsIdNonExisting = '000000000'
    Given url SRUBasePath + '?mms_id=' + mmsIdNonExisting + '&institution=HIT&libraryCode=' + libCode + '&recordSchema=isohold'
    When method get
    Then status 200
    And match response.mmsId == mmsIdNonExisting
    And match response.institution == 'HIT'
    And match response.libraryCode == libCode
    And match response.totalNumberOfItems == 0
    And match response.numberAvailForInterLibraryLoan == 0
    And match response.availableDate == ''

  Scenario: Requesting with missing parameters returns empty array
    * def mmsId = '999919774625402210'
    Given url SRUBasePath + '?mms_id=' + mmsId
    When method get
    Then status 200
    And match response == []

  Scenario: Requesting with no parameters returns error
    Given url SRUBasePath
    When method get
    Then status 400
    And match response.error == '#present'
    And match response.mmsId == '#notpresent'



