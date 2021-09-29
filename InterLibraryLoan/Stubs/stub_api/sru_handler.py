from InterLibraryLoan.Stubs.stub_api.constants_ids import FAILURE_LIBRARY


def sru_handler(event, _context):
    query = event['queryStringParameters']
    institution = event['institution']
    mms_id = query['mms_id']
    library_code = query['libraryCode']
    total_items = 2
    number_available_for_inter_library_loan = 1

    if FAILURE_LIBRARY == library_code:
        number_available_for_inter_library_loan = 0

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8"
        },
        "body": {
            "mmsId": mms_id,
            "institution": institution,
            "libraryCode": library_code,
            "totalNumberOfItems": total_items,
            "numberAvailForInterLibraryLoan": number_available_for_inter_library_loan,
            "availableDate": "2021-09-08T00:00Z"
        }
    }
