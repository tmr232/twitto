from mongoengine import *
from backend import configuration
import os


class Student(Document):
    """
    Represents a Student in the Course.
    """
    first_name = StringField(max_length=40, required=True)
    last_name = StringField(max_length=40, required=True)
    id_number = StringField()  # The Student's Identification Number
    number = IntField(required=True)  # An Inner numbering scheme for the student
    year = IntField(required=True)
    domain_username = StringField()  # The Student's username in Microsoft Windows Domain
    picture_path = StringField()  # The path to the student's picture in the server


class Teacher(Document):
    """
    Represents a Teacher in the Course.
    """
    first_name = StringField(max_length=40, required=True)
    last_name = StringField(max_length=40, required=True)
    username = StringField(max_length=20, required=True)
    password = StringField(required=True)
    password_salt = BinaryField()
    year = IntField(required=True)
    email = EmailField()
    # The students this teacher wants to hear about. we delete references automatically when students are deleted.
    followed_students = ListField(ReferenceField("Student", reverse_delete_rule=PULL))

    def __init__(self, **values):
        """
        This function initializes the Teacher instance and generates a new salt for the teacher.
        :param values: passed to the Document class __init__.
        """
        super(Teacher, self).__init__(**values)

        if not self.password_salt and self.password:  # we only generate a new salt if its not set
            self.password_salt = os.urandom(configuration.PASSWORD_SALT_LENGTH)
            self.password = configuration.PASSWORD_HASH_FUNCTION(self.password + self.password_salt).hexdigest()


class Group(Document):
    """
    Represents a Group of students.
    """
    name = StringField(max_length=50, required=True)
    description = StringField(max_length=50, required=True)
    students = ListField(ReferenceField("Student", reverse_delete_rule=PULL))
