import json

def handler_basebibliotek_sender(event, _context):
    # api gateway already checks if identifier exists in the template.yml file
    # so no need to check if base_bibliotek_identifier is None
    base_bibliotek_identifier = event['pathParameters']['identifier']

    json_file = open("/var/task/resources/mock_ids.json", "r")
    mock_ids = json.load(json_file)
    closed_library_id = mock_ids['libraries']['trigger_closed_library_response']
    ncip_success_id = mock_ids['ncip']['success']
    failure_library_id = mock_ids['libraries']['library_that_trigger_failure_response_from_ncip']
    ncip_failure_id_id = mock_ids['ncip']['failure']
    ncip_only_library_id = mock_ids['libraries']['ncip_only_library']
    alma_only_library_id = mock_ids['libraries']['alma_only_library']
    neither_alma_nor_ncip_library_id = mock_ids['libraries']['neither_alma_nor_ncip_library']
    server_crash_library_id = mock_ids['libraries']['trigger_garbled_base_bibliotek_response']

    if server_crash_library_id == base_bibliotek_identifier:
        return {
            "statusCode": 200, "headers": {
                "Content-Type": "application/xml"
            },
            "body": "GURBA!"
        }

    # CLOSED LIBRARY
    if closed_library_id == base_bibliotek_identifier:
        closed_library_file = open("/var/task/resources/FromBaseBibliotekStengt.xml", "r")
        closed_library = closed_library_file.read()
        closed_library = closed_library.replace("replace_bibnr_replace", base_bibliotek_identifier)
        closed_library = closed_library.replace("replace_with_mock_ncip_url",
                                                "https://api.test.bibs.aws.unit.no/ncip?id=" + ncip_success_id)
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

    if ncip_only_library_id == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("replace_with_mock_ncip_url",
                                                "https://api.test.bibs.aws.unit.no/ncip?id=" + ncip_success_id)
        base_bibliotek = base_bibliotek.replace("<katsyst>Alma</katsyst>", "<katsyst>Mikromarc 3</katsyst>")

    elif alma_only_library_id == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("<nncip_uri>replace_with_mock_ncip_url</nncip_uri>", "")

    elif neither_alma_nor_ncip_library_id == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("<nncip_uri>replace_with_mock_ncip_url</nncip_uri>", "")
        base_bibliotek = base_bibliotek.replace("<katsyst>Alma</katsyst>", "<katsyst>Mikromarc 3</katsyst>")

    # FAILURE LIBRARY
    elif failure_library_id == base_bibliotek_identifier:
        base_bibliotek = base_bibliotek.replace("replace_with_mock_ncip_url",
                                                "https://api.test.bibs.aws.unit.no/ncip?id=" + ncip_failure_id_id)
    else:
        # Default library is library with working ncip and sru
        base_bibliotek = base_bibliotek.replace("replace_with_mock_ncip_url",
                                            "https://api.test.bibs.aws.unit.no/ncip?id=" + ncip_success_id)

    return {
        "statusCode": 200, "headers": {
            "Content-Type": "application/xml"
        },
        "body": base_bibliotek
    }
