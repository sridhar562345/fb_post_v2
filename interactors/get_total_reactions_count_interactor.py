from fb_post_v2.interactors.storages.reaction_storage_interface import \
	ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import\
	PresenterInterface


class GetTotalReactionsCountInteractor:
	def __init__(
		self,
		storage: ReactionStorageInterface,
		presenter: PresenterInterface
	):
		self.storage = storage
		self.presenter = presenter
	
	def get_total_reactions_count_interactor(self):
		total_reactions_count = self.storage.get_total_reactions_count()
		response = self.presenter.get_total_reactions_count_response(
			total_reactions_count
		)
		
		return response
		
	