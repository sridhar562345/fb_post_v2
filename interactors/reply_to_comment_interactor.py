from fb_post_v2.interactors.storages.validators_storage_interface import\
	ValidatorsStorageInterface
from fb_post_v2.interactors.storages.comment_storage_interface import\
	CommentStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import\
	PresenterInterface

class ReplyToComment:
	def __init__(
		self,
		validator: ValidatorsStorageInterface,
		storage: CommentStorageInterface,
		presenter: PresenterInterface
	):
		self.validator = validator
		self.storage = storage
		self.presenter = presenter

	def reply_to_comment_return_comment_id(
		self, user_id,
		comment_id, reply_content
	):
		if self.validator.is_invalid_comment_id(comment_id):
			raise self.presenter.raise_invalid_comment_id_exception()
		if self.validator.is_reply(comment_id):
			parent_id = self.storage.get_reply_parent_id(
				comment_id
			)
		else:
			parent_id = comment_id
		post_id = self.storage.get_post_id(comment_id)
		reply_id = self.storage.reply_to_comment(
			user_id=user_id,
			post_id=post_id,
			parent_id=parent_id,
			reply_content=reply_content
		)
		response = self.presenter.get_reply_to_comment_response(reply_id)

		return response
		
		
		
		
