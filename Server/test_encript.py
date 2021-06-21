from Crypto.Cipher import AES
from Crypto.Util import Padding
from key.readkey import get_key  # AESキーの取得
from DB.check_idm import get_data


def encript(data: str):
    iv = b'0' * 16
    cipher = AES.new(key=get_key(), mode=AES.MODE_CBC, iv=iv)  # AESのキーで暗号化準備
    # 任意長のデータを暗号化するため，PKCS7 形式によりデータにパディング処理してから暗号化
    # 何故か動かないTypeError: object of type 'function' has no len()
    # とりあえず放置また今度
    data1 = Padding.pad(data.encode('UTF-8'), 32, 'pkcs7')
    encript_data = cipher.encrypt(data1)

    return encript_data, iv


if __name__ == '__main__':
    data1 = 'test'
    data2 = 'idm_test'
    encrypt1, iv = encript(data1)
    encrypt2, iv = encript(data2)
    decrypt = get_data(encrypt1, encrypt2, iv)
