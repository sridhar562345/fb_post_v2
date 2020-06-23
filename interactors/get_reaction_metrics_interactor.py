from fb_post_v2.interactors.storages.validators_storage_interface \
	import ValidatorsStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface import \
	ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
	PresenterInterface


class GetReactionMetricsInteractor:
	def __init__(
		self,
		validator: ValidatorsStorageInterface,
		storage: ReactionStorageInterface,
		presenter: PresenterInterface
	):
		self.validator = validator
		self.storage = storage
		self.presenter = presenter
	
	def get_post_reaction_metrics_interactor(self, post_id: int):
		if self.validator.is_invalid_post_id(post_id):
			self.presenter.raise_invalid_post_id_exception()

		reaction_metrics = self.storage.get_reaction_metrics(post_id)
		response = self.presenter.get_post_reaction_metrics_response(
			reaction_metrics
		)

		return response
	
	
	