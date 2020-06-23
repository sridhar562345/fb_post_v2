from unittest.mock import create_autospec


from fb_post_v2.interactors.storages.post_storage_interface import\
	PostStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import\
	PresenterInterface
from fb_post_v2.interactors.create_post_interactor import\
	CreatePostInteractor


def test_create_post_interactor():
	#arrrange
	new_post_id = 1
	user_id = 1
	post_content = "hello"
	expected_response_dict = {
		"post_id": 1
	}
	storage = create_autospec(PostStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = CreatePostInteractor(
		storage,
		presenter,
	)
	storage.create_post.return_value = new_post_id
	presenter.get_create_post_response.return_value = \
		expected_response_dict
	
	#act
	response = interactor.create_post_return_post_id(
		user_id=user_id,
		post_content=post_content,
	)
	
	#assert
	storage.create_post.assert_called_once_with(
		user_id=user_id,
		post_content=post_content
	)
	presenter.get_create_post_response.assert_called_once_with(
		post_id=new_post_id
	)
	assert response == expected_response_dict
	