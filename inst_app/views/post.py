from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ObjectDoesNotExist, PermissionDenied

from inst_app.serializer import PostSerializer
from inst_app.models import Post, PostLike


class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

class GetPostByID(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UpdatePost(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = self.serializer_class(post, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save(user=request.user)
                return Response({'message': 'Post has been updated'})
            except ObjectDoesNotExist:
                return Response({'exception': 'Post does not exist'})

class DeletePost(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            if request.user.id == post.user.id:
                post.delete()
                return Response({'message': 'Post has been deleted'})
            else:
                return Response({'exception': 'You\'re haven\'nt permissons'})
        except ObjectDoesNotExist:
            return Response({'exception': 'Post does not exist'})

class GetUserPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

    def list(self, request,  *args, **kwargs):
        posts = Post.objects.filter(user = request.user.id)
        serializer = self.serializer_class(posts, many=True)
        return Response({'posts': serializer.data })

class LikePost(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            likedPost = PostLike.objects.get_or_create(user=request.user, post=post)
            if not likedPost[1]:
                likedPost[0].delete()
                return Response({'message': 'Post has been unliked'})
            else:
                return Response({'message': 'Like has been liked'})
        except ObjectDoesNotExist:
                return Response({'exception': 'Post does not exist'})


