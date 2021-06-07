# -*- coding: utf-8 -*-
import binascii
import nfc
import time
from threading import Thread, Timer

# カード待ち受けの1サイクル秒
TIME_cycle = 1.0
# カード待ち受けの反応インターバル秒
TIME_interval = 0.2
# タッチされてから次の待ち受けを開始するまで無効化する秒
TIME_wait = 3

# NFC接続リクエストのための準備
# 212F(FeliCa)で設定
target_req_card = nfc.clf.RemoteTarget("212F")
# 0003(Suica)
target_req_card.sensf_req = bytearray.fromhex("0000030000")

print 'waiting...'
while True:
    # USBに接続されたNFCリーダに接続してインスタンス化
    clf = nfc.ContactlessFrontend('usb')
    # カード待ち受け開始
    # clf.sense( [リモートターゲット], [検索回数], [検索の間隔] )
    target_res = clf.sense(target_req_card, iterations=int(TIME_cycle//TIME_interval)+1 , interval=TIME_interval)
    if target_res != None:

        tag = nfc.tag.activate_tt3(clf, target_res)
        tag.sys = 3

        #IDmを取り出す
        idm = binascii.hexlify(tag.idm)
        print 'idm = ' + idm
        time.sleep(TIME_wait)
    #end if
    clf.close()
#end while
