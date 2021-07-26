
#from Server.DB.db_subject import get_subject_student
#from Server.DB.db_csv import csv_create
from fastapi import FastAPI, Depends, Form
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
# DBフォルダにいるdb.pyの関数を読み込み．なお同じフォルダ内のファイルをインポートする場合は","で追加
from DB import db, db_subject
from routers import login, front
from DB.check_idm import get_data
from DB.db_csv import csv_create

# uvicorn main:app --reload
app = FastAPI(
    title="Team1 Attendance Management System",
    description="I'm tired ... . It's a black company.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)
# routers/login からインポートする
app.include_router(login.router)
app.include_router(front.router)

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
    return get_data(teacher_id, student_idm)

@app.get("/")
def get_root():
    return {"message": "fastapi sample"}

# curl -X POST -H "Content-Type: application/json" -d '{"param1":"test1", "param2":"text2"}' http://localhost:8000/


@app.post("/")
def post_root(testParam: TestParam):
    print(testParam)
    return testParam

@app.post("/csv/",tags=["DB"])
def get_csv(token:str = Form(...),id:str = Form(...)):
    """csvファイルを作成します"""
    return csv_create(token, id)
    
