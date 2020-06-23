import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec


from fb_post_v2.exceptions.exceptions import InvalidPostId
from fb_post_v2.interactors.get_post_interactor import \
    GetPostInteractor
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.validators_storage_interface import \
    ValidatorsStorageInterface
from fb_post_v2.interactors.storages.post_storage_interface import \
    PostStorageInterface
from fb_post_v2.interactors.storages.dtos import (
    PostCompleteDetailsDto,
    PostCompleteDto
)

def test_given_invalid_post_id_raises_exception():
    #Arrange
    post_id = 1
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(validator,storage,presenter)
    validator.is_invalid_post_id.return_value = True
    presenter.raise_invalid_post_id_exception.side_effect = NotFound

    #Act
    with pytest.raises(NotFound):
        interactor.get_post_interactor(
            post_id=post_id,
        )

    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    presenter.raise_invalid_post_id_exception.assert_called_once()


def test_get_post_given_valid_post_id_returns_post_details(
    post_dto,
    user_dtos,
    comment_dtos,
    reaction_dtos,
    get_post_response,
    post_reactions_dto,
    post_comments_count_dto,
    comment_reaction_metrics_dto,
    comment_replies_count_dtos
):
    #Arrange
    post_id = 1
    expected_post_details_dict = get_post_response
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(validator, storage, presenter)
    get_post_dto = PostCompleteDetailsDto(
        post_dto=post_dto,
        users_dto=user_dtos,
        comments_dto=comment_dtos,
        reactions_dto=reaction_dtos
    )
    get_post_presenter_dto = PostCompleteDto(
        post_details_dto = get_post_dto,
        post_reactions_dto=post_reactions_dto,
        post_comments_count_dto=post_comments_count_dto,
        comment_reactions_dtos = comment_reaction_metrics_dto,
        comment_replies_count_dtos = comment_replies_count_dtos
    )
    storage.get_post.return_value = get_post_dto
    presenter.get_post_details_response.return_value = \
        expected_post_details_dict

    #Act
    post_details_dict = interactor.get_post_interactor(
        post_id=post_id,
    )

    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    presenter.get_post_details_response.assert_called_once_with(
        get_post_presenter_dto
    )
    assert post_details_dict == expected_post_details_dict

def test_get_post_given_no_reply_comment_post_returns_post_details(
    no_comments_reply_post_dtos,
):
    #Arrange
    post_id = 2
    user_posts_dto = no_comments_reply_post_dtos
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(validator, storage, presenter)
    get_post_dto = PostCompleteDetailsDto(
        post_dto=user_posts_dto["post_dto"],
        users_dto=user_posts_dto["user_dtos"],
        comments_dto=user_posts_dto["comment_dtos"],
        reactions_dto=user_posts_dto["reaction_dtos"]
    )
    get_post_presenter_dto = PostCompleteDto(
        post_details_dto = get_post_dto,
        post_reactions_dto=user_posts_dto["post_reactions_dto"],
        post_comments_count_dto=user_posts_dto["post_comments_count_dto"],
        comment_reactions_dtos = user_posts_dto["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = user_posts_dto["comment_replies_count_dtos"]
    )
    storage.get_post.return_value = get_post_dto

    #Act
    interactor.get_post_interactor( 
        post_id=post_id,
    )

    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    presenter.get_post_details_response.assert_called_once_with(
        get_post_presenter_dto
    )

def test_get_post_given_no_comments_post_returns_post_comment_empty_list(
    no_comments_post_dtos,
):
    #Arrange
    post_id = 2
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(validator, storage, presenter)
    get_post_dto = PostCompleteDetailsDto(
        post_dto=no_comments_post_dtos["post_dto"],
        users_dto=no_comments_post_dtos["user_dtos"],
        comments_dto=no_comments_post_dtos["comment_dtos"],
        reactions_dto=no_comments_post_dtos["reaction_dtos"]
    )
    get_post_presenter_dto = PostCompleteDto(
        post_details_dto = get_post_dto,
        post_reactions_dto=no_comments_post_dtos["post_reactions_dto"],
        post_comments_count_dto=no_comments_post_dtos["post_comments_count_dto"],
        comment_reactions_dtos = no_comments_post_dtos["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = no_comments_post_dtos["comment_replies_count_dtos"]
    )
    storage.get_post.return_value = get_post_dto

    #Act
    interactor.get_post_interactor(
        post_id=post_id,
    )

    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    presenter.get_post_details_response.assert_called_once_with(
        get_post_presenter_dto
    )

def test_get_post_given_post_with_one_comment_with_one_reply_returns_post_details(
    post_with_one_comment_with_one_reply
):
    #Arrange
    post_id = 2
    all_fields = post_with_one_comment_with_one_reply
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(validator, storage, presenter)
    get_post_dto = PostCompleteDetailsDto(
        post_dto=all_fields["post_dto"],
        users_dto=all_fields["user_dtos"],
        comments_dto=all_fields["comment_dtos"],
        reactions_dto=all_fields["reaction_dtos"]
    )
    get_post_presenter_dto = PostCompleteDto(
        post_details_dto = get_post_dto,
        post_reactions_dto=all_fields["post_reactions_dto"],
        post_comments_count_dto=all_fields["post_comments_count_dto"],
        comment_reactions_dtos = all_fields["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = all_fields["comment_replies_count_dtos"]
    )
    storage.get_post.return_value = get_post_dto

    #Act
    interactor.get_post_interactor(
        post_id=post_id,
    )

    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    presenter.get_post_details_response.assert_called_once_with(
        get_post_presenter_dto
    )

def test_get_post_given_post_with_one_comment_with_one_reply_and_reply_to_reply_returns_post_details(
    post_with_one_comment_with_one_reply_and_reply_to_reply
):
    #Arrange
    post_id = 2
    all_fields = post_with_one_comment_with_one_reply_and_reply_to_reply
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(validator, storage, presenter)
    get_post_dto = PostCompleteDetailsDto(
        post_dto=all_fields["post_dto"],
        users_dto=all_fields["user_dtos"],
        comments_dto=all_fields["comment_dtos"],
        reactions_dto=all_fields["reaction_dtos"]
    )
    get_post_presenter_dto = PostCompleteDto(
        post_details_dto = get_post_dto,
        post_reactions_dto=all_fields["post_reactions_dto"],
        post_comments_count_dto=all_fields["post_comments_count_dto"],
        comment_reactions_dtos = all_fields["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = all_fields["comment_replies_count_dtos"]
    )
    storage.get_post.return_value = get_post_dto

    #Act
    interactor.get_post_interactor(
        post_id=post_id,
    )

    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    presenter.get_post_details_response.assert_called_once_with(
        get_post_presenter_dto
    )

def test_get_post_given_multiple_repeated_reactions_for_post_returns_post_details(
    multiple_repeated_reactions_for_post
):
    #Arrange
    post_id = 2
    all_fields = multiple_repeated_reactions_for_post
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(validator, storage, presenter)
    get_post_dto = PostCompleteDetailsDto(
        post_dto=all_fields["post_dto"],
        users_dto=all_fields["user_dtos"],
        comments_dto=all_fields["comment_dtos"],
        reactions_dto=all_fields["reaction_dtos"]
    )
    get_post_presenter_dto = PostCompleteDto(
        post_details_dto = get_post_dto,
        post_reactions_dto=all_fields["post_reactions_dto"],
        post_comments_count_dto=all_fields["post_comments_count_dto"],
        comment_reactions_dtos = all_fields["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = all_fields["comment_replies_count_dtos"]
    )
    storage.get_post.return_value = get_post_dto

    #Act
    interactor.get_post_interactor(
        post_id=post_id,
    )

    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    presenter.get_post_details_response.assert_called_once_with(
        get_post_presenter_dto
    )

def test_get_post_given_multiple_repeated_reactions_for_comments_post_details(
    multiple_repeated_reactions_for_comments
):
    #Arrange
    post_id = 2
    all_fields = multiple_repeated_reactions_for_comments
    validator = create_autospec(ValidatorsStorageInterface)
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostInteractor(validator, storage, presenter)
    get_post_dto = PostCompleteDetailsDto(
        post_dto=all_fields["post_dto"],
        users_dto=all_fields["user_dtos"],
        comments_dto=all_fields["comment_dtos"],
        reactions_dto=all_fields["reaction_dtos"]
    )
    get_post_presenter_dto = PostCompleteDto(
        post_details_dto = get_post_dto,
        post_reactions_dto=all_fields["post_reactions_dto"],
        post_comments_count_dto=all_fields["post_comments_count_dto"],
        comment_reactions_dtos = all_fields["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = all_fields["comment_replies_count_dtos"]
    )
    storage.get_post.return_value = get_post_dto

    #Act
    interactor.get_post_interactor(
        post_id=post_id,
    )

    #Assert
    validator.is_invalid_post_id.assert_called_once_with(
        post_id=post_id
    )
    presenter.get_post_details_response.assert_called_once_with(
        get_post_presenter_dto
    )
