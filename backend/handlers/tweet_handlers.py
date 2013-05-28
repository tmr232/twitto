import tornado.web
from tornado import template
from backend.user_auth import user_required
from backend.models.tweet import Tweet
from backend.models.users import Teacher, Student
import backend.configuration as configuration
from backend.parsers.tweet_parser import get_users


class TweetPostHandler(tornado.web.RequestHandler):
    @user_required
    def post(self, *args, **kwargs):
        user_id = self.get_secure_cookie("user_id")
        user = Teacher.objects.get(id=user_id)

        new_tweet = Tweet(
            content=self.get_argument("content"),
            author=user
        )

        mentioned_user_numbers = get_users(self.get_argument("content"))
        for user_number in mentioned_user_numbers:
            mentioned_user = Student.objects.get(number=user_number)
            new_tweet.students.append(mentioned_user)

        new_tweet.save()

    @user_required
    def get(self):
        error = self.get_argument("error", None)

        loader = template.Loader("frontend")
        self.write(
            loader.load("tweet.html").generate(logo="logo.jpg", title=configuration.SITE_NAME, error=error))