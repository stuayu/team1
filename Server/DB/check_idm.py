import datetime
from fastapi import HTTPException
from DB import db


def get_data(teacher_id: str, student_idm: str):
    """ここにメイン関数を作る
    """
    subject_id = get_subject(teacher_id)

    if subject_id == 0:
        raise HTTPException(status_code=401, detail='すでに登録時刻を過ぎているか，開始していません．')

    result = create_attend(subject_id, student_idm)
    return 0


def get_subject(teacher_id: str):
    """ここに現在の日時と曜日と教員のIDから出欠登録しようとしている科目の決定
       戻り値：講義ID
    """
    temp = []  # 一時的に配列に代入するよう
    dt = datetime.datetime.now()  # 今日の日付を取得 (2021-06-23)
    date = "{}/{}/{}".format(dt.year, dt.month,
                             dt.day)  # 日付の形式を変更(2021/6/23)
    time= "{}:{}".format(dt.hour,dt.minute) #取得した時間 (16:41)
    # time-rule テーブルを操作
    # %sを変数 date に置き換える
    selectSql_1 = "Select `日付`, `時間割`,`回数` FROM `subject-rules2` WHERE  `日付`='%s'" % date
    conn = db.createMysqlConnecter()

    temp = db.selectData(conn, selectSql_1)

    time_rule: str = temp[0][1]  # 時間割データ
    #number: int = temp[0][2]  # 第何回の講義か

    #受付開始時間以上遅刻限度以下かつ時間割と教員IDがあっている場合のみ実行される．
    selectSql_2 = "Select `講義ID`,`時間割`,`教員ID`,`受付開始`,`遅刻限度` FROM `time-rules` WHERE `時間割`='%s'&& `教員ID`='%s' && '%s' BETWEEN `受付開始` AND `遅刻限度`" % (time_rule , teacher_id , time)

    temp = db.selectData(conn, selectSql_2)

    if len(temp) == 0:
        return 0

    subject:str = temp[0][0]

    return subject


def create_attend(subject_id: str, student_idm: str):
    """渡された科目IDと学生IDmを使いデータベースに一致する箇所を探し
       一致するデータが存在していれば時刻に応じて出席，遅刻，欠席を登録(回数を+1)する
       一致するデータがなければエラーを返す．
       これを元にメインではラズパイに返すメッセージ文を生成し返す．
    """

if __name__ == '__main__':
    res = get_subject('P003')
    print(res)
