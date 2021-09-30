from stub_api.constants_ids import FAILURE_LIBRARY, CLOSED_LIBRARY


def sru_handler(_event, _context):

    f = open("/var/task/resources/sru_holdings_with_only_copy.xml", "r")
    sru_response_1_hit = f.read()

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/xml; charset=utf-8"
        },
        "body": sru_response_1_hit
    }
