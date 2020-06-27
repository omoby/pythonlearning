import io
import requests
from urllib.parse import urljoin
from parsel import Selector

try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

url = 'https://www.gxrc.com/company/60056'
response = requests.get(url)
selector = Selector(response.text)

image_name = selector.css('.con::attr("src")').extract_first()

print(image_name)
image_url = 'https://vip.gxrc.com/Public/Phone/0F555FA2-D465-435E-9A94-1FACA77FD9C0'
print(image_url)

image_body = requests.get(image_url).content

image_stream = Image.open(io.BytesIO(image_body))

data = pytesseract.image_to_string(image_stream)
print(data)
