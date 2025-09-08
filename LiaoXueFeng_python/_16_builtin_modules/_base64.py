'''BASE64 encodes any BINARY to 64 CHARACTERS'''
import base64

# b_str = b'this is a binary string'
# encoded_str = base64.encodebytes(b_str)
# print(encoded_str)
# decoded_str = base64.decodebytes(encoded_str)
# print(decoded_str)

def safe_base64_decode(s):
    while len(s) % 4 != 0:
        s += '='
    return base64.decodebytes(bytes(s, encoding='utf-8'))
# 测试:
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
