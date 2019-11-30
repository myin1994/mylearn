from django.http import QueryDict
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse

class HttpPost2HttpOtherMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        可以继续添加HEAD、PATCH、OPTIONS以及自定义方法
        HTTP_X_METHODOVERRIDE貌似是以前版本的key？？？
        :param request: 经过原生中间件处理过后的请求
        :return:
        """
        try:
            http_method = request.META['REQUEST_METHOD']
            if http_method.upper() not in ('GET', 'POST'):
                setattr(request, http_method.upper(), QueryDict(request.body))
        # except KeyError:
        #     http_method = request.META['HTTP_X_METHODOVERRIDE']
        #     if http_method.upper() not in ('GET', 'POST'):
        #         setattr(request, http_method.upper(), QueryDict(request.body))
        except Exception:
            pass
        finally:
            return None