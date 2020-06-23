from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.comment_storage_interface import \
	CommentStorageInterface
from fb_post_v2.models import (
	User,
	Post,
	Reaction,
	Comment
)
from fb_post_v2.interactors.storages.dtos import CommentRepliesDto


class CommentStorageImplementation(CommentStorageInterface):
	def create_comment(
		self, user_id: int,
		post_id: int, comment_content: str
	) -> int:
		new_comment = Comment.objects.create(
			content=comment_content,
            commented_by_id=user_id,
            post_id=post_id,
		)
		new_comment_id = new_comment.id
		
		return new_comment_id
	
	def reply_to_comment(
		self, user_id: int,
		post_id: int,
		parent_id: int, reply_content: str
	) -> int:
		new_comment = Comment.objects.create(
			content=reply_content,
			commented_by_id=user_id,
			post_id=post_id,
			parent_comment_id=parent_id
		)
		
		new_comment_id = new_comment.id
		
		return new_comment_id
	
	def get_reply_parent_id(self, reply_id: int) -> int:
		comment = Comment.objects.get(id=reply_id)
		parent_id = comment.parent_comment_id
		return parent_id
	
	
	def get_comment_replies(self, comment_id: int) -> CommentRepliesDto:
		pass
	
