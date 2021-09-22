def handler_basebibliotek_sender(event, context):
    f = open("../resources/baseBibliotekWithLineEndingInInst.xml", "r")
    pnx_example = f.read()
    return {
        "statusCode": 200, "headers": {
            "Content-Type": "text/xml"
        },
        "body": pnx_example
    }