import pytest

from fb_post_v2.interactors.storages.dtos import (
	PostCompleteDetailsDto,
	PostReactionCompleteDetailsDto,
	UserPostDetailsDto,
	CommentRepliesDto
)
from fb_post_v2.exceptions.exceptions import (
	ReactionDoesNotExist,
	InvalidPostId,
	InvalidCommentId,
	InvalidReactionType
)
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.presenters.presenter_implementation import \
	PresenterImplementation
from fb_post_v2.models import (
	User,
	Post,
	Reaction,
	Comment
)


def test_raise_invalid_post_id_exception_raises_exception():
	#Arrange
	presenter = PresenterImplementation()
	
	#Act
	with pytest.raises(InvalidPostId):
		presenter.raise_invalid_post_id_exception()
	

def test_raise_invalid_comment_id_exception_raises_exception():
	#Arrange
	presenter = PresenterImplementation()
	
	#Act
	with pytest.raises(InvalidCommentId):
		presenter.raise_invalid_comment_id_exception()

def test_raise_invalid_reaction_type_exception_raises_exception():
	#Arrange
	presenter = PresenterImplementation()
	
	#Act
	with pytest.raises(InvalidReactionType):
		presenter.raise_invalid_reaction_type_exception()
	
	

def test_get_create_post_response_return_post_id_dict():
	#Arrange
	post_id = 1
	expected = {
		"post_id": post_id
	}
	presenter = PresenterImplementation()
	
	#Act
	actual = presenter.get_create_post_response(post_id)
	
	#assert
	assert expected == actual

def test_get_create_comment_response_return_comment_id_dict():
	#Arrange
	comment_id=1
	expected = {
		"comment_id": comment_id
	}
	presenter = PresenterImplementation()
	
	#Act
	actual = presenter.get_create_comment_response(comment_id)
	
	#assert
	assert expected == actual



	

