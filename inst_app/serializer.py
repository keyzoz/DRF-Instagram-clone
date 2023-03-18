from rest_framework import serializers
from inst_app.models import User,Post,PostComment

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    about_me = serializers.CharField()
    
    class Meta:
        model = User
        fields = '__all__'
           
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'

    def update(self, instance, validated_data):
        if instance.user.id == validated_data['user'].id:
            return super().update(instance, validated_data)

class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PostComment
        fields = '__all__'

    def save(self, **kwargs):
        super(CommentSerializer, self).save(**kwargs)
        return self.instance
