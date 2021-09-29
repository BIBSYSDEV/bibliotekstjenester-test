from constants_ids import CLOSED_LIBRARY, NCIP_SUCCESS_ID, FAILURE_LIBRARY, \
    NCIP_FAILURE_ID, NCIP_ONLY_LIBRARY, ALMA_ONLY_LIBRARY, NEITHER_ALMA_NOR_NCIP_LIBRARY, ALMA_AND_NCIP_LIBRARY


def handler_basebibliotek_sender(event, _context):
    # api gateway already checks if identifier exists in the template.yml file
    # so no need to check if base_bibliotek_identifier is None
    base_bibliotek_identifier = event['pathParameters']['identifier']

    # CLOSED LIBRARY
    if CLOSED_LIBRARY == base_bibliotek_identifier:
        closed_library_file = open("/var/task/resources/FromBaseBibliotekStengt.xml", "r")
        closed_library = closed_library_file.read()
        closed_library = closed_library.replace("replace_bibnr_replace", base_bibliotek_identifier)
        closed_library = closed_library.replace("replace_with_mock_ncip_url",
                                                "https://api.test.bibs.aws.unit.no/ncip?id=" + NCIP_SUCCESS_ID)
        closed_library = closed_library.replace("replace_sru_url", "https://api.test.bibs.aws.unit.no/view/sru")
        return {
            "statusCode": 200, "headers": {
                "Content-Type": "application/xml"
            },
            "body": closed_library
        }

    f = open("/var/task/resources/alma_library_with_ncip.xml", "r")
    base_bibliotek = f.read()
    base_bibliotek = base_bibliotek.replace("replace_bibnr_replace", base_bibliotek_identifier)
    base_bibliotek = base_bibliotek.replace("replace_sru_url", "https://api.test.bibs.aws.unit.no/view/sru")

    # ALMA AND / OR NCIP LIB CHECK LIBRARIES

    if NCIP_ONLY_LIBRARY == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("replace_with_mock_ncip_url",
                                                "https://api.test.bibs.aws.unit.no/ncip?id=" + NCIP_SUCCESS_ID)
        base_bibliotek = base_bibliotek.replace("<katsyst>Alma</katsyst>", "<katsyst>Mikromarc 3</katsyst>")

    elif ALMA_ONLY_LIBRARY == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("<nncip_uri>replace_with_mock_ncip_url</nncip_uri>", "")

    elif NEITHER_ALMA_NOR_NCIP_LIBRARY == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("<nncip_uri>replace_with_mock_ncip_url</nncip_uri>", "")
        base_bibliotek = base_bibliotek.replace("<katsyst>Alma</katsyst>", "<katsyst>Mikromarc 3</katsyst>")

    # FAILURE LIBRARY
    elif FAILURE_LIBRARY == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("replace_with_mock_ncip_url",
                                                "https://api.test.bibs.aws.unit.no/ncip?id=" + NCIP_FAILURE_ID)
    else:
        # Default library is library with working ncip and sru
        base_bibliotek = base_bibliotek.replace("replace_with_mock_ncip_url",
                                            "https://api.test.bibs.aws.unit.no/ncip?id=" + NCIP_SUCCESS_ID)

    return {
        "statusCode": 200, "headers": {
            "Content-Type": "application/xml"
        },
        "body": base_bibliotek
    }
