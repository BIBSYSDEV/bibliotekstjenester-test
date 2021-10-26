import json


def sru_handler(event, _context):
    json_file = open("/var/task/resources/mock_ids.json", "r")
    mock_ids = json.load(json_file)
    mms_id_that_trigger_complex_sru_response = mock_ids['mms_ids']['triggers_complex_sru_response']
    isbn_that_trigger_2_hits = mock_ids['isbn']['isbn_that_trigger_2_hits']
    isbn_that_trigger_1_hit = mock_ids['isbn']['isbn_that_trigger_1_hit']
    isbn_that_trigger_0_hits = mock_ids['isbn']['isbn_that_trigger_0_hit']

    query = event['queryStringParameters']['query']

    if isbn_that_trigger_2_hits in query:
        f = open("/var/task/resources/SRU_response_2_hits.xml", "r")
        isbn_that_trigger_2_hits_xml_response = f.read()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml; charset=utf-8"
            },
            "body": isbn_that_trigger_2_hits_xml_response
        }

    if isbn_that_trigger_1_hit in query:
        f = open("/var/task/resources/search_for_isbn_9788205377547_response.xml", "r")
        pelsjeger_liv = f.read()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml; charset=utf-8"
            },
            "body": pelsjeger_liv
        }

    if isbn_that_trigger_0_hits in query:
        f = open("/var/task/resources/search_for_isbn_0_hit.xml", "r")
        zero_hits = f.read()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml; charset=utf-8"
            },
            "body": zero_hits
        }

    if mms_id_that_trigger_complex_sru_response in query:
        f = open("/var/task/resources/sru_holdings_complex.xml", "r")
        sru_holdings_complex = f.read()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml; charset=utf-8"
            },
            "body": sru_holdings_complex
        }

    if 'isohold' in query:
        f = open("/var/task/resources/sru_holdings_with_only_copy.xml", "r")
        sru_response_1_hit = f.read()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml; charset=utf-8"
            },
            "body": sru_response_1_hit
        }

    f = open("/var/task/resources/lensvik_indremisjon.xml", "r")
    marc = f.read()
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/xml; charset=utf-8"
        },
        "body": marc
    }
