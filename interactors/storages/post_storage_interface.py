from abc import abstractmethod
from typing import Dict, List


from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import (
	PostCompleteDetailsDto,
	PostReactionCompleteDetailsDto,
	UserPostDetailsDto,
	CommentRepliesDto,
)


class PostStorageInterface:
	@abstractmethod
	def create_post(self, user_id: int, post_content: str) -> int:
		pass
	
	@abstractmethod
	def delete_post(self, post_id: int):
		pass
	
	@abstractmethod
	def get_post(self,post_id: int) -> PostCompleteDetailsDto:
		pass
	
	@abstractmethod
	def get_user_posts(self, user_id: int) -> UserPostDetailsDto:
		pass
	