import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    text = req.params.get('text')
    if not text:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('text')
    if text:
        # if text parameter is provided in the request, append company name with Copyright symbol
        dicts = {}
        # get Non-ASCII copyright symbol  
        copyright_symbol= chr(169)
        company = ["Microsoft", "Oracle","Google", "Amazon", "Deloitte"]
        # loop to create add copyright symbol to company name
        for k in company:
            company_copyright = k + copyright_symbol
            dicts[k] = company_copyright
        # Loop to replace Company name with Company name with copyright Symbol
        for i, j in dicts.items():
            text = text.replace(i, j)
        return func.HttpResponse(f"{text}")

    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass text parameter in the query string or in the request body to append company name with copyright symbol",
             status_code=200
        )
