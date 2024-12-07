from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from schemas import UserCreate, UserResponse, MessageCreate, MessageResponse
from utils import get_db_session, get_kafka_producer
from services import UserService
from services import MessageService

router = APIRouter()


@router.post("/users", response_model=UserResponse, status_code=201)
def create_user(user_data: UserCreate, session: Session = Depends(get_db_session)):
    try:
        service = UserService(session)
        return service.create_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/messages", response_model=MessageResponse, status_code=202)
def send_message(
    message_data: MessageCreate, session: Session = Depends(get_db_session)
):
    try:
        service = MessageService(session, get_kafka_producer())
        return service.send_message(message_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
