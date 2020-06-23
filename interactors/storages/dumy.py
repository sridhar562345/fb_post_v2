from abc import abstractmethod
from typing import Dict, List


from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import (
	PostCompleteDetailsDto,
	PostReactionCompleteDetailsDto,
	UserPostDetailsDto,
	CommentRepliesDto,
)


class StorageInterface:
	@abstractmethod
	def is_invalid_post_id(self, post_id: int) -> bool:
		pass

	@abstractmethod
	def is_invalid_comment_id(self, comment_id: int) -> bool:
		pass

	@abstractmethod
	def is_reply(self, comment_id: int) -> bool:
		pass
	
	@abstractmethod
	def is_user_not_posted_the_post(self, user_id: int, post_id: int):
		pass
	
	@abstractmethod
	def is_invalid_reaction_type(self, reaction_type: ReactionType) -> bool:
		pass
	
	@abstractmethod
	def is_user_reaction_to_post_exists_return_reaction_type(
		self, user_id: int,
		post_id: int
	) -> ReactionType:
		pass
	
	@abstractmethod
	def is_user_reaction_to_comment_exists_return_reaction_type(
		self, user_id: int, 
		comment_id: int
	)-> ReactionType:
		pass
	

	@abstractmethod
	def create_post(self, user_id: int, post_content: str) -> int:
		pass
	
	@abstractmethod
	def create_comment(
		self, user_id: int, post_id: int, comment_content: str) -> int:
		pass
	
	@abstractmethod
	def get_reply_parent_id(self, reply_id: int) -> int:
		pass
	
	@abstractmethod
	def reply_to_comment(
		self, user_id: int,
		parent_id: int, reply_content: str
	) -> int:
		pass
	
	
	@abstractmethod
	def  create_comment_reaction(
		self, user_id: int,
		comment_id: int, reaction_type: ReactionType
	):
		pass
	
	@abstractmethod
	def delete_comment_reaction(self, user_id: int, comment_id: int):
		pass
	
	@abstractmethod
	def update_comment_reaction(
		self, user_id: int,
		comment_id: int, reaction_type: ReactionType
	):
		pass
	
	
	
	@abstractmethod
	def  create_post_reaction(
		self, user_id: int,
		post_id: int, reaction_type: ReactionType
	):
		pass
	
	@abstractmethod
	def delete_post_reaction(self, user_id: int, post_id: int):
		pass
	
	@abstractmethod
	def update_post_reaction(
		self, user_id: int,
		post_id: int, 
		reaction_type: ReactionType
	):
		pass

	@abstractmethod
	def get_total_reactions_count(self):
		pass
	
	@abstractmethod
	def get_reaction_metrics(self, post_id: int) -> Dict[str, int]:
		pass

	@abstractmethod
	def delete_post(self, post_id: int):
		pass
	
	@abstractmethod
	def get_posts_with_more_positive_reactions(self) -> List[int]:
		pass
	
	@abstractmethod
	def get_posts_reacted_by_user(self, user_id: int) -> List[int]:
		pass
	
	@abstractmethod
	def get_post(self,post_id: int) -> PostCompleteDetailsDto:
		pass
	
	@abstractmethod
	def get_post_reactions(
		self,
		post_id: int
	) -> PostReactionCompleteDetailsDto:
		pass
	
	@abstractmethod
	def get_user_posts(self, user_id: int) -> UserPostDetailsDto:
		pass
	
	@abstractmethod
	def get_comment_replies(self, comment_id: int) -> CommentRepliesDto:
		pass