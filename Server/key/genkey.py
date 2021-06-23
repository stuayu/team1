from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# 鍵の生成
private_key = AES.get_random_bytes(32) #AES256のキーを生成
with open('./key/key.bin', 'wb') as f:
    f.write(private_key)
