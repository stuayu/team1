#ログインした人の教科データの入手
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from auth_pro import get_current_user, get_current_user_with_refresh_token, create_tokens, authenticate
from login.auth_pro import get_current_user, get_current_user_with_refresh_token, create_tokens, authenticate, create_user, password_renew
from DB import db


def get_subject(tokens):
    user1 = get_current_user(tokens)
    selectSql = 'Select * from %s' % table
    conn = db.createMysqlConnecter()
    user2 = db.selectData(conn, selectSql)
    if user1 == user2:
        subject = user2[0]

    return subject





