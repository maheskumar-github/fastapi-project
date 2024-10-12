import os
import sys
from src.exception import CustomException
from src.logger import logging

from fastapi import FastAPI, HTTPEception, Depends
from pydantic import BasModel
from typing import List, Annotated

app = FastAPI()

class ChoiceBase(BasModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BasModel):
    question_text: str
    choices: List[ChoiceBase]


