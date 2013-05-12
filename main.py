import tornado.web
import tornado.ioloop
from tornado.options import define, options
from backend import configuration
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
        handlers = [
            (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': "css"}),
            (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': "js"}),
            (r'/img/(.*)', tornado.web.StaticFileHandler, {'path': "img"}),

            (r'/', IndexHandler),
            ]

        super(TwittoApp, self).__init__(handlers)

if __name__ == "__main__":

    application = TwittoApp()
        # static directories

    options.parse_command_line()
    print 'Listening on port %s' % options.port
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
