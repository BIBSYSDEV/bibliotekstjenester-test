
def handler_pnx_sender(event, context):
    f = open("full_pnx_example_1.json", "r")
    pnx_example = f.read()
    return {
        "statusCode": 200, "headers": {
            "Content-Type": "text/xml"
        },
        "body": pnx_example
    }
