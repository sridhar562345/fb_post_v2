from abc import abstractmethod


from fb_post_v2.constants.enums import ReactionType


class ValidatorsStorageInterface:
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
	