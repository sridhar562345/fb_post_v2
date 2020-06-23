import pytest


from fb_post_v2.storages.comment_storage_implementation import \
	CommentStorageImplementation
	
@pytest.mark.django_db
def test_create_comment_returns_comment_id(posts):
	#Arrange
	post_id=1
	user_id=1
	comment_content="hello"
	expected_comment_id = 1
	comment_storage = CommentStorageImplementation()
	
	#Act
	actual_comment_id = comment_storage.create_comment(
		user_id=user_id,
		post_id=post_id,
		comment_content=comment_content
	)
	
	#Assert
	actual_comment_id == expected_comment_id


