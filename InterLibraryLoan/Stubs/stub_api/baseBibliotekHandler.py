
def handler_basebibliotek_sender(event, context):
    print("BASEBIBLIOTEK EVENT", event)
    f = open("/var/task/resources/baseBibliotekWithLineEndingInInst.xml", "r")
    pnx_example = f.read()
    # The ncip url is changed here programatically for maintenance reasons.
    pnx_example = pnx_example.replace("https://bibsys.alma.exlibrisgroup.com/view/NcipP2PServlet", "https://api.test.bibs.aws.unit.no/stub/ncip")
    return {
        "statusCode": 200, "headers": {
            "Content-Type": "text/xml"
        },
        "body": pnx_example
    }
