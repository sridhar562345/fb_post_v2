from typing import Dict, List
from django_swagger_utils.drf_server.exceptions import NotFound

from fb_post_v2.constants.exception_messages import INVALID_POST_ID
from fb_post_v2.interactors.storages.dtos import (
	PostCompleteDetailsDto,
	PostReactionCompleteDetailsDto,
	UserPostDetailsDto,
	CommentRepliesDto
)
from fb_post_v2.exceptions.exceptions import (
	ReactionDoesNotExist,
	InvalidPostId,
	InvalidCommentId,
	InvalidReactionType
)
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.presenters.presenter_interface import \
	PresenterInterface
from fb_post_v2.models import (
	User,
	Post,
	Reaction,
	Comment
)

class PresenterImplementation(PresenterInterface):
	def raise_invalid_post_id_exception(self):
		raise NotFound(INVALID_POST_ID)
	

	def raise_invalid_comment_id_exception(self):
		raise InvalidCommentId


	def raise_unauthorized_access_exception(self):
		pass
	

	def raise_invalid_reaction_type_exception(self):
		raise InvalidReactionType


	def get_create_post_response(self, post_id: int):
		return_dict = {
			"post_id": post_id
		}
		return return_dict

	def get_create_comment_response(self, comment_id: int):
		return_dict = {
			"comment_id": comment_id
		}
		return return_dict
	

	def get_reply_to_comment_response(self, reply_id: int):
		return_dict = {
			"comment_id": reply_id
		}
		return return_dict
	

	def get_total_reactions_count_response(self, count: int):
		pass
	

	def get_post_reaction_metrics_response(
		self,
		reaction_metrics: Dict[str, int]
	):
		pass
	
	

	def get_posts_with_more_positive_reactions_response(
		self,
		posts_ids: List[int]
	):
		pass
	

	def get_posts_reacted_by_user_response(self, posts_ids: List[int]):
		pass
	

	def get_post_details_response(
		self,
		post_dto: PostCompleteDetailsDto
	):
		pass
	

	def get_post_reactions_response(
		self,
		post_reaction_dto: PostReactionCompleteDetailsDto
	):
		pass
	

	def get_response_for_user_posts(
		self,
		user_posts_dto: UserPostDetailsDto
	):
		pass
	

	def get_comment_replies_response(
		self,
		comment_replies_dto: CommentRepliesDto
	):
		pass
	