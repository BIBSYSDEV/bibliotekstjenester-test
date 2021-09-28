from InterLibraryLoan.Stubs.stub_api.constants_ids import CLOSED_LIBRARY, NCIP_SUCCESS_ID, FAILURE_LIBRARY, \
    NCIP_FAILURE_ID, NCIP_ONLY_LIBRARY, ALMA_ONLY_LIBRARY, NEITHER_ALMA_NOR_NCIP_LIBRARY, ALMA_AND_NCIP_LIBRARY


def handler_basebibliotek_sender(event, context):
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
        return {
            "statusCode": 200, "headers": {
                "Content-Type": "application/xml"
            },
            "body": closed_library
        }

    f = open("/var/task/resources/sampleLibraryFromBaseBibliotek.xml", "r")
    base_bibliotek = f.read()
    base_bibliotek = base_bibliotek.replace("replace_bibnr_replace", base_bibliotek_identifier)

    # ALMA AND / OR NCIP LIB CHECK LIBRARIES
    if NCIP_ONLY_LIBRARY == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("replace_with_mock_ncip_url",
                                                "https://api.test.bibs.aws.unit.no/ncip?id=" + NCIP_SUCCESS_ID)
        # TODO: replace SRU
        return {
            "statusCode": 200, "headers": {
                "Content-Type": "application/xml"
            },
            "body": base_bibliotek
        }
    if ALMA_ONLY_LIBRARY == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("<nncip_uri>replace_with_mock_ncip_url</nncip_uri>", "")
        base_bibliotek = base_bibliotek.replace("<katsyst>Mikromarc 3</katsyst>", "<katsyst>Alma</katsyst>")
        # TODO: replace SRU
        return {
            "statusCode": 200, "headers": {
                "Content-Type": "application/xml"
            },
            "body": base_bibliotek
        }

    if NEITHER_ALMA_NOR_NCIP_LIBRARY == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("<nncip_uri>replace_with_mock_ncip_url</nncip_uri>", "")
        # TODO: replace SRU
        return {
            "statusCode": 200, "headers": {
                "Content-Type": "application/xml"
            },
            "body": base_bibliotek
        }

    if ALMA_AND_NCIP_LIBRARY == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("<katsyst>Mikromarc 3</katsyst>", "<katsyst>Alma</katsyst>")
        base_bibliotek = base_bibliotek.replace("replace_with_mock_ncip_url",
                                                "https://api.test.bibs.aws.unit.no/ncip?id=" + NCIP_SUCCESS_ID)
        # TODO: replace SRU
        return {
            "statusCode": 200, "headers": {
                "Content-Type": "application/xml"
            },
            "body": base_bibliotek
        }

    # FAILURE LIBRARY
    if FAILURE_LIBRARY == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("replace_with_mock_ncip_url",
                                                "https://api.test.bibs.aws.unit.no/ncip?id=" + NCIP_FAILURE_ID)
        # TODO: replace SRU
        return {
            "statusCode": 200, "headers": {
                "Content-Type": "application/xml"
            },
            "body": base_bibliotek
        }

    # Default library is library with working ncip and sru
    base_bibliotek = base_bibliotek.replace("replace_with_mock_ncip_url",
                                            "https://api.test.bibs.aws.unit.no/ncip?id=" + NCIP_SUCCESS_ID)
    # TODO: replace SRU

    return {
        "statusCode": 200, "headers": {
            "Content-Type": "application/xml"
        },
        "body": base_bibliotek
    }
