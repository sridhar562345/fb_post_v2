from fb_post_v2.interactors.storages.reaction_storage_interface import \
	ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import\
	PresenterInterface

class GetPostsWithMorePositiveReactionsInteractor:
	def __init__(
		self,
		storage: ReactionStorageInterface,
		presenter: PresenterInterface
	):
		self.storage = storage
		self.presenter = presenter
	
	def get_posts_with_more_positive_reactions_interactor(self):
		posts_ids = self.storage.get_posts_with_more_positive_reactions()
		response = self.presenter.\
			get_posts_with_more_positive_reactions_response(
				posts_ids
			)

		return response
		