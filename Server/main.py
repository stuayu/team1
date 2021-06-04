
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from DB import db   # DBフォルダにいるdb.pyの関数を読み込み

# uvicorn main:app --reload --host 0.0.0.0
app = FastAPI()

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


@app.get("/")
def get_root():
    return {"message": "fastapi sample"}

# curl -X POST -H "Content-Type: application/json" -d '{"param1":"test1", "param2":"text2"}' http://localhost:8000/

@app.post("/")
def post_root(testParam: TestParam):
    print(testParam)
    return testParam

@app.get("/db/{table}")     # docsに表示されるURL
def get_table(table:str):   # table変数を文字列に定義
    selectSql = 'Select * from %s' % table  # %sを変数 table に置き換える
    conn = db.createMysqlConnecter()    # データベースにログイン
    return db.selectData(conn,selectSql)    # データベースから情報取得
