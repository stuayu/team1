from Crypto.Cipher import AES

# ファイルからキーを読み込む
def get_key():
    with open('./key/key.bin', 'rb') as f:
        key_r = f.read(32)  #keyの読み込み

    return key_r
