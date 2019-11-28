from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse


class MD2(MiddlewareMixin):
    def process_request(self, request):
        print("MD2里面的 process_request")
        pass

    def process_response(self, request, response):
        print("MD2里面的 process_response")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("-" * 80)
        print("MD2 中的process_view")
        print(view_func, view_func.__name__)

    def process_exception(self, request, exception):
        print(exception)
        print("MD2 中的process_exception")

    def process_template_response(self, request, response):
        print("MD2 中的process_template_response")
        return response