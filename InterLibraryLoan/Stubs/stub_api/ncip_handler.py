def handler_pnx_sender(event, context):
    f = open("/var/task/resources/full_pnx_example_1.json", "r")
    pnx_example = f.read()
    return {
        "statusCode": 200, "headers": {
            "Content-Type": "text/xml"
        },
        "body": pnx_example
    }
