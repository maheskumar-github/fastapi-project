import os
import sys
from src.exception import CustomException
from src.logger import logging

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)

    logging.info("Questions table is create")

class Choices(Base):
    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True, index=True)
    choices_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))

    logging.info("Choices table is create")



