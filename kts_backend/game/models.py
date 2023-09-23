from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from sqlalchemy import Column, String, BigInteger, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from kts_backend.base.models import GameScore
from kts_backend.store.database.sqlalchemy_base import db


@dataclass
class QuestionAnswer:
    id: int
    question_text: str
    answer_text: str


@dataclass
class Game:
    id: int
    created_at: datetime
    chat_id: int
    question: QuestionAnswer
    status: bool = True
    players: List[GameScore] = field(default_factory=list)


class GameModel(db):
    __tablename__ = "games"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    chat_id = Column(BigInteger)
    status = Column(Boolean, default=True)
    question_id = Column(BigInteger, ForeignKey('questions.id'))
    question = relationship("QuestionAnswerModel", back_populates="games")
    players = relationship("UserModel", secondary="game_user", back_populates="games")


class QuestionAnswerModel(db):
    __tablename__ = 'questions'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    question_text = Column(String)
    answer_text = Column(String)
    games = relationship("GameModel", back_populates="question")