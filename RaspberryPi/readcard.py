# -*- coding: utf-8 -*-
import binascii
import nfc
from time import time
import sys
import requests
from requests.api import request

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
        IDm = cr.idm
        ID = 'P001'
        #data引数に、postパラメータを渡す
        payload = {'ID': 'value1','IDm':'value2'}
        res =  requests.post('http://192.168.1.23:8000/user/check/',data=payload)
        print("res.tex")
        current_time = time()
        #print("time = %3.2f" % (current_time - start_time))
        if current_time - start_time > 10.0:
            sys.exit()