import pytest

from django.core.exceptions import ObjectDoesNotExist
from fb_post_v2.models import Reaction
from fb_post_v2.storages.reaction_storage_implementation import \
	ReactionStorageImplementation
from fb_post_v2.constants.enums import ReactionType


@pytest.mark.django_db
def test_create_post_reaction_new_reaction_created(posts):
	#Arrange
	user_id=1
	post_id=1
	reaction_type=ReactionType.WOW.value
	storage = ReactionStorageImplementation()
	
	#Act
	storage.create_post_reaction(
		user_id=user_id,
		post_id=post_id,
		reaction_type=reaction_type
	)
	
	#Assert
	reaction_obj = Reaction.objects.get(
		reacted_by_id=user_id,
		post_id=post_id
	)
	assert reaction_obj.reaction == reaction_type

@pytest.mark.django_db	
def test_update_post_reaction_post_reaction_updated(reactions):
	#Arrange
	user_id=2
	post_id=2
	reaction_type=ReactionType.WOW.value
	storage = ReactionStorageImplementation()
	
	#Act
	storage.update_post_reaction(
		user_id=user_id,
		post_id=post_id, reaction_type=reaction_type
	)
	
	#Assert
	reaction_obj = Reaction.objects.get(
		reacted_by_id=user_id,
		post_id=post_id
	)
	assert reaction_obj.reaction == reaction_type

@pytest.mark.django_db
def test_delete_post_reaction_post_reaction_deleted(reactions):
	#Arrange
	user_id=2
	post_id=2
	storage = ReactionStorageImplementation()
	
	#Act
	storage.delete_post_reaction(
		user_id=user_id,
		post_id=post_id,
	)
	
	#Act
	with pytest.raises(ObjectDoesNotExist):
		Reaction.objects.get(
			reacted_by_id=user_id,
			post_id=post_id
		)
	

@pytest.mark.django_db
def test_create_comment_reaction_new_reaction_created(comments):
	#Arrange
	user_id=1
	comment_id=1
	reaction_type=ReactionType.WOW.value
	storage = ReactionStorageImplementation()
	
	#Act
	storage.create_comment_reaction(
		user_id=user_id,
		comment_id=comment_id,
		reaction_type=reaction_type
	)
	
	#Assert
	reaction_obj = Reaction.objects.get(
		reacted_by_id=user_id,
		comment_id=comment_id
	)
	assert reaction_obj.reaction == reaction_type
	

@pytest.mark.django_db
def test_update_comment_reaction_comment_reaction_updated(reactions):
	#Arrange
	user_id=2
	comment_id=1
	reaction_type=ReactionType.WOW.value
	storage = ReactionStorageImplementation()
	
	#Act
	storage.update_comment_reaction(
		user_id=user_id,
		comment_id=comment_id, reaction_type=reaction_type
	)
	
	#Assert
	reaction_obj = Reaction.objects.get(
		reacted_by_id=user_id,
		comment_id=comment_id
	)
	assert reaction_obj.reaction == reaction_type

@pytest.mark.django_db
def test_delete_comment_reaction_comment_reaction_deleted(reactions):
	#Arrange
	user_id=2
	comment_id=1
	storage = ReactionStorageImplementation()
	
	#Act
	storage.delete_comment_reaction(
		user_id=user_id,
		comment_id=comment_id,
	)
	
	#Act
	with pytest.raises(ObjectDoesNotExist):
		Reaction.objects.get(
			reacted_by_id=user_id,
			comment_id=comment_id
		)

