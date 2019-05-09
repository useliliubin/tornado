import tornado.web
import tornado.ioloop
import tornado.options
from tornado.options import define, options
from handlers.main_handler import ExploreHandler, IndexHandler, PostHandler
define('port', default='8000', help='Listening port', type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/explore', ExploreHandler),
            (r'/post/(?P<id>\d+)', PostHandler),#正则的分组捕获
        ]
        settings = dict(
            debug=True,
            template_path='templates',
            static_path='static_file',

        )
        super().__init__(handlers, **settings)


application = Application()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    print('server start on port {}'.format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()





