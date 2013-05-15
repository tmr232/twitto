import tornado.web
import tornado.ioloop
from tornado.options import define, options
from backend import configuration
from backend.handlers.RESTFactory import RESTHandlerFactory
from backend.models.users import Student
import mongoengine

define("port", default=configuration.APP_PORT, help="The port to listen on")

# connect to mongodb (for mongoengine)
mongoengine.connect(configuration.DATABASE_NAME)


class TwittoApp(tornado.web.Application):
    """
    This is the Twitto Application.
    """
    def __init__(self):
        """
        The constructor for the main Twitto Application
        """
        rest_factory = RESTHandlerFactory()

        handlers = [
            (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': "css"}),
            (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': "js"}),
            (r'/img/(.*)', tornado.web.StaticFileHandler, {'path': "img"}),

            (r'/students', rest_factory.get_model_rest_handler(Student)),
            ]

        settings = {"cookie_secret" : configuration.COOKIE_SECRET}
        super(TwittoApp, self).__init__(handlers, **settings)

if __name__ == "__main__":

    application = TwittoApp()
        # static directories

    options.parse_command_line()
    print 'Listening on port %s' % options.port
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
