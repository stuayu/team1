
from fastapi import FastAPI, Depends, Form
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from DB import db  # DBフォルダにいるdb.pyの関数を読み込み
from routers import login
from DB import db_subject

# uvicorn main:app --reload --host 0.0.0.0
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


@app.post("/user/check/", tags=["RaspberryPi"])
async def check_idm(teacher: str = Form(...), IDm: str = Form(...)):
    """idmと教職員データを利用して
       戻り値に出席，遅刻を返す 
    """


@app.get("/")
def get_root():
    return {"message": "fastapi sample"}

# curl -X POST -H "Content-Type: application/json" -d '{"param1":"test1", "param2":"text2"}' http://localhost:8000/


@app.post("/")
def post_root(testParam: TestParam):
    print(testParam)
    return testParam


@app.get("/db/{table}")     # docsに表示されるURL
def get_table(table: str):  # table変数を文字列に定義
    """データベースにあるテーブル名を入力すると中身がそのまま帰ってくる機能です(危険)"""
    selectSql = 'Select * from %s' % table  # %sを変数 table に置き換える
    conn = db.createMysqlConnecter()    # データベースにログイン
    return db.selectData(conn, selectSql)    # データベースから情報取得

#ユーザの教科を取得(仮)
#@app.get("/db/",tags=["Subject"])
#def get_db_subject(tokens):
 #   return get_subject(tokens)

