import tornado.web
from mongoengine.queryset import DoesNotExist
from tornado import template
from backend.user_auth import user_required
from backend.models.tweet import Tweet
import datetime
from backend.models.users import Teacher
import backend.configuration as configuration


class PostHandler(tornado.web.RequestHandler):
    @user_required
    def post(self, *args, **kwargs):
        user_id = self.get_secure_cookie("user_id")
        user = Teacher.objects.get(id=user_id)

        new_tweet = Tweet(
            content=self.get_argument("content"),
            author=user
        )

        new_tweet.save()

        self.redirect(r'/tweet')

    @user_required
    def get(self):
        error = self.get_argument("error", None)

        loader = template.Loader("frontend")
        self.write(
            loader.load("tweet.html").generate(logo="logo.jpg", title=configuration.SITE_NAME, error=error))