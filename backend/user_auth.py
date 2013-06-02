import functools
from mongoengine.errors import DoesNotExist
from backend.models.users import Teacher


def user_required(method):
    """Decorator for getting the user through a secure cookie user identifier
    :param method: the method we want to protect against unauthorized access.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        user_id = self.get_secure_cookie("user_id")

        if user_id:
            try:
                self.user = Teacher.objects.get(id=user_id)
            except DoesNotExist:
                # If the user_id does not exist, we want to redirect to the login page as well.
                #TODO: remove code duplication.
                self.redirect("/login")
                return
        else:
            self.redirect("/login")
            return

        method(self, *args, **kwargs)

    return wrapper
