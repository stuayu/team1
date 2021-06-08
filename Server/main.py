
from fastapi import FastAPI, Depends, Form
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from DB import db  # DBフォルダにいるdb.pyの関数を読み込み
from fastapi.security import OAuth2PasswordRequestForm
from login.auth_pro import get_current_user, get_current_user_with_refresh_token, create_tokens, authenticate, create_user, password_renew

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


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str

    class Config:
        orm_mode = True


@app.post("/token", response_model=Token, tags=["login"])
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """トークン発行"""
    user = authenticate(form.username, form.password)
    return create_tokens(user.id)


@app.get("/refresh_token/", response_model=Token, tags=["login"])
async def refresh_token(current_user: User = Depends(get_current_user_with_refresh_token)):
    """リフレッシュトークンでトークンを再取得"""
    return create_tokens(current_user.id)


@app.get("/users/me/", response_model=User, tags=["login"])
async def read_users_me(current_user: User = Depends(get_current_user)):
    """ログイン中のユーザーを取得"""
    return current_user


@app.post("/user/create/", tags=["login"])
async def signup(username: str = Form(...), password: str = Form(...)):
    """ユーザー作成"""
    res = create_user(username, password)
    return res

@app.post("/user/renewpass/", tags=["login"])
async def renewpass(username: str = Form(...), old_password: str = Form(...), new_password: str = Form(...)):
    """ パスワード更新"""
    res = password_renew(username, old_password,new_password)
    return res

@app.get("/")
def get_root():
    return {"message": "fastapi sample"}

# curl -X POST -H "Content-Type: application/json" -d '{"param1":"test1", "param2":"text2"}' http://localhost:8000/


@app.post("/")
def post_root(testParam: TestParam):
    print(testParam)
    return testParam


@app.get("/db/{table}")     # docsに表示されるURL
def get_table(table: str):   # table変数を文字列に定義
    selectSql = 'Select * from %s' % table  # %sを変数 table に置き換える
    conn = db.createMysqlConnecter()    # データベースにログイン
    return db.selectData(conn, selectSql)    # データベースから情報取得
