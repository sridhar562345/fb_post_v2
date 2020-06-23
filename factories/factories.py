import pytest
import factory

from ..models import (
	User, Post, Comment, Reaction
)
from fb_post_v2.constants.enums import ReactionType

class UserFactor(factory.django.DjangoModelFactory):
	class Meta:
		model = User
	
	name = factory.Iterator(['Anusha', 'Suma', 'Akhila', 'Bhagi', 'Kusuma', 'Sneha'])

class PostFactor(factory.django.DjangoModelFactory):
	class Meta:
		model = Post
	
	content = factory.Sequence(lambda a: f'post content {a}')
	posted_by = factory.SubFactory(UserFactor)