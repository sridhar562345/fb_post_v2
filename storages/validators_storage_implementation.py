from django.core.exceptions import ObjectDoesNotExist

from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.validators_storage_interface import \
	ValidatorsStorageInterface
from fb_post_v2.models import (
	User,
	Post,
	Reaction,
	Comment
)

class ValidatorsStorageImplementation(ValidatorsStorageInterface):
	def is_invalid_post_id(self, post_id: int) -> bool:
		try:
			Post.objects.get(id=post_id)
		except ObjectDoesNotExist:
			return True
		return False
	
	def is_invalid_comment_id(self, comment_id: int) -> bool:
		try:
			Comment.objects.get(id=comment_id)
		except ObjectDoesNotExist:
			return True
		return False
	
	def is_reply(self, comment_id: int) -> bool:
		comment_obj = Comment.objects.get(id=comment_id)
		is_reply = comment_obj.parent_comment_id
		if is_reply:
			return True
		return False
	
	def is_user_not_posted_the_post(self, user_id: int, post_id: int):
		post_obj = Post.objects.get(id=post_id)
		user_posted_the_post = post_obj.posted_by_id == user_id
		if user_posted_the_post:
			return False
		return True

	def is_invalid_reaction_type(self, reaction_type: ReactionType):
		reactions = [reaction.value for reaction in ReactionType]
		invalid_reaction_type = reaction_type in reactions
		if invalid_reaction_type:
			return False
		return True
	
	def is_user_reaction_to_post_exists_return_reaction_type(
		self, user_id: int,
		post_id: int
	) -> ReactionType:
		try:
			reaction_obj = Reaction.objects.get(
				post_id=post_id,
				reacted_by_id=user_id
			)
		except ObjectDoesNotExist:
			raise ReactionDoesNotExist
		
		reaction_type = reaction_obj.reaction
		
		return reaction_type
	
	def is_user_reaction_to_comment_exists_return_reaction_type(
		self, user_id: int,
		comment_id: int
	) -> ReactionType:
		try:
			reaction_obj = Reaction.objects.get(
				comment_id=comment_id,
				reacted_by_id=user_id
			)
		except ObjectDoesNotExist:
			raise ReactionDoesNotExist
		
		reaction_type = reaction_obj.reaction
		
		return reaction_type
	