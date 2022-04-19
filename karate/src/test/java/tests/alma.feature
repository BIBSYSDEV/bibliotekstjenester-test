Feature: Testing ALMA-update

  Background:
    * def BasePath = 'https://api-eu.hosted.exlibrisgroup.com/almaws/v1/bibs'
    * def almaApiKey = ALMA_APIKEY
    * def expectedResponse = read('responses/alma_bibs_record.xml')
    * def testText = 'Test test test'
    * def shouldBeText = 'Fulltekst'

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
    Given url BasePath + getParams
    When method get
    Then status 200
    * def orgRecord = response
    * json record = response
    * def orgText = record.bibs._.bib.record.datafield[25]._.subfield[0]._
    * print orgText
    * if (orgText == shouldBeText) record.bibs._.bib.record.datafield[25]._.subfield[0]._ = testText
    * print record.bibs._.bib.record.datafield[25]._.subfield[0]._
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
    * def tempText = orgRecordAsJson.bibs._.bib.record.datafield[25]._.subfield[0]._
    * if (tempText != shouldBeText) orgRecordAsJson.bibs._.bib.record.datafield[25]._.subfield[0]._ = shouldBeText
    * def orgBibRecord = orgRecordAsJson.bibs._
    * xml orgRecord = orgBibRecord
    Given url BasePath + putParams
    And request orgRecord
    When method put
    Then status 200
    * json resp = response
    Then print resp
    * def subfield = resp.bib.record.datafield[25]._.subfield[0]._
    * assert (subfield == testText) || (subfield == shouldBeText)




