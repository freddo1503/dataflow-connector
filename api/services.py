from kafka import KafkaProducer
from sqlmodel import Session
from models import User, Message
from schemas import UserCreate, UserResponse, MessageCreate, MessageResponse
from config import KAFKA_TOPIC
import datetime


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user_data: UserCreate) -> UserResponse:
        user = User(**user_data.model_dump())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return UserResponse(**user.model_dump())

    def get_user(self, user_id: int) -> UserResponse:
        user = self.session.get(User, user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
        return UserResponse(**user.model_dump())


class MessageService:
    def __init__(self, session: Session, producer: KafkaProducer):
        self.session = session
        self.producer = producer

    def send_message(self, message_data: MessageCreate) -> MessageResponse:
        # Check if the user exists
        user = self.session.get(User, message_data.user_id)
        if not user:
            raise ValueError(f"User with ID {message_data.user_id} not found")

        # Generate timestamp
        timestamp = datetime.utcnow().isoformat()

        # Create message object
        message = Message(
            content=message_data.content,
            timestamp=timestamp,
            user_id=message_data.user_id,
        )
        self.session.add(message)
        self.session.commit()
        self.session.refresh(message)

        # Send message to Kafka
        kafka_message = message.model_dump_json(exclude={"user"})
        self.producer.send(KAFKA_TOPIC, value=kafka_message)

        # Prepare response
        return MessageResponse(
            id=message.id,
            content=message.content,
            timestamp=message.timestamp,
            user=UserResponse(**user.model_dump()),
        )
