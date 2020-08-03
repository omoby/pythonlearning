import base64
import hashlib
import hmac

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class EnDecryUtil():
    '''
    加密加密算法工具类
    '''

    def Ebase64(self, data):
        '''
        base64加密算法
        :param data: 加密前数据
        :return: 加密结果
        '''
        encode_data = data.encode(encoding='utf-8')
        result = base64.b64encode(encode_data)
        return result

    def Dbase64(self, data):
        '''
        base64解密
        :param data: 解密前数据
        :return: 解密结果
        '''
        decode_data = base64.b64decode(data.decode())
        result = decode_data.decode()
        return result

    def EMD5(self, data):
        '''
        MD5加密算法
        :param data: 加密前数据
        :return: 加密结果
        '''
        m = hashlib.md5()
        m.update(data.encode())
        return m.hexdigest()

    def ESha1(self, key, data):
        '''
        使用hmac实现hmac算法（以sha1为例）
        :param key: key--加密用的盐值
        :param data: 加密前数据
        :return: 加密结果
        '''
        sha1_m = hmac.new(key.encode(), digestmod="sha1")
        sha1_m.update(data.encode())
        return sha1_m.hexdigest()

    def EAES_CBC(self, data):
        '''
        AES CBC模式加密
        :param data: 加密前数据
        :return: 加密结果
        '''
        # 要加密的内容
        data = data.encode()
        # 随机生成16字节（即128位）的加密密钥
        key = get_random_bytes(16)
        # 实例化加密套件，使用CBC模式
        cipher = AES.new(key, AES.MODE_CBC)
        # 对内容进行加密，pad函数用于分组和填充
        encrypted_data = cipher.encrypt(pad(data, AES.block_size))

        # 将加密内容写入文件
        # file_out = open("encrypted.bin", "wb")
        # 在文件中依次写入key、iv和密文encrypted_data
        # [file_out.write(x) for x in (key, cipher.iv, encrypted_data)]
        cry_data_list = []
        # [print(x) for x in (key, cipher.iv, encrypted_data)]
        [cry_data_list.append(x) for x in (key, cipher.iv, encrypted_data)]

        return cry_data_list

    def DAES_CBC(self, data):
        '''
        AES CBC解密
        :param data: 解密前数据
        :return: 解密结果
        '''
        # 从前边文件中读取出加密的内容
        # file_in = open("encrypted.bin", "rb")
        # 依次读取key、iv和密文encrypted_data，16等是各变量长度，最后的-1则表示读取到文件末尾
        # key, iv, encrypted_data = [file_in.read(x) for x in (16, AES.block_size, -1)]
        key, iv, encrypted_data = data[0], data[1], data[2]

        # 实例化加密套件
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # 解密，如无意外data值为最先加密的b"123456"
        data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        return data.decode('utf-8')

    def generate_key(self):
        '''
        RSA 加密算法生成私钥和公钥
        :return:
        '''
        from Crypto.PublicKey import RSA  # 生成密钥对
        key = RSA.generate(2048)

        # 提取私钥并存入文件
        private_key = key.export_key()
        with open("private_key.pem", "wb") as f:
            f.write(private_key)

        # 提取公钥存入文件
        public_key = key.publickey().export_key()
        with open("public_key.pem", "wb") as f:
            f.write(public_key)

    def ERSA(self, data):
        '''
        RSA 加密
        :param data: 加密前数据
        :return: 解密结果
        '''
        from Crypto.PublicKey import RSA
        from Crypto.Cipher import PKCS1_OAEP
        data = data.encode('utf-8')
        # 从文件中读取公钥
        public_key = RSA.import_key(open("public_key.pem").read())
        # 实例化加密套件
        cipher = PKCS1_OAEP.new(public_key)
        # 加密
        encrypted_data = cipher.encrypt(data)

        # 将加密后的内容写入到文件
        file_out = open("encrypted_data.bin", "wb")
        file_out.write(encrypted_data)
        print(encrypted_data)

    def DRSA(self):
        '''
        RSA解密
        :return: 解密结果
        '''
        from Crypto.PublicKey import RSA
        from Crypto.Cipher import PKCS1_OAEP

        # 从私钥文件中读取私钥
        private_key = RSA.import_key(open("private_key.pem", "rb").read())
        # 实例化加密套件
        cipher = PKCS1_OAEP.new(private_key)
        # 从文件中读取加密内容
        encrypted_data = open("encrypted_data.bin", "rb").read()
        # 解密，如无意外data值为最先加密的b"123456"
        data = cipher.decrypt(encrypted_data)
        print(data.decode('utf-8'))

    def signature_RSA(self, data):
        from Crypto.Signature import pkcs1_15
        from Crypto.Hash import SHA256
        from Crypto.PublicKey import RSA

        # 以下是签名部分
        # 要签名的内容
        # data = b'123456'
        data = data.encode('utf-8')
        # 获取要签名的内容的HASH值。摘要算法是什么不重要，只要验证时使用一样的摘要算法即可
        digest = SHA256.new(data)
        # 读取私钥
        private_key = RSA.import_key(open('private_key.pem').read())
        # 对HASH值使用私钥进行签名。所谓签名，本质就是使用私钥对HASH值进行加密
        signature = pkcs1_15.new(private_key).sign(digest)

        # 以下是签名校验部分
        # 签名部分要传给签名校验部分三个信息：签名内容原文、摘要算法、HASH值签名结果
        # 获取被签名的内容的HASH值。使用与签名部分一样的摘要算法计算
        digest = SHA256.new(data)
        # 读取公钥
        public_key = RSA.import_key(open('public_key.pem').read())

        try:
            # 进行签名校验。本质上就是使用公钥解密signature，看解密出来的值是否与digest相等
            # 相等则校验通过，说明确实data确实原先的内容；不等则校验不通过，data或signature被篡改
            # 可能有人会想，如果我先修改data然后再用自己的私钥算出signature，是不是可以完成欺骗？
            # 答案是不能，因为此时使用原先的公钥去解signature，其结果不会等于digest
            pkcs1_15.new(public_key).verify(digest, signature)
            print(f"The signature is valid.")
        except (ValueError, TypeError):
            print("The signature is not valid.")

    def RC4(self, data):
        from Crypto.Cipher import ARC4
        from Crypto.Hash import SHA
        from Crypto.Random import get_random_bytes

        # 要加密的内容
        # data = b"123456"
        data = data.encode('utf-8')
        # 流加密密码长度是可变的，RC4为40到2048位
        # 一般上使用一个字符串作为初始密钥，然后再用sha1等生成真正的密钥
        # 我们这是直接点，随机生成16字节（即128位）作为密钥
        key = get_random_bytes(16)
        # 实例化加密套件
        cipher = ARC4.new(key)
        # 加密内容
        encrypted_data = cipher.encrypt(data)
        print(encrypted_data)

        # 注意在即便加解密像这里一样在同一文件里，解密时一定要重新实例化不然解密不正确
        cipher = ARC4.new(key)
        # 解密，如无意外data为前边加密的b"123456"
        data = cipher.decrypt(encrypted_data)
        print(data.decode('utf-8'))


endecry_tool = EnDecryUtil()


def main():
    data = '你好！'
    e_data = endecry_tool.Ebase64(data)
    d_data = endecry_tool.Dbase64(e_data)
    print(f'e_data={e_data},d_data={d_data}')
    print(f'md5={endecry_tool.EMD5(data)}')
    print(f'sha1={endecry_tool.ESha1("123", data)}')
    en_data = endecry_tool.EAES_CBC(data)
    endecry_tool.DAES_CBC(en_data)
    # endecry_tool.generate_key()
    endecry_tool.ERSA(data)
    endecry_tool.DRSA()
    endecry_tool.signature_RSA(data)
    endecry_tool.RC4(data)


if __name__ == '__main__':
    main()
