# -*- coding: utf-8 -*-
import os
import hashlib

from django.http import HttpResponse


class LoginMiddleware(object):
    def __init__(self, get_response):
        self.tokens = []
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/login":
            if not self.login(request):
                return
            token = self.genToken()
            request.session["token"] = token
            response = HttpResponse()
            response.set_cookie("token", token)
            return response

        if request.path == "/logout":
            self.logout(request)
            return HttpResponse()

        if self.checkToken(request):
            return self.get_response(request)

        return HttpResponse()

    @staticmethod
    def login(request):
        password = request.POST.get("password", "")
        if password == "111":
            return True
        return False

    @staticmethod
    def logout(request):
        request.session["token"] = None
        return True

    @staticmethod
    def checkToken(request):
        token = request.COOKIES.get("token", "")
        return request.session.get("token") == token

    @staticmethod
    def genToken():
        token = hashlib.sha1(os.urandom(24)).hexdigest()
        return token
