def handler_pnx_sender(event, context):
    f = open("/var/task/resources/ItemRequestResponseSuccess.xml", "r")
    success_item_request_response = f.read()
    print("NCIP REQUEST: ", event)
    return {
        "statusCode": 202, "headers": {
            "Content-Type": "text/xml"
        },
        "body": {success_item_request_response, event}
    }
