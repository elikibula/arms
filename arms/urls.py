from django.urls import path, include
from . import views
from .views import ArmListJson




urlpatterns=[

        path('',views.home,name='home'),
        path("login", views.login_request, name="login"),
        path('logout/', views.logoutUser, name="logout"),
        path('arms/', views.arms_list, name='arms_list'),
        path('arm_list_json/', ArmListJson.as_view(), name='arm_list_json')
        


]