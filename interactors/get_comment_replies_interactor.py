from fb_post_v2.interactors.storages.validators_storage_interface \
	import ValidatorsStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.comment_storage_interface import \
    CommentStorageInterface

class GetCommentReplies:
	def __init__(
		self,
		validator: ValidatorsStorageInterface,
		storage: CommentStorageInterface,
		presenter: PresenterInterface
	):
		self.validator = validator
		self.storage = storage
		self.presenter = presenter
	
	def get_comment_replies_interactor(self, comment_id):
		if self.validator.is_invalid_comment_id(comment_id):
			self.presenter.raise_invalid_comment_id_exception()
		comment_replies_dto = self.storage.get_comment_replies(comment_id)
		comment_replies_dict = self.presenter.get_comment_replies_response(
			comment_replies_dto
		)
		return comment_replies_dict