from mongoengine import *
from backend.models.course import Lesson, Subject
import backend.configuration as configuration

print "Connecting to database", configuration.DATABASE_NAME
connect(configuration.DATABASE_NAME)

subjects = [
    Subject(name="C"), Subject(name="Networking")
]

print 'Saving subjects'
for subject in subjects:
    subject.save()

lessons = [
    Lesson(name="Expressions", subject=subjects[0]),
    Lesson(name="Structs", subject=subjects[0]),
    Lesson(name="Ethernet", subject=subjects[1]),
    Lesson(name="IP", subject=subjects[1])
]

print 'Saving lessons'
for lesson in lessons:
    lesson.save()

subjects[0].lessons = [lessons[0], lessons[1]]
subjects[1].lessons = [lessons[2], lessons[3]]

print 'Saving subjects again..'
for subject in subjects:
    subject.save()
