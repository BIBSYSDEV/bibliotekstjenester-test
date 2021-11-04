Feature: Testing ILL-PROXY

  Background:
    * def BasePath = 'https://api.bibs.aws.unit.no/ill/'

  Scenario: Requesting libcheck for libuser
    * def libuser = '2012200'
    Given url BasePath + 'libcheck?libuser=' + libuser
    When method get
    Then status 200
    And match response.isAlmaLibrary == '#boolean'
    And match response.ncip_server_url == '#string'

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
    * def mmsId = 'BIBSYS_ILS71469955110002201'
    Given url BasePath + 'metadata?document_id=' + mmsId
    When method get
    Then status 200
    And match response.isbn == "#string"
    And match response.source == "#string"
    And match response.record_id == "#string"
    And match response.publication_place == "#string"
    And match response.b_title == "#string"
    And match response.volume == "#string"
    And match response.creation_year == "#string"
    And match response.creator == "#string"
    And match response.pages == "#string"
    And match response.publisher == "#string"
    And match response.display_title == "#string"
    And match response.libraries[0].institution_code == "#string"
    And match response.libraries[0].display_name == "#string"
    And match response.libraries[0].mms_id == "#string"
    And match response.libraries[0].library_code == "#string"
    And match response.libraries[0].available_for_loan == "#boolean"






