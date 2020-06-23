from django.db import models
from .post import Post
from .comment import Comment
from .user import User


class Reaction(models.Model) :
	react_choices = (
		("WOW","WOW"),
		("LIT","LIT"),
		("LOVE","LOVE"),
		("HAHA","HAHA"),
		("THUMBS-UP","THUMBS-UP"),
		("THUMBS-DOWN","THUMBS-DOWN"),
		("ANGRY","ANGRY"),
		("SAD","SAD")
		)
	post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True, blank = True,related_name = "post_reactions")
	comment = models.ForeignKey(Comment, on_delete = models.CASCADE, null = True, blank = True, related_name = "comment_reactions")
	
	reaction = models.CharField(max_length = 100, choices = react_choices)
	reacted_at = models.DateTimeField(auto_now = True,null=True)
	reacted_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_reactions")
	
	def __str__(self) :
		return self.reaction
