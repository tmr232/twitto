"""
Defines handlers for student CRUD.

"""
#TODO: Choose URL patterns for students & student listing. Try and avoid code duplication (autocomplete code)
import tornado.web
from tornado import template
from backend.user_auth import user_required
from backend.models.tweet import Tweet
from backend.models.users import Teacher, Student
import backend.configuration as configuration
from backend.parsers.tweet_parser import get_users


class StudentDisplayHandler(tornado.web.RequestHandler):
    @user_required
    def get(self, year, student_number):
        print year, student_number
        student = Student.objects.get(number=student_number, year=int(year))
        print student
        loader = template.Loader("frontend")
        self.write(
            loader.load("students.html").generate(logo="logo.jpg", title=configuration.SITE_NAME, student=student)
        )