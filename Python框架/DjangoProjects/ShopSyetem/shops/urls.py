from django.conf.urls import url
from shops.views import *
urlpatterns = [
    url(r'^login/', Login.as_view(),name="login"),
    url(r'^logout/', Logout.as_view(),name="logout"),
    url(r'^signup/', SignUp.as_view(),name="signup"),
    url(r'^goods/', Goods.as_view(),name="goods"),
    url(r'^usergoods/', UserGoods.as_view(),name="usergoods"),
    url(r'^shopcar/', ShopCar.as_view(),name="shopcar"),
    url(r'^orderlist/', OrderList.as_view(),name="orderlist"),
    url(r'^orderdetails/', OrderDetails.as_view(),name="orderdetails"),

]