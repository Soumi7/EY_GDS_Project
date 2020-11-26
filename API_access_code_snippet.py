import requests
from requests_ntlm import HttpNtlmAuth

requests.get("http://sharepoint-site.com", auth=HttpNtlmAuth('DOMAIN\\USERNAME','PASSWORD'))

#https://www.pharmasug.org/proceedings/2020/AD/PharmaSUG-2020-AD-341.pdf