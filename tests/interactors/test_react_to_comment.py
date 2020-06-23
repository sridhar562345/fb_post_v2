import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import (
    NotFound,
    BadRequest
)


from fb_post_v2.interactors.react_to_comment_interactor import \
    ReactToCommentInteractor
from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.validators_storage_interface import \
    ValidatorsStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface import \
    ReactionStorageInterface


    
def asserting_validating_comment_fun_calls(validator, comment_id):
    validator.is_invalid_comment_id.assert_called_once_with(
        comment_id=comment_id
    )

    

def test_react_to_comment_given_invalid_comment_id_raises_exception():
    #Arrange
    comment_id = 1
    user_id = 1
    reaction_type = ReactionType.WOW.value
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToCommentInteractor(
        validator,
        storage,
        presenter
    )
    
    validator.is_invalid_comment_id.return_value = True
    presenter.raise_invalid_comment_id_exception.side_effect = \
        NotFound
                                                                                                                                                                                                                                                                  
    #Act
    with pytest.raises(NotFound):
        interactor.react_to_comment_interactor(
            comment_id=comment_id,
            user_id=user_id,
            reaction_type=reaction_type,
        )
    
    #Assert
    asserting_validating_comment_fun_calls(validator, comment_id)
    presenter.raise_invalid_comment_id_exception.\
        assert_called_once()


def test_react_to_comment_given_invalid_reaction_type_raises_exception():
    #Arrange
    comment_id = 1
    user_id = 1
    reaction_type = "COOL"
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToCommentInteractor(
        validator,
        storage,
        presenter
    )
    validator.is_invalid_comment_id.return_value = False
    validator.is_invalid_reaction_type.return_value = True
    presenter.raise_invalid_reaction_type_exception.\
        side_effect = BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.react_to_comment_interactor(
            comment_id=comment_id,
            user_id=user_id,
            reaction_type=reaction_type,
        )
    
    #Assert
    validator.is_invalid_comment_id.assert_called_once_with(
        comment_id=comment_id
    )
    validator.is_invalid_reaction_type.assert_called_once_with(
        reaction_type=reaction_type
    )
    presenter.raise_invalid_reaction_type_exception.\
        assert_called_once()


def test_react_to_comment_given_valid_details_new_reaction_created():
    #Arrange
    comment_id = 1
    user_id = 1
    reaction_type = ReactionType.WOW.value
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToCommentInteractor(
        validator,
        storage,
        presenter
    )
    validator.is_invalid_comment_id.return_value = False
    validator.is_invalid_reaction_type.return_value = False
    validator.is_user_reaction_to_comment_exists_return_reaction_type. \
        side_effect = ReactionDoesNotExist

    #Act
    interactor.react_to_comment_interactor(
        comment_id=comment_id,
        user_id=user_id,
        reaction_type=reaction_type,
    )

    #Assert
    validator.is_user_reaction_to_comment_exists_return_reaction_type. \
        assert_called_once_with(
            comment_id=comment_id,
            user_id=user_id
        )
    storage.create_comment_reaction.assert_called_once_with(
        comment_id=comment_id,
        user_id=user_id,
        reaction_type=reaction_type
    )


def test_react_to_comment_user_reacted_with_same_reaction_type_reaction_deleted():
    #Arrange
    comment_id = 1
    user_id = 1
    reaction_type = ReactionType.WOW.value
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToCommentInteractor(
        validator,
        storage,
        presenter
    )
    validator.is_invalid_comment_id.return_value = False
    validator.is_user_reaction_to_comment_exists_return_reaction_type. \
        return_value = "WOW"

    #Act
    interactor.react_to_comment_interactor(
        comment_id=comment_id,
        user_id=user_id,
        reaction_type=reaction_type,
    )

    #Assert
    validator.is_invalid_comment_id.assert_called_once_with(
        comment_id=comment_id
    )
    validator.is_invalid_reaction_type.assert_called_once_with(
        reaction_type=reaction_type
    )
    validator.is_user_reaction_to_comment_exists_return_reaction_type. \
        assert_called_once_with(comment_id=comment_id,
                                user_id=user_id
                                )
    storage.delete_comment_reaction.assert_called_once_with(
        comment_id=comment_id,
        user_id=user_id,
    )


def test_react_to_comment_user_reacted_with_different_reaction_type_reaction_updated():
    #Arrange
    comment_id = 1
    user_id = 1
    reaction_type = ReactionType.WOW.value
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ReactToCommentInteractor(
        validator,
        storage,
        presenter
    )
    validator.is_invalid_comment_id.return_value = False
    validator.is_invalid_reaction_type.return_value = False
    validator.is_user_reaction_to_comment_exists_return_reaction_type. \
        return_value = "HAHA"

    #Act
    interactor.react_to_comment_interactor(
        comment_id=comment_id,
        user_id=user_id,
        reaction_type=reaction_type,
    )

    #Assert
    validator.is_invalid_comment_id.assert_called_once_with(
        comment_id=comment_id
    )
    validator.is_invalid_reaction_type.assert_called_once_with(
        reaction_type=reaction_type
    )
    validator.is_user_reaction_to_comment_exists_return_reaction_type. \
        assert_called_once_with(
            comment_id=comment_id,
            user_id=user_id
        )
    storage.update_comment_reaction.assert_called_once_with(
        comment_id=comment_id,
        user_id=user_id,
        reaction_type=reaction_type
    )
