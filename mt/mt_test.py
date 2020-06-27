import requests

url = "http://172.22.5.243:30080/download-api/v1/requests/1255/a3c8352c-c239-4a29-80cc-68454bb5eb59"

querystring = {"user":"inspur","size":"1","ts":"1589506604187"}

payload = ""
headers = {
    'Authorization': 'hmac username="inspur", algorithm="hmac-sha256", headers="date", signature="yJFQUvNMu/oOZPnY6lZnLGxPNrSLOsA7WQyDZjP7IaU="',
    'Date': "Fri, 15 May 2020 01:36:44 GMT",
    'cache-control': "no-cache",
    'Postman-Token': "4ae3c269-477f-408f-8d2d-deff8f6f19db"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)