import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound


from fb_post_v2.interactors.storages.validators_storage_interface import \
    ValidatorsStorageInterface
from fb_post_v2.interactors.storages.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.get_reaction_metrics_interactor import \
    GetReactionMetricsInteractor


def test_get_reactions_metrics_given_invalid_post_id_raises_exception():
    #Arrange
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetReactionMetricsInteractor(
        validator,
        storage,
        presenter
    )
    post_id = 1
    validator.is_invalid_post_id.return_value = True
    presenter.raise_invalid_post_id_exception.side_effect = NotFound
    
    
    #Act
    with pytest.raises(NotFound):
        interactor.get_post_reaction_metrics_interactor(post_id)
    
    #assert
    validator.is_invalid_post_id.assert_called_once_with(post_id)
    presenter.raise_invalid_post_id_exception.assert_called_once()
    

def test_get_reactions_metrics_given_valid_post_id_returns_post_reactions_metrics():
    #Arrange
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(ReactionStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetReactionMetricsInteractor(
        validator,
        storage,
        presenter
    )
    post_id = 1
    expected_response = [
        {
            "reaction_type": "HAHA",
            "count": 3
        },
        {
            "reaction_type":"SAD",
            "count": 2
        }
    ]
    reaction_metrics = {
        "HAHA": 3,
        "SAD": 2
    }
    validator.is_invalid_post_id.return_value = False
    storage.get_reaction_metrics.return_value = reaction_metrics
    presenter.get_post_reaction_metrics_response.return_value = \
        expected_response

    
    #act
    actual_response = interactor.get_post_reaction_metrics_interactor(
        post_id
    )
    
    #assert
    validator.is_invalid_post_id.assert_called_once_with(post_id)
    storage.get_reaction_metrics.assert_called_once_with(post_id)
    presenter.get_post_reaction_metrics_response.\
        assert_called_once_with(
            reaction_metrics
        )
    assert expected_response == actual_response
    