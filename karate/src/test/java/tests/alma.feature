Feature: Testing ALMA-update

  Background:
    * def BasePath = 'https://api-eu.hosted.exlibrisgroup.com/almaws/v1/bibs'
    * def almaApiKey = ALMA_APIKEY
    * def expectedResponse = read('responses/alma_bibs_record.xml')

  Scenario: get by mms_id
    * def mms_id = '999208985724702201'
    * def params = '?mms_id=' + mms_id + '&view=full&expand=None&apikey=' + almaApiKey
    Given url BasePath + params
    When method get
    Then status 200
    And match response == expectedResponse

  Scenario: get record by mms_id, update 856 and reset record to former state
    * def mms_id = '999208985724702201'
    * def getParams = '?mms_id=' + mms_id + '&apikey=' + almaApiKey
    * def putParams = '/' + mms_id + '?apikey=' + almaApiKey
    * def testText = 'Test test test'
#    * def testText = 'Fulltekst'
    Given url BasePath + getParams
    When method get
    Then status 200
    * def orgRecord = response
    * json record = response
    * def orgText = record.bibs._.bib.record.datafield[25]._.subfield[0]._
    * set record.bibs._.bib.record.datafield[25]._.subfield[0]._ = testText
    * def bibRecord = record.bibs._
    * xml xmlRecord = bibRecord

    Given url BasePath + putParams
    And request xmlRecord
    When method put
    Then status 200
    * json resp = response
    And match resp.bib.record.datafield[25]._.subfield[0]._ == testText

    Given url BasePath + getParams
    When method get
    Then status 200
    * json resp = response
    And match resp.bibs._.bib.record.datafield[25]._.subfield[0]._ == testText

    * json orgRecordAsJson = orgRecord
    * def orgBibRecord = orgRecordAsJson.bibs._
    * xml orgRecord = orgBibRecord
    Given url BasePath + putParams
    And request orgRecord
    When method put
    Then status 200
    * json resp = response
    Then print resp
    And match resp.bib.record.datafield[25]._.subfield[0]._ != testText
    And match resp.bib.record.datafield[25]._.subfield[0]._ == orgText





