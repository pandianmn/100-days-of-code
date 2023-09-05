from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from models import Users
from database import SessionLocal
from .auth import get_current_user, bcrypt_context
from pydantic import BaseModel, Field


router = APIRouter(prefix="/users", tags=["users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


@router.get("/get_user", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    user = db.query(Users).filter(Users.id == user.get("id")).first()
    return user


@router.put("/change_password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(
    user: user_dependency, db: db_dependency, user_verification: UserVerification
):
    user = db.query(Users).filter(Users.id == user.get("id")).first()
    if not bcrypt_context.verify(user_verification.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Authentication Failed")
    user.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.commit()
    return user
