from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.post_storage_interface import \
    PostStorageInterface
from fb_post_v2.interactors.storages.dtos import (
	PostReactionsDto,
	PostCommentCountDto,
	CommentReactionMetricsDto,
	CommentRepliesCountDto,
	UserPostsCompleteDto,
)


class GetUserPostsInteractor:
	def __init__(
		self,
		storage: PostStorageInterface,
		presenter: PresenterInterface
	):
		self.storage = storage
		self.presenter = presenter
	
	def get_post_reaction_dto(self, post_id, reactions_dto):
		post_reactions = []
		post_reactions_count = 0

		for reaction in reactions_dto:
			if reaction.post_id == post_id:
				if reaction.reaction not in post_reactions:
					post_reactions.append(reaction.reaction)
				post_reactions_count += 1
		
		post_reactions_dto = PostReactionsDto(
			post_id=post_id,
			reactions_count=post_reactions_count,
			reactions_list=post_reactions
		)

		return post_reactions_dto
	

	def get_comment_reactions_metrics_dto(self, comment_id, reactions_dto):
		comment_reactions = []
		comment_reactions_count = 0

		for reaction in reactions_dto:
			if reaction.comment_id == comment_id:
				if reaction.reaction not in comment_reactions:
					comment_reactions.append(reaction.reaction)
				comment_reactions_count += 1

		comment_reactions_metrics_dto = CommentReactionMetricsDto(
			comment_id = comment_id,
			reactions_count = comment_reactions_count,
			reactions_list = comment_reactions
		)
		return comment_reactions_metrics_dto


	def get_reply_count_dto(self, comment_id, comments_dtos):
		replies_count = 0
		for comment in comments_dtos:
			if comment.parent_comment_id == comment_id:
				replies_count +=1
		reply_count_dto = CommentRepliesCountDto(
			comment_id=comment_id,
			replies_count=replies_count
		)
		return reply_count_dto
	
	
	def get_post_comments_count_dto(self, post_id, comment_dtos):
		comments_count = 0
		for comment in comment_dtos:
			is_given_post_comment = comment.post_id == post_id and \
				(not comment.parent_comment_id)
			if is_given_post_comment:
				comments_count += 1
				
		post_comments_count_dto = PostCommentCountDto(
			post_id=post_id,
			comments_count=comments_count
		)
		return post_comments_count_dto
	
	def get_posts_reactions_dtos(self, posts_dtos, reactions_dto):
		posts_dtos_list = []
		for post in posts_dtos:
			posts_dtos_list.append(
				self.get_post_reaction_dto(post.id, reactions_dto)
			)
		return posts_dtos_list
	
	def get_posts_comments_count_dtos(self, posts_dtos, comments_dto):
		posts_comments_count_dtos = []
		for post in posts_dtos:
			posts_comments_count_dtos.append(
				self.get_post_comments_count_dto(post.id, comments_dto)
			)
		return posts_comments_count_dtos
	
	def get_complete_user_posts_dto(self, user_posts_dto):
		comment_reaction_fields_dtos = []
		replies_count_dtos = []
		posts_dtos = user_posts_dto.post_dto
		reactions_dto = user_posts_dto.reactions_dto
		comments_dto = user_posts_dto.comments_dto
		posts_reactions_dtos = self.get_posts_reactions_dtos(
			posts_dtos,
			reactions_dto
		)
		posts_comments_count_dtos = self.get_posts_comments_count_dtos(
			posts_dtos,
			comments_dto
		)
		for comment in comments_dto:
			comment_reaction_fields_dtos.append(self.\
				get_comment_reactions_metrics_dto(comment.id, reactions_dto))
			is_comment = not comment.parent_comment_id
			if is_comment:
				replies_count_dtos.append(self.get_reply_count_dto(
					comment.id, comments_dto))
		
		post_complete_dto = UserPostsCompleteDto(
			user_post_details_dto=user_posts_dto,
			post_reactions_dtos=posts_reactions_dtos,
			post_comments_count_dtos=posts_comments_count_dtos,
    		comment_reactions_dtos=comment_reaction_fields_dtos,
    		comment_replies_count_dtos=replies_count_dtos
		)
		return post_complete_dto
	
	def get_user_posts_interactor(self, user_id):
		user_posts_dto = self.storage.get_user_posts(user_id)
		user_complete_posts_dto = self.get_complete_user_posts_dto(
			user_posts_dto
		)
		user_posts_dict = self.presenter.get_response_for_user_posts(
			user_complete_posts_dto
		)

		return user_posts_dict