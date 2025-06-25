Feature: Testing alma-sru-proxy in sandbox environment

  Background:
    * def BASE_PATH = 'https://api.sandbox.bibs.aws.unit.no/alma/'

  Scenario: GET Henrik Ibsen's "Samlede verker" by mms_id
    * def mms_id_value = '990600890834702201'
    Given url BASE_PATH
    And param mms_id = mms_id_value
    When method GET
    Then status 200
    And match response[0].id == '990600890834702201'
    And match response[0].mainTitle == 'Samlede verker'
    And match response[0].statementOfResponsibility == 'Henrik Ibsen'
    And match response[0].authors[0].name == 'Ibsen, Henrik'
    And match response[0].authors[0].date == '1828-1906'
    And match response[0].authors[0].id == '(NO-TrBIB)90061718'
    And match response[0].year == '2006'
    And match response[0].isbn contains '9788205345362'
    And match response[0].isbn contains '8205345368'
    And match response[0].publisher == 'Gyldendal'
    And match response[0].xmlPresentation == '#present'
    # Do not verify complete xml, but tests some fields to know there is something here
    And match response[0].xmlPresentation contains '<leader>02701cam a2200541 c 4500</leader>'
    And match response[0].xmlPresentation contains '<controlfield tag="001">990600890834702201</controlfield>'
    And match response[0].xmlPresentation contains '<controlfield tag="005">20230304142941.0</controlfield>'

  Scenario: GET Henrik Ibsen's "Samlede verker" by isbn
    * def isbn_value = '9788205345362'
    Given url BASE_PATH
    And param isbn = isbn_value
    When method GET
    Then status 200
    And match response[0].id == '990600890834702201'
    And match response[0].mainTitle == 'Samlede verker'
    And match response[0].statementOfResponsibility == 'Henrik Ibsen'
    And match response[0].authors[0].name == 'Ibsen, Henrik'
    And match response[0].authors[0].date == '1828-1906'
    And match response[0].authors[0].id == '(NO-TrBIB)90061718'
    And match response[0].year == '2006'
    And match response[0].isbn contains '9788205345362'
    And match response[0].isbn contains '8205345368'
    And match response[0].publisher == 'Gyldendal'
    And match response[0].xmlPresentation == '#present'
    # Do not verify complete xml, but tests some fields to know there is something here
    And match response[0].xmlPresentation contains '<leader>02701cam a2200541 c 4500</leader>'
    And match response[0].xmlPresentation contains '<controlfield tag="001">990600890834702201</controlfield>'
    And match response[0].xmlPresentation contains '<controlfield tag="005">20230304142941.0</controlfield>'
