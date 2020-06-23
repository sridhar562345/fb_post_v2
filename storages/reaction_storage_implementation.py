from typing import Dict, List

from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.reaction_storage_interface import \
	ReactionStorageInterface
from fb_post_v2.models import (
	User,
	Post,
	Reaction,
	Comment
)
from fb_post_v2.interactors.storages.dtos import (
	PostCompleteDetailsDto,
	PostReactionCompleteDetailsDto,
	UserPostDetailsDto,
	CommentRepliesDto,
)



class ReactionStorageImplementation(ReactionStorageInterface):
	
	def  create_comment_reaction(
		self, user_id: int,
		comment_id: int, reaction_type: ReactionType
	):
		Reaction.objects.create(
			reacted_by_id=user_id,
			comment_id=comment_id,
			reaction=reaction_type
		)
	
	def delete_comment_reaction(self, user_id: int, comment_id: int):
		Reaction.objects.get(
			reacted_by_id=user_id,
			comment_id=comment_id
		).delete()
	

	def update_comment_reaction(
		self, user_id: int,
		comment_id: int, reaction_type: ReactionType
	):
		reaction_obj = Reaction.objects.get(
			reacted_by_id=user_id,
			comment_id=comment_id,
		)
		reaction_obj.reaction = reaction_type
		reaction_obj.save()


	def create_post_reaction(
		self, user_id: int,
		post_id: int, reaction_type: ReactionType
	):
		Reaction.objects.create(
			post_id = post_id,
            reaction = reaction_type,
            reacted_by_id = user_id
		)
	

	def delete_post_reaction(self, user_id: int, post_id: int):
		Reaction.objects.get(post_id=post_id, reacted_by_id=user_id).\
			delete()
	

	def update_post_reaction(
		self, user_id: int,
		post_id: int, 
		reaction_type: ReactionType
	):
		reaction_obj = Reaction.objects.get(
			post_id=post_id,
			reacted_by_id=user_id
		)
		reaction_obj.reaction = reaction_type
		reaction_obj.save()


	def get_total_reactions_count(self):
		pass
	
	def get_reaction_metrics(self, post_id: int) -> Dict[str, int]:
		pass


	def get_posts_with_more_positive_reactions(self) -> List[int]:
		pass
	

	def get_posts_reacted_by_user(self, user_id: int) -> List[int]:
		pass
	
	
	def get_post_reactions(
		self,
		post_id: int
	) -> PostReactionCompleteDetailsDto:
		pass
	