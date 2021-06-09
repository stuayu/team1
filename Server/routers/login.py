from fastapi import APIRouter, Depends, Form
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from login.auth_pro import get_current_user, get_current_user_with_refresh_token, create_tokens, authenticate, create_user, password_renew
router = APIRouter()


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


@router.post("/token", response_model=Token, tags=["login"])
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """トークン発行"""
    user = authenticate(form.username, form.password)
    return create_tokens(user.id)


@router.get("/refresh_token/", response_model=Token, tags=["login"])
async def refresh_token(current_user: User = Depends(get_current_user_with_refresh_token)):
    """リフレッシュトークンでトークンを再取得"""
    return create_tokens(current_user.id)


@router.get("/users/me/", response_model=User, tags=["login"])
async def read_users_me(current_user: User = Depends(get_current_user)):
    """ログイン中のユーザーを取得"""
    return current_user


@router.post("/user/create/", tags=["login"])
async def signup(username: str = Form(...), password: str = Form(...)):
    """ユーザー作成"""
    res = create_user(username, password)
    return res


@router.post("/user/renewpass/", tags=["login"])
async def renewpass(username: str = Form(...), old_password: str = Form(...), new_password: str = Form(...)):
    """ パスワード更新"""
    res = password_renew(username, old_password, new_password)
    return res
