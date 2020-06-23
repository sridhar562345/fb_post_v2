from fb_post_v2.interactors.storages.validators_storage_interface \
	import ValidatorsStorageInterface
from fb_post_v2.interactors.storages.comment_storage_interface import \
	CommentStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
	PresenterInterface
from fb_post_v2.exceptions.exceptions import InvalidPostId

class  CreateCommentInteractor:
	def __init__(
		self,
		validator: ValidatorsStorageInterface,
		storage: CommentStorageInterface,
		presenter: PresenterInterface
	):
		self.validator = validator
		self.storage = storage
		self.presenter = presenter
	
	def create_comment_return_comment_id(
		self,
		user_id: int,
		post_id: int,
		comment_content: str
	):
		if self.validator.is_invalid_post_id(post_id):
			raise self.presenter.raise_invalid_post_id_exception()
		
		new_comment_id = self.storage.create_comment(
			user_id=user_id,
			post_id=post_id,
			comment_content=comment_content
		)
		response = self.presenter.get_create_comment_response(
			comment_id=new_comment_id
		)

		return response

