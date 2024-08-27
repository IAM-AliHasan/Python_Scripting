# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://alihasan07.atlassian.net/rest/api/3/project"
API_TOKEN = "place your own or use as the environment variable "

auth = HTTPBasicAuth("ah7069249@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)



output=json.loads(response.text)
for i, project in enumerate(output):
    name = project["name"]
    print(f"The name of project number {i + 1} is {name}")
