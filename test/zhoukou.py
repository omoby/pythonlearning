import requests

url = "http://www.ly.com/HotelInfo-91671048.html"

headers = {
    'Connection': "keep-alive",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Cookie': 'qdid=-9999; 17uCNRefId=RefId=0&SEFrom=&SEKeyWords=; TicketSEInfo=RefId=0&SEFrom=&SEKeyWords=; CNSEInfo=RefId=0&tcbdkeyid=&SEFrom=&SEKeyWords=&RefUrl=; Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1590567678; Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1590567678; route=8b01b73ddb9a0b35bfc0aec7417be66a; __tctmc=144323752.95755802; __tctmd=144323752.737325; __tctma=144323752.1590567675491115.1590567675803.1590567675803.1590567675803.1; __tctmb=144323752.519688206059060.1590567675803.1590567675803.1; __tctmu=144323752.0.0; __tctmz=144323752.1590567675803.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); longKey=1590567675491115; __tctrack=0; Hm_lvt_f97c1b2277f4163d4974e7b5c8aa1e96=1590567678; Hm_lpvt_f97c1b2277f4163d4974e7b5c8aa1e96=1590567678; User-Ref-SessionId=7559-e2ae-d14b-2889-351a-2c8d; trace_extend={"deviceid":"1590567675491115","appid":"1","userid":"1590567675491115","orderfromid":"57000","sessionid":"7559-e2ae-d14b-2889-351a-2c8d","pvid":"49de9a2d"}; wangba=1590567677917; td_sid=MTU5MDU2NzY4MCw3YzdjNGUzYzcyNzA0NWUzMGQ1OTU1ZWQxNGY0MmI1MzU3M2ZlYWY2MmJmMDMwZjk1ZmE1YThiYjY3OWMxYWM2LDI4MTE2NzRlNDZlZjQ1YjAwYzQyYWY1YTVjZmNkY2QxNDliZDBkMzk5NDlhYTViNDA1NWQwN2FkYzE0YTg0Mjk=; k_st=61.160.89.186|1590567680; td_did=nB3iLNeFoZ1DWay0lcsGOR7m%2FU1EpjE720kpUbOCnVXOPU6OSPjiCKlb8gQHG5Z9PuqD94aElKlgbTStOPOJD%2FHoESU8xHnDY4v%2B0cewBoBaNqJ3IvB0d5%2Bk0P8%2F40eXkL6KyqA5DqplxnjP%2F8sGPhf9tNIfKwTHo8J8wMXz2jeBQTvSEmTPbxRwdNJ91oshgsNvmM8Fk8xWgi9Kwoz3ew%3D%3D; t_q=1590567679285; firsttime=1590567679401; lasttime=1590567679401; sug_act_info=; trace_token=',
    'cache-control': "no-cache",
    'Postman-Token': "d4689b77-c590-44c7-a3dc-52a3a85a7404"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)