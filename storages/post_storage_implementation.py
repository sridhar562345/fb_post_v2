from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.storages.post_storage_interface import \
	PostStorageInterface
from fb_post_v2.models import (
	User,
	Post,
	Reaction,
	Comment
)
from fb_post_v2.interactors.storages.dtos import (
	PostCompleteDetailsDto,
	UserPostDetailsDto
)

class PostStorageImplementation(PostStorageInterface):
	def create_post(self, user_id: int, post_content: str) -> int:
		new_post = Post.objects.create(
			content=post_content,
			posted_by_id=user_id
		)
		return new_post.id
	
	def delete_post(self, post_id: int):
		pass
	
	def get_post(self,post_id: int) -> PostCompleteDetailsDto:
		pass
	
	def get_user_posts(self, user_id: int) -> UserPostDetailsDto:
		pass
	