from abc import abstractmethod
from typing import Dict, List


from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import (
	PostCompleteDetailsDto,
	PostReactionCompleteDetailsDto,
	UserPostDetailsDto,
	CommentRepliesDto,
)


class CommentStorageInterface:
	@abstractmethod
	def create_comment(
		self, user_id: int, post_id: int, comment_content: str) -> int:
		pass
	
	@abstractmethod
	def get_reply_parent_id_and_post_id(self, reply_id: int) -> int:
		pass
	
	
	@abstractmethod
	def reply_to_comment(
		self, user_id: int,
		post_id: int,
		parent_id: int, reply_content: str
	) -> int:
		pass
	
	@abstractmethod
	def get_comment_replies(self, comment_id: int) -> CommentRepliesDto:
		pass