import logging

logging = logging.getLogger('cloud.webconsole')


# 用户session 拦截
class MyUserSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logging.info("begin invoke view")
        response = self.get_response(request)
        logging.info("end invoke view")
        return response
