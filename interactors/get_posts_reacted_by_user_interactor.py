from fb_post_v2.interactors.storages.reaction_storage_interface import \
	ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
	PresenterInterface

class GetPostsReactedByUser:
	def __init__(
		self,
		storage: ReactionStorageInterface,
		presenter: PresenterInterface
	):
		self.storage = storage
		self.presenter = presenter
	
	def get_user_reacted_posts(self, user_id):
		posts_ids = self.storage.get_posts_reacted_by_user(user_id)
		response = self.presenter.get_posts_reacted_by_user_response(
			posts_ids
		)

		return response