import xmlschema

from stub_api.constants_ids import NCIP_FAILURE_ID

PROBLEM_TYPE = "Not Renewable"
PROBLEM_DETAILS = "Item may not be renewed"


def handler_pnx_sender(event, _context):
    print("NCIP HANDLER EVENT: ", event)
    body = event['body']
    id_in_search_params = event['queryStringParameters']['id']

    if id_in_search_params is None:
        id_in_search_params = ""

    xsd = xmlschema.XMLSchema("/var/task/resources/ncip_v2_02.xsd")

    failure_xml_response_file = open("/var/task/resources/ncipResponseFailure.xml", "r")
    failure_xml_response = failure_xml_response_file.read()

    if body is None:
        failure_xml_response = failure_xml_response.replace(PROBLEM_TYPE, "Missing request body")
        failure_xml_response = failure_xml_response.replace(PROBLEM_DETAILS, "No request body was supplied")
        return {
            "statusCode": 400, "headers": {
                "Content-Type": "application/xml"
            },
            "body": failure_xml_response
        }
    try:
        xsd.validate(body)
    except Exception as e:
        print("NCIP VALIDATION FAILED", e)
        failure_xml_response = failure_xml_response.replace(PROBLEM_TYPE, "Malformed request body")
        failure_xml_response = failure_xml_response.replace(PROBLEM_DETAILS, repr(e))
        return {
            "statusCode": 400, "headers": {
                "Content-Type": "application/xml"
            },
            "body": failure_xml_response
        }

    if NCIP_FAILURE_ID in body or id_in_search_params == NCIP_FAILURE_ID:
        return {
            "statusCode": 400, "headers": {
                "Content-Type": "application/xml"
            },
            "body": failure_xml_response
        }

    xml_file = open("/var/task/resources/ItemRequestedResponseSuccess.xml", "r")
    success_item_request_response = xml_file.read()

    return {
        "statusCode": 202, "headers": {
            "Content-Type": "application/xml; charset=utf-8"
        },
        "body": success_item_request_response
    }
