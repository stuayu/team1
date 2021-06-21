from Crypto.Cipher import AES
from Crypto.Util import Padding
from peewee import *
import datetime
from DB.db_access import db_login
from key.readkey import get_key  # AESキーの取得


db = db_login()


def get_data(teacher_id: str, student_idm: str, iv: bytes):
    """ここにメイン関数を作る
    teacher_id : AES公開キーで暗号化
    student_idm: AES公開キーで暗号化
    """
    cipher = AES.new(key=get_key, mode=AES.MODE_CBC, iv=iv)    # AESの秘密キーで復号化準備
    teacher = cipher.decrypt(teacher_id) # AESの秘密キーで復号化
    student = cipher.decrypt(student_idm)  # AESの秘密キーで復号化
    plain_teacher = Padding.unpad(teacher, 32, 'pkcs7')
    plain_student = Padding.unpad(student, 32, 'pkcs7')


    # debug
    print('teacherの復号結果:' + plain_teacher)
    print('studentの復号結果:' + plain_student)

    #subject = get_subject(teacher)

    #result = create_attend(subject, student)
    return 0


def get_subject(teacher_id: str):
    """ここに現在の日時と曜日と教員のIDから出欠登録しようとしている科目の決定
       戻り値：科目ID
    """

    return subject


def create_attend(subject_id: str, student_idm: str):
    """渡された科目IDと学生IDmを使いデータベースに一致する箇所を探し
       一致するデータが存在していれば時刻に応じて出席，遅刻，欠席を登録(回数を+1)する
       一致するデータがなければエラーを返す．
       これを元にメインではラズパイに返すメッセージ文を生成し返す．
    """
