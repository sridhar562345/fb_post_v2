from unittest.mock import create_autospec


from fb_post_v2.interactors.\
	get_posts_with_more_postive_reactions_interactor import \
		GetPostsWithMorePositiveReactionsInteractor
from fb_post_v2.interactors.storages.reaction_storage_interface import \
	ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
	PresenterInterface


def test_get_posts_with_more_postive_reactions_returns_posts_ids():
	#Arrange
	expected_post_ids = [2, 3]
	storage = create_autospec(ReactionStorageInterface)
	presenter = create_autospec(PresenterInterface)
	storage.get_posts_with_more_positive_reactions.return_value = \
		expected_post_ids
	presenter.get_posts_with_more_positive_reactions_response.\
		return_value = expected_post_ids
	interactor = GetPostsWithMorePositiveReactionsInteractor(
		storage,
		presenter
	)
	
	#Act
	actual_response = interactor.\
		get_posts_with_more_positive_reactions_interactor()
	
	#Assert
	storage.get_posts_with_more_positive_reactions.assert_called_once()
	presenter.get_posts_with_more_positive_reactions_response.\
		assert_called_once_with(
			expected_post_ids
		)
	assert expected_post_ids == actual_response

