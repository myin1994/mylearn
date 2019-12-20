from django.conf.urls import url
from web.views import customer
from web.views import payment
from web.views import auth

urlpatterns = [

    url(r'^customer/list/$', customer.customer_list,name='customer_list'),
    url(r'^customer/add/$', customer.customer_add,name='customer_add'),
    url(r'^customer/edit/(\d+)/$', customer.customer_edit,name='customer_edit'),
    url(r'^customer/del/(\d+)/$', customer.customer_del,name='customer_del'),

    url(r'^payment/list/$', payment.payment_list,name='payment_list'),
    url(r'^payment/add/$', payment.payment_add,name='payment_add'),
    url(r'^payment/edit/(\d+)/$', payment.payment_edit,name='payment_edit'),
    url(r'^payment/del/(\d+)/$', payment.payment_del,name='payment_del'),

    url(r'^tax/list/$', payment.tax_list,name='tax_list'),
    url(r'^home/$', payment.home,name='home'),
    url(r'^login/$', auth.Login.as_view(),name='login'),
]
