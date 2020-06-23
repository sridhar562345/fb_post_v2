import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound


from fb_post_v2.interactors.get_post_reactions_interactor import \
	GetPostReactionsInteractor
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post_v2.interactors.storages.validators_storage_interface import \
    ValidatorsStorageInterface
from fb_post_v2.interactors.storages.dtos import \
	PostReactionCompleteDetailsDto


def test_get_post_reaction_given_invalid_post_id_raises_exception():
	#Arrange
	post_id = 1
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(ReactionStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = GetPostReactionsInteractor(
		validator,
		storage,
		presenter
	)
	validator.is_invalid_post_id.return_value = True
	presenter.raise_invalid_post_id_exception.side_effect = NotFound
	
	
	#act
	with pytest.raises(NotFound):
		interactor.get_post_reactions_interactor(post_id)
	
	#assert
	validator.is_invalid_post_id.assert_called_once_with(post_id)
	presenter.raise_invalid_post_id_exception.assert_called_once()
	
def test_get_post_reaction_given_valid_post_id_returns_post_reactions(
	user_dtos,
	post_reactions_dtos
):
	#Arrange
	post_id = 1
	post_reactions_dtos = PostReactionCompleteDetailsDto(
		user_dtos = user_dtos,
		reaction_dtos = post_reactions_dtos
	)
	expected_response = [
		{
			"user_id": 1,
			"name": "Anusha",
			"profile_pic":"avatar.png",
			"reaction": "LIKE"
		},
		{
			"user_id": 2,
			"name": "Sneha",
			"profile_pic":"avatar.png",
			"reaction": "HAHA"
		},
	]
	validator = create_autospec(ValidatorsStorageInterface)
	storage = create_autospec(ReactionStorageInterface)
	presenter = create_autospec(PresenterInterface)
	interactor = GetPostReactionsInteractor(
		validator,
		storage,
		presenter
	)
	validator.is_invalid_post_id.return_value = False
	storage.get_post_reactions.return_value = post_reactions_dtos
	presenter.get_post_reactions_response.return_value = expected_response
	
	
	#act
	actual_response = interactor.get_post_reactions_interactor(post_id)
	
	#assert
	validator.is_invalid_post_id.assert_called_once_with(post_id)
	storage.get_post_reactions.assert_called_once_with(post_id)
	presenter.get_post_reactions_response.assert_called_once_with(
		post_reactions_dtos
	)
	assert expected_response == actual_response
