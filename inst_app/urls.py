from django.urls import path
from inst_app.views import user, post

urlpatterns = [
    path('user/create/',user.CreateUser.as_view()),
    path('user/login/',user.LoginUser.as_view()),
    path('user/<int:pk>/',user.GetUserByID.as_view()),
    path('user/update/',user.UpdateUser.as_view()),
    path('user/delete/<int:pk>/',user.DeleteUser.as_view()),

    path('posts/', post.GetUserPosts.as_view()),

    path('post/create/', post.CreatePost.as_view()),
    path('post/<int:pk>/',post.GetPostByID.as_view()),
    path('post/update/<int:pk>/',post.UpdatePost.as_view()),
    path('post/delete/<int:pk>/',post.DeletePost.as_view()),
    path('post/like/<int:pk>/',post.LikePost.as_view()),
    path('post/comment/<int:pk>/',post.CommentPost.as_view()),
    path('post/comment/delete/<int:pk>/',post.DeleteComment.as_view()),

    path('post/comments/<int:pk>/', post.GetUserComments.as_view()),


]
