import base64
import hmac
from hashlib import sha256

public_key = "eqGRl7KlipogzCWXt5lvKRbgOAOOcdj8"

def get_secret(date):

    date = 'date: '+date
    appsecret = bytes(public_key, encoding = "utf8")
    data = bytes(date,encoding="utf8")  # 加密数据
    signature = base64.b64encode(hmac.new(appsecret, data, digestmod=sha256).digest())
    return signature.decode("utf8")
    # 获取十六进制加密数据
    # signature = base64.b64encode(hmac.new(appsecret, data, digestmod=sha256).hexdigest())
    # return signature