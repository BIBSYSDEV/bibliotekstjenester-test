Feature: Testing authority-sru-proxy in sandbox environment

  Background:
    * def BASE_PATH = 'https://api.sandbox.bibs.aws.unit.no/authority/'

  Scenario: GET Jude Fisher by auth_id
    # https://api.sandbox.bibs.aws.unit.no/authority?auth_id=1093967
    * def auth_id_value = '1093967'
    Given url BASE_PATH
    And param auth_id = auth_id_value
    When method GET
    Then status 200
    And match response[0].id == '1093967'
    And match response[0].authors[0].name == 'Fisher, Jude'
    And match response[0].xmlPresentation == '#present'
    # Do not verify complete xml, but tests some fields to know there is something here
    And match response[0].xmlPresentation contains '<leader>99999nz  a2299999n  4500</leader>'
    And match response[0].xmlPresentation contains '<controlfield tag="001">1093967</controlfield>'
    And match response[0].xmlPresentation contains '<controlfield tag="003">NO-TrBIB</controlfield>'
    And match response[0].linePresentation == '#present'
    And match response[0].linePresentation contains '*ldr 99999nz  a2299999n  4500'
    And match response[0].linePresentation contains '*003 NO-TrBIB'
    And match response[0].linePresentation contains '005 20240415100400.0'
