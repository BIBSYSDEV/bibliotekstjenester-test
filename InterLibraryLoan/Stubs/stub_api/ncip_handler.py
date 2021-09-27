import xmlschema


def handler_pnx_sender(event, _context):
    print("NCIP HANDLER EVENT: ", event)

    xsd = xmlschema.XMLSchema("/var/task/resources/ncip_v2_02.xsd")

    if event['body'] is None:
        return {
            "statusCode": 400, "headers": {
                "Content-Type": "application/xml"
            },
            "body": "bad request"
        }
    try:
        xsd.validate(event['body'])
    except Exception as e:
        print("NCIP VALIDATION FAILED", e)

    if not xsd.is_valid(event['body']):
        return {
            "statusCode": 400, "headers": {
                "Content-Type": "application/xml"
            },
            "body": "bad request"
        }

    xml_file = open("/var/task/resources/ItemRequestedResponseSuccess.xml", "r")
    success_item_request_response = xml_file.read()

    return {
        "statusCode": 202, "headers": {
            "Content-Type": "application/xml"
        },
        "body": success_item_request_response
    }
