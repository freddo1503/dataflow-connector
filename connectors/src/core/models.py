from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr
from typing import Optional, List


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    messages: List["Message"] = Relationship(back_populates="user")


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    timestamp: str
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="messages")
