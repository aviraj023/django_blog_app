from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostDetailSeri,PostListSeri,LogsSerializer
from .models import Post
from .models import PostLog
# Create your views here.

class PostsAPIView(APIView):

    def get(self,request):
        posts = Post.objects.all()

        seri = PostDetailSeri(posts,many=True) #Serialize obj->dict

        print("----------------------------------------")
        print("seri (dict) type: "+ str(type(seri)))
        

        return Response(seri.data,status=200)
    
    def post(self,request):

        res=request.data # res is a dict

        seri= PostDetailSeri(data=res) #this is De Serialize dict->obj

        print("----------------------------------------")
        print("seri (obj) type: "+ str(type(seri)))

        if seri.is_valid():
           seri.save()
           return Response(seri.data)
        

        return Response({"msg":"Bad data","Seri Erros":seri.errors,"status":400})


    

class PostDetailAPIView(APIView):

    def get(self,request,pk):
        post = Post.objects.filter(pk=pk).first()


        if not post:
            return Response({"error":"Post NOt Found"},
                            status=404)
        

        seri = PostDetailSeri(post)

        return Response(seri.data)
    
class TestAPIView(APIView):

    def get(self,request,tb):

        if tb=="Post":
            posts = Post.objects.all()

            seriedPosts = PostDetailSeri(posts,many=True)

            return Response(seriedPosts.data)
        
        if(tb=="Logs"):
            logs = PostLog.objects.all()

            seriedLogs = LogsSerializer(logs,many=True)

            return Response(seriedLogs.data)