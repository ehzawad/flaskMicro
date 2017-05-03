import datetime
from peewee import *

VirtualDB = SqliteDatabase('courses.sqlite')

class Course(Model):
    title = CharField()
    url = CharField(unique=True)
    creatingTime = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = VirtualDB

class Review(Model):
    course = ForeignKeyField(Course, related_name='review_set')
    rating = IntegerField()
    creatingTime = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = VirtualDB
