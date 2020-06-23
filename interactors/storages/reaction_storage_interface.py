from abc import abstractmethod
from typing import Dict, List


from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.dtos import (
	PostCompleteDetailsDto,
	PostReactionCompleteDetailsDto,
	UserPostDetailsDto,
	CommentRepliesDto,
)


class ReactionStorageInterface:
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
	def get_posts_with_more_positive_reactions(self) -> List[int]:
		pass
	
	@abstractmethod
	def get_posts_reacted_by_user(self, user_id: int) -> List[int]:
		pass
	
	@abstractmethod
	def get_post_reactions(
		self,
		post_id: int
	) -> PostReactionCompleteDetailsDto:
		pass
	
	