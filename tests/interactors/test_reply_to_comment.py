import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec


from fb_post_v2.interactors.reply_to_comment_interactor import \
	ReplyToComment
from fb_post_v2.interactors.storages.comment_storage_interface import \
	CommentStorageInterface
from fb_post_v2.interactors.storages.validators_storage_interface import \
	ValidatorsStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
	PresenterInterface


def test_reply_to_comment_given_invalid_data_raise_exception():
	user_id = 1
	comment_id = 1
	comment_content = "invalid comment"
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(CommentStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = ReplyToComment(validator, storage, presenter)
	validator.is_invalid_comment_id.return_value = True
	presenter.raise_invalid_comment_id_exception.side_effect = NotFound
	
	with pytest.raises(NotFound):
		interactor.reply_to_comment_return_comment_id(
			user_id=user_id,
			comment_id=comment_id,
			reply_content = comment_content
		)
	
	validator.is_invalid_comment_id.assert_called_once_with(comment_id)
	presenter.raise_invalid_comment_id_exception.assert_called_once()
	
def test_reply_to_reply_given_valid_data_returns_reply_to_reply_id():
	#arrange
	user_id = 1
	parent_id = 1
	comment_id = 2
	reply_to_reply_id = 3
	comment_content = "reply to reply"
	expected_response = {
		"comment_id": reply_to_reply_id
	}
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(CommentStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = ReplyToComment(validator, storage, presenter)
	validator.is_invalid_comment_id.return_value = False
	validator.is_reply.return_value = True
	storage.get_reply_parent_id.return_value = parent_id
	storage.reply_to_comment.return_value = reply_to_reply_id
	presenter.get_reply_to_comment_response.return_value = \
		expected_response
	
	#act
	actual_response = interactor.reply_to_comment_return_comment_id(
		user_id=user_id,
		comment_id=comment_id,
		reply_content = comment_content
	)
	
	#assert
	validator.is_invalid_comment_id.assert_called_once_with(comment_id)
	validator.is_reply.assert_called_once_with(comment_id)
	storage.get_reply_parent_id.assert_called_once_with(comment_id)
	storage.reply_to_comment.assert_called_once_with(
		user_id,
		parent_id,
		comment_content
	)
	assert actual_response == expected_response
	
def test_reply_to_comment_given_valid_data_returns_reply_id():
	#arrange
	user_id = 1
	comment_id = 1
	reply_id = 2
	comment_content = "reply comment"
	expected_response = {
		"comment_id": reply_id
	}
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(CommentStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = ReplyToComment(validator, storage, presenter)
	validator.is_invalid_comment_id.return_value = False
	validator.is_reply.return_value = False
	storage.reply_to_comment.return_value = reply_id
	presenter.get_reply_to_comment_response.return_value = \
		expected_response
	
	#act
	actual_response = interactor.reply_to_comment_return_comment_id(
		user_id=user_id,
		comment_id=comment_id,
		reply_content = comment_content
	)
	
	#assert
	validator.is_invalid_comment_id.assert_called_once_with(comment_id)
	validator.is_reply.assert_called_once_with(comment_id)
	storage.reply_to_comment.assert_called_once_with(
		user_id,
		comment_id,
		comment_content
	)
	assert actual_response == expected_response