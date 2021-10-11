Feature: Testing Base-bibliotek

  Background:
    * def SRUBasePath = 'https://bibsys.alma.exlibrisgroup.com/'

  Scenario: Search
    * def mmsId = '999921024491202201'
    Given url SRUBasePath + 'view/sru/47BIBSYS_NETWORK?operation=searchRetrieve&version=1.2&query=alma.mms_id=' + mmsId
    When method get
    Then status 200
    And match response/searchRetrieveResponse/numberOfRecords == '1'
    And match response/searchRetrieveResponse/records/record/recordIdentifier == mmsId



