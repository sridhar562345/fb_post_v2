import pytest


from fb_post_v2.storages.post_storage_implementation import \
	PostStorageImplementation
from fb_post_v2.exceptions.exceptions import ReactionDoesNotExist

@pytest.mark.django_db
def test_create_post_returns_post_id(users):
	#Arrange
	user_id = 1
	expected_post_id = 1
	post_content = "hello"
	post_storage = PostStorageImplementation()
	
	#Act
	actual_post_id = post_storage.create_post(user_id=user_id, post_content=post_content)
	
	#Arrange
	assert expected_post_id == actual_post_id


	