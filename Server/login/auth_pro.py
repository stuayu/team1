# ログインした際のパスワード認証とトークン生成の関数

from fastapi import Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt
from login.model import User
from hashlib import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate(name: str, password: str):
    """パスワード認証し、userを返却"""
    # ユーザー名が登録されているかチェック
    try:
        user = User.get(name=name)
    except:
        raise HTTPException(status_code=401, detail='ユーザIDが正しくありません')
    dat = password
    hs = sha256(dat.encode()).hexdigest()
    # パスワードが違った際は例外(エラー)を発生させる
    if user.password != hs:
        raise HTTPException(status_code=401, detail='パスワード不一致')
    return user


def create_tokens(user_id: int):
    """パスワード認証を行い、トークンを生成"""
    # ペイロード作成
    access_payload = {
        'token_type': 'access_token',
        'exp': datetime.utcnow() + timedelta(minutes=60),
        'user_id': user_id,
    }
    refresh_payload = {
        'token_type': 'refresh_token',
        'exp': datetime.utcnow() + timedelta(days=90),
        'user_id': user_id,
    }

    # トークン作成（'SECRET_KEY123'はより複雑にした方がいい）
    access_token = jwt.encode(
        access_payload, 'SECRET_KEY123', algorithm='HS256')
    refresh_token = jwt.encode(
        refresh_payload, 'SECRET_KEY123', algorithm='HS256')

    # DBにリフレッシュトークンを保存
    User.update(refresh_token=refresh_token).where(
        User.id == user_id).execute()

    #return access_token
    return {'access_token': access_token, 'refresh_token': refresh_token, 'token_type': 'bearer'}


def create_user(_name: str, _password: str):
    """ユーザを作成する"""
    dat = _password
    hs = sha256(dat.encode()).hexdigest()  # sha256で暗号化しデータベース内に保存
    if User.select().where(User.name == _name):
        raise HTTPException(status_code=401, detail='すでにユーザーは存在しています')
    User.create(name=_name, password=hs)
    return {'user': _name}


def password_renew(_name: str, old_password: str, new_password: str):
    """パスワード変更"""
    old_dat = old_password
    new_dat = new_password
    new_hs = sha256(new_dat.encode()).hexdigest()  # sha256で暗号化
    old_hs = sha256(old_dat.encode()).hexdigest()  # sha256で暗号化

    if User.select().where(User.name != _name):
        raise HTTPException(status_code=401, detail='すでにユーザーは存在していません')

    elif User.select().where(User.password != old_hs):
        raise HTTPException(
            status_code=401, detail='パスワードが間違っていますもう一度確認してください')

    else:
        User.update(password=new_hs).where(User.name == _name).execute()

    return {'message': '新しいパスワードになりました'}


def get_current_user_from_token(token: str, token_type: str):
    """tokenからユーザーを取得"""
    # トークンをデコードしてペイロードを取得。有効期限と署名は自動で検証される。
    payload = jwt.decode(token, 'SECRET_KEY123', algorithms=['HS256'])

    # トークンタイプが一致することを確認
    if payload['token_type'] != token_type:
        raise HTTPException(status_code=401, detail=f'トークンタイプ不一致')

    # DBからユーザーを取得
    user = User.get_by_id(payload['user_id'])

    # リフレッシュトークンの場合、受け取ったものとDBに保存されているものが一致するか確認
    if token_type == 'refresh_token' and user.refresh_token != token:
        print(user.refresh_token, '¥n', token)
        raise HTTPException(status_code=401, detail='リフレッシュトークン不一致')

    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """アクセストークンからログイン中のユーザーを取得"""
    return get_current_user_from_token(token, 'access_token')


async def get_current_user_with_refresh_token(token: str = Depends(oauth2_scheme)):
    """リフレッシュトークンからログイン中のユーザーを取得"""
    return get_current_user_from_token(token, 'refresh_token')
