
#from Server.DB.db_subject import get_subject_student
from fastapi import FastAPI, Depends, Form
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
# DBフォルダにいるdb.pyの関数を読み込み．なお同じフォルダ内のファイルをインポートする場合は","で追加
from DB import db, db_subject
from routers import login
from DB.db_subject import get_subject_teacher, get_subject_student
from DB.check_idm import get_data

# uvicorn main:app --reload
app = FastAPI()
# routers/login からインポートする
app.include_router(login.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class TestParam(BaseModel):
    param1: str
    param2: str

# curl http://localhost:8000/
# メモ
# tags=[""]で指定した文字列がグループ名になります．
# def を書いた下に"""文字列"""このように書くとブラウザにコメントを表示できます．
# Form(...)を指定した場合の動作：URLに書かれた文字列が残らないよって，積極的に利用してほしい．


@app.post("/user/check/", tags=["RaspberryPi"])
async def check_idm(teacher_id: str = Form(...), student_idm: str = Form(...)):
    """idmと教職員データを利用して
       戻り値に出席，遅刻を返す 
    """
    get_data(teacher_id, student_idm)
    
    return {"message": "登録が完了しました．"}



@app.get("/")
def get_root():
    return {"message": "fastapi sample"}

# curl -X POST -H "Content-Type: application/json" -d '{"param1":"test1", "param2":"text2"}' http://localhost:8000/


@app.post("/")
def post_root(testParam: TestParam):
    print(testParam)
    return testParam


@app.get("/db/{table}",tags=["DB"])     # docsに表示されるURL
def get_table(table: str):  # table変数を文字列に定義
    """データベースにあるテーブル名を入力すると中身がそのまま帰ってくる機能です(危険)"""
    selectSql = 'Select * from %s' % table  # %sを変数 table に置き換える
    conn = db.createMysqlConnecter()    # データベースにログイン
    return db.selectData(conn, selectSql)  # データベースから情報取得

#ユーザ(教員)の教科を取得
@app.post("/db/",tags=["Subject"])
def get_db_subject(token: str=Form(...)):
    """アクセストークンを利用して先生の担当科目を返す"""
    return get_subject_teacher(token)
    
#ユーザ(学生)の教科を取得
@app.post("/db2/",tags=["Subject"])
def get_db_subject(token: str = Form(...)):
    """アクセストークンを利用して学生の担当科目を返す"""
    return get_subject_student(token)


