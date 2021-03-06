from fastapi import APIRouter, Depends, Form
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from DB.db_subject import get_subject
from DB.db_front import print_attend

router = APIRouter()


# ユーザ(教員)やユーザ(学生)の教科を取得
@router.post("/getSub/", tags=["Subject"])
def get_db_subject(token: str = Form(...)):
    """アクセストークンを利用して先生の担当科目や学生の履修教科を返す"""
    return get_subject(token)

# 講義回数をJSONで返す


# 出欠状況検索


#@router.post("/attend", tags=["Subject"])
#def print_db_attend(subject_id: str = Form(...), number: int = Form(...), userid: str = Form(...)):
#    """出欠状況の検索"""
#    return print_attend(subject_id, number, userid)

@router.post("/attend", tags=["Subject"])
def print_db_attend(subject_id: str = Form(...), token: str = Form(...)):
    """出欠状況の検索"""
    return print_attend(subject_id, token)

