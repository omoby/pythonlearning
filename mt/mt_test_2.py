import requests

url = "http://172.22.5.243:30080/download-api/v1/requests/11422/32d2e6a7-767d-4915-8210-754befd4aa01?user=inspur&size=1&ts=1589451849780"

payload  = {}
headers = {
  'Date': 'Thu, 14 May 2020 10:27:23 GMT',
  'Authorization': 'hmac username="inspur", algorithm="hmac-sha256", headers="date", signature="I/qSxXH68uKb9WOyFlOBjNDOfULLXkI1Eu4Ml8jLe/g="',
  'X-API-TOKEN': 'sadb',
  'connection': 'Keep-Alive',
  'Accept': 'application/json',
  'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))