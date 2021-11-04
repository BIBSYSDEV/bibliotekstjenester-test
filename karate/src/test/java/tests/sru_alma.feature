Feature: Testing SRU-bibliotek

  Background:
    * def SRUBasePath = 'https://bibsys.alma.exlibrisgroup.com/'

  Scenario: Search sru (marcxml)
    * def mmsId = '999921024491202201'
    * def lib = '47BIBSYS_NETWORK'
    Given url SRUBasePath + 'view/sru/' + lib + '?operation=searchRetrieve&version=1.2&query=alma.mms_id=' + mmsId
    When method get
    Then status 200
    And match response/searchRetrieveResponse/numberOfRecords == '1'
    And match response/searchRetrieveResponse/records/record/recordIdentifier == mmsId
    And match response/searchRetrieveResponse/records/record/recordData/record/controlfield[1] == mmsId
    * def firstDatafieldPath = 'response/searchRetrieveResponse/records/record/recordData/record/datafield[1]'
    And match firstDatafieldPath + /subfield[1]  == '#string'

  Scenario: Search sru holdings
    * def mmsId = '990939573514702259'
    * def lib = '47BIBSYS_UNIS'
    Given url SRUBasePath + 'view/sru/' + lib + '?operation=searchRetrieve&recordSchema=isohold&version=1.2&query=alma.mms_id=' + mmsId
    When method get
    Then status 200
    And match response/searchRetrieveResponse/numberOfRecords == '1'
    And match response/searchRetrieveResponse/records/record/recordIdentifier == mmsId
    * def firstHoldingsPath = 'response/searchRetrieveResponse/records/record/recordData/holdings/holding[1]'
    And match firstHoldingsPath + /institutionIdentifier/value  == '#string'
    And match firstHoldingsPath + /holdingSimple/copiesSummary/copiesCount  == '#string'
    * def statusPath = '/holdingSimple/copiesSummary/status'
    And match firstHoldingsPath + statusPath + /availableFor  == '#string'
    And match firstHoldingsPath + statusPath + /availableCount  == '#string'
    And match firstHoldingsPath + statusPath + /earliestDispatchDate  == '#string'

  Scenario: Requesting non-existing resource returns empty (holdings)
    * def mmsId = '00000000000000'
    * def lib = '47BIBSYS_UNIS'
    Given url SRUBasePath + 'view/sru/' + lib + '?operation=searchRetrieve&recordSchema=isohold&version=1.2&query=alma.mms_id=' + mmsId
    When method get
    Then status 200
    And match response/searchRetrieveResponse/numberOfRecords == '0'

  Scenario: Requesting without parameters returns errormessage
    * def lib = '47BIBSYS_UNIS'
    Given url SRUBasePath + 'view/sru/' + lib
    When method get
    Then status 200
    And match response/searchRetrieveResponse/diagnostics/diagnostic/message == '#string'


