from fb_post_v2.interactors.storages.validators_storage_interface import \
	ValidatorsStorageInterface
from fb_post_v2.interactors.storages.post_storage_interface import \
	PostStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
	PresenterInterface


class DeletePostInteractor:
	def __init__(
		self,
		validator: ValidatorsStorageInterface,
		storage: PostStorageInterface,
		presenter: PresenterInterface
	):
		self.validator = validator
		self.storage = storage
		self.presenter = presenter
	
	def delete_post_interactor(self, user_id, post_id):
		if self.validator.is_invalid_post_id(post_id):
			self.presenter.raise_invalid_post_id_exception()
		if self.validator.is_user_not_posted_the_post(user_id, post_id):
			self.presenter.raise_unauthorized_access_exception()
		self.storage.delete_post(post_id)
		