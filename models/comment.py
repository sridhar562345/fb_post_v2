from django.db import models
from .user import User
from .post import Post

class Comment(models.Model) :
	content = models.CharField(max_length = 1000)
	commented_at = models.DateTimeField(auto_now = True,null=True)
	commented_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_comments")
	post = models.ForeignKey(Post, on_delete = models.CASCADE,related_name = "post_comments")
	parent_comment = models.ForeignKey('self',null = True, on_delete = models.CASCADE,blank = True, related_name = "replies")
	
	def __str__(self) :
		return self.content
