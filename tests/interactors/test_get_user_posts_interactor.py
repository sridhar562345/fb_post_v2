from unittest.mock import create_autospec


from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.post_storage_interface import \
    PostStorageInterface
from fb_post_v2.interactors.storages.dtos import (
	PostCompleteDetailsDto,
	UserPostDetailsDto,
	UserPostsCompleteDto
)
from fb_post_v2.interactors.get_user_posts_interactor import \
	GetUserPostsInteractor




def test_get_user_post_given_no_reply_comment_post_returns_post_details(
    no_comments_reply_post_dtos,
    single_comment_post_fields,
):
    #Arrange
    user_id = 1
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage, presenter)
    get_user_post_dto = UserPostDetailsDto(
        post_dto=single_comment_post_fields["post_dto"],
        users_dto=no_comments_reply_post_dtos["user_dtos"],
        comments_dto=no_comments_reply_post_dtos["comment_dtos"],
        reactions_dto=no_comments_reply_post_dtos["reaction_dtos"]
    )
    get_user_post_presenter_dto = UserPostsCompleteDto(
        user_post_details_dto = get_user_post_dto,
        post_reactions_dtos=single_comment_post_fields["post_reactions_dtos"],
        post_comments_count_dtos=single_comment_post_fields["post_comments_count_dtos"],
        comment_reactions_dtos = no_comments_reply_post_dtos["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = no_comments_reply_post_dtos["comment_replies_count_dtos"]
    )
    storage.get_user_posts.return_value = get_user_post_dto

    #Act
    interactor.get_user_posts_interactor( 
        user_id=user_id,
    )

    #Assert
    storage.get_user_posts.assert_called_once_with(user_id)
    presenter.get_response_for_user_posts.assert_called_once_with(
        get_user_post_presenter_dto
    )


def test_get_user_post_given_no_comments_post_returns_post_comment_empty_list(
    no_comments_post_dtos,
    no_comments_post_fields,
):
    #Arrange
    user_id = 1
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage, presenter)
    get_user_post_dto = UserPostDetailsDto(
        post_dto=no_comments_post_fields["post_dto"],
        users_dto=no_comments_post_dtos["user_dtos"],
        comments_dto=no_comments_post_dtos["comment_dtos"],
        reactions_dto=no_comments_post_dtos["reaction_dtos"]
    )
    get_user_post_presenter_dto = UserPostsCompleteDto(
        user_post_details_dto = get_user_post_dto,
        post_reactions_dtos=no_comments_post_fields["post_reactions_dtos"],
        post_comments_count_dtos=no_comments_post_fields["post_comments_count_dtos"],
        comment_reactions_dtos = no_comments_post_dtos["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = no_comments_post_dtos["comment_replies_count_dtos"]
    )
    storage.get_user_posts.return_value = get_user_post_dto

    #Act
    interactor.get_user_posts_interactor(
        user_id=user_id,
    )

    #Assert
    presenter.get_response_for_user_posts.assert_called_once_with(
        get_user_post_presenter_dto
    )

def test_get_user_post_given_post_with_one_comment_with_one_reply_returns_post_details(
    post_with_one_comment_with_one_reply,
    single_comment_post_fields
):
    #Arrange
    user_id = 1
    all_fields = post_with_one_comment_with_one_reply
    post_fields = single_comment_post_fields
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage, presenter)
    get_user_post_dto = UserPostDetailsDto(
        post_dto=post_fields["post_dto"],
        users_dto=all_fields["user_dtos"],
        comments_dto=all_fields["comment_dtos"],
        reactions_dto=all_fields["reaction_dtos"]
    )
    get_user_post_presenter_dto = UserPostsCompleteDto(
        user_post_details_dto = get_user_post_dto,
        post_reactions_dtos=post_fields["post_reactions_dtos"],
        post_comments_count_dtos=post_fields["post_comments_count_dtos"],
        comment_reactions_dtos = all_fields["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = all_fields["comment_replies_count_dtos"]
    )
    storage.get_user_posts.return_value = get_user_post_dto

    #Act
    interactor.get_user_posts_interactor(
        user_id=user_id,
    )

    #Assert
    presenter.get_response_for_user_posts.assert_called_once_with(
        get_user_post_presenter_dto
    )

def test_get_user_post_given_post_with_one_comment_with_one_reply_and_reply_to_reply_returns_post_details(
    post_with_one_comment_with_one_reply_and_reply_to_reply,
    single_comment_post_fields
):
    #Arrange
    user_id = 1
    all_fields = post_with_one_comment_with_one_reply_and_reply_to_reply
    post_fields = single_comment_post_fields
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage, presenter)
    get_user_post_dto = UserPostDetailsDto(
        post_dto=post_fields["post_dto"],
        users_dto=all_fields["user_dtos"],
        comments_dto=all_fields["comment_dtos"],
        reactions_dto=all_fields["reaction_dtos"]
    )
    get_user_post_presenter_dto = UserPostsCompleteDto(
        user_post_details_dto = get_user_post_dto,
        post_reactions_dtos=post_fields["post_reactions_dtos"],
        post_comments_count_dtos=post_fields["post_comments_count_dtos"],
        comment_reactions_dtos = all_fields["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = all_fields["comment_replies_count_dtos"]
    )
    storage.get_user_posts.return_value = get_user_post_dto

    #Act
    interactor.get_user_posts_interactor(
        user_id=user_id,
    )

    #Assert
    presenter.get_response_for_user_posts.assert_called_once_with(
        get_user_post_presenter_dto
    )

def test_get_user_post_given_multiple_repeated_reactions_for_post_returns_post_details(
    multiple_repeated_reactions_for_post,
    user_post_fields_single_post_multiple_reactions_dtos
):
    #Arrange
    user_id = 1
    all_fields = multiple_repeated_reactions_for_post
    post_fields = user_post_fields_single_post_multiple_reactions_dtos
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage, presenter)
    get_user_post_dto = UserPostDetailsDto(
        post_dto=post_fields["post_dto"],
        users_dto=all_fields["user_dtos"],
        comments_dto=all_fields["comment_dtos"],
        reactions_dto=all_fields["reaction_dtos"]
    )
    get_user_post_presenter_dto = UserPostsCompleteDto(
        user_post_details_dto = get_user_post_dto,
        post_reactions_dtos=post_fields["post_reactions_dtos"],
        post_comments_count_dtos=post_fields["post_comments_count_dtos"],
        comment_reactions_dtos = all_fields["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = all_fields["comment_replies_count_dtos"]
    )
    storage.get_user_posts.return_value = get_user_post_dto

    #Act
    interactor.get_user_posts_interactor(
        user_id=user_id,
    )

    #Assert
    presenter.get_response_for_user_posts.assert_called_once_with(
        get_user_post_presenter_dto
    )

def test_get_user_post_given_multiple_repeated_reactions_for_comments_post_details(
    multiple_repeated_reactions_for_comments,
    single_comment_post_fields
):
    #Arrange
    user_id = 1
    all_fields = multiple_repeated_reactions_for_comments
    post_fields = single_comment_post_fields
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage, presenter)
    get_user_post_dto = UserPostDetailsDto(
        post_dto=post_fields["post_dto"],
        users_dto=all_fields["user_dtos"],
        comments_dto=all_fields["comment_dtos"],
        reactions_dto=all_fields["reaction_dtos"]
    )
    get_user_post_presenter_dto = UserPostsCompleteDto(
        user_post_details_dto = get_user_post_dto,
        post_reactions_dtos=post_fields["post_reactions_dtos"],
        post_comments_count_dtos=post_fields["post_comments_count_dtos"],
        comment_reactions_dtos = all_fields["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = all_fields["comment_replies_count_dtos"]
    )
    storage.get_user_posts.return_value = get_user_post_dto

    #Act
    interactor.get_user_posts_interactor(
        user_id=user_id,
    )

    #Assert
    presenter.get_response_for_user_posts.assert_called_once_with(
        get_user_post_presenter_dto
    )


def test_get_user_post_user_posted_two_posts_retorn_posts_details(
    user_post_two_posts_dtos,
    user_post_fields_double_posts_dtos,

):
    #Arrange
    user_id = 1
    all_fields = user_post_two_posts_dtos
    post_fields = user_post_fields_double_posts_dtos
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage, presenter)
    get_user_post_dto = UserPostDetailsDto(
        post_dto=post_fields["post_dto"],
        users_dto=all_fields["user_dtos"],
        comments_dto=all_fields["comment_dtos"],
        reactions_dto=all_fields["reaction_dtos"]
    )
    get_user_post_presenter_dto = UserPostsCompleteDto(
        user_post_details_dto = get_user_post_dto,
        post_reactions_dtos=post_fields["post_reactions_dtos"],
        post_comments_count_dtos=post_fields["post_comments_count_dtos"],
        comment_reactions_dtos = all_fields["comment_reaction_metrics_dto"],
        comment_replies_count_dtos = all_fields["comment_replies_count_dtos"]
    )
    storage.get_user_posts.return_value = get_user_post_dto

    #Act
    interactor.get_user_posts_interactor(
        user_id=user_id,
    )

    #Assert
    presenter.get_response_for_user_posts.assert_called_once_with(
        get_user_post_presenter_dto
    )
