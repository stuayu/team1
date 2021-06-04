import mysql.connector as mydb
import sys
import json   # jsonファイルの読み込み

# データベースのユーザ名などの設定を読み込み
with open('./Server/DB/db.json') as f:
  db=json.load(f)

## DBコネクターを作成する
# 引数: なし
# 戻値: mysql.connectオブジェクト

def createMysqlConnecter():
  # DB接続に失敗した場合の例外対策
  try:
    resconn = mydb.connect(
        host=db['mariadb']['host'],
        port=db['mariadb']['port'],
        user=db['mariadb']['user'],
        password=db['mariadb']['password'],
        database=db['mariadb']['dbname']
    )
  except Exception as e:
    print('[DB Connection Error]', e)
    sys.exit(1)  # プログラムをエラー終了

  # 接続が切れた場合に自動的に再接続する
  resconn.ping(reconnect=True)

  return resconn

## テーブルを作成するクエリを実行する
# 引数: ([mysql.connect]コネクタ, [str]クエリ)
# 戻値: なし


def createTable(_conn, _query):
 # CREATEのクエリかどうかを判別
  if _query.split(' ')[0].upper() != 'CREATE':
    print('[CREATE Error] Query is not create.', _query)
    sys.exit(1)

  cur = _conn.cursor()  # カーソル作成

  try:
    cur.execute(_query)  # sqlの実行
  except Exception as e:
    print('[Table Create Error]', e)
    sys.exit(1)

## データをインサートするクエリを実行する
# 引数: ([mysql.connect]コネクタ, [str]クエリ)
# 戻値: なし


def insertData(_conn, _query):
  # INSERTのクエリかどうかを判別
  if _query.split(' ')[0].upper() != 'INSERT':
    print('[INSERT Error] Query is not insert.', _query)
    sys.exit(1)

  cur = _conn.cursor()  # カーソル作成

  try:
    cur.execute(_query)  # sqlの実行
    _conn.commit()  # コミットする
  except Exception as e:
    print('[Insert Data Error]', e)
    _conn.rollback()  # ロールバックする
    sys.exit(1)

## データを参照するクエリを実行する
# 引数: ([mysql.connect]コネクタ, [str]クエリ)
# 戻値: ([Arr(data)Select結果])

def selectData(_conn, _query):
  # SELECTのクエリかどうかを判別
  if _query.split(' ')[0].upper() != 'SELECT':
    print('[SELECT Error] Query is not select.', _query)
    sys.exit(1)

  cur = _conn.cursor()  # カーソル作成

  res = []  # 戻り値用変数

  try:
    cur.execute(_query)  # sqlの実行
    res = cur.fetchall()
  except Exception as e:
    print('[Select Data Error]', e)

  return res


def main():
  print('----- mysql connector test -----')

  conn = createMysqlConnecter()
  print('DB conected [' + db['mariadb']['user'] +
        '@' + db['mariadb']['host'] + '] ... :', conn.is_connected())
  
  # select用SQL
  selectSql = '''Select * from student;
  '''

  rows = selectData(conn, selectSql)

  print('result:')
  for r in rows:
    print(r)


if __name__ == "__main__":
  main()
