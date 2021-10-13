Feature: Testing Base-bibliotek

  Background:
    * def BasePath = 'https://api-eu.hosted.exlibrisgroup.com/primo/v1/search'
    * def apiKey = ALMA_APIKEY


  Scenario: environment-variable-test
    Given def pcb = apiKey
    Then match apiKey == '/root'


#  Scenario: Lookup by bibnr
#    * def recordId = 'BIBSYS_ILS71560264980002201'
#    * def params = `?vid=BIBSYS&tab=default_tab&scope=default_scope&q=any,contains,${recordId}&lang=eng&apikey=${apiKey}`
#    Given url BasePath + params
#    When method get
#    Then status 200
#    And match response.docs[0].pnx.control.recordid[0] == '#string'
#    And match response.docs[0].pnx.search.sourceid[0] == '#string'
#    And match response.docs[0].pnx.addata.isbn[0] == '#string'
#    And match response.docs[0].pnx.addata.cop[0] == '#string'
#    And match response.docs[0].pnx.addata.btitle[0] == '#string'
#    #And match response.docs[0].pnx.addata.volume[0] == '#string' #testpost dosn't have volume
#    And match response.docs[0].pnx.addata.pages[0] == '#string'
#    And match response.docs[0].pnx.display.creationdate[0] == '#string'
#    And match response.docs[0].pnx.display.creator[0] == '#string'
#    And match response.docs[0].pnx.display.title[0] == '#string'
#    And match response.docs[0].pnx.display.publisher[0] == '#string'
#    And match response.docs[0].pnx.facets.library[0] == '#string'
#
#
#  Scenario: Requesting non-existing resoure
#    * def recordId = 'BIBSYS_ILS000000000000000000'
#    * def params = `?vid=BIBSYS&tab=default_tab&scope=default_scope&q=any,contains,${recordId}&lang=eng&apikey=${apiKey}`
#    Given url BasePath + params
#    When method get
#    Then status 200
#    And match response.info.total == 0







