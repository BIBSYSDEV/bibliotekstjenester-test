def handler_pnx_sender(event, context):
    f = open("/var/task/resources/ItemRequestedResponseSuccess.xml", "r")
    success_item_request_response = f.read()

    return {
        "statusCode": 202, "headers": {
            "Content-Type": "text/xml"
        },
        "body": success_item_request_response
    }
