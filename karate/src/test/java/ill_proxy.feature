Feature: Testing ILL-PROXY

  Background:
    * def libCode = '1060501'
    * def BasePath = 'https://api.sandbox.bibs.aws.unit.no/ill/'

  Scenario: Requesting libcheck for libuser
    * def libuser = '2012200'
    Given url BasePath + 'libcheck?libuser=' + libuser
    When method get
    Then status 200
    And match response.isAlmaLibrary == '#boolean'
    And match response.isNcipLibrary == '#boolean'

  Scenario: Requesting libcheck for non-existing libuser returns error
    * def libuser = '99999999999'
    Given url BasePath + 'libcheck?libuser=' + libuser
    When method get
    Then status 400
    And match response.status == 400

  Scenario: Requesting libcheck without parameters returns error
    Given url BasePath + 'libcheck'
    When method get
    Then status 400
    And match response.status == 400

  Scenario: Requesting metadata for for document
    * def savedResponse = read('metadata_response.json')
    Given url 'https://api.bibs.aws.unit.no/ill/metadata?document_id=BIBSYS_ILS71469955110002201'
    When method get
    Then status 200
    And match response == savedResponse





