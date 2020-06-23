from unittest.mock import create_autospec


from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post_v2.interactors.get_posts_reacted_by_user_interactor import \
	GetPostsReactedByUser


def test_get_user_reacted_posts_interactor_given_user_id_return_post_ids():
	#arrange
	user_id = 1
	expected_posts_ids = [2,3,4]
	expected_response = {
		"posts_ids": expected_posts_ids
	}
	storage = create_autospec(ReactionStorageInterface)
	presenter = create_autospec(PresenterInterface)
	storage.get_posts_reacted_by_user.return_value = expected_posts_ids
	presenter.get_posts_reacted_by_user_response.return_value = expected_response
	interactor = GetPostsReactedByUser(storage, presenter)
	
	#act
	actual_respoonse = interactor.get_user_reacted_posts(user_id)
	
	#assert
	storage.get_posts_reacted_by_user.assert_called_once_with(user_id)
	presenter.get_posts_reacted_by_user_response.assert_called_once_with(expected_posts_ids)
	assert expected_response == actual_respoonse
	