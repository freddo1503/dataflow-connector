from pydantic import BaseModel, EmailStr


# User schemas
class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


# Message schemas
class MessageBase(BaseModel):
    content: str


class MessageCreate(MessageBase):
    user_id: int


class MessageResponse(MessageBase):
    id: int
    user: UserResponse
    timestamp: str

    class Config:
        from_attributes = True
