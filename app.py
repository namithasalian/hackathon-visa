from flask import Flask, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/searchMerchants', methods=["POST"])
def search_merchants():
    request_body = request.json

    #category_code_mappings = {"FAST_FOOD_RESTAURANTS": 5814}
    print(request_body)

    payload = {"header": {
        "messageDateTime": "2020-06-20T18:14:39.903",
        "requestMessageId": "Request_001",
        "startIndex": "0"
    },
        "searchAttrList": {
            "merchantCategoryCode":
                request_body['category'],

            "merchantCountryCode": "840",
            "latitude": request_body['latitude'],
            "longitude": request_body['longitude'],
            "distance": "99",
            "distanceUnit": "M"
        },
        "responseAttrList": [
            "GNLOCATOR"
        ],
        "searchOptions": {
            "wildCard": [
                "merchantName"
            ],
            "maxRecords": "5",
            "matchIndicators": "true",
            "matchScore": "true"
        }
    }

    url = "https://sandbox.api.visa.com/merchantlocator/v1/locator"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic Sk9IUkUyQTNHTUtHWjNLN0xPMlMyMWNCWlZlNjhHenJlencyeTF2eVpXdzIzVnNfNDpXMGUyNGZ4SVBk'
    }
    r = requests.post(url,
                      cert=('Certificates/cert.pem', 'Certificates/privateKey.pem'),
                      headers=headers,
                      auth=("5COPOJAN7B63B74JMML121Z4flu5-fyzcdQ0HNwFM5zBxlwtc", "zhrd4VO3R4Owe7"),
                      data=json.dumps(payload))
    # print(r.content())
    response = r.text.encode('utf8')
    print(response)
    return response


@app.route('/fundsTransfer', methods=["POST"])
def funds_transfer():
    request_body = request.json
    print(request_body)


    payload = {
        "acquirerCountryCode": "840",
        "acquiringBin": "408999",
        "amount": request_body['amount'],
        "businessApplicationId": "AA",
        "cardAcceptor": {
            "address": {
                "country": "USA",
                "county": "081",
                "state": "CA",
                "zipCode": "94404"
            },
            "idCode": "ABCD1234ABCD123",
            "name": "Visa Inc. USA-Foster City",
            "terminalId": "ABCD1234"
        },
        "cavv": "0700100038238906000013405823891061668252",
        "foreignExchangeFeeTransaction": "11.99",
        "localTransactionDateTime": request_body["localTransactionDateTime"],
        "retrievalReferenceNumber": "330000550000",
        "senderCardExpiryDate": request_body['cardExpiryDate'],
        "senderCurrencyCode": request_body['currency'],
        "senderPrimaryAccountNumber": request_body['cardNumber'],
        "surcharge": "11.99",
        "systemsTraceAuditNumber": "451001",
        "nationalReimbursementFee": "11.22",
        "cpsAuthorizationCharacteristicsIndicator": "Y",
        "addressVerificationData": {
            "street": "XYZ St",
            "postalCode": "12345"
        },
        "settlementServiceIndicator": "9",
        "colombiaNationalServiceData": {
            "countryCodeNationalService": "170",
            "nationalReimbursementFee": "20.00",
            "nationalNetMiscAmountType": "A",
            "nationalNetReimbursementFeeBaseAmount": "20.00",
            "nationalNetMiscAmount": "10.00",
            "addValueTaxReturn": "10.00",
            "taxAmountConsumption": "10.00",
            "addValueTaxAmount": "10.00",
            "costTransactionIndicator": "0",
            "emvTransactionIndicator": "1",
            "nationalChargebackReason": "11"
        },
        "riskAssessmentData": {
            "delegatedAuthenticationIndicator": True,
            "lowValueExemptionIndicator": True,
            "traExemptionIndicator": True,
            "trustedMerchantExemptionIndicator": True,
            "scpExemptionIndicator": True
        },
        "visaMerchantIdentifier": request_body['merchantId']
    }

    url = "https://sandbox.api.visa.com/visadirect/fundstransfer/v1/pullfundstransactions"

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic Sk9IUkUyQTNHTUtHWjNLN0xPMlMyMWNCWlZlNjhHenJlencyeTF2eVpXdzIzVnNfNDpXMGUyNGZ4SVBk'
    }
    r = requests.post(url,
                      cert=('Certificates/cert.pem', 'Certificates/privateKey.pem'),
                      headers=headers,
                      auth=("5COPOJAN7B63B74JMML121Z4flu5-fyzcdQ0HNwFM5zBxlwtc", "zhrd4VO3R4Owe7"),
                      data=json.dumps(payload))
    # print(r.content())
    response = r.text.encode('utf8')
    print(response)

    if r.status_code!= 200:
        return {"Message":"Error"}


    payload = {
               "acquirerCountryCode": "840",
               "acquiringBin": "408999",
               "amount": request_body['amount'],
               "businessApplicationId": "AA",
               "cardAcceptor": {
                   "address": {
                       "country": "USA",
                       "county": "San Mateo",
                       "state": "CA",
                       "zipCode": "94404"
                   },
                   "idCode": "CA-IDCode-77765",
                   "name": "Visa Inc. USA-Foster City",
                   "terminalId": "TID-9999"
               },
               "localTransactionDateTime": request_body["localTransactionDateTime"],
              # "merchantCategoryCode": "6012",
               "pointOfServiceData": {
                   "motoECIIndicator": "0",
                   "panEntryMode": "90",
                   "posConditionCode": "00"
               },
               "recipientName": "rohan",
               "recipientPrimaryAccountNumber": "4957030420210496",
               "retrievalReferenceNumber": "412770451018",
               "senderAccountNumber": request_body['cardNumber'],
           #   "senderAddress": "901 Metro Center Blvd",
            #   "senderCity": "Foster City",
             #  "senderCountryCode": "124",
              # "senderName": "Mohammed Qasim",
              # "senderReference": "",
             #  "senderStateCode": "CA",
               "sourceOfFundsCode": "05",
               "systemsTraceAuditNumber": "451018",
               "transactionCurrencyCode": request_body['currency'],
               "transactionIdentifier": "381228649430015",
               "settlementServiceIndicator": "9",
               "colombiaNationalServiceData": {
                   "countryCodeNationalService": "170",
                   "nationalReimbursementFee": "20.00",
                   "nationalNetMiscAmountType": "A",
                   "nationalNetReimbursementFeeBaseAmount": "20.00",
                   "nationalNetMiscAmount": "10.00",
                   "addValueTaxReturn": "10.00",
                   "taxAmountConsumption": "10.00",
                   "addValueTaxAmount": "10.00",
                   "costTransactionIndicator": "0",
                   "emvTransactionIndicator": "1",
                   "nationalChargebackReason": "11"
               }
               }
    url = "https://sandbox.api.visa.com/visadirect/fundstransfer/v1/pushfundstransactions"

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic Sk9IUkUyQTNHTUtHWjNLN0xPMlMyMWNCWlZlNjhHenJlencyeTF2eVpXdzIzVnNfNDpXMGUyNGZ4SVBk'
    }
    r = requests.post(url,
                      cert=('Certificates/cert.pem', 'Certificates/privateKey.pem'),
                      headers=headers,
                      auth=("5COPOJAN7B63B74JMML121Z4flu5-fyzcdQ0HNwFM5zBxlwtc", "zhrd4VO3R4Owe7"),
                      data=json.dumps(payload))
    # print(r.content())
    response = r.text.encode('utf8')
    print(response)
    return response


@app.route('/financialStruggle', methods=["POST"])
def financial_struggle():

    request_body = request.json
    print(request_body)

    payload =  {
        "requestHeader": {
        "messageDateTime": "2020-06-26T21:21:03.327Z",
        "requestMessageId": "6da60e1b8b024532a2e0eacb1af58581"
        },
        "requestData": {
        "naicsCodeList": [
        ""
        ],
        "merchantCategoryCodeList": [
        request_body['merchantCategoryCodeList']
        ],
        "merchantCategoryGroupsCodeList": [
        ""
        ],
        "postalCodeList": [
            request_body['postalCodeList']
        ],
        "msaList": [
            request_body['msaList']
        ],
        "countrySubdivisionList": [
        ""
        ],
        "merchantCountry": "840",
        "monthList": [
            request_body['monthList']
        ],
        "accountFundingSourceList": [
        "ALl"
        ],
        "eciIndicatorList": [
        "All"
        ],
        "platformIDList": [
        "All"
        ],
        "posEntryModeList": [
        "All"
        ],
        "cardPresentIndicator": "CARDPRESENT",
        "groupList": [
        "STANDARD"

        ]
        }
        }

    url = "https://sandbox.api.visa.com/merchantmeasurement/v1/merchantbenchmark"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic Sk9IUkUyQTNHTUtHWjNLN0xPMlMyMWNCWlZlNjhHenJlencyeTF2eVpXdzIzVnNfNDpXMGUyNGZ4SVBk'
    }
    r = requests.post(url,
                      cert=('Certificates/cert.pem', 'Certificates/privateKey.pem'),
                      headers=headers,
                      auth=("5COPOJAN7B63B74JMML121Z4flu5-fyzcdQ0HNwFM5zBxlwtc", "zhrd4VO3R4Owe7"),
                      data=json.dumps(payload))
    # print(r.content())
    response = r.text.encode('utf8')
    print(response)
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80")
    #app.run()









