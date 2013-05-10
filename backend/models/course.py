"""
course.py
This module defines course related models, like Subject and Lesson
"""
from mongoengine import *
from backend.models.users import Teacher


class Lesson(Document):
    """
    This class represents a Lesson in a given Subject.
    """
    name = StringField(required=True)
    subject = ReferenceField("Subject", required=True)


class Subject(Document):
    """
    This module represents a Subject studied in the course.
    """
    name = StringField(required=True)
    teacher = ReferenceField(Teacher, reverse_delete_rule=NULLIFY)  # the teacher that teaches the subject
