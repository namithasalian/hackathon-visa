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

    category_code_mappings = {"FAST_FOOD_RESTAURANTS": 5814}
    print(request_body)

    payload = {"header": {
                "messageDateTime": "2020-06-20T18:14:39.903",
                "requestMessageId": "Request_001",
                "startIndex": "0"
                    },
                    "searchAttrList": {
                    "merchantCategoryCode": [
                        category_code_mappings[request_body['category']]
                        ],
                    "merchantCountryCode": "840",
                    "latitude": "37.363922",
                    "longitude": "-121.929163",
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80")
