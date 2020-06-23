import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import(
	NotFound,
	Forbidden
)

from fb_post_v2.interactors.storages.validators_storage_interface import \
	ValidatorsStorageInterface
from fb_post_v2.interactors.storages.post_storage_interface import \
	PostStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
	PresenterInterface
from fb_post_v2.interactors.delete_post_interactor import \
	DeletePostInteractor


def test_delete_post_given_invalid_post_id_raises_exception():
	#arrange
	user_id = 1
	post_id = 1
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(PostStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = DeletePostInteractor(validator, storage, presenter)
	validator.is_invalid_post_id.return_value = True
	presenter.raise_invalid_post_id_exception.side_effect = NotFound
	
	
	#act
	with pytest.raises(NotFound):
		interactor.delete_post_interactor(user_id, post_id)
	
	#assert
	validator.is_invalid_post_id.assert_called_once_with(post_id)
	presenter.raise_invalid_post_id_exception.assert_called_once()


def test_delete_post_given_unauthorized_user_raises_exception():
	#arrange
	user_id = 1
	post_id = 1
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(PostStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = DeletePostInteractor(validator, storage, presenter)
	validator.is_invalid_post_id.return_value = False
	validator.is_user_not_posted_the_post.return_value = True
	presenter.raise_unauthorized_access_exception.side_effect = \
		Forbidden
	
	#act
	with pytest.raises(Forbidden):
		interactor.delete_post_interactor(user_id, post_id)
	
	#assert
	validator.is_invalid_post_id.assert_called_once_with(post_id)
	validator.is_user_not_posted_the_post.assert_called_once_with(
		user_id,
		post_id
	)
	presenter.raise_unauthorized_access_exception.assert_called_once()


def test_delete_post_given_valid_details_post_deleted():
	#arrange
	user_id = 1
	post_id = 1
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(PostStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = DeletePostInteractor(validator, storage, presenter)
	validator.is_invalid_post_id.return_value = False
	validator.is_user_not_posted_the_post.return_value = False
	
	#act
	interactor.delete_post_interactor(user_id, post_id)
	
	#assert
	validator.is_invalid_post_id.assert_called_once_with(post_id)
	validator.is_user_not_posted_the_post.assert_called_once_with(
		user_id,
		post_id
	)
	storage.delete_post.assert_called_once_with(post_id)
	
