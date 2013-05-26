"""
tweets.py
This module defines all Tweet related models.
author: Arie Bro
"""
import datetime
from mongoengine import *
import mongoengine.signals
from backend.models.users import Teacher, Student
from backend.models.course import Lesson
from backend.parsers.tweet_parser import get_users
from mongoengine.queryset import DoesNotExist


class Tweet(Document):
    """
    Represents a Tweet in the database.
    If the lesson associated with this tweet is deleted, so is this tweet.
    However, if a student is deleted then this Tweet isn't.
    """
<<<<<<< HEAD
    #TODO: datetime.datetime.now() as default argument is prrobably a bug...
    creation_date = DateTimeField(required=True, default=datetime.datetime.now())
    modification_date = DateTimeField(required=True, default=datetime.datetime.now())
=======
    creation_date = DateTimeField(required=True, default=datetime.datetime.utcnow)
    modification_date = DateTimeField(required=True, default=datetime.datetime.utcnow)
>>>>>>> ff15da55a042e527266a57025a769b5e7b967c83
    author = ReferenceField(Teacher, required=True)  # The Teacher who last edited the tweet
    # The students mentioned the the tweets content.
    students = ListField(ReferenceField(Student, reverse_delete_rule=PULL))
    lesson = ReferenceField(Lesson, reverse_delete_rule=CASCADE)  # The Lesson this tweet is associated with.
    content = StringField(required=True)  # The Tweets text
    tags = ListField(StringField())  # Tags associated with this Tweet

    meta = {'ordering': '-modification_date'}

<<<<<<< HEAD
    def __init__(self, **values):
        super(Tweet, self).__init__(***values)

        self.creation_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()

        for student_number in get_users(self.content):
            try:
                student = Student.object.get(number=student_number)
            except DoesNotExist:
                continue
            self.students.append(student)
=======
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        """
        This method updates the modification time of the model upon saving it
        to the database.
        This method responds to the save signal sent.
        """
        document["modification_date"] = datetime.datetime.utcnow()


mongoengine.signals.pre_save.connect(Tweet.pre_save, sender=Tweet)
>>>>>>> ff15da55a042e527266a57025a769b5e7b967c83
