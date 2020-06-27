import json
import sys

data = '{"msg": "您的网络好像不太给力，请稍后再试", "code": 406, "customData": {"verifyPageUrl": "https://verify.meituan.com/v2/web/general_page?action=spiderindefence&requestCode=25db161d89c74a81bf7a102924720fba&platform=1&adaptor=auto&succCallbackUrl=https%3A%2F%2Foptimus-mtsi.meituan.com%2Foptimus%2FverifyResult%3ForiginUrl%3Dhttps%253A%252F%252Fm.dianping.com%252Fsiping%252Fch10%252Fr-744", "imageUrl": "https://verify.meituan.com/v2/captcha?action=spiderindefence&request_code=25db161d89c74a81bf7a102924720fba", "requestCode": "25db161d89c74a81bf7a102924720fba", "verifyUrl": "https://optimus-mtsi.meituan.com/optimus/verify?request_code=25db161d89c74a81bf7a102924720fba"}}'

if "403 Forbidden" in data:
    print(f"res={data}")
    sys.exit(0)
elif "您的网络好像不太给力" in data:
    data = json.loads(data)
    print(data)
    print(type(data))
    customData = data['customData']
    print(customData)
    print(type(customData))
    verifyPageUrl = customData['verifyPageUrl']
    imageUrld = customData['imageUrl']
    requestCode = customData['requestCode']
    verifyUrl = customData['verifyUrl']
    print(f"verifyPageUrl=%s "%(verifyPageUrl))
    print(f"imageUrld=%s"%(imageUrld))
    print(f"requestCode=%s "%(requestCode))
    print(f"verifyUrl=%s"%(verifyUrl))



    sys.exit(0)