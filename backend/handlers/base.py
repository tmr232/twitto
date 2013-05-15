import tornado.web
from mongoengine.queryset import DoesNotExist
from tornado import template
from backend.user_auth import user_required
from backend.models.users import Teacher
import backend.configuration as configuration


class IndexHandler(tornado.web.RequestHandler):
    """
    The Handler for the index page (/).
    """
    @user_required
    def get(self):
        loader = template.Loader("templates")

        self.write(
            loader.load("index.html").generate(logo="logo.jpg", title="bka", tweets=[], user=self.user))


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        error = self.get_argument("error", None)

        loader = template.Loader("templates")
        self.write(
            loader.load("login.html").generate(logo="logo.jpg", title="bla", tweets=[], error=error))

    def post(self):
        """
        The POST Handler for the login page.
        Checks whether there is a user with the given username and if there is,
        compares the password hashes.
        """
        try:
            user = Teacher.objects.get(
                username=self.get_argument("username"),
            )
            checked_hash = configuration.PASSWORD_HASH_FUNCTION(user["password_salt"] + self.get_argument("password"))
            if user.password != checked_hash:
                self.redirect("/login?error=wrong-username-password")
                return

        except DoesNotExist:
            self.redirect("/login?error=wrong-username-password")
            return

        self.set_secure_cookie("user_id", unicode(user.id))
        self.redirect("/")


# class RegisterHandler(tornado.web.RequestHandler):
#     def get(self):
#         error = self.get_argument("error", None)
#         loader = template.Loader("templates")
#         self.write(
#             loader.load("register.html").generate(logo=SITE_LOGO, title=SITE_TITLE, tweets=Tweet.objects, error=error))
#
#     def post(self):
#         if self.get_argument("admin-password") != ADMIN_PASSWORD:
#             self.redirect("/register?error=wrong-admin-password")
#             return
#
#         if self.get_argument("password") != self.get_argument("confirm"):
#             self.redirect("/register?error=password-not-confirmed")
#             return
#
#         if User.objects.filter(username=self.get_argument("username")).count() > 0:
#             self.redirect("/register?error=user-exists")
#             # if username already exists then delete it. mwahahaha
#             # User.objects.get(username = self.get_argument("username")).delete()
#
#             return
#
#         new_user = User(
#             username=self.get_argument("username"),
#             password=hash_password(self.get_argument("password")),
#             year=int(self.get_argument("year"))
#         )
#
#         new_user.save()
#         self.set_secure_cookie("user_id", unicode(new_user.id))
#         self.redirect("/")


class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("user_id")
        self.redirect("/login")
