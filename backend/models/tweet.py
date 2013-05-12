"""
tweets.py
This module defines all Tweet related models.
author: Arie Bro
"""
import datetime
from mongoengine import *
from backend.models.users import Teacher, Student
from backend.models.course import Lesson


class Tweet(Document):
    """
    Represents a Tweet in the database.
    If the lesson associated with this tweet is deleted, so is this tweet.
    However, if a student is deleted then this Tweet isn't.
    """
    creation_date = DateTimeField(required=True, default=datetime.datetime.now())
    modification_date = DateTimeField(required=True, default=datetime.datetime.now())
    author = ReferenceField(Teacher, required=True)  # The Teacher who last edited the tweet
    # The students mentioned the the tweets content.
    students = ListField(ReferenceField(Student, reverse_delete_rule=PULL))
    lesson = ReferenceField(Lesson, reverse_delete_rule=CASCADE)  # The Lesson this tweet is associated with.
    content = StringField(required=True)  # The Tweets text
    tags = ListField(StringField())  # Tags associated with this Tweet

    meta = {'ordering': '-modification_date'}
