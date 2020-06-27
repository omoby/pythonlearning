import io
import requests
from urllib.parse import urljoin
from parsel import Selector

try:
    from PIL import Image
except ImportError:
    import Image
import  pytesseract

url = 'http://www.porters.vip/confusion/recruit.html'

resp = requests.get(url)
sel = Selector(resp.text)

image_name  = sel.css('.pn::attr("src")').extract_first()

image_url = urljoin(url,image_name)
print(image_url)
'http://www.porters.vip/confusion/phonenumber.png'

image_body = requests.get(image_url).content

image_stream = Image.open(io.BytesIO(image_body))


print(pytesseract.image_to_string(image_stream))