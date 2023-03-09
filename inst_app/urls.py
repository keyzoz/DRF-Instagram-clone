from django.urls import path
from inst_app.views import user

urlpatterns = [
    path('user/create/',user.CreateUser.as_view()),
    path('user/login/',user.LoginUser.as_view()),
    path('user/<int:pk>/',user.GetUserByID.as_view()),
    path('user/update/',user.UpdateUser.as_view()),
    path('user/delete/<int:pk>/',user.DeleteUser.as_view())
]
