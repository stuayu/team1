from peewee import *
from DB.db_access import db_login

db = db_login()


def get_data(teacher_id: str, student_idm: str):
    """ここにメイン関数を作る"""


def get_subject(teacher_id: str):
    """ここに現在の日時と曜日と教員のIDから出欠登録しようとしている科目の決定
       戻り値：科目ID
    """


def create_attend(subject_id: str, student_idm: str):
    """渡された科目IDと学生IDmを使いデータベースに一致する箇所を探し
       一致するデータが存在していれば時刻に応じて出席，遅刻，欠席を登録(回数を+1)する
       一致するデータがなければエラーを返す．
       これを元にメインではラズパイに返すメッセージ文を生成し返す．
    """
