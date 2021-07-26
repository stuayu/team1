import binascii
import nfc
from time import time
import sys
import requests
from requests.api import request
from requests.models import Response
import json

def setting_load():
    with open('./setting.json', 'r', encoding='utf-8') as f:
        setting = json.load(f)

    return setting

class MyCardReader(object):

    def on_connect(self, tag):
        print("touched")
        self.idm = binascii.hexlify(tag.idm).decode().upper()
        return True
    
    def read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect' : self.on_connect})
        finally:
            clf.close()

def ReadCard_Post(teacher_id:str):
    cr = MyCardReader()
    start_time = time()
    set_ip = setting_load()
    IP = "http://"+str(set_ip['access_ip'])+'/api/user/check'
    while True:
        print("touch card:")
        cr.read_id()
        print("released")
        print("IDm = {}".format(cr.idm))
        IDm = 'cr.idm'
        #data引数に、postパラメータを渡す
        payload = {'teacher_id': teacher_id, 'student_idm': cr.idm}
        header = {'accept': 'application/json',
                  'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.post(IP,
                            data=payload, headers=header)
        json_data = res.json()
        print(json_data['detail'])
        current_time = time()
        #print("time = %3.2f" % (current_time - start_time))
        if current_time - start_time > 10.0:
            sys.exit()
        return json_data['detail']
        

if __name__ == '__main__':
    id = 'P001'
    message = ReadCard_Post(id)
    print(message)
