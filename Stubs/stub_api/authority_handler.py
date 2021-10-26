import json


def handler_authority_sender(event, _context):
    json_file = open("/var/task/resources/mock_ids.json", "r")
    query = event['queryStringParameters']['query']
    mock_ids = json.load(json_file)
    record_id_that_trigger_0_hit = mock_ids['authority']['recordid_trigger_empty_response']

    if record_id_that_trigger_0_hit in query:
        f = open("/var/task/resources/authority_recordid_1199960_0-hit.xml", "r")
        zero_hits = f.read()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml; charset=utf-8"
            },
            "body": zero_hits
        }

    f = open("/var/task/resources/authority_record_id_1093967_1_hit.xml", "r")
    one_hit = f.read()
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/xml; charset=utf-8"
        },
        "body": one_hit
    }
