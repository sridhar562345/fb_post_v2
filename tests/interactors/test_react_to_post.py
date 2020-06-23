import pytest
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)
from unittest.mock import create_autospec


from fb_post_v2.interactors.react_to_post_interactor import \
    ReactToPostInteractor
from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.validators_storage_interface import \
    ValidatorsStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface import \
    ReactionStorageInterface
    

def test_react_to_post_given_invalid_post_id_raises_exception():
    #Arrange
    post_id = 1
    user_id = 1
    reaction_type = "HAHA"
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToPostInteractor(
        validator,
        storage,
        presenter
    )
    validator.is_invalid_post_id.return_value = True
    presenter.raise_invalid_post_id_exception.side_effect = \
        NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.react_to_post_interactor(
            post_id=post_id,
            user_id=user_id,
            reaction_type=reaction_type,
        )
    
    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    presenter.raise_invalid_post_id_exception.assert_called_once()

def test_react_to_comment_given_invalid_reaction_type_raises_exception():
    #arrange
    post_id = 1
    user_id = 1
    reaction_type = "COOL"
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToPostInteractor(
        validator,
        storage,
        presenter
    )
    validator.is_invalid_post_id.return_value = False
    validator.is_invalid_reaction_type.return_value = True
    presenter.raise_invalid_reaction_type_exception.\
        side_effect = BadRequest
    

    #act
    with pytest.raises(BadRequest):
        interactor.react_to_post_interactor(
            post_id=post_id,
            user_id=user_id,
            reaction_type=reaction_type,
        )
    
    #assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    validator.is_invalid_reaction_type.assert_called_once_with(
        reaction_type=reaction_type
    )
    presenter.raise_invalid_reaction_type_exception.\
        assert_called_once()


def test_react_to_post_given_valid_details_new_reaction_created():
    #Arrange
    post_id = 1
    user_id = 1
    reaction_type = ReactionType.WOW.value
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToPostInteractor(
        validator,
        storage,
        presenter
    )
    validator.is_invalid_post_id.return_value = False
    validator.is_invalid_reaction_type.return_value = False
    validator.is_user_reaction_to_post_exists_return_reaction_type. \
        side_effect = ReactionDoesNotExist

    #Act
    interactor.react_to_post_interactor(
        post_id=post_id,
        user_id=user_id,
        reaction_type=reaction_type,
    )

    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    validator.is_invalid_reaction_type.assert_called_once_with(
        reaction_type=reaction_type
    )
    validator.is_user_reaction_to_post_exists_return_reaction_type. \
        assert_called_once_with(
            post_id=post_id,
            user_id=user_id
    )
    storage.create_post_reaction.assert_called_once_with(
        post_id=post_id,
        user_id=user_id,
        reaction_type=reaction_type
    )

def test_react_to_post_user_reacted_with_same_reaction_type_reaction_deleted():
    #Arranhe
    post_id = 1
    user_id = 1
    reaction_type = ReactionType.WOW.value
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToPostInteractor(
        validator,
        storage,
        presenter
    )
    validator.is_invalid_post_id.return_value = False
    validator.is_invalid_reaction_type.return_value = False
    validator.is_user_reaction_to_post_exists_return_reaction_type. \
        return_value = "WOW"
    
    #Act
    interactor.react_to_post_interactor(
        post_id=post_id,
        user_id=user_id,
        reaction_type=reaction_type,
    )

    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    validator.is_invalid_reaction_type.assert_called_once_with(
        reaction_type=reaction_type
    )
    validator.is_user_reaction_to_post_exists_return_reaction_type. \
        assert_called_once_with(
            post_id=post_id,
            user_id=user_id
        )
    storage.delete_post_reaction.assert_called_once_with(
        post_id=post_id,
        user_id=user_id,
    )


def test_react_to_post_user_reacted_with_different_reaction_type_reaction_updated():
    #Arrange
    post_id = 1
    user_id = 1
    reaction_type = ReactionType.WOW.value
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToPostInteractor(
        validator,
        storage,
        presenter
    )
    validator.is_invalid_post_id.return_value = False
    validator.is_invalid_reaction_type.return_value = False
    validator.is_user_reaction_to_post_exists_return_reaction_type. \
        return_value = "HAHA"

    #Act  
    interactor.react_to_post_interactor(
        post_id=post_id,
        user_id=user_id,
        reaction_type=reaction_type,
    )

    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    validator.is_invalid_reaction_type.assert_called_once_with(
        reaction_type=reaction_type
    )
    validator.is_user_reaction_to_post_exists_return_reaction_type. \
        assert_called_once_with(
            post_id=post_id,
            user_id=user_id
        )
    storage.update_post_reaction.assert_called_once_with(
        post_id=post_id,
        user_id=user_id,
        reaction_type=reaction_type
    )
        