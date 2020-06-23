from fb_post_v2.interactors.storages.validators_storage_interface \
	import ValidatorsStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.reaction_storage_interface import \
    ReactionStorageInterface


class GetPostReactionsInteractor:
	def __init__(
		self,
		validator: ValidatorsStorageInterface,
		storage: ReactionStorageInterface,
		presenter: PresenterInterface
	):
		self.validator = validator
		self.storage = storage
		self.presenter = presenter
	
	def get_post_reactions_interactor(self, post_id):
		if self.validator.is_invalid_post_id(post_id):
			self.presenter.raise_invalid_post_id_exception()

		post_reaction_dtos = self.storage.get_post_reactions(post_id)
		post_reaction_dict = self.presenter.get_post_reactions_response(
			post_reaction_dtos
		)

		return post_reaction_dict

