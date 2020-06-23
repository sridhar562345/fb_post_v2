from fb_post_v2.interactors.storages.validators_storage_interface import \
	ValidatorsStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface import \
	ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import PresenterInterface
from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist

class ReactToPostInteractor:
	def __init__(
		self,
		validator: ValidatorsStorageInterface,
		storage: ReactionStorageInterface,
		presenter: PresenterInterface
	):
		self.validator = validator
		self.storage = storage
		self.presenter = presenter
	
	def react_to_post_interactor(
		self, user_id,
		post_id, reaction_type
	):
		if self.validator.is_invalid_post_id(post_id):
			self.presenter.raise_invalid_post_id_exception()
		if self.validator.is_invalid_reaction_type(reaction_type):
			self.presenter.raise_invalid_reaction_type_exception()


		try:
			existing_reaction_type = self.validator.\
				is_user_reaction_to_post_exists_return_reaction_type(
					user_id,
					post_id
				)
		except ReactionDoesNotExist:
			self.storage.create_post_reaction(user_id, post_id, reaction_type)
			return
		

		is_undo_reaction = existing_reaction_type == reaction_type
		
		if is_undo_reaction:
			self.storage.delete_post_reaction(user_id, post_id)
		else:
			self.storage.update_post_reaction(user_id, post_id, reaction_type)
		