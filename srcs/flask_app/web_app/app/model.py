from sqlalchemy import Column, Integer, String, DateTime

from .db_connect import Base


class Quiz(Base):
    __tablename__ = "quiz_questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_question = Column(Integer, unique=True)
    question = Column(String)
    answer = Column(String)
    date_time = Column(DateTime)

    def __init__(self, id, question, answer, date_time):
        self.id_question = id
        self.question = question
        self.answer = answer
        self.date_time = date_time
