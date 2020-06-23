import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
)


from fb_post_v2.exceptions.exceptions import InvalidPostId
from fb_post_v2.interactors.storages.validators_storage_interface import \
	ValidatorsStorageInterface
from fb_post_v2.interactors.storages.comment_storage_interface import \
	CommentStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import\
	PresenterInterface
from fb_post_v2.interactors.create_comment_interactor import\
	CreateCommentInteractor


def test_create_comment_interactor_given_valid_details():
	#arrange
	user_id = 1
	post_id = 1
	comment_content = "HELLO"
	new_comment_id = 1
	expected_response = {
		"comment_id": new_comment_id
	}
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(CommentStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = CreateCommentInteractor(
		validator=validator,
		storage=storage,
		presenter=presenter
	)
	validator.is_invalid_post_id.return_value = False
	storage.create_comment.return_value = new_comment_id
	presenter.get_create_comment_response.return_value = \
		expected_response
	#act
	response = interactor.create_comment_return_comment_id(
		user_id=user_id,
		post_id=post_id,
		comment_content=comment_content
	)
	
	#assert
	storage.create_comment.assert_called_once_with(
		user_id=user_id,
		post_id=post_id,
		comment_content=comment_content
	)
	presenter.get_create_comment_response.assert_called_once_with(
		comment_id = new_comment_id
	)
	assert response == expected_response
	
	
def test_create_comment_interactor_given_invalid_details_raise_exception():
	#arrange
	user_id = 1
	post_id = 1
	comment_content = "HELLO"
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(CommentStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = CreateCommentInteractor(
		validator=validator,
		storage=storage,
		presenter=presenter
	)
	validator.is_invalid_post_id.return_value = True
	presenter.raise_invalid_post_id_exception.side_effect = NotFound
	
	#act
	with pytest.raises(NotFound):
		interactor.create_comment_return_comment_id(
        	post_id=post_id,  
            comment_content=comment_content,
            user_id=user_id,
        )
	validator.is_invalid_post_id.assert_called_once_with(post_id)
	presenter.raise_invalid_post_id_exception.assert_called_once()
