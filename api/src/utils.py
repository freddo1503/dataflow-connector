from sqlmodel import create_engine, Session
from kafka import KafkaProducer
from src.config import DATABASE_URL, KAFKA_BROKER_URL

# Database setup
engine = create_engine(DATABASE_URL, echo=True)


def get_db_session():
    with Session(engine) as session:
        yield session


# Kafka producer setup
def get_kafka_producer() -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda v: v.encode("utf-8"),
    )
