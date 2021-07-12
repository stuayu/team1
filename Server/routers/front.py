from fastapi import APIRouter, Depends, Form
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from DB.db_subject import get_subject
from DB.db_front import get_number, print_attend

router = APIRouter()


# ユーザ(教員)やユーザ(学生)の教科を取得
@router.post("/getSub/", tags=["Subject"])
def get_db_subject(token: str = Form(...)):
    """アクセストークンを利用して先生の担当科目や学生の履修教科を返す"""
    return get_subject(token)

# 講義回数をJSONで返す
@router.post("/number", tags=["Subject"])
def get_number1(subject_id: str = Form(...)):
    """教科IDを送信されたら科目IDと実施回数をJSONで返す"""
    return get_number(subject_id)

# 出欠状況検索
@router.post("/attend", tags=["Subject"])
def print_db_attend(subject_id: str = Form(...), number: int = Form(...), userid: str = Form(...)):
    """出欠状況の検索"""
    return print_attend(subject_id, number, userid)
