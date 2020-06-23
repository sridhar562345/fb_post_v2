import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound


from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.comment_storage_interface import \
    CommentStorageInterface
from fb_post_v2.interactors.storages.validators_storage_interface import \
    ValidatorsStorageInterface
from fb_post_v2.interactors.get_comment_replies_interactor import \
	GetCommentReplies
from fb_post_v2.interactors.storages.dtos import \
	CommentRepliesDto


def test_comment_replies_given_invalid_comment_id_raises_exception():
	#Arrange
	comment_id = 1
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(CommentStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = GetCommentReplies(validator,storage, presenter)
	validator.is_invalid_comment_id.return_value = True
	presenter.raise_invalid_comment_id_exception.side_effect = NotFound
	
	
	#act
	with pytest.raises(NotFound):
		interactor.get_comment_replies_interactor(comment_id)
	
	#assert
	validator.is_invalid_comment_id.assert_called_once_with(comment_id)
	presenter.raise_invalid_comment_id_exception.assert_called_once()


def test_comment_replies_given_valid_comment_id_returns_comment_replies(
		user_dtos,
		reply_dtos,
		get_comment_replies_response
	):
	#Arrange
	comment_id = 1
	comment_replies_dto = CommentRepliesDto(
		users_dto = user_dtos,
		comments_dto = reply_dtos
	)
	expected_comment_replies = get_comment_replies_response
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(CommentStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = GetCommentReplies(validator,storage, presenter)
	validator.is_invalid_comment_id.return_value = False
	storage.get_comment_replies.return_value = comment_replies_dto
	presenter.get_comment_replies_response.return_value = \
		expected_comment_replies
	
	#act
	actual_comment_replies = interactor.get_comment_replies_interactor(
		comment_id
	)

	#assert
	validator.is_invalid_comment_id.assert_called_once_with(comment_id)
	storage.get_comment_replies.assert_called_once_with(comment_id)
	presenter.get_comment_replies_response.assert_called_once_with(
		comment_replies_dto
	)

	assert expected_comment_replies == actual_comment_replies


