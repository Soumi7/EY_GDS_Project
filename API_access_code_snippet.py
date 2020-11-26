import requests
from requests_ntlm import HttpNtlmAuth

requests.get("http://sharepoint-site.com", auth=HttpNtlmAuth('DOMAIN\\USERNAME','PASSWORD'))
