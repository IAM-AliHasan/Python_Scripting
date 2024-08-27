import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://alihasan07.atlassian.net/rest/api/3/issue"
API_TOKEN = "paste your API token here "

auth = HTTPBasicAuth("ah7069249@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps({
  "fields": {
    "project": {
      "key": "SCRUM"
    },
    "issuetype": {
      "id": "10003"
    },
    "summary": "This is the creation of the second issue ",
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
    }
  }
})

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
