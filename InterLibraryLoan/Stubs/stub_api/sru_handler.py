import json


def sru_handler(event, _context):
    json_file = open("/var/task/resources/mock_ids.json", "r")
    mock_ids = json.load(json_file)
    mms_id_that_trigger_complex_sru_response = mock_ids['mms_ids']['triggers_complex_sru_response']

    query = event['queryStringParameters']['query']

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

    f = open("/var/task/resources/sru_holdings_with_only_copy.xml", "r")
    sru_response_1_hit = f.read()

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/xml; charset=utf-8"
        },
        "body": sru_response_1_hit
    }
