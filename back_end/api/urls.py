from django.urls import path, include
from . import views
from rest_framework import routers

#
# router = routers.DefaultRouter()
# router.register(r'account', views.AccountViewSet, basename="allaccount")

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    path('account/', views.getaccounts),
    path('getres/', views.getallres),
    path('login/', views.login),
    path('logout/<str:token>',views.logout),
    path('getorder/',views.MyorderView.as_view()),
    path('getfoods/<int:pk>',views.getfoods),
    path('getmyinfo/<str:pk>',views.getMyinfo),
    path('placeorder/',views.TakeOrderView.as_view()),
    path('setnickname/',views.SetNicknameView.as_view()),
    path('getuser/',views.GetUserView.as_view()),
    path('getresinfo/',views.ResView().as_view()),
    path('getresfood/',views.GetFoodView.as_view()),
    path('updatefood/',views.UpdateFoodView().as_view()),
    path('addfood/',views.AddFoodView().as_view()),
    path('delete/<int:pk>',views.delete),
    path('accessorder/<int:pk>',views.accessorder),
    path('completeorder/<int:pk>',views.completeorder),
    path('deleteorder/<int:pk>',views.deleteorder),
]
