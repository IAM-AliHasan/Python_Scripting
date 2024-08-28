# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

# Define a route that handles POST requests
@app.route('/createJira', methods=['POST'])
def createJira():
    payload = request.json  # Assuming the payload is in JSON format

    # Extract the comment text
    comment_text = payload.get('comment', {}).get('body', '')

    # Check if the comment starts with '/jira'
    if comment_text.startswith('/jira'):
        url = "https://alihasan07.atlassian.net/rest/api/3/issue"
        API_TOKEN="write your token here "
        auth = HTTPBasicAuth("ah7069249@gmail.com", API_TOKEN)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = json.dumps({
            "fields": {
                "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": "Order entry fails when selecting supplier.",
                                    "type": "text"
                                }
                            ],
                            "type": "paragraph"
                        }
                    ],
                    "type": "doc",
                    "version": 1
                },
                "project": {
                    "key": "SCRUM"
                },
                "issuetype": {
                    "id": "10003"
                },
                "summary": "Main order flow broken",
            },
            "update": {}
        })

        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        # Ignore the request if the comment does not start with '/jira'
        return "Command not recognized."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
