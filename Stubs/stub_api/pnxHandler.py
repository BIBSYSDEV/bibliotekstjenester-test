import json


def handler_pnx_sender(event, _context):
    query = event['queryStringParameters']['q']

    json_file = open("/var/task/resources/mock_ids.json", "r")
    mock_ids = json.load(json_file)
    pnx_empty_object_id = mock_ids['pnx']['trigger_empty_pnx_response']

    if query is None:
        empty_file = open("/var/task/resources/empty_pnx_example.json", "r")
        empty_response = empty_file.read()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json; charset=utf-8"
            },
            "body": empty_response
        }

    if pnx_empty_object_id in query:
        empty_file = open("/var/task/resources/empty_pnx_example.json", "r")
        empty_response = empty_file.read()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json; charset=utf-8"
            },
            "body": empty_response
        }

    f = open("/var/task/resources/full_pnx_example_1.json", "r")
    pnx_example = f.read()
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8"
        },
        "body": pnx_example
    }
