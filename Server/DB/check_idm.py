import datetime
from fastapi import HTTPException
from DB import db


def get_data(teacher_id: str, student_idm: str):
    """ここにメイン関数を作る
    """
    subject_id, attend, number = get_subject(teacher_id)

    attend = create_attend(subject_id, student_idm, attend)

    message = attend+"と正常に登録しました。"
    print(message)
    return {'detail': message}


def get_subject(teacher_id: str):
    """ここに現在の日時と曜日と教員のIDから出欠登録しようとしている科目の決定
       戻り値：講義ID
    """
    temp = []  # 一時的に配列に代入するよう
    dt = datetime.datetime.now()  # 今日の日付を取得 (2021-06-23)
    date = "{}/{}/{}".format(dt.year, dt.month,
                             dt.day)  # 日付の形式を変更(2021/6/23)
    time = "{}:{}".format(dt.hour, dt.minute)  # 取得した時間 (16:41)
    # time_rule テーブルを操作
    # %sを変数 date に置き換える
    selectSql_1 = "Select `日付`, `時間割`,`回数` FROM `subject_rules2` WHERE  `日付`='%s'" % date
    conn = db.createMysqlConnecter()

    temp = db.selectData(conn, selectSql_1)
    if len(temp) == 0:
        raise HTTPException(
            status_code=401, detail="データベースに今日の日付が存在していません．もう一度確認してください．")

    time_rule: str = temp[0][1]  # 時間割データ 例) Wed
    number: int = temp[0][2]  # 第何回の講義か

    # 受付開始時間以上遅刻限度以下かつ時間割と教員IDがあっている場合のみ実行される．
    selectSql_2 = "Select `講義ID`,`時間割`,`教員ID`,`受付開始`,`出席限度`,`遅刻限度` FROM `time_rules` WHERE `時間割`='%s'&& `教員ID`='%s' && '%s' BETWEEN `受付開始` AND `遅刻限度`" % (
        time_rule, teacher_id, time)

    temp = db.selectData(conn, selectSql_2)

    if len(temp) == 0:  # 配列が空の場合(検索結果がなしでエラーを発生させる)
        raise HTTPException(status_code=401, detail='すでに登録時刻を過ぎているか，開始していません．')

    if len(temp) != 1:  # もし配列が2以上の場合エラーを発生させる．
        raise HTTPException(
            status_code=401, detail='教科を検索しましたが2件以上ヒットしてしまいました．デバッグしましょう．')

    subject: str = temp[0][0]

    if temp[0][3] <= time <= temp[0][4]:
        attend = 1  # 出席とする

    elif temp[0][4] < time <= temp[0][5]:
        attend = 0  # 遅刻とする
    else:
        attend = -1

    return subject, attend, number  # 講義ID,出席チェック結果,第何回目を返す


def create_attend(subject_id: str, student_idm: str, attend: int, number: int):
    """渡された科目IDと学生IDmを使いデータベースに一致する箇所を探し
       これを元にメインではラズパイに返すメッセージ文を生成し返す．
    """
    temp = []
    # 暫定的に 履修教科一覧が書かれているファイルを student_all としている．
    selectSql_1 = "Select * FROM `student_all` WHERE `IDm`='%s' AND `%s`='%s'" % (
        student_idm, subject_id, subject_id)

    conn = db.createMysqlConnecter()
    temp = db.selectData(conn, selectSql_1)

    if len(temp) == 0:  # 配列が空の場合(検索結果がなしでエラーを発生させる)
        raise HTTPException(status_code=401, detail='履修登録がされているかもう一度確認してください．')

    if attend == 1:
        attend_str = '出席'
    elif attend == 0:
        attend_str = '遅刻'
    else:
        raise HTTPException(status_code=401, detail='出席遅刻判定でエラーが発生しました．')

    selectSql_2 = "INSERT INTO `student_attend` (`回数`,`講義ID`,`学籍番号`,`名前`,`出欠`) VALUES ('%d','%s','%s','%s','%s')" % (
        number, subject_id, temp[0][0], temp[0][1], attend_str)

    db.insertData(conn, selectSql_2)

    result = temp[0][0]+'は'+attend+'と登録しました'
    return result


if __name__ == '__main__':
    res = get_subject('P003')
    print(res)
