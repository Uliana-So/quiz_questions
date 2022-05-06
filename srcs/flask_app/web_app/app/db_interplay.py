import logging
from sqlalchemy.sql import exists

from .db_connect import db_session
from .model import Quiz
from .send_request import send_request


def last_question():
    return db_session.query(Quiz).order_by(Quiz.id.desc()).first()


def check_id(id) -> bool:
    return db_session.query(exists().where(Quiz.id_question == id)).scalar()


def add_data(**data):
    while check_id(data["id"]):
        data = send_request(1)[0]

    new_row = Quiz(data["id"],data["question"],
                   data["answer"],data["created_at"])

    logging.info(data)
    db_session.add(new_row)
    db_session.commit()
