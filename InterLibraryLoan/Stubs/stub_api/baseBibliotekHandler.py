from InterLibraryLoan.Stubs.stub_api.constants_ids import CLOSED_LIBRARY


def handler_basebibliotek_sender(event, context):
    # api gateway already checks if identifier exists in the template.yml file
    # so no need to check if base_bibliotek_identifier is None
    base_bibliotek_identifier = event['pathParameters']['identifier']

    if CLOSED_LIBRARY in base_bibliotek_identifier:
        closed_library_file = open("/var/task/resources/FromBaseBibliotekStengt.xml", "r")
        closed_library = closed_library_file.read()
        return {
            "statusCode": 200, "headers": {
                "Content-Type": "application/xml"
            },
            "body": closed_library
        }

    f = open("/var/task/resources/baseBibliotekWithLineEndingInInst.xml", "r")
    base_bibliotek = f.read()
    # The ncip url is changed here programatically for maintenance reasons.
    base_bibliotek = base_bibliotek.replace("https://bibsys.alma.exlibrisgroup.com/view/NcipP2PServlet",
                                            "https://api.test.bibs.aws.unit.no/stub/ncip")
    return {
        "statusCode": 200, "headers": {
            "Content-Type": "application/xml"
        },
        "body": base_bibliotek
    }
