import binascii
import nfc
from time import time
import sys
import requests
from requests.api import request
from requests.models import Response

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

if __name__ == '__main__':
    cr = MyCardReader()
    start_time = time()
    while True:
        print("touch card:")
        cr.read_id()
        print("released")
        print("IDm = {}".format(cr.idm))
        IDm = 'cr.idm'
        ID = 'entry1_frame.get()'
        #data引数に、postパラメータを渡す
        payload = {'teacher_id': ID,'student_idm':cr.idm}
        header = {'accept': 'application/json','Content-Type': 'application/x-www-form-urlencoded'}
        res =  requests.post('http://localhost:8000/user/check/',data=payload,headers=header)
        json_data = res.json()
        print(json_data['detail'])
        current_time = time()
        #print("time = %3.2f" % (current_time - start_time))
        if current_time - start_time > 10.0:
            sys.exit()