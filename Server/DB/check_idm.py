import datetime
from DB import db
from key.readkey import get_key  # AESキーの取得


def get_data(teacher_id: str, student_idm: str, iv: bytes):
    """ここにメイン関数を作る
    """

    #subject = get_subject(teacher)

    #result = create_attend(subject, student)
    return 0


def get_subject(teacher_id: str):
    """ここに現在の日時と曜日と教員のIDから出欠登録しようとしている科目の決定
       戻り値：講義ID
    """
    temp = []  # 一時的に配列に代入するよう
    date = datetime.date.today()  # 今日の日付を取得 (2021-06-23)
    date = "{}/{}/{}".format(date.year, date.month,
                             date.day)  # 日付の形式を変更(2021/6/23)
    # time-rule テーブルを操作
    # %sを変数 date に置き換える
    selectSql = "Select `日付`, `時間割`,`回数` FROM `subject-rules2` WHERE  `日付`=%s" % date
    conn = db.createMysqlConnecter()

    temp = db.selectData(conn, selectSql)

    time_rule = temp[1][2]  # 時間割データ
    number = temp[1][3]  # 第何回の講義か
    


    return subject


def create_attend(subject_id: str, student_idm: str):
    """渡された科目IDと学生IDmを使いデータベースに一致する箇所を探し
       一致するデータが存在していれば時刻に応じて出席，遅刻，欠席を登録(回数を+1)する
       一致するデータがなければエラーを返す．
       これを元にメインではラズパイに返すメッセージ文を生成し返す．
    """
