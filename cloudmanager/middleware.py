#!/usr/bin/python
#-*- coding: utf-8 -*-
class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # 调用 view 之前的代码
        print("begin invoke view")
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        # 调用 view 之后的代码
        print("end invoke view")
        return response