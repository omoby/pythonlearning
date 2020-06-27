import execjs


def get_hello():
    with open('test.js' ,'r') as f:
        js_code = f.read()
    result = execjs.compile(js_code).call('get_hello')
    print(result)


if __name__ == '__main__':
    get_hello()