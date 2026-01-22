from rest_framework import serializers
from .models import Post
from .models import PostLog

class PostListSeri(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id','title','content','author','location']



class PostDetailSeri(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=2000)
    author = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=5)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


    # def create(self,validated_data):
    #     return Post.objects.create(**valiodated_data)
    
class LogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostLog
        fields = ['id','post','created_at']
