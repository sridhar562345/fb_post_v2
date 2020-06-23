import pytest


from fb_post_v2.storages.validators_storage_implementation import \
	ValidatorsStorageImplementation
from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist


@pytest.mark.django_db
def test_is_invalid_post_id_given_invalid_post_id_returns_true():
	#Arrange
	post_id = 1
	expected = True
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_invalid_post_id(post_id)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_invalid_post_id_given_valid_post_id_returns_false(posts):
	#Arrange
	post_id = 1
	expected = False
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_invalid_post_id(post_id)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_invalid_comment_id_given_invalid_comment_id_returns_true():
	#Arrange
	comment_id = 1
	expected = True
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_invalid_comment_id(comment_id)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_invalid_comment_id_given_valid_comment_id_returns_false(comments):
	#Arrange
	comment_id = 1
	expected = False
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_invalid_comment_id(comment_id)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_reply_given_reply_id_returns_true(comments):
	#Arrange
	comment_id = 2
	expected = True
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_reply(comment_id)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_reply_given_comment_id_returns_false(comments):
	#Arrange
	comment_id = 1
	expected = False
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_reply(comment_id)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_user_not_posted_the_post_given_unauthorized_user_returns_true(posts):
	#Arrange
	user_id = 2
	post_id = 1
	expected = True
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_user_not_posted_the_post(user_id, post_id)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_user_not_posted_the_post_given_authorized_user_returns_false(posts):
	#Arrange
	user_id = 1
	post_id = 1
	expected = False
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_user_not_posted_the_post(user_id, post_id)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_invalid_reaction_type_given_invalid_reaction_type_returns_true(posts):
	#Arrange
	user_id = 2
	post_id = 1
	expected = True
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_user_not_posted_the_post(user_id, post_id)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_invalid_reaction_type_given_valid_reaction_type_returns_false(posts):
	#Arrange
	user_id = 1
	post_id = 1
	expected = False
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_user_not_posted_the_post(user_id, post_id)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_user_reaction_to_post_exists_given_reaction_exists_return_reaction_type(posts, reactions):
	#Arrange
	user_id = 2
	post_id = 2
	expected = "LIT"
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_user_reaction_to_post_exists_return_reaction_type(
		user_id,
		post_id
	)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_user_reaction_to_post_exists_given_reaction_does_not_exists_raises_exception(posts, reactions):
	#Arrange
	user_id = 1
	post_id = 2
	storage = ValidatorsStorageImplementation()
	
	#Act
	with pytest.raises(ReactionDoesNotExist):
		storage.is_user_reaction_to_post_exists_return_reaction_type(
			user_id,
			post_id
		)

@pytest.mark.django_db
def test_is_user_reaction_to_comment_exists_given_reaction_exists_return_reaction_type(
	comments,
	reactions
):
	#Arrange
	user_id = 2
	comment_id = 1
	expected = "THUMBS-UP"
	storage = ValidatorsStorageImplementation()
	
	#Act
	actual = storage.is_user_reaction_to_comment_exists_return_reaction_type(
		user_id,
		comment_id
	)
	
	#assert
	assert expected == actual

@pytest.mark.django_db
def test_is_user_reaction_to_comment_exists_given_reaction_does_not_exists_raises_exceptions(
	comments,
	reactions
):
	#Arrange
	user_id = 1
	comment_id = 1
	storage = ValidatorsStorageImplementation()
	
	#Act
	with pytest.raises(ReactionDoesNotExist):
		storage.is_user_reaction_to_comment_exists_return_reaction_type(
			user_id,
			comment_id
		)