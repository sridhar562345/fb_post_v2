from abc import abstractmethod
from typing import Dict, List
from fb_post_v2.interactors.storages.dtos import (
	PostCompleteDetailsDto,
	PostReactionCompleteDetailsDto,
	UserPostDetailsDto,
	CommentRepliesDto
)


class PresenterInterface:
	@abstractmethod
	def raise_invalid_post_id_exception(self):
		pass
	
	@abstractmethod
	def raise_invalid_comment_id_exception(self):
		pass

	@abstractmethod
	def raise_unauthorized_access_exception(self):
		pass
	
	@abstractmethod
	def raise_invalid_reaction_type_exception(self):
		pass

	@abstractmethod
	def get_create_post_response(self, post_id: int):
		pass

	@abstractmethod
	def get_create_comment_response(self, comment_id: int):
		pass
	
	@abstractmethod
	def get_reply_to_comment_response(self, reply_id: int):
		pass
	
	@abstractmethod
	def get_total_reactions_count_response(self, count: int):
		pass
	
	@abstractmethod
	def get_post_reaction_metrics_response(
		self,
		reaction_metrics: Dict[str, int]
	):
		pass
	
	
	@abstractmethod
	def get_posts_with_more_positive_reactions_response(
		self,
		posts_ids: List[int]
	):
		pass
	
	@abstractmethod
	def get_posts_reacted_by_user_response(self, posts_ids: List[int]):
		pass
	
	@abstractmethod
	def get_post_details_response(
		self,
		post_dto: PostCompleteDetailsDto
	):
		pass
	
	@abstractmethod
	def get_post_reactions_response(
		self,
		post_reaction_dto: PostReactionCompleteDetailsDto
	):
		pass
	
	@abstractmethod
	def get_response_for_user_posts(
		self,
		user_posts_dto: UserPostDetailsDto
	):
		pass
	
	@abstractmethod
	def get_comment_replies_response(
		self,
		comment_replies_dto: CommentRepliesDto
	):
		pass