from InterLibraryLoan.Stubs.stub_api.constants_ids import PNX_EMPTY_OBJECT_ID


def handler_pnx_sender(event, _context):
    query = event['queryStringParameters']['q']

    if query is None:
        empty_file = open("/var/task/resources/full_pnx_example_1.json", "r")
        empty_response = empty_file.read()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json; charset=utf-8"
            },
            "body": empty_response
        }

    if PNX_EMPTY_OBJECT_ID in query:
        empty_file = open("/var/task/resources/full_pnx_example_1.json", "r")
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
