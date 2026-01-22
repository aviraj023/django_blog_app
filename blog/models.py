from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    location=models.CharField(max_length=50)

    # when an object of this class is printed it is represented by title e.g print(obj)
    def __str__(self):
        return self.title
    


class PostLog(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Log for Post {self.post.id}"
    
