from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from auth_pro import get_current_user, get_current_user_with_refresh_token, create_tokens, authenticate
from login.auth_pro import get_current_user, get_current_user_with_refresh_token, create_tokens, authenticate, create_user
from DB import db

#ログインした人の履修科目を取り出す
def get_subject(tokens):
    user1 = get_current_user(tokens)
    user2 = []
    selectSql = 'Select * from %s' % table
    conn = db.createMysqlConnecter()
    user2 = db.selectData(conn, selectSql)
    for i in user2:
        if user1 == user2:
            subject = user2[i][4,5]
    return subject





