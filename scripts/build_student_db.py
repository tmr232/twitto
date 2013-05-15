from mongoengine import *
from backend.models.users import Student, Teacher
import backend.configuration as configuration


print "Connecting to database", configuration.DATABASE_NAME
connect(configuration.DATABASE_NAME)

students = [
    Student(first_name="Mike", last_name="Hirsh", year=2013, number=1),
    Student(first_name="Jimmy", last_name="Hertzog", year=2013, number=2),
    Student(first_name="Leo", last_name="Rothshild", year=2013, number=3),
    Student(first_name="Eliot", last_name="Millard", year=2013, number=4),
    Student(first_name="Ben", last_name="Landau", year=2013, number=5),
    Student(first_name="Adam", last_name="Hertz", year=2013, number=6),
]

print 'Saving students'
for student in students:
    student.save()

teachers = [
    Teacher(first_name="Luke", last_name="Skywalker", username="luke", year=2013, password="1234",
            followed_students=[students[0], students[1]]),
    Teacher(first_name="Clark", last_name="Kent", username="superman", year=2013, password="5678",
            followed_students=[students[2], students[4]]),
    Teacher(first_name="Bruce", last_name="Wayne", username="batman", year=2013, password="b@tm@n"),
]

print 'Saving teachers'
for teacher in teachers:
    teacher.save()
