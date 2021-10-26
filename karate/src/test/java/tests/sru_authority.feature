Feature: Testing SRU-authority

  Background:
    * def SRUBasePath = 'https://authority.bibsys.no/authority/'

  Scenario: Search sru (marcexchange)
    * def authId = '90386146'
    Given url SRUBasePath + 'rest/sru?operation=searchRetrieve&version=1.2&recordPacking=xml&recordSchema=marcxchange&query=' + authId
    When method get
    Then status 200
    And match response/srw:searchRetrieveResponse/srw:numberOfRecords == '1'
    And match response/srw:searchRetrieveResponse/srw:records/srw:record/srw:recordIdentifier == authId
    And match response/srw:searchRetrieveResponse/srw:records/srw:record/srw:recordData/marc:record/marc:controlfield[1] == authId
    * def firstDatafieldPath = 'response/srw:searchRetrieveResponse/srw:records/srw:record/srw:recordData/marc:record/marc:datafield[1]'
    And match firstDatafieldPath + /marc:subfield[1]  == '#string'

  Scenario: Requesting non-existing resource returns empty (authority)
    * def authId = '00000000000000'
    Given url SRUBasePath + 'rest/sru?operation=searchRetrieve&version=1.2&recordPacking=xml&recordSchema=marcxchange&query=' + authId
    When method get
    Then status 200
    And match response/searchRetrieveResponse/numberOfRecords == '0'

  Scenario: Requesting without parameters returns errormessage
    Given url SRUBasePath + 'rest/sru'
    When method get
    Then status 200
    And match response/searchRetrieveResponse/diagnostics/diagnostic/message == '#string'


